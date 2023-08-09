"""
this program is used to move all the negative numbers to the left and
the positive to the right
"""


def mov_neg_num(lst: list) -> list:
    j = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
    return lst


if __name__ == '__main__':
    print(mov_neg_num([-12, 11, -13, -5, 6, -7, 5, -3, -6]))

