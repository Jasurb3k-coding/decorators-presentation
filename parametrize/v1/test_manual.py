# !pip install pytest
import pytest

from main import calculate_total_price


def test_calculate_total_price():
    # Test Case 1
    quantity = 5
    price = 10
    expected_total = 50
    assert calculate_total_price(quantity, price) == expected_total

    # Test Case 2
    quantity = 2
    price = 7.5
    expected_total = 15
    assert calculate_total_price(quantity, price) == expected_total

    # Test Case 3
    quantity = 0
    price = 100
    expected_total = 0
    assert calculate_total_price(quantity, price) == expected_total
