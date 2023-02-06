from node import RedBlackNode
from my_execptions import RedBlackTreeException


class RedBlackTree:
    def __init__(self, head: int = None):
        if head is not None:
            self.__head = RedBlackNode(head, is_red=False)
        else:
            self.__head = None

    def __repr__(self):
        return f"Red-Black Tree with root node: {self.__head}"

    """
    HEAD getter
    """

    @property
    def head(self) -> RedBlackNode:
        return self.__head

    def insert(self, new_node: int):
        new_node = RedBlackNode(new_node, is_red=True)
        parent = None
        x = self.__head
        while x is not None:
            parent = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right
        new_node.parent = parent
        if parent is None:
            self.__head = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        self.__fix_insert(new_node)

    def __fix_insert(self, node: RedBlackNode):
        while node.parent is not None and node.parent.is_red is True:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.is_red is True:
                    node.parent.is_red = False
                    uncle.is_red = False
                    node.parent.parent.is_red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__left_rotate(node)
                    node.parent.is_red = False
                    node.parent.parent.is_red = True
                    self.__right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.is_red is True:
                    node.parent.is_red = False
                    uncle.is_red = False
                    node.parent.parent.is_red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__right_rotate(node)
                    node.parent.is_red = False
                    node.parent.parent.is_red = True
                    self.__left_rotate(node.parent.parent)
        self.__head.is_red = False

    def __minimum(self, node: RedBlackNode):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def __left_rotate(self, node: RedBlackNode):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.__head = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def __right_rotate(self, node: RedBlackNode):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.__head = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def __rb_transplant(self, u, v):
        if u.parent is None:
            self.__head = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def travers(self):
        return self.__travers(current_node=self.__head, string="Inorder: ")

    def __travers(self, current_node: RedBlackNode, string: str):
        if current_node is not None:
            string = self.__travers(current_node=current_node.left, string=string)
            string += str(current_node.value) + " "
            string = self.__travers(current_node=current_node.right, string=string)
        return string

    def __search(self, value: int):
        current_node = self.__head
        while current_node is not None and current_node.value != value:
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def delete(self, value: int):
        node = self.__search(value)
        if node is not None:
            self.__delete(node)

    def __delete(self, node: RedBlackNode):
        original_color = node.is_red
        if node.left is None:
            replacement = node.right
            self.__rb_transplant(node, node.right)
        elif node.right is None:
            replacement = node.left
            self.__rb_transplant(node, node.left)
        else:
            minimum_node = self.__minimum(node.right)
            original_color = minimum_node.is_red
            replacement = minimum_node.right
            if minimum_node.parent == node:
                replacement.parent = minimum_node
            else:
                self.__rb_transplant(minimum_node, minimum_node.right)
                minimum_node.right = node.right
                minimum_node.right.parent = minimum_node
            self.__rb_transplant(node, minimum_node)
            minimum_node.left = node.left
            minimum_node.left.parent = minimum_node
            minimum_node.is_red = node.is_red
        if not original_color:
            self.__fix_delete(replacement)

    def __fix_delete(self, node: RedBlackNode):
        while node != self.__head and not node.is_red:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.is_red:
                    sibling.is_red = False
                    node.parent.is_red = True
                    self.__left_rotate(node.parent)
                    sibling = node.parent.right
                if not sibling.left.is_red and not sibling.right.is_red:
                    sibling.is_red = True
                    node = node.parent
                else:
                    if not sibling.right.is_red:
                        sibling.left.is_red = False
                        sibling.is_red = True
                        self.__right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.is_red = node.parent.is_red
                    node.parent.is_red = False
                    sibling.right.is_red = False
                    self.__left_rotate(node.parent)
                    node = self.__head
            else:
                sibling = node.parent.left
                if sibling.is_red:
                    sibling.is_red = False
                    node.parent.is_red = True
                    self.__right_rotate(node.parent)
                    sibling = node.parent.left
                if not sibling.right.is_red and not sibling.left.is_red:
                    sibling.is_red = True
                    node = node.parent
                else:
                    if not sibling.left.is_red:
                        sibling.right.is_red = False
                        sibling.is_red = True
                        self.__left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.is_red = node.parent.is_red
                    node.parent.is_red = False
                    sibling.left.is_red = False


tree = RedBlackTree()
print(tree)
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(5)
tree.insert(4)
tree.insert(2)
print(tree.travers())
print(f"head: {tree.head}")
print(f"head.left: {tree.head.left}")
print(f"head.left.left: {tree.head.left.left}")
print(f"head.left.left.left: {tree.head.left.left.left}")
print(f"head.left.right: {tree.head.left.right}")
print(f"head.right: {tree.head.right}")

tree.delete(2)
print(tree.travers())
# print()
# tree.delete(10)
# tree.delete(210)
# tree.delete(10)
# tree.delete(19)
# print(tree.travers())
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
# print(tree.travers())
