from my_exceptions import MoneyException
from typing import Union

class Money:
    exchange = {'AMD': 1, 'RUB': 5.8, 'USD': 400, 'EUR': 430}

    def __init__(self, amount: float, currency: str):
        if isinstance(amount, (int, float)) and amount >= 0:
            self.__amount = amount
        else:
            raise MoneyException(f"Amount must be non-negative number")

        if isinstance(currency, str) and currency.upper() in Money.exchange.keys():
            self.__currency = currency.upper()
        else:
            raise MoneyException(f"Wrong currency name pick from: {Money.exchange.keys()}")

    def __repr__(self):
        return f"{self.__amount} {self.__currency}"

    def __add__(self, other: "Money"):
        if not isinstance(other, Money):
            raise MoneyException(f"Can add only Money class")
        if self.__currency != other.__currency:
            other = other.convert(self.__currency)
        return Money(self.__amount + other.__amount, self.__currency)

    def __sub__(self, other: "Money"):
        if not isinstance(other, Money):
            raise MoneyException(f"Can sub only Money class")
        if self.__currency != other.__currency:
            other = other.convert(self.__currency)
        return Money(self.__amount - other.__amount, self.__currency)

    def __truediv__(self, other: Union[int, float]):
        if not isinstance(other, (float, int)):
            raise MoneyException(f"Can divide only on number")
        if other > 0:
            return Money(round(self.__amount / other, 2), self.__currency)
        else:
            raise MoneyException("Can divide only on positive number")

    def __eq__(self, other: "Money"):
        if not isinstance(other, Money):
            raise MoneyException("Can compare only with Money class")
        if self.__currency != other.__currency:
            other = other.convert(self.__currency)
        return self.__amount == other.__amount

    def __ne__(self, other: "Money"):
        if not isinstance(other, Money):
            raise MoneyException("Can compare only with Money class")
        if self.__currency != other.__currency:
            other = other.convert(self.__currency)
        return self.__amount != other.__amount

    def __lt__(self, other: "Money"):
        if not isinstance(other, Money):
            raise MoneyException("Can compare only with Money class")
        if self.__currency != other.__currency:
            other = other.convert(self.__currency)
        return self.__amount < other.__amount

    def __gt__(self, other: "Money"):
        if not isinstance(other, Money):
            raise MoneyException("Can compare only with Money class")
        if self.__currency != other.__currency:
            other = other.convert(self.__currency)
        return self.__amount > other.__amount

    def __le__(self, other: "Money"):
        if not isinstance(other, Money):
            raise MoneyException("Can compare only with Money class")
        if self.__currency != other.__currency:
            other = other.convert(self.__currency)
        return self.__amount <= other.__amount

    def __ge__(self, other: "Money"):
        if not isinstance(other, Money):
            raise MoneyException("Can compare only with Money class")
        if self.__currency != other.__currency:
            other = other.convert(self.__currency)
        return self.__amount >= other.__amount

    """
    AMOUNT, CURRENCY setter, getter
    """

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        if isinstance(amount, (int, float)) and amount >= 0:
            self.__amount = amount
        else:
            raise MoneyException(f"Amount must be non-negative number")

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency: str):
        if isinstance(currency, str) and currency.upper() in Money.exchange.keys():
            self.__currency = currency.upper()
        else:
            raise MoneyException(f"Wrong currency name pick from: {Money.exchange.keys()}")

    def convert(self, currency: str):
        if isinstance(currency, str) and currency.upper() in Money.exchange.keys():
            converted = self.__amount / Money.exchange[currency.upper()] * Money.exchange[self.__currency]
            return Money(round(converted, 2), currency.upper())
        else:
            raise MoneyException(f"Wrong currency name pick from: {Money.exchange.keys()}")


# a = Money(400, 'amd')
# b = Money(2, 'usd')
#
# print(f"a: {a}, b: {b}")
# print(f"Get a currency: {a.currency}")
# print(f"Convert a to USD: {a.convert('usd')}")
# print(f"a/2: {a/2}")
# print(f"Is a grater than b?: {a>b}")
