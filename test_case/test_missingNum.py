import pytest
import missingNum


@pytest.mark.parametrize(
    'lst, n, expected',
    [
        ([1, 2, 3, 5], 5, 4),
        ([1, 2, 3, 4], 5, 5),
        ([1, 2, 3, 5, 6], 6, 4)
    ]
)
def test_missing(lst: list, n: int, expected: int):
    actual = missingNum.missing(lst, n)
    assert actual == expected
