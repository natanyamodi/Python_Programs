"""
this program is used to find the duplicate numbers in a list
"""
from typing import List, Optional


def find_duplicates(elements: List[int]) -> Optional[List[int]]:
    unique = set()
    duplicates = set()
    for element in elements:
        if element in unique:
            duplicates.add(element)
        else:
            unique.add(element)
    return list(duplicates)


if __name__ == '__main__':
    print(find_duplicates([1, 2, 3, 2, 3, 3]))
