import pytest
import common


@pytest.mark.parametrize(
    'lst1, lst2, lst3, expected',
    [
        ([1, 2, 3], [2, 3], [0, 2, 3], {2, 3}),
        ([1, 2, 3], [1], [0, 6, 1], {1}),
        ([1, 2], [3, 4], [6, 5], set()),
        ([1, 2], [2, 3], [3, 4], set()),
        ([1, 2, 3, 3], [2, 3, 3], [5, 2, 3, 3], {2, 3})
    ]
)
def test_common_ele(lst1: list, lst2: list, lst3: list, expected: list):
    actual = common.common_ele(lst1, lst2, lst3)
    assert actual == expected
