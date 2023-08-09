import pytest
import max_subarrSum


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
        ([-1, 0, 1, 4], 5),
        ([-5, 5], 5),
    ]
)
def test_max_subarr_sum(lst: list, expected: int):
    actual = max_subarrSum.max_subarr_sum(lst)
    assert actual == expected
