"""
this program is used to reverse the array
"""


def reverse(lst: list) -> list:
    i = 0
    j = len(lst) - 1
    while i <= j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst


if __name__ == '__main__':
    print(reverse([0, -2, 4, 6]))
