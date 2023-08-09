import pytest
import maxSum


@pytest.mark.parametrize(
    'elements, expected',
    [
        ([8, 13, 1, 2], 57),
        ([8], 0),
        ([8, 1], 8),
        ([1, 2, 3], 8),
        ([], 0)
    ]
)
def test_max_sum(elements: list, expected: int):
    actual = maxSum.max_sum(elements)
    assert actual == expected
    