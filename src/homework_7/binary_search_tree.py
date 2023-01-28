from my_execptions import BinarySearchTreeException
from node import Node

class BinarySearchTree:
    def __init__(self, head: Node = None):
        if (not isinstance(head, Node)) or head is None:
            self.__head = head

    def __repr__(self):
        return f"Binary Search Tree with head {self.__head}"

    def insert(self, new_node: Node):
        pass
