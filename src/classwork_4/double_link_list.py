class Node:
    def __init__(self, value: int, prev: "Node" = None, next: "Node" = None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"{self.value}"

class DoubleLinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def __repr__(self):
        return f"DoubleLinkedList with head {self.head}"

    def append(self, new_node: Node):
        self.head.next = new_node
        new_node.prev = self.head

    def delete_at_head(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_at_tail(self):
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.prev.next = None

    def insert_at_tail(self, new_node: Node):
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
        new_node.prev = tail

    def insert_at_head(self, new_node: Node):
        self.head.prev = new_node
        new_node.next = self.head
        self.head = self.head.prev

    def search(self, value):
        node = self.head
        while node.value != value:
            if node.next:
                node = node.next
            else:
                return False

        return node


ll = DoubleLinkedList(Node(1))
print(ll)
ll.insert_at_tail(Node(2))
print(ll.head.next)
ll.insert_at_head(Node(0))
# print(ll.head.prev)
print(ll.search(2))
# print(ll.head)
