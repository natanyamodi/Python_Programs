import pytest
import unionList


@pytest.mark.parametrize(
    'lst1, lst2, expected',
    [
        ([1, 3, 4], [2, 6, 7], [1, 2, 3, 4, 6, 7]),
        ([1], [3, 6], [1, 3, 6]),
        ([1, 4, 6], [0], [0, 1, 4, 6]),
        ([], [], [])
    ]
)
def test_union(lst1: list, lst2: list, expected: list):
    actual = unionList.union(lst1, lst2)
    assert actual == expected
