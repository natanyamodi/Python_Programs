import pytest
import minDiff


@pytest.mark.parametrize(
    'heights, given_num, expected',
    [
        ([1, 15, 10], 6, 5),
        ([1, 15, 10, 5], 3, 8),
        ([1, 3], 5, 2),
        ([5, 7], 4, 2),
        ([1], 3, 0),
        ([7], 3, 0)
    ]
)
def test_find_get_min_height_difference(heights: list, given_num: int, expected: int):
    actual = minDiff.find_min_height_difference(heights, given_num)
    assert actual == expected
