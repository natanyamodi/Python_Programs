import pytest
import findRowWithMaxOne
from typing import List


@pytest.mark.parametrize(
    'number_matrix, expected',
    [
        ([[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]], [2]),
        ([[1, 1, 0, 0], [0, 0, 0, 0]], [0]),
        ([[0, 1, 0, 1], [1, 1, 1, 1]], [1]),
        ([[0, 1], [0, 1]], [0, 1]),
        ([[0], [1]], [1]),
        ([[], []], [0, 1])
    ]
)
def test_find_row_with_max_ones(number_matrix: List[List[int]], expected: List[int]):
    actual = findRowWithMaxOne.find_row_with_max_ones(number_matrix)
    assert actual == expected
