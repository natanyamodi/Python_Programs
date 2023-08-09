"""
This program is used to find the length of the longest consecutive
subsequence
"""
from typing import List
from sorting import sort_list


def find_longest_conseq_subseq(elements: List[int]) -> int:
    longest = 0
    elements_set = set(elements)
    longest = 0
    for i in range(len(elements)):
        j = elements[i]
        while j in elements_set:
            j += 1
        longest = max(longest, j-elements[i])
    return longest


if __name__ == '__main__':
    print(find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2]))
