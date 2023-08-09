import pytest
import firstRepeating


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([1, 2, 3, 2, 5, 3], 2),
        ([0, 0, 1, 2, 1], 0),
        ([1, 2, 3, 4], None),
        ([1, 2, 3, 1, 2, 3], 1)
    ]
)
def test_first_repeating(lst: list, expected: int):
    actual = firstRepeating.find_first_repeating_element(lst)
    assert actual == expected
