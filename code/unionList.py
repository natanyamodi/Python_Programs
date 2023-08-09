"""
this program is used to find a union of 2 sorted lists
"""


def union(lst1: list, lst2: list) -> list:
    n1 = len(lst1)
    n2 = len(lst2)
    i = 0
    j = 0
    union_lst = []
    for ui in range(n1 + n2):
        if i < n1 and (j >= n2 or lst1[i] < lst2[j]):
            union_lst.append(lst1[i])
            i += 1
        else:
            union_lst.append(lst2[j])
            j += 1
    return union_lst


if __name__ == '__main__':
    print(union([1, 3, 5], [2]))
