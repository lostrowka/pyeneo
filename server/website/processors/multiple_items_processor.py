import logging
from typing import List, Dict, Set

from server.website.models.deal import Deal
from server.website.models.item import Item
from server.website.models.seller import Seller


class MultipleItemsProcessor:

    items: List[Item] = None
    item_names: str

    def __init__(self, items: List[Item]):
        self.items = items
        self.log = logging.getLogger(MultipleItemsProcessor.__name__)
        self.item_names = ''.join(item.prod_id+', ' for item in self.items)

    def get_deals(self) -> List[Deal]:
        all_seller_names = []
        for g in map(lambda item: (offer.name for offer in item.offers), self.items):
            for o in g:
                all_seller_names.append(o)
        all_seller_names = set(all_seller_names)

        sellers = [Seller(name, self.items) for name in all_seller_names]

        deals = [self.assemble_a_deal(seller) for seller in sellers]
        self.log.info(f"assembled {len(deals)} deals for items {self.item_names}")

        return sorted(deals, key=lambda d: d.calculate_price())

    @staticmethod
    def assemble_a_deal(seller: Seller) -> Deal:
        deal = Deal()
        for g in seller.goods:
            if g['offer'] is not None:
                deal.append(g['item'], g['offer'])
            else:
                deal.append(g['item'], g['item'].get_best_offer())
        return deal

