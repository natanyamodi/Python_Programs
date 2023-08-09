import pytest
import subarr_sum


@pytest.mark.parametrize(
    'lst, start_idx, end_idx, expected',
    [
        ([1, 2, 3, 4, 5], 1, 3, 5),
        ([1, 2, 3], 1, 2, 2),
        ([-1, 3, 5, 3, 2], 0, 3, 7)
    ]
)
def test_sum_subarray_ele(lst: list, start_idx: int, end_idx: int, expected: int):
    actual = subarr_sum.sum_subarray_ele(lst, start_idx, end_idx)
    assert actual == expected
