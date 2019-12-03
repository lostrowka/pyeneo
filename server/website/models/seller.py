from typing import Dict, List

from server.website.models.item import Item


class Seller:
    name: str
    stock: List[Dict]

    def __init__(self, name: str, items: List[Item] = None):
        self.name = name
        self.stock = []
        if items is not None:
            self.add_many(items)

    def add(self, item: Item):
        entry = {
            'item': item,
            'offer': item.get_offer_by_name(self.name),
            'price': item.get_price_by_seller(self.name),
        }
        self.stock.append(entry)

    def add_many(self, items: List[Item]):
        for item in items:
            self.add(item)
