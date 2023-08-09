import pytest
import duplicates


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([1, 2, 3, 2, 3], [2, 3]),
        ([1, 1, 1, 1], [1]),
        ([1, 2, 3, 4], [])
    ]
)
def test_find_duplicates(lst: list, expected: list):
    actual = duplicates.find_duplicates(lst)
    assert actual == expected
