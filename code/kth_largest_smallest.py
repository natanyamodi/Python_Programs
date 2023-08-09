"""
this program is used to find the kth largest and smallest
number from the unsorted list
"""
from typing import List, Tuple, Optional


def find_kth_largest_smallest_element(elements: List[int], k: int) -> Optional[Tuple[int, int]]:
    elements_set = set(elements)
    kth_smallest, kth_largest = 0, 0
    for element in elements_set:
        if k == 1:
            kth_smallest = element
        if k == -1:
            kth_largest = element
        k -= 1
    return kth_smallest, kth_largest


if __name__ == '__main__':
    print(find_kth_largest_smallest_element([12, 3, 5, 7, 19], 4))
