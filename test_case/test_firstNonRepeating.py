import pytest
import firstNonRepeating


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([1, 2, 3, 1, 2], 3),
        ([1, 2, 1, 2], None),
        ([1, 2, 3], 1)
    ]
)
def test_first_non_repeating(lst: list, expected: int):
    actual = firstNonRepeating.find_first_non_repeating_element(lst)
    assert actual == expected
