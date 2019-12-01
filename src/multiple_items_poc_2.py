from src.models.deal import Deal
from src.models.item import Item
from src.models.offer import Offer
from src.processors.multiple_items_processor import MultipleItemsProcessor

sample_offers = []
for i in range(1, 20):
    name = 'shop' + str(i)
    sample_offers.append(Offer(name=name, price=i+15, url=None, rating=i*11, opinions=10))

item1 = Item(prod_id='item1')
item1.set_offers(sample_offers[1:11])
item2 = Item(prod_id='item2')
item2.set_offers(sample_offers[2:12])
item3 = Item(prod_id='item3')
item3.set_offers(sample_offers[3:13])

items = [item1, item2, item3]

deal = Deal()
for i in items:
    deal.append(i, i.get_best_offer())
print(deal)
