"""
this program is used to find the sum of the contiguous subarray
with the largest sum
"""
from typing import List, TypeVar
T = TypeVar("T")


def max_subarr_sum(elements: List[T]) -> T:
    max_till_now = elements[0]
    max_ending = 0
    for i in range(0, len(elements)):
        max_ending = max_ending + elements[i]
        if max_ending < 0:
            max_ending = 0
        elif max_till_now < max_ending:
            max_till_now = max_ending
    return max_till_now


if __name__ == '__main__':
    print(max_subarr_sum([-3, 0, 9, -6]))
