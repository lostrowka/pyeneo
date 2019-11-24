class Offer:
    """ Object containing single offer for a specific product """

    def __init__(self, name: str, price: float, url: str, rating: float, opinions: int):
        """ Create new Offer """
        self.name = name
        self.price = price
        self.url = url
        self.rating = rating
        self.opinions = opinions

    def __str__(self):
        return f"{self.name} - {self.price} zł"
