import pytest
import occurence


@pytest.mark.parametrize(
    'lst, num, expected',
    [
        ([1, 2, 4, 3, 2], 2, 2),
        ([1, 1, 1, 5, 3, 7], 1, 3),
        ([1, 5, 3, 6, 3], 7, 0)
    ]
)
def test_finding_occurrence(lst: list, num: int, expected: int):
    actual = occurence.finding_occurrence(lst, num)
    assert actual == expected
