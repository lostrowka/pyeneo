from typing import List, Dict, Tuple

from server.website.models.item import Item
from server.website.models.offer import Offer
from server.website.models.seller import Seller


class Deal:
    """Class reflecting a set of offers each associated with specific product"""

    name: str
    items_to_offers: List[Tuple[Item, Offer]]
    empty: bool
    single_item_template: str = "{ITEM} for {PRICE} in {SELLER}\n"

    def __init__(self):
        self.items_to_offers = []
        self.empty = True

    def __str__(self) -> str:
        result = ''
        for d in self.items_to_offers:
            result += self.single_item_template.format(ITEM=d[0].prod_name,
                                                       PRICE=d[1].price,
                                                       SELLER=d[1].name)
        return result

    def append(self, item: Item, offer: Offer):
        self.empty = False
        self.items_to_offers.append((item, offer,))

    # TODO: price should be multiplied by quantity
    def calculate_price(self) -> str:
        """returns dynamically calculated price"""
        price = sum(d[1].price for d in self.items_to_offers)
        return "{:.2f}".format(price) + ' zł'

    @classmethod
    def assemble_a_deal(cls, seller: Seller):
        deal = Deal()
        for entry in seller.stock:
            if entry['offer'] is not None:
                deal.append(entry['item'], entry['offer'])
            else:
                deal.append(entry['item'], entry['item'].get_best_offer())
        return deal
