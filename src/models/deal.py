from typing import List, Dict

from src.models.item import Item
from src.models.offer import Offer


class Deal:
    """Class reflecting a set of offers each associated with specific product"""

    name: str
    items_to_offers: List[Dict]
    empty: bool

    def __init__(self):
        # self.name = name
        self.items_to_offers = []
        self.empty = True

    def append(self, item: Item, offer: Offer):
        self.empty = False
        self.items_to_offers.append({'item': item, 'offer': offer})

    def append_dict(self, matching_seller_dict: Dict):
        for item in filter(lambda k: (type(k) == Item), matching_seller_dict):
            self.append(item, item.get_offer_by_name(matching_seller_dict['name']))

    def calculate_price(self) -> float:
        """returns dynamically calculated price"""
        return sum(d['offer'].price for d in self.items_to_offers)
