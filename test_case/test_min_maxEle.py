import pytest
import min_maxEle


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([1, 2, 3, 4], (1, 4)),
        ([5, 4, 3, 2, 1], (1, 5)),
        ([1], (1, 1)),
        ([], (None, None)),
        ([9, 8], (8, 9))
    ]
)
def test_min_max_ele(lst: list, expected: tuple):
    actual = min_maxEle.find_min_max(lst)
    assert actual == expected
    