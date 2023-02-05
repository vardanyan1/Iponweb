from node import RedBlackNode
from my_execptions import RedBlackTreeException

class RedBlackTree:
    def __init__(self, head: int = None):
        if isinstance(head, int) and (head is not None):
            self.__head = RedBlackNode(head, is_red=False)
        else:
            self.__head = None

    def __repr__(self):
        return f"RedBlackTree with head: {self.__head.value if self.__head else None}"

    """
    HEAD getter
    """

    @property
    def head(self) -> RedBlackNode:
        return self.__head

    def insert(self, new_node: int):
        if not isinstance(new_node, int):
            raise RedBlackTreeException("New node must be integer")
        new_node = RedBlackNode(new_node)
        self.__head = self.__insertion(current_node=self.__head, new_node=new_node)
        self.__head.is_red = False

    def __insertion(self, current_node: RedBlackNode, new_node: RedBlackNode):
        if current_node is None:
            return new_node
        else:
            if current_node.value == new_node.value:
                current_node.count += 1
                return current_node
            elif new_node.value < current_node.value:
                current_node.left = self.__insertion(current_node.left, new_node)
            else:
                current_node.right = self.__insertion(current_node.right, new_node)

        if current_node.is_red and current_node.right and current_node.right.is_red:
            current_node = self.__left_rotate(current_node)
        if current_node.is_red and current_node.left and current_node.left.is_red \
                and current_node.left.left and current_node.left.left.is_red:
            current_node = self.__right_rotate(current_node)
        if current_node.left and current_node.left.is_red and current_node.right and current_node.right.is_red:
            current_node = self.__color_flip(current_node)
        return current_node

    def __left_rotate(self, node: RedBlackNode):
        x = node.right
        node.right = x.left
        x.left = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def __right_rotate(self, node: RedBlackNode):
        x = node.left
        node.left = x.right
        x.right = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def __color_flip(self, node: RedBlackNode):
        node.is_red = True
        node.left.is_red = False
        node.right.is_red = False
        return node

    def travers(self):
        return self.__travers(current_node=self.__head, string="Inorder: ")

    def __travers(self, current_node: RedBlackNode, string: str):
        if current_node is not None:
            string = self.__travers(current_node.left, string)
            string += f"{current_node.value}({current_node.count}) "
            string = self.__travers(current_node.right, string)
        return string

    def delete(self, value: int):
        self.__head = self.__delete(self.__head, value)
        if self.__head:
            self.__head.is_red = False

    def __delete(self, node: RedBlackNode, value: int):
        if node is None:
            raise RedBlackTreeException("Node not found in the tree")
        if value < node.value:
            node.left = self.__delete(node.left, value)
        elif value > node.value:
            node.right = self.__delete(node.right, value)
        else:
            if node.count > 1:
                node.count -= 1
                return node
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            min_larger_node = node.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            node.value = min_larger_node.value
            node.right = self.__delete(node.right, min_larger_node.value)
        if node.is_red:
            return node
        if node.right and node.right.is_red:
            node = self.__left_rotate(node)
        if node.left and node.left.is_red and node.left.left and node.left.left.is_red:
            node = self.__right_rotate(node)
        if node.left and node.left.is_red and node.right and node.right.is_red:
            node = self.__color_flip(node)
        return node


tree = RedBlackTree()
print(tree)
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(10)
print(tree.travers())
print(f"head.right: {tree.head}")
print(f"head.left: {tree.head.left}")
print(f"head.left.left: {tree.head.left.left}")
print(f"head.left.left.left: {tree.head.left.left}")
print()
# tree.delete(10)
# tree.delete(210)
# tree.delete(10)
# tree.delete(19)
print(tree.travers())
# tree.delete(20)
# tree.delete(18)
# tree.delete(120)
# tree.delete(120)
# print(tree.travers())
# print(tree)
# tree.insert(20)
# tree.insert(20)
# tree.insert(10)
# print(tree.travers())
print(tree.travers())
