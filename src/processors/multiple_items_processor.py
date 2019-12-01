from typing import List, Dict, Set

from src.models.deal import Deal
from src.models.item import Item

class MultipleItemsProcessor:

    @staticmethod
    def find_best_combination(items: List[Item]) -> List[Deal]:
        unique_sellers = MultipleItemsProcessor.__extract_unique_sellers(items)
        sellers_mapped_prices = MultipleItemsProcessor.__map_prices(unique_sellers, items)
        seller_full_match = MultipleItemsProcessor.__check_full_match(sellers_mapped_prices, items)

        deals = []
        best_effort_deal = Deal()
        for item in items:
            best_effort_deal.append(item, item.get_best_offer())

        deals.append(best_effort_deal)

        for dict in seller_full_match:
            tmp_deal = Deal()
            tmp_deal.append_dict(dict)
            deals.append(tmp_deal)

        return sorted(deals, key=lambda d: d.calculate_price())

    @staticmethod
    def __extract_unique_sellers(items: List[Item]) -> Set[str]:
        """helper method to extract unique sellers from list of items"""
        all_sellers = []
        for g in map(lambda item: (offer.name for offer in item.offers), items):
            for o in g:
                all_sellers.append(o)
        all_sellers = set(all_sellers)
        return all_sellers

    @staticmethod
    def __map_prices(sellers: Set[str], items: List[Item]) -> List[Dict]:
        possible_sellers = []
        for seller in sellers:
            tmp_seller = {'name': seller}
            for item in items:
                tmp_seller[item.prod_id+'_price'] = item.get_price_by_seller(seller)
                tmp_seller[item] = item

            possible_sellers.append(tmp_seller)
        return possible_sellers

    @staticmethod
    def __check_full_match(prices_to_sellers: List[Dict], items: List[Item]) -> List[Dict]:
        # TODO: get rid of items here -- maybe extract them from map
        return list(filter(lambda dict: MultipleItemsProcessor.has_all_items(dict, items), prices_to_sellers))

    @staticmethod
    def has_all_items(seller_dict: Dict, items: List[Item]) -> bool:
        """helper method to get sellers with each of given items"""
        return sum(seller_dict[item.prod_id + '_price'] for item in items) == sum(
            abs(seller_dict[item.prod_id + '_price']) for item in items)


