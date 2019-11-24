from datetime import datetime
from src.constants import Ceneo
import logging


class ItemQuery:
    """ Class reflecting query for items with given name and given price range """

    name = ""
    quantity = 0
    min_price = 0
    max_price = 0
    timestamp = None

    def __init__(self, name: str, quantity: int, min_price: int, max_price: int, timestamp: datetime):
        """ Create new ItemQuery """
        self.name = name
        self.quantity = quantity
        self.min_price = min_price
        self.max_price = max_price
        self.timestamp = timestamp
        self.log_ItemQuery = "generating ItemQuery for {PRODUCT}"
        self.log = logging.getLogger(ItemQuery.__name__)

    def create_url(self) -> str:
        """ Create URL for query with object params """
        self.log.info(self.log_ItemQuery.format(PRODUCT=self.name))
        return f"{Ceneo.URI};szukaj-{self.name};m{self.min_price};n{self.max_price};0112-0.htm"
