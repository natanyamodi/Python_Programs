import pytest
import countPairs
from typing import List


@pytest.mark.parametrize(
    'elements, s, expected',
    [
        ([1, 2, -2, 1], 3, 2),
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 6, 0),
        ([8, 2, 1, 7, 3], 10, 2)
    ]
)
def test_pairs_sum(elements: List[int], s: int, expected: int):
    actual = countPairs.count_pairs(elements, s)
    assert actual == expected
