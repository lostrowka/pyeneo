from server.website.models.item_query import ItemQuery
from server.website.views import process_data

item1 = ItemQuery('mysz', 1, 10, 40, 3)
item2 = ItemQuery('podkładka', 1, 20, 50, 4)
item3 = ItemQuery('komputer lenovo', 1, 100, 3000, 4)

output = process_data([item1, item2, item3])
print(str(output))
