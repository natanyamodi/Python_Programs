import pytest
import findTriplet
from typing import List, Tuple


@pytest.mark.parametrize(
    'elements, sum, expected',
    [
        ([1, 2, 3, 4, 5], 9, (1, 3, 5)),
        ([12, 3, 4, 1, 6, 9], 24, (3, 9, 12)),
        ([1], 2, (0, 0, 0)),
        ([1, 2, 33, 4], 40, (0, 0, 0)),
        ([], 5, (0, 0, 0))
    ]
)
def test_find_triplet(elements: List[int], sum: int, expected: Tuple[int, int, int]):
    actual = findTriplet.find_triplet(elements, sum)
    assert actual == expected
