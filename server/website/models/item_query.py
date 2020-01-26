import logging
from datetime import datetime

from server.website.constants import Ceneo
from server.website.models.exceptions import InvalidItemException, MinGreaterThanMaxException, \
    ReputationNotInBoundariesException


class ItemQuery:
    """ Class reflecting query for items with given name and given price range """

    name: str = ""
    quantity: float = 0
    min_price: float = 0
    max_price: float = 0
    timestamp: str = None

    def __init__(self, name: str, quantity: int, min_price: float, max_price: float, min_reputation: float = 4):
        """ Create new ItemQuery """
        self.name = name
        self.quantity = quantity
        self.min_price = min_price
        self.max_price = max_price
        self.min_reputation = min_reputation
        self.timestamp = str(datetime.now())
        self.log = logging.getLogger(ItemQuery.__name__)

    def __str__(self):
        return f'{self.name}, {self.quantity}, {self.min_price}-{self.max_price}, {self.min_reputation}'

    def create_url(self) -> str:
        """ Create URL for query with object params """
        self.log.info(f"generating ItemQuery URL for {self.name}")
        return f"{Ceneo.URI};szukaj-{self.name};m{self.min_price};n{self.max_price};0112-0.htm"

    @classmethod
    def validate_query(cls, item_name: str, quantity: str, min_price: str, max_price: str, min_reputation: str):
        """ Server-side validation for product input from user """

        if item_name == '' or quantity == '' or min_price == '' or max_price == '':
            raise InvalidItemException()

        min_price = float(min_price.replace(",", "."))
        max_price = float(max_price.replace(",", "."))

        if min_price > max_price:
            raise MinGreaterThanMaxException()

        quantity = int(quantity)

        if min_reputation == '':
            return cls(item_name, quantity, min_price, max_price)

        if float(min_reputation) > 5 or float(min_reputation) < 0:
            raise ReputationNotInBoundariesException()

        return cls(item_name, quantity, min_price, max_price, float(min_reputation))
