from functools import reduce
from typing import List

from server.website.constants import Ceneo
from server.website.models.item_query import ItemQuery
from server.website.models.offer import Offer


class Item:
    """ Class reflecting a specific item"""

    prod_id: str = ""
    prod_name: str = ""
    # TODO: must provide item_query as "parent" to item -- get name
    parent_item_query: ItemQuery = None
    offers: List[Offer] = []
    mean_price: float = None

    def __init__(self, prod_id: str, prod_name: str, parent_item_query: ItemQuery = None):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.parent_item_query = parent_item_query

    def __str__(self):
        return f"{self.prod_name}"

    def create_url(self) -> str:
        """ Create URL for and item with specific ID sorted by lowest price (delivery included) """
        return f"{Ceneo.URI}{self.prod_id};0284-0.htm"

    def add_seller(self, name: str, price: float):
        """ Method to append seller with their price to prices """
        self.offers.append(Offer(name, price))

    def get_price_by_seller(self, name: str) -> float:
        """ Method returning price at given seller or -1 if there is no such seller in Offers list"""
        return next((offer.price for offer in self.offers if offer.name == name), -1)

    def set_offers(self, offers: List[Offer]):
        # TODO: consider raising an exception when this list is empty -- just for security?
        self.offers = offers
        self.mean_price = reduce(lambda value, acc: value + acc,
                                 map(lambda offer: offer.price, self.offers)) / len(self.offers)

    def get_best_offer(self) -> Offer:
        return sorted(self.offers, key=lambda p: p.price)[0]

    def get_offer_by_name(self, name: str) -> Offer:
        return next((offer for offer in self.offers if offer.name == name), None)
