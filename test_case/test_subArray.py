import pytest
import subArray
from typing import List, Optional


@pytest.mark.parametrize(
    'elements, expected',
    [
        ([-3, 1, 2], True),
        ([1, 2, -2, 8], True),
        ([1, 0], True),
        ([0], True),
        ([1, 2, 3], False)
    ]
)
def test_sub_array(elements: List[int], expected: bool):
    actual = subArray.sub_array(elements)
    assert actual == expected


