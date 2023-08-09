"""
this program is used to find missing integer from the array
"""


def missing(lst: list, n: int) -> int:
    sum_with_missing = (n*(n+1))//2
    sum = 0
    for i in range(n-1):
        sum += lst[i]
    missing_int = sum_with_missing - sum
    return missing_int


if __name__ == '__main__':
    print(missing([1, 3, 4], 4))
