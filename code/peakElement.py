"""
this program is used to find the peak element from a list. eg [1, 3, 2] 3 is the peak ele
which is bigger than its neighbours
"""
from typing import List, TypeVar, Optional
T = TypeVar("T")


def find_peak_element(elements: List[T]) -> Optional[int]:
    total_elements = len(elements)
    return None if total_elements <= 2 else _find_peak_element(elements, total_elements)


def _find_peak_element(elements: List[T], total_elements: int) -> Optional[int]:
    for idx in range(1, total_elements-1):
        if elements[idx] >= elements[idx-1] and elements[idx] >= elements[idx+1]:
            return elements[idx]
    return None


if __name__ == '__main__':
    print(find_peak_element([1, 2, 3]))
