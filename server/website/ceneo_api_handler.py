import logging

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from server.website.models.exceptions import CeneoWebDriverTimeoutException
from server.website.models.item import Item
from server.website.models.item_query import ItemQuery


class CeneoAPIHandler:
    """ Class handling HTTP requests to Ceneo based on ItemQuery and Item """

    def __init__(self):
        self.log_GET = "sending GET to {URL}"
        self.log = logging.getLogger(CeneoAPIHandler.__name__)

        self.driver = webdriver.Chrome()

        # Optional headless parameter, not tested properly
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        #
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def send_search_request(self, item_query: ItemQuery) -> str:
        """ Serve HTTP GET request regarding desired item """
        url = item_query.create_url()
        self.log.info(self.log_GET.format(URL=url))
        try:
            self.driver.get(url)
            # Wait until table with results load (wait for JS execution)
            WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_class_name("js_search-results"))
        except TimeoutError:
            raise CeneoWebDriverTimeoutException
        return self.driver.page_source

    def send_product_request(self, item: Item) -> str:
        """ Serve HTTP GET request regarding specific item to obtain sorted list of prices """
        url = item.create_url()
        self.log.info(self.log_GET.format(URL=url))
        try:
            self.driver.get(url)
            # Wait until table with product offers load (wait for JS execution)
            WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_class_name("product-offers"))
        except TimeoutError:
            raise CeneoWebDriverTimeoutException
        return self.driver.page_source
