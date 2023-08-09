import pytest
import revList


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([-1, -2], [-2, -1]),
        ([0], [0]),
        ([], [])
    ]
)
def test_reverse(lst: list, expected: list):
    actual = revList.reverse(lst)
    assert actual == expected
