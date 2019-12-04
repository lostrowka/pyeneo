import logging
from typing import List, Set

from server.website.models.deal import Deal
from server.website.models.item import Item
from server.website.models.seller import Seller


class MultipleItemsProcessor:

    items: List[Item] = None
    item_names: str

    def __init__(self, items: List[Item]):
        self.items = items
        self.log = logging.getLogger(MultipleItemsProcessor.__name__)
        self.item_names = ', '.join(item.prod_id for item in self.items)

    def get_deals(self) -> List[Deal]:
        sellers = [Seller(name, self.items) for name in self.get_unique_seller_names()]

        deals = [self.assemble_a_deal(seller) for seller in sellers]
        self.log.info(f"assembled {len(deals)} deals for items {self.item_names}")

        return sorted(deals, key=lambda d: d.calculate_price())

    def get_unique_seller_names(self) -> Set[str]:
        return set(offer.name for offer in sum(map(lambda item: item.offers, self.items), []))

    @staticmethod
    def assemble_a_deal(seller: Seller) -> Deal:
        deal = Deal()
        for entry in seller.stock:
            if entry['offer'] is not None:
                deal.append(entry['item'], entry['offer'])
            else:
                deal.append(entry['item'], entry['item'].get_best_offer())
        return deal
