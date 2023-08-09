"""
this program is used to find the sum of elements in the subarray
"""


def sum_subarray_ele(lst: list, start_idx: int, end_idx: int) -> int:
    sum = 0
    for i in range(start_idx, end_idx):
        sum += lst[i]
    return sum


if __name__ == '__main__':
    print(sum_subarray_ele([1, 2, 3], 1, 2))
