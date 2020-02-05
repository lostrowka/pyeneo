class InvalidItemException(Exception):
    """ Raised if any of the required fields are None (in factory method) """
    pass


class MinGreaterThanMaxException(Exception):
    """ Raised if min_price is greater then max_price (in factory method) """
    pass


class ReputationNotInBoundariesException(Exception):
    """ Raised if reputation provided is > 5 or < 1 """
    pass


class CeneoWebDriverTimeoutException(Exception):
    """ Raised if WebDriver fails to load data in given timeout """
    pass


class InvalidDataTypeException(Exception):
    """ Raised if data type is wrong """
    pass
