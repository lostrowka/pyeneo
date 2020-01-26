from typing import List

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from server.website.models.exceptions import (
    InvalidItemException, MinGreaterThanMaxException,
    ReputationNotInBoundariesException)
from server.website.models.item import ItemQuery
from .ceneo_api_handler import CeneoAPIHandler
from .forms import ItemForm
from .processors.multiple_items_processor import MultipleItemsProcessor
from .processors.product_offers_processor import ProductOffersProcessor
from .processors.search_results_processor import SearchResultsProcessor


def request_page(request: WSGIRequest):
    if request.method == "POST":
        item_name_list = request.POST.getlist('item_name')
        quantity_list = request.POST.getlist('quantity')
        min_price_list = request.POST.getlist('min_price')
        max_price_list = request.POST.getlist('max_price')
        min_reputation_list = request.POST.getlist('min_reputation')

        queries = []

        for i in range(len(item_name_list)):
            try:
                item_query = ItemQuery.validate_query(item_name_list[i],
                                                      quantity_list[i],
                                                      min_price_list[i],
                                                      max_price_list[i],
                                                      min_reputation_list[i])
                queries.append(item_query)
            except InvalidItemException:
                if len(queries) > 0:
                    break
                else:
                    form_list = [ItemForm(), ItemForm(), ItemForm(), ItemForm(), ItemForm()]
                    return render(request=request,
                                  template_name='website/home.html',
                                  context={'form_list': form_list})

            except MinGreaterThanMaxException:
                messages = ['Cena minimalna jest większa od maksymalnej']
                form_list = [ItemForm(), ItemForm(), ItemForm(), ItemForm(), ItemForm()]
                return render(request=request,
                              template_name='website/home.html',
                              context={'form_list': form_list, 'messages': messages})

            except ReputationNotInBoundariesException:
                messages = ['Reputacja musi zawierać się w przedziale od 1 do 5']
                form_list = [ItemForm(), ItemForm(), ItemForm(), ItemForm(), ItemForm()]
                return render(request=request,
                              template_name='website/home.html',
                              context={'form_list': form_list, 'messages': messages})

        if len(queries) > 0:
            deals = process_data(queries)
            return render(request=request,
                          template_name='website/output.html',
                          context={'deals': deals})

    form_list = [ItemForm(), ItemForm(), ItemForm(), ItemForm(), ItemForm()]
    return render(request=request,
                  template_name='website/home.html',
                  context={'form_list': form_list})


def process_data(queries: List[ItemQuery]):
    api_handler = CeneoAPIHandler()
    items = []
    for item_query in queries:
        item_query_html = api_handler.send_search_request(item_query)
        search_processor = SearchResultsProcessor(item_query_html, item_query)

        item = search_processor.get_first_item_with_multiple_sellers()
        item_html = api_handler.send_product_request(item)

        product_processor = ProductOffersProcessor(item_html, item)
        item.offers = product_processor.get_offers_list(res_len=10)
        items.append(item)

    multiple_items_processor = MultipleItemsProcessor(items)
    return multiple_items_processor.get_deals()
