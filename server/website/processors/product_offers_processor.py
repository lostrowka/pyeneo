import logging
import re
from typing import List, Optional

from bs4 import BeautifulSoup, element

from server.website.models.item import Item
from server.website.models.offer import Offer
from server.website.processors import DataProcessorException


class ProductOffersProcessor:
    html_soup = ""

    def __init__(self, html_doc: str, item: Item):
        self.html_soup = BeautifulSoup(html_doc, 'html.parser')
        self.log = logging.getLogger(ProductOffersProcessor.__name__)
        self.item = item

    def get_seller_table(self) -> element.Tag:
        """ Get table of sellers DOM for given product """
        return self.html_soup.find("table", class_="product-offers")

    def get_seller_list_items_dom(self) -> List[element.Tag]:
        """ Get list of sellers for given product """
        return self.get_seller_table().find_all("tr", class_="product-offer")

    def parse_seller_list_item_dom(self, list_item_dom: element.Tag) -> Optional[Offer]:
        """ Parse list item DOM to Offer object """
        name = list_item_dom["data-shopurl"]
        self.log.debug(f"Processing seller {name}")
        try:
            price = self.get_price(list_item_dom)
            url = list_item_dom.find("a", class_="go-to-shop")["href"][1:]
            rating = self.get_rating(list_item_dom)
            opinions = self.get_no_of_opinions(list_item_dom)

            return Offer(name, price, url, rating, opinions)
        except DataProcessorException as e:
            self.log.debug(f"Error while processing {name} record: {e}")
            return None

    # TODO: consider refactoring this method to just provide offers to item
    def get_offers_list(self, min_rep: int = 4, min_opinions: int = 20, res_len: int = 5) -> List[Offer]:
        """ Get List of Offer objects for given product """
        seller_list_items = self.get_seller_list_items_dom()
        offers_list = []
        for list_item in seller_list_items:
            offer = self.parse_seller_list_item_dom(list_item)
            if offer and offer.rating >= min_rep and offer.opinions >= min_opinions:
                offers_list.append(offer)
            if len(offers_list) == res_len:
                break
        self.item.set_offers(offers_list)
        return offers_list

    @staticmethod
    def get_price(tag: element.Tag) -> float:
        """ Get price offered by given seller """
        if tag.find("span", class_="free-delivery-txt"):
            value = int(tag.find("span", class_="value").text)
            penny = float(re.search(r",(\d{2})", tag.find("span", class_="penny").text).group(1))/100
        else:
            delivery_regex = re.search(r"(\d+),(\d{2})", tag.find("div", class_="product-delivery-info").text)
            if delivery_regex:
                value = int(delivery_regex.group(1))
                penny = float(delivery_regex.group(2))/100
            else:
                raise DataProcessorException("Did not find price with delivery included")
        return value + penny

    @staticmethod
    def get_rating(tag: element.Tag) -> float:
        """ Get rating (no of stars) for given seller """
        rating_dom = tag.find("span", class_="score-marker")
        return float(re.search(r"width: (\d+.?\d?)%;", rating_dom["style"]).group(1))/20

    @staticmethod
    def get_no_of_opinions(tag: element.Tag) -> int:
        """ Get number of opinions for given seller """
        no_str = tag.find("span", class_="dotted-link").text
        return int(re.search(r"^(\d+) opini[iea]$", no_str).group(1))
