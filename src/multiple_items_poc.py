from server.website.ceneo_api_handler import CeneoAPIHandler
from server.website.models.item_query import ItemQuery
from datetime import datetime

from server.website.processors.multiple_items_processor import MultipleItemsProcessor
from server.website.processors.product_offers_processor import ProductOffersProcessor
from server.website.processors.search_results_processor import SearchResultsProcessor

item_query = ItemQuery("anysharp ostrzałka", 1, 50, 250)

print(item_query.create_url())

api_handler = CeneoAPIHandler()
item_query_html = api_handler.send_search_request(item_query).text

search_processor = SearchResultsProcessor(item_query_html, item_query)
item = search_processor.get_first_item_with_multiple_sellers()

print(item.create_url())

item_html = api_handler.send_product_request(item).text
product_processor = ProductOffersProcessor(item_html, item)

item.offers = product_processor.get_offers_list(res_len=10)
# for offer in item.prices:
#     print(offer)

# second_item_query = item_query
second_item_query = ItemQuery("bodum brazil zaparzacz", 1, 50, 140)

print(second_item_query.create_url())

second_item_query_html = api_handler.send_search_request(second_item_query).text

second_search_processor = SearchResultsProcessor(second_item_query_html, second_item_query)
second_item = second_search_processor.get_first_item_with_multiple_sellers()

print(second_item.create_url())

second_item_html = api_handler.send_product_request(second_item).text
second_product_processor = ProductOffersProcessor(second_item_html, second_item)

second_offers_list = second_product_processor.get_offers_list(res_len=10)

items = [item, second_item]
l = MultipleItemsProcessor.find_best_combination(items)
