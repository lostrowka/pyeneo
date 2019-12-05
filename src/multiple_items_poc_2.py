from server.website.models.deal import Deal
from server.website.models.item import Item
from server.website.models.offer import Offer
from server.website.models.seller import Seller
from server.website.processors.multiple_items_processor import MultipleItemsProcessor

# prepare offers
sample_offers = []
for i in range(1, 20):
    name = 'shop' + str(i)
    sample_offers.append(Offer(name=name, price=i+15, url=None, rating=i*11, opinions=10))

# prepare items
item1 = Item(prod_id='item1', prod_name='item1')
item1.set_offers(sample_offers[1:11])
item2 = Item(prod_id='item2', prod_name='item2')
item2.set_offers(sample_offers[2:12])
item3 = Item(prod_id='item3', prod_name='item3')
item3.set_offers(sample_offers[3:13])

items = [item1, item2, item3]

seller_names = MultipleItemsProcessor(items).get_unique_seller_names()
deals = MultipleItemsProcessor(items).get_deals()
