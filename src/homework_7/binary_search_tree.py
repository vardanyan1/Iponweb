from my_execptions import BinarySearchTreeException
from node import Node


class BinarySearchTree:
    def __init__(self, head: int = None):
        if isinstance(head, int) and (head is not None):
            self.__head = Node(head)
        else:
            self.__head = None

    def __repr__(self):
        return f"BST with head: {self.__head.value if self.__head else None}"

    """
    HEAD getter
    """

    @property
    def head(self) -> Node:
        return self.__head

    def insert(self, new_node: int):
        if not isinstance(new_node, int):
            raise BinarySearchTreeException("New node must be integer")
        new_node = Node(new_node)
        if self.__head is None:
            self.__head = new_node
        else:
            self.__insertion(current_node=self.__head, new_node=new_node)

    def __insertion(self, current_node: Node, new_node: Node):
        if current_node is None:
            return new_node
        else:
            if current_node.value == new_node.value:
                current_node.count += 1
                return current_node
            elif current_node.value < new_node.value:
                current_node.right = self.__insertion(current_node.right, new_node)
            else:
                current_node.left = self.__insertion(current_node.left, new_node)
        return current_node

    def travers(self):
        print(self.__travers(current_node=self.__head, string="Inorder: "))

    def __travers(self, current_node: Node, string: str):
        if current_node is not None:
            string = self.__travers(current_node.left, string)
            string += f"{current_node.value}({current_node.count}) "
            string = self.__travers(current_node.right, string)
        return string

    @staticmethod
    def __min_value_node(node: Node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, delete_node: int):
        if not isinstance(delete_node, int):
            raise BinarySearchTreeException("Deleting node must be integer")
        self.__deletion(current_node=self.__head, value=delete_node)

    def __deletion(self, current_node: Node, value: int):
        if current_node is None:
            return current_node

        if current_node.left is None and current_node.right is None:
            self.__head = None

        if value < current_node.value:
            current_node.left = self.__deletion(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__deletion(current_node.right, value)
        else:
            if current_node.count > 1:
                current_node.count -= 1
                return current_node
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            min_larger_node = self.__min_value_node(current_node.right)
            current_node.right = self.__deletion(current_node.right, min_larger_node.value)

        return current_node

    def search(self, value: int):
        pass


tree = BinarySearchTree()
print(tree)
tree.insert(20)
tree.insert(18)
tree.insert(19)
tree.insert(210)
tree.insert(10)
# tree.insert(14)
tree.insert(10)
# tree.insert(15)
print(f"head.right: {tree.head.right}")
print(f"head.left: {tree.head.right}")
print(f"head.left.left: {tree.head.left.left}")
tree.travers()
tree.delete(10)
tree.delete(210)
tree.delete(10)
tree.delete(19)
tree.delete(20)
tree.delete(18)
tree.delete(120)
tree.delete(120)
tree.travers()
print(tree)
tree.insert(20)
tree.insert(20)
tree.insert(10)
tree.travers()

print(tree)


