import pytest
import max_subarrProduct


@pytest.mark.parametrize(
    'elements, expected',
    [
        ([-6, -2, -3, 10, 9], 540),
        ([1, 2, 3], 6),
        ([1], 1),
        ([-6, -4, 20], 20)
    ]
)
def test_max_subarr_product(elements: list, expected: int):
    actual = max_subarrProduct.max_subarray_product(elements)
    assert actual == expected
