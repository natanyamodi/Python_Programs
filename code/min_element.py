"""
This program is used to find the minimum element from the sorted and
rotated list
"""
from typing import List


def find_min_element(elements: List[int], start_idx: int, end_idx: int) -> int:
    if start_idx == end_idx:
        return elements[start_idx]
    mid_idx = (start_idx + end_idx)//2
    if mid_idx < end_idx and elements[mid_idx+1] < elements[mid_idx]:
        return elements[mid_idx+1]
    if mid_idx > start_idx and elements[mid_idx] < elements[mid_idx-1]:
        return elements[mid_idx]
    if elements[end_idx] > elements[mid_idx]:
        return find_min_element(elements, start_idx, mid_idx-1)
    return find_min_element(elements, mid_idx+1, start_idx)


if __name__ == '__main__':
    print(find_min_element([5, 6, 1, 2, 3, 4], 0, 5))
