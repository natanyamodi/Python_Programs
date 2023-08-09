import pytest
import longestConsecutiveSubseq
from typing import List


@pytest.mark.parametrize(
    'elements, expected',
    [
        ([1, 2, 3, 4], 4),
        ([9, 5, 2, 8, 7], 3),
        ([1], 1),
        ([], 0)
    ]
)
def test_find_longest_conseq_subseq(elements: List[int], expected: int):
    actual = longestConsecutiveSubseq.find_longest_conseq_subseq(elements)
    assert actual == expected
