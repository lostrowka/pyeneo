from src.CeneoAPIHandler import CeneoAPIHandler
from src.models.item_query import ItemQuery
from datetime import datetime

from src.processors.search_results_processor import SearchResultsProcessor

item_query = ItemQuery("pralka wsad 7 kg", 1, 1000, 1600, datetime.now())

print(item_query.create_url())

api_handler = CeneoAPIHandler()
html = api_handler.send_search_request(item_query).text

search_processor = SearchResultsProcessor(html, item_query)
search_processor.get_first_item_with_multiple_sellers()
