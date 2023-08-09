import pytest
import min_element


@pytest.mark.parametrize(
    'elements, start_idx, end_idx, expected',
    [
        ([5, 6, 1, 2, 3, 4], 0, 5, 1),
        ([15, 18, 12, 13], 0, 3, 12),
        ([1], 0, 0, 1),
        ([1, 2, 3], 0, 2, 1),
        ([3, 2, 1], 0, 2, 1),
    ]
)
def test_find_min_element(elements: list, start_idx: int, end_idx: int, expected: int):
    actual = min_element.find_min_element(elements, start_idx, end_idx)
    assert actual == expected
