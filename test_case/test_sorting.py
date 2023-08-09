import pytest
import sorting


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([-1, -4, -2, -5], [-5, -4, -2, -1]),
        ([0, 1], [0, 1]),
        ([], [])
    ]
)
def test_sort_list(lst: list, expected: list):
    actual = sorting.sort_list(lst)
    assert actual == expected
