"""
this program is used to find the first non repeating number from the list
"""
from typing import List, TypeVar
T = TypeVar("T")


def find_first_non_repeating_element(elements: List[T]):
    count_dict = dict()
    for element in elements:
        count = count_dict.get(element, 0)
        count_dict[element] = count + 1
    for element, count in count_dict.items():
        if count == 1:
            return element
    return None


if __name__ == '__main__':
    print(find_first_non_repeating_element([2, 3, 2, 3, 4]))
