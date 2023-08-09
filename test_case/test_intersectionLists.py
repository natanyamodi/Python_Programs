import pytest
import intersectionLists


@pytest.mark.parametrize(
    'lst1, lst2, expected',
    [
        ([1, 2, 3], [2, 3, 4], [2, 3]),
        ([1, 2, 3], [], []),
        ([], [1, 2, 3], []),
        ([], [], []),
        ([1], [2], [])
    ]
)
def test_intersection(lst1: list, lst2: list, expected: list):
    actual = intersectionLists.intersection(lst1, lst2)
    assert actual == expected
