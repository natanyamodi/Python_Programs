"""
This program is used to minimize the difference between the heights of the
longest and shortest tower after increasing or decreasing the height of every
tower by K
"""
from typing import List, TypeVar
T = TypeVar("T")


def find_min_height_difference(heights: List[T], given_num: int) -> int:
    mid = (max(heights) + min(heights)) // 2
    new_heights = []
    for height in heights:
        if max(heights) - min(heights) < given_num:
            return max(heights) - min(heights)
        elif height < mid:
            new_heights.append(height + given_num)
        else:
            new_heights.append(height - given_num)
    return max(new_heights) - min(new_heights)


if __name__ == '__main__':
    print(find_min_height_difference([1, 3], 5))
