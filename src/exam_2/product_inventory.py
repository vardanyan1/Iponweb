from my_exceptions import ProductException
from typing import List


class Product:
    def __init__(self, price: int, id: int, quantity: int):
        self.price = price
        self.id = id
        self.quantity = quantity

    def __repr__(self):
        return f"Product id: {self.id}, price: {self.price}, quantity: {self.quantity}"

    def buy(self, count):
        if count > self.quantity:
            raise ProductException


class Inventory:
    def __init__(self, list: List[Product]):
        self.list = list

    def __repr__(self):
        return f"List of IDs: {self.list}"

    def get_by_id(self, id: int):
        for i in self.list:
            if i.id == id:
                return i

    def sum_of_products(self):
        sum = 0
        for id in self.list:
            sum += id.quantity * id.price

        return sum


p1 = Product(10, 1, 2)
p2 = Product(20, 2, 2)
p3 = Product(100, 3, 1)
inv = Inventory([p1, p2, p3])
print(inv.get_by_id(2))
print(inv.sum_of_products())
