
import pytest
import homework1.src.task2 as t2

# Verify that we get a float-ified version of the integer input
def test_intToFloat():
    assert t2.intToFloat(10) == 10.0

# Verify that the decimals are dropped
def test_floatToInt():
    assert t2.floatToInt(14.06) == 14

# Verify that we get the final character in the input string
def test_getFinalChar():
    assert t2.getFinalChar("Hello") == "o"

# Verify that the obviously equal numbers are read as such
def test_isEqual():
    assert t2.isEqual(116, 116) == True
    assert t2.isEqual(1, 2) == False