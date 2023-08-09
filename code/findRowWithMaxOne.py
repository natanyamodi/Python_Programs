"""
This program is used to find the row with the max numbers of 1's
"""
from typing import List


def find_row_with_max_ones(number_matrix: List[List[int]]) -> List[int]:
    max_count = 0
    counting_ones = []
    for row in number_matrix:
        count = row.count(1)
        counting_ones.append(count)
    row_no = [idx for idx, max_value in enumerate(counting_ones) if max_value == max(counting_ones)]
    return row_no


if __name__ == '__main__':
    print(find_row_with_max_ones([[], []]))
