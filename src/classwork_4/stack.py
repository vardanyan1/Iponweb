from typing import List
from my_exceptions import StackException

"""
Write a Stack Class
"""


class Stack:
    def __init__(self, stack: List = None, max_size: int = 10):
        self.__max_size = max_size
        if stack:
            self.__stack = stack
            self.__size = len(stack)
        else:
            self.__stack = []
            self.__size = 0

    def __repr__(self):
        return f"{self.__stack}"

    def __len__(self):
        return len(self.__stack)

    def add(self, new_value):
        if self.__size == self.__max_size:
            raise StackException("The stack is full")
        elif self.__size < self.__max_size:
            self.__stack.append(new_value)
            self.__size += 1

    def take(self):
        if self.__size != 0:
            self.__size -= 1
            return self.__stack.pop()

    def is_empty(self):
        return True if self.__size == 0 else False


s1 = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9])
s1.add(99)
print(s1)
print(len(s1))
# s1.add(666)
# print(s1)
# print(len(s1))
print(s1.is_empty())
print(s1.take())
print(s1)
