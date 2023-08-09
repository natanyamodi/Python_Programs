"""
This program is used to find the maximum sum of i*list[i] among all the rotations
of the list
"""
from typing import List


def max_sum(elements: List[int]) -> int:
    sorted_list = sorted(elements)
    maxm_sum = 0
    for element, position in enumerate(sorted_list):
        maxm_sum += element * position
    return maxm_sum


if __name__ == '__main__':
    print(max_sum([]))
