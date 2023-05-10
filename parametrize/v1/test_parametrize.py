import pytest

from main import calculate_total_price


@pytest.mark.parametrize("quantity, price, expected_total", [
    (5, 10, 50),      # Test Case 1
    (2, 7.5, 15),     # Test Case 2
    (0, 100, 0)       # Test Case 3
])
def test_calculate_total_price(quantity, price, expected_total):
    assert calculate_total_price(quantity, price) == expected_total