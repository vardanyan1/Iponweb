from my_execptions import MySortingException
from typing import List, Union


class Sorting:
    def __init__(self):
        pass

    def __repr__(self):
        return "Sorting class with sorting methods"

    @staticmethod
    def merge_sort(items: List[Union[int, float]], reverse: bool = False) -> List[Union[int, float]]:
        if not isinstance(items, List):
            raise MySortingException("Items must be List type object")
        if not all(isinstance(item, (int, float)) for item in items):
            raise MySortingException("All items in the list must be either int or float.")
        if not isinstance(reverse, bool):
            raise MySortingException("Reverse must be Bool type object")

        length = len(items)
        if length <= 2:
            if length == 1:
                return items
            elif length == 2:
                if items[0] >= items[1]:
                    if not reverse:
                        items[0], items[1] = items[1], items[0]
                else:
                    if reverse:
                        items[0], items[1] = items[1], items[0]
                return items

        else:
            first_half = Sorting.merge_sort(items[:(length // 2)], reverse)
            second_half = Sorting.merge_sort(items[(length // 2):], reverse)
            result = []
            i, j = 0, 0
            while i < len(first_half) and j < len(second_half):
                if (not reverse and first_half[i] <= second_half[j]) or (reverse and first_half[i] >= second_half[j]):
                    result.append(first_half[i])
                    i += 1
                else:
                    result.append(second_half[j])
                    j += 1
            result.extend(first_half[i:])
            result.extend(second_half[j:])
            return result


items1 = [-6, 1, 2, 3, 5.5, 5.4, 4, -1, -66, -12]

print(f"Sorted: {Sorting.merge_sort(items1, reverse=False)}")
print(f"Reversed: {Sorting.merge_sort(items1, reverse=True)}")
