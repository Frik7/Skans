from enum import Enum, unique


@unique
class Currency(str, Enum):
    USD = "USD"
    ZAR = "ZAR"


@unique
class Side(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
