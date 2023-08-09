"""
This program is used to find 3 numbers that sum to a given value
"""
from typing import List, Optional, Tuple


def find_triplet(elements: List[int], sum: int) -> Optional[Tuple[int, int, int]]:
    elements_list = []
    for i in elements:
        if i < sum:
            elements_list.append(i)
    elements_list.sort()
    for i in range(len(elements_list)):
        j = i + 1
        k = len(elements_list) - 1
        while j < k:
            if elements_list[i] + elements_list[j] + elements_list[k] == sum:
                return elements_list[i], elements_list[j], elements_list[k]
            elif elements_list[i] + elements_list[j] + elements_list[k] < sum:
                j += 1
            else:
                k -= 1
    return 0, 0, 0


if __name__ == '__main__':
    print(find_triplet([], 24))
