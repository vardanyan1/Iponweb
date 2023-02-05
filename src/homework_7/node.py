from my_execptions import NodeException, RedBlackNodeException
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


class RedBlackNode(Node):
    def __init__(self, value: int, left: "RedBlackNode" = None, right: "RedBlackNode" = None, is_red: bool = True):
        super().__init__(value, left, right)
        self.parent = None
        self.__is_red = is_red

    def __repr__(self):
        return f"RedBlackNode with value: {self.value}, color: {'Red' if self.is_red else 'Black'}"

    @property
    def is_red(self):
        return self.__is_red

    @is_red.setter
    def is_red(self, new_is_red):
        if not isinstance(new_is_red, bool):
            raise RedBlackNodeException("Node color must be a boolean")
        self.__is_red = new_is_red
