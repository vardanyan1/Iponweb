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

    @staticmethod
    def insertion_sort(items: List[Union[int, float]], reverse: bool = False) -> List[Union[int, float]]:
        if not isinstance(items, List):
            raise MySortingException("Items must be List type object")
        if not all(isinstance(item, (int, float)) for item in items):
            raise MySortingException("All items in the list must be either int or float.")
        if not isinstance(reverse, bool):
            raise MySortingException("Reverse must be Bool type object")

        result = items.copy()

        for i in range(1, len(result)):
            j = i
            while j > 0 and (result[j - 1] > result[j] if not reverse else result[j - 1] < result[j]):
                result[j - 1], result[j] = result[j], result[j - 1]
                j -= 1
        return result

    @staticmethod
    def counting_sort(items: List[int], reverse: bool = False,
                      use_anyway: bool = False) -> List[int]:
        if not isinstance(items, List):
            raise MySortingException("Items must be list type object")
        if not all(isinstance(item, int) and item >= 0 for item in items):
            raise MySortingException("All items in the list must be non-negative int.")

        max_item = max(items)
        length = len(items)

        if not use_anyway and max_item / length > 3:
            raise MySortingException("Difference is too big, use other algorythm or change use_anyway to True")
        if not isinstance(reverse, bool):
            raise MySortingException("Reverse must be bool type object")

        indexing_list = [0 for _ in range(max_item+1)]
        for item in items:
            indexing_list[item] += 1

        result = []
        if not reverse:
            for i in range(max_item+1):
                for j in range(indexing_list[i]):
                    result.append(i)
        else:
            for i in range(max_item+1 - 1, -1, -1):
                for j in range(indexing_list[i]):
                    result.append(i)
        return result


items1 = [-6, 1, 2, 3, 5.5, 5.4, 4, -1, -66, -12]
items2 = [1, 2, 0, 3, 4, 5, 12, 7, 7, 10]

print(f"Merge Sorted: {Sorting.merge_sort(items1, reverse=False)}")
print(f"Merge Reversed: {Sorting.merge_sort(items1, reverse=True)}")
print(f"Insertion Sorted: {Sorting.insertion_sort(items1, reverse=False)}")
print(f"Insertion Reversed: {Sorting.insertion_sort(items1, reverse=True)}")
print(f"Counting Sorted: {Sorting.counting_sort(items2, reverse=False)}")
print(f"Counting Reversed: {Sorting.counting_sort(items2, reverse=True)}")
