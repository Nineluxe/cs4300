import pytest
import homework1.src.task4 as t4

# Calculate this with integers first
def test_calculate_discount_int():
    assert t4.calculate_discount(15, 50) == 7.5

# Then calculate with floats
def test_calculate_discount_float():
    assert t4.calculate_discount(11, 0.5) == 5.50

# Finally input the data as strings
def test_calculate_discount_string():
    assert t4.calculate_discount("5", "50") == 2.50
