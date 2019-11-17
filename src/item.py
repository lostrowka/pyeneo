from src.item_query import ItemQuery
from .constants import Ceneo


class Item:
    """ Class reflecting a specific item"""

    prod_id = ""
    # TODO: consider leaving item_query as "parent" to item
    parent_item_query = ""

    def __init__(self, prod_id: str, parent_item_query: ItemQuery = None):
        self.prod_id = prod_id
        self.parent_item_query = parent_item_query

    def create_url(self) -> str:
        """ Create URL for and item with specific ID sorted by lowest price (delivery included) """
        return f"{Ceneo.URI}{self.prod_id};0284-0.htm"
