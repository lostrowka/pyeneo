from .constants import Ceneo


class ItemQuery:
    name = ""
    quantity = 0
    min_price = 0
    max_price = 0
    timestamp = None

    def __init__(self, name, quantity, min_price, max_price, timestamp):
        self.name = name
        self.quantity = quantity
        self.min_price = min_price
        self.max_price = max_price
        self.timestamp = timestamp

    def create_url(self):
        return f"{Ceneo.URI};szukaj-{self.name};m{self.min_price};n{self.max_price};0112-0.htm"
