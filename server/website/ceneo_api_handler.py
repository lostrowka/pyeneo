import logging

from requests import Response, request
from server.website.models.item import Item
from server.website.models.item_query import ItemQuery


class CeneoAPIHandler:
    """ Class handling HTTP requests to Ceneo based on ItemQuery and Item """

    def __init__(self):
        self.log_GET = "sending GET to {URL}"
        self.log = logging.getLogger(CeneoAPIHandler.__name__)

    def send_search_request(self, item_query: ItemQuery) -> Response:
        """ Serve HTTP GET request regarding desired item """
        url = item_query.create_url()
        self.log.info(self.log_GET.format(URL=url))
        return request('GET', url)

    def send_product_request(self, item: Item) -> Response:
        """ Serve HTTP GET request regarding specific item to obtain sorted list of prices """
        url = item.create_url()
        self.log.info(self.log_GET.format(URL=url))
        return request('GET', url)
