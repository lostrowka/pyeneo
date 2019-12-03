from typing import List, Dict

from server.website.models.item import Item
from server.website.models.offer import Offer


class Deal:
    """Class reflecting a set of offers each associated with specific product"""

    name: str
    items_to_offers: List[Dict]
    empty: bool
    single_item_template: str = "{ITEM} for {PRICE} in {SELLER}\n"

    def __init__(self):
        self.items_to_offers = []
        self.empty = True

    def __str__(self) -> str:
        result = ''
        for d in self.items_to_offers:
            # TODO: use item.name instead of item.prod_id here
            result += self.single_item_template.format(ITEM=d['item'].prod_id,
                                                       PRICE=d['offer'].price,
                                                       SELLER=d['offer'].name)
        return result

    def append(self, item: Item, offer: Offer):
        self.empty = False
        self.items_to_offers.append({'item': item, 'offer': offer})

    def calculate_price(self) -> float:
        """returns dynamically calculated price"""
        return sum(d['offer'].price for d in self.items_to_offers)
