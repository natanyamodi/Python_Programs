"""
this program is used to find the number of occurrences of a particular
integer in the list
"""


def finding_occurrence(lst: list, num: int) -> int:
    count = 0
    for i in range(len(lst)):
        if lst[i] == num:
            count += 1
    if count == 0:
        return 0
    return count


if __name__ == '__main__':
    print(finding_occurrence([1, 3, 6, 2, 2, 7, 3, 2], 2))
