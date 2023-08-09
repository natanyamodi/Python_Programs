"""
this program is used to sort an array of elements
"""


def sort_list(lst: list) -> list:
    for i in range(0, len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


if __name__ == '__main__':
    print(sort_list([1, 3, 2, 4, 5]))
