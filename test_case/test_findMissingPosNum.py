import pytest
import findMissingPosNum
from typing import List


@pytest.mark.parametrize(
    'numbers, expected',
    [
        ([2, 3, -7, 6, 8, 1, -10, 15], 4),
        ([1, -10, -20], 2),
        ([0, 1], 2),
        ([0], 1),
        ([], 1)
    ]
)
def test_finding_missing_positive_num(numbers: List[int], expected: int):
    actual = findMissingPosNum.finding_missing_positive_num(numbers)
    assert actual == expected
    