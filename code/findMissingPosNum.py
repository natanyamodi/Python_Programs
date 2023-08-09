"""
This program is used to find the smallest positive number missing from the array
"""
from typing import List


def finding_missing_positive_num(numbers: List[int]) -> int:
    numbers.sort()
    res = 1
    for i in numbers:
        if res == i:
            res += 1
    return res


if __name__ == '__main__':
    print(finding_missing_positive_num([]))
