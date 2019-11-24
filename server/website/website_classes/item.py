from datetime import datetime

from .website_exceptions import (InvalidItemException,
                                 MinGreaterThanMaxException,
                                 ReputationNotInBoundariesException)


class Item:
    """
    Class representing single Item wanted by user.

    Attributes
    -----------
    name : str
        String representing an Item name
    quantity : int
        Represents quantity of a single Item wanted by user. It should
        be greater then 0.
    price_min : int
        Represents the lower price boundary for the Item. It needs to be
        less than price_max.
    price_max : int
        Represents the higher price boundary for the Item. It needs to be
        greater than price_min.
    min_reputation : int
        Represents the minimal reputation of the seller. It needs to be
        in the range of <1, 5>
    url : str
        It is the url used for the first request to the website.
    timestamp : str
        Consists of a date and time of the first request to the website.
        It is a return value of datetime.now().__str__()

    Methods
    -----------
    create_url()
        Based on the ceneo RESTish API it creates url and sets the (TODO: figure out WHICH URL. Search? Product?
        Maybe the final offer (external shop)?) object parameter url to it.
    set_and_get_timestamp()
        Sets the object's timestamp to string representation of datetime.now().
        It also returns that value.
    validate_item(item_name, quantity, min_price, max_price, min_reputation)
        It is a factory (classmethod) for creating Items from a form sent by user.
        It contains data validation and raises exceptions if something is wrong
        with the data.
    """

    name = ''
    quantity = 1
    price_min = 0
    price_max = 0
    min_reputation = 0
    url = ''
    timestamp = None

    def __init__(self, name: str, quantity: int, price_min: int, price_max: int, min_reputation=4):
        self.name = name
        self.quantity = quantity
        self.price_min = price_min
        self.price_max = price_max
        self.min_reputation = min_reputation

    def __str__(self):
        # basically it is for debugging in development. That syntax works ONLY in Python 3.8
        return f'{self.name}, {self.quantity}, {self.price_min}, {self.price_max}, {self.min_reputation}'

    def create_url(self):
        pass

    def set_and_get_timestamp(self):
        self.timestamp = str(datetime.now())
        return self.timestamp

    @classmethod
    def validate_item(cls, item_name, quantity, min_price, max_price, min_reputation):
        if item_name == '' or quantity == '' or min_price == '' or max_price == '':
            # that validation is needed, because the way this webapp works is that
            # it always sends 5 forms, but those not filled by user will contain
            # empty strings as data
            raise InvalidItemException()

        min_price = int(min_price)
        max_price = int(max_price)

        if min_price > max_price:
            raise MinGreaterThanMaxException()

        quantity = int(quantity)

        if min_reputation == '':
            return cls(item_name, quantity, min_price, max_price)
        else:
            if int(min_reputation) > 5 or int(min_reputation) < 1:
                raise ReputationNotInBoundariesException()

        return cls(item_name, quantity, min_price, max_price, int(min_reputation))
