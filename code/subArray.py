"""
this program is used to check if there is a subarray with sum as 0
"""
from typing import List, Optional


def sub_array(elements: List[int]) -> Optional[bool]:
    elements_set = set()
    sum = 0
    for i in range(len(elements)):
        sum += elements[i]
        if sum == 0 or sum in elements_set:
            return True
        elements_set.add(sum)
    return False


if __name__ == '__main__':
    print(sub_array([1, 2, 3, 0]))
