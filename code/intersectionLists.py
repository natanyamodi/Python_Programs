"""
this program is used to find intersection of two sorted lists
"""


def intersection(lst1: list, lst2: list) -> list:
    intersection_lst = []
    for i in lst1:
        for j in lst2:
            if i == j:
                intersection_lst.append(i)
    return intersection_lst


if __name__ == '__main__':
    print(intersection([1, 2, 3], [2]))
