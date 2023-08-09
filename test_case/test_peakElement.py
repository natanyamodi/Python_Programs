import pytest
from typing import List, TypeVar, Optional
T = TypeVar("T")
import peakElement


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([1, 3, 2], 3),
        ([1], None),
        ([1, 3], None),
        ([3, 1], None),
        ([1, 2, 3], None),
        ([4, 6, 3, 8], 6),
        ([], None)
    ]
)
def test_peak_ele(lst: List[T], expected: int):
    actual = peakElement.find_peak_element(lst)
    assert actual == expected
