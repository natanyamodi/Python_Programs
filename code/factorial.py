"""
this program is used to find factorial of a large number like 100
"""


def fact(num: int) -> int:
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
    return fact


if __name__ == '__main__':
    print(fact(12345))
