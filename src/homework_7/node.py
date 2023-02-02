from my_execptions import NodeException
from typing import Union

class Node:
    def __init__(self, value: int, left: "Node" = None, right: "Node" = None):
        if not isinstance(value, int):
            raise NodeException("Node value must be integer")
        self.__value = value
        self.__left = left
        self.__right = right
        self.__count = 1

    def __repr__(self):
        return f"Node with value: {self.__value}"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, int):
            raise NodeException("Node value must be integer")
        self.__value = new_value

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, new_count):
        if not isinstance(new_count, int) and not new_count > 0:
            raise NodeException("Node count must be integer")
        self.__count = new_count

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, new_left):
        if not isinstance(new_left, (Node, type(None))):
            raise NodeException(f"Left Node must be Node class, you passed: {new_left}")
        self.__left = new_left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, new_right):
        if not isinstance(new_right, (Node, type(None))):
            raise NodeException(f"Right Node must be Node class, you passed: {new_right}")
        self.__right = new_right