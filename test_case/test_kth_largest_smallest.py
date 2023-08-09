import pytest
import kth_largest_smallest


@pytest.mark.parametrize(
    'lst, k, expected',
    [
        ([4, 2, 1, 5], 2, (2, 4)),
        ([-5, 0, -2, -1], 4, (0, -5)),
        ([7, 10, 4, 3, 20, 15], 4, (10, 7)),
        ([1], 1, (1, 1)),
        ([2, -1], 1, (-1, 2)),
        ([7, 10, 4, 3, 20, 15], 10, (None, None))
    ]
)
def test_kth_large_small(lst: list, k: int, expected: tuple):
    actual = kth_largest_smallest.kth_large_small(lst, k)
    assert actual == expected
