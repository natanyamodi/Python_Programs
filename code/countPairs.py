"""
this program is used to find the pairs having the given sum
"""
from typing import List, Optional
from sorting import sort_list


def count_pairs(elements: List[int], given_sum: int) -> Optional[int]:
    sorted_elements = sort_list(elements)
    start_idx, end_idx = 0, len(elements)-1
    count = 0
    while start_idx < end_idx:
        if elements[start_idx] + elements[end_idx] == given_sum:
            count += 1
        if elements[start_idx] + elements[end_idx] <= given_sum:
            start_idx += 1
        else:
            end_idx -= 1
    return count


if __name__ == '__main__':
    print(count_pairs([8, 2, 1, 7, 3, 7], 10))
