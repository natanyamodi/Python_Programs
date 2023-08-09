"""
this program is used to rotate a list by one
"""


def rotate(lst: list) -> list:
    n = len(lst)
    new_lst = [None]*n
    i = 0
    while i < n-1:
        new_lst[i+1] = lst[i]
        i += 1
    new_lst[0] = lst[n-1]
    return new_lst


if __name__ == '__main__':
    print(rotate([1, 2]))
