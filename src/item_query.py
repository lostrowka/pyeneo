from datetime import datetime
from .constants import Ceneo


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

    def create_url(self):
        """ Create URL for query with object params """
        return f"{Ceneo.URI};szukaj-{self.name};m{self.min_price};n{self.max_price};0112-0.htm"
