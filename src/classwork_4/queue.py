from typing import List

"""
Write a Queue Class
"""


class Queue:
    def __init__(self, queue: List = None, max_size: int = 10):
        self.__max_size = max_size
        if queue:
            self.__queue = queue
            self.__size = len(queue)
        else:
            self.__queue = []
            self.__size = 0

    def __repr__(self):
        return f"{self.__queue}"

    def __len__(self):
        return len(self.__queue)

    def enqueue(self, new_value):
        if self.__size == self.__max_size:
            self.__queue.pop()
            self.__queue.insert(0, new_value)
        elif self.__size < self.__max_size:
            self.__queue.insert(0, new_value)
            self.__size += 1

    def dequeue(self):
        if self.__size != 0:
            self.__size -= 1
            return self.__queue.pop()

    def is_empty(self):
        return True if self.__size == 0 else False


q1 = Queue([1, 2, 3, 4, 5, 6, 7, 8, 9])
q1.enqueue(99)
print(q1)
print(len(q1))
q1.enqueue(666)
print(q1)
print(len(q1))
print(q1.is_empty())
print(q1.dequeue())
print(q1)