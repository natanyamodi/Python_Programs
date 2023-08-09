"""
this program is used ot sort an array of 0s, 1s and 2s
"""


def dnf(lst: list) -> list:
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            count_0 += 1
        elif lst[i] == 1:
            count_1 += 1
        else:
            count_2 += 1

    dnf_lst = []
    while count_0 > 0:
        dnf_lst.append(0)
        count_0 -= 1

    while count_1 > 0:
        dnf_lst.append(1)
        count_1 -= 1

    while count_2 > 0:
        dnf_lst.append(2)
        count_2 -= 1

    return dnf_lst


if __name__ == '__main__':
    print(dnf([1, 2, 0, 1, 2, 0]))

