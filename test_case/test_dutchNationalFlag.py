import pytest
import dutchNationalFlag


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([1, 2, 0, 1, 2, 0], [0, 0, 1, 1, 2, 2]),
        ([1, 2, 1, 2], [1, 1, 2, 2]),
        ([2, 2, 2], [2, 2, 2]),
        ([0, 2, 0, 0], [0, 0, 0, 2]),
        ([], [])
    ]
)
def test_dnf(lst: list, expected: list):
    actual = dutchNationalFlag.dnf(lst)
    assert actual == expected
