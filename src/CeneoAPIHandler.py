import requests
import logging

from src.item import Item
from src.item_query import ItemQuery


class CeneoAPIHandler:
    """ Class handling HTTP requests to Ceneo based on ItemQuery and Item """

    # append log entries to a file in appropriate
    logging.basicConfig(filename='../logs/pyeneo.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    def __init__(self):
        self.log_GET = "sending GET to {URL}"

    def send_search_request(self, item_query: ItemQuery) -> requests.Response:
        """ Serve HTTP GET request regarding desired item """
        url = item_query.create_url()
        logging.log(logging.INFO, self.log_GET.format(URL=url))
        return requests.request('GET', url)

    def send_product_request(self, item: Item) -> requests.Response:
        """ Serve HTTP GET request regarding specific item to obtain sorted list of prices """
        url = item.create_url()
        logging.log(logging.INFO, self.log_GET.format(URL=url))
        return requests.request('GET', url)
