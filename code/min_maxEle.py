"""
this program is used to find the minimum and the maximum number
from the list
"""
from typing import List, Optional, Tuple


def find_min_max(elements: List[int]) -> Optional[Tuple[int, int]]:
    total_elements = len(elements)
    return (None, None) if total_elements == 0 else _find_min_max(elements, total_elements)


def _find_min_max(elements: List[int], total_elements: int) -> Tuple[int, int]:
    min_element, max_element = elements[0], elements[0]
    for idx in range(1, total_elements):
        if elements[idx] < min_element:
            min_element = elements[idx]
        if elements[idx] > max_element:
            max_element = elements[idx]
    return min_element, max_element


if __name__ == '__main__':
    print(find_min_max([1, 2, 3]))
