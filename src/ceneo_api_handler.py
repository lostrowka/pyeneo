import requests
import logging

from src.models.item import Item
from src.models.item_query import ItemQuery


class CeneoAPIHandler:
    """ Class handling HTTP requests to Ceneo based on ItemQuery and Item """

    def __init__(self):
        self.log_GET = "sending GET to {URL}"
        self.log = logging.getLogger(CeneoAPIHandler.__name__)

    def send_search_request(self, item_query: ItemQuery) -> requests.Response:
        """ Serve HTTP GET request regarding desired item """
        url = item_query.create_url()
        self.log.info(self.log_GET.format(URL=url))
        return requests.request('GET', url)

    def send_product_request(self, item: Item) -> requests.Response:
        """ Serve HTTP GET request regarding specific item to obtain sorted list of prices """
        url = item.create_url()
        self.log.info(self.log_GET.format(URL=url))
        return requests.request('GET', url)
