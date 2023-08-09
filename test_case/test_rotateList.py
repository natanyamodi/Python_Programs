import pytest
import rotateList


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([1, 2, 3, 4], [4, 1, 2, 3]),
        ([0, 1, 2, 3, 4], [4, 0, 1, 2, 3]),
        ([1], [1]),
        ([1, 2], [2, 1])
    ]
)
def test_rotate(lst: list, expected: list):
    actual = rotateList.rotate(lst)
    assert actual == expected

