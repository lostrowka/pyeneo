import logging
from typing import List

from bs4 import BeautifulSoup, element

from server.website.models.item import Item
from server.website.models.item_query import ItemQuery
from server.website.processors import DataProcessorException


class SearchResultsProcessor:
    html_soup = ""

    def __init__(self, html_doc: str, query: ItemQuery):
        self.html_soup = BeautifulSoup(html_doc, 'html.parser')
        self.log = logging.getLogger(SearchResultsProcessor.__name__)
        self.query = query

    def get_search_results_dom(self) -> element.Tag:
        return self.html_soup.find("div", class_="js_search-results")

    def get_item_results_list(self) -> List[element.Tag]:
        if self.get_search_results_dom() is not None:
            return self.get_search_results_dom().find_all("div", class_="js_category-list-item")

    def get_first_item_with_multiple_sellers(self) -> Item:
        """ Get first item with more than one seller """
        for item_dom in self.get_item_results_list():
            name_dom: element.Tag = item_dom.select_one("strong > a.go-to-product")
            go_to_dom: element.Tag = item_dom.select_one("a.go-to-product.btn")
            if name_dom and go_to_dom:
                self.log.info(f"Found item {go_to_dom['title']}")
                return Item(go_to_dom['href'][1:], name_dom.text.strip(), self.query)
        raise DataProcessorException(f"No item with more than 1 seller found in search results.")
