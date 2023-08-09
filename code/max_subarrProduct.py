"""
this program is used to find the sum of the contiguous subarray
with the largest product
"""
from typing import List, TypeVar
T = TypeVar("T")


def max_subarray_product(elements: List[T]) -> T:
    result = max(elements)
    cur_min, cur_max = 1, 1
    for element in elements:
        if element == 0:
            cur_min, cur_max = 1, 1
        temp = element * cur_max
        cur_max = max(element * cur_max, element * cur_min, element)
        cur_min = min(temp, element * cur_min, element)
        result = max(result, cur_max)
    return result


if __name__ == '__main__':
    print(max_subarray_product([-6, -3, -10, 0, 2]))
