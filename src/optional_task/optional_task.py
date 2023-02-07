from typing import List
from sortedcontainers import SortedList


def find_pair(arr: List[int], index_diff: int, value_diff: int):
    d = SortedList()
    for i, val in enumerate(arr):
        d.add((val, i))
        while 
    print(d)


print(find_pair([1, 2, 3, 1], 3, 0))
# print(find_pair([1, 5, 9, 1, 5, 9], 2, 3))
