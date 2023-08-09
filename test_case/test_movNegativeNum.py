import pytest
import movNegativeNum


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([-12, 11, -13, -5, 6, -7, 5, -3, -6], [-12, -13, -5, -7, -3, -6, 5, 6, 11]),
        ([-1, -2], [-1, -2]),
        ([1, 2], [1, 2]),
        ([-1, 4], [-1, 4]),
        ([], [])
    ]
)
def test_mov_neg_num(lst: list, expected: list):
    actual = movNegativeNum.mov_neg_num(lst)
    assert actual == expected
    