import requests
import logging


class CeneoAPIHandler:

    logging.basicConfig(filename='../logs/CeneoAPIHandler.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    def __init__(self):
        self.log_GET = "sending GET to {URL}"

    def send_search_request(self, itemQuery):
        url = itemQuery.create_url()
        logging.log(logging.INFO, self.log_GET.format(URL = url))
        return requests.request('GET', url)

    def send_product_request(self, item):
        pass
