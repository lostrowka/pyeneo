# pyeneo

**pyeneo** is a state-of-the-art Ceneo.pl handler written in **Python 3** as a project for **Software Engineering** 
class at AGH University of Science and Technology by:

* Łukasz Ostrówka,
* Maciej Kania,
* Maciej Jankowski.

## Prerequisites
* Python 3
* Beautiful Soup
* Django //version?

## Running the application
```bash
git clone <<repo URL>>
cd pyeneo
??? 
```

# implementation details

## data structures

### Offer
Offer is a class containing single offer for a specific product. Fields are self-explanatory.

### ItemQuery
Class reflecting a searchbar entry in the service. Consists of following fields with pretty much self-explanatory names:
* name: str = ""
* quantity: float = 0
* min_price: float = 0
* max_price: float = 0
* timestamp: str = None

ItemQuery has create_url method providing URL for website with according search results.
Apart from that this class has methods to validate entered prices for example, convert commas with dots (as decimal 
separators).

### Item
Class reflecting a specific item as returned in Ceneo search results. Fields:
* prod_id: str = ""
* parent_item_query: ItemQuery = None
* offers: List[Offer] = []
* mean_price: float = None

Item has method create_url similar to one implemented in ItemQuery.
get_price_by_seller returns either price for given seller or -1 if there is no such seller. This feauture is used to 
find sellers with all desired items later on.

Item has two Offer related mwethods, one returning best Offer chosen by lowest price. The other is used to get a 
desired Offer by its name.


## data flow

