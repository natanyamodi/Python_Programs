"""
this program is used to find common elements in 3 lists
"""

from typing import List, Optional, TypeVar
T = TypeVar("T")


def find_common_elements(list1: List[T], list2: List[T], list3: List[T]) -> T:
    common = set()
    set1, set2 = set(list1), set(list2)
    for element in list3:
        if element in set1 and element in set2:
            common.add(element)
    return list(common)


if __name__ == '__main__':
    print(find_common_elements([1, 2], [4, 3], [6, 5]))
