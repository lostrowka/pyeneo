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
git clone arepo URL
cd pyeneo
??? 
```

# implementation details

## data structures

### Offer
Offer is a class containing single offer for a specific product. Fields are self-explanatory.

### ItemQuery
Class reflecting a search bar entry in the service. Consists of following fields with pretty much self-explanatory 
names:
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

### Deal
Deal is a structure bind Item to a suggested Offer.

Item has method create_url similar to one implemented in ItemQuery.
get_price_by_seller returns either price for given seller or -1 if there is no such seller. This feature is used to 
find sellers with all desired items later on.

Item has two Offer related methods, one returning best Offer chosen by lowest price.
The other is used to get a desired Offer by its name, it returns None if no such Offer was found. 

## Data Flow

![Data flow chart](https://github.com/lostrowka/pyeneo/blob/master/images/data_flow.png)


## Data Processing

### CeneoAPIHandler
This class is managing HTTP requests sent to Ceneo, logging included.

send_search_request method takes an ItemQuery as input and returns an HTTP response with according HTML.

send_product_request operates in the same manner but with a specific Item as input. This method is used to get 
details about specific offers.

### SearchResultsProcessor
SearchResultsProcessor is a HTML parser based on BeautifulSoup. It accepts a HTML document and corresponding 
ItemQuery. It is supposed to extract a desired Item or raise an Exception if there is no such Item.

### ProductOffersProcessor
ProductOffersProcessor is a similar HTML parser but for an Item. It provides a List of offers for a given Item.
It has several self-explanatory helper methods to get values such as prices, rating and number of opinions.

### MultipleItemsProcessor
MultipleItemsProcessor operates on a List of Items (each with at least one Offer) to find either the best Deal or at
 least the "best effort" one. "Best effort" meaning each Item is paired with its best Offer.
 
Algorithm:
1. extract List of sellers from List of Items
2. map each seller to Item and according price
3. create a "best effort" deal -- lowest Offer from every Item
4. find best seller with most items
5. sort obtained Deals by total price
6. return this List of Deals

