from src.CeneoAPIHandler import CeneoAPIHandler
from src.models.item_query import ItemQuery
from datetime import datetime

item_query = ItemQuery("pralka wsad 7 kg", 1, 1000, 1600, datetime.now())

print(item_query.create_url())

api_handler = CeneoAPIHandler()
html = api_handler.send_search_request(item_query).text
