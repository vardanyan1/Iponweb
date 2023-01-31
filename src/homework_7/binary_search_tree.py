from my_execptions import BinarySearchTreeException
from node import Node


class BinarySearchTree:
    def __init__(self, head: int = None):
        if (not isinstance(head, int)) or (head is not None):
            self.__head = Node(head)

    def __repr__(self):
        return f"BST with head: {self.__head.value}"

    """
    HEAD getter
    """

    @property
    def head(self) -> Node:
        return self.__head

    def insert(self, new_node: Node):
        if not isinstance(new_node, Node):
            raise BinarySearchTreeException("New node must be Node class")
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


tree = BinarySearchTree(120)
print(tree)
tree.insert(Node(20))
tree.insert(Node(18))
tree.insert(Node(19))

print(f"head.right: {tree.head.right}")
tree.insert(Node(210))
print(f"head.left: {tree.head.right}")
tree.insert(Node(10))
tree.insert(Node(10))
print(f"head.left.left: {tree.head.left.left}")
print(tree.travers())
# print(tree.head.right)
# print(tree.head.left)
# # tree.insert(Node(1))
# # tree.insert(Node(8))
