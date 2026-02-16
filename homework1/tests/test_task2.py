
import pytest
import homework1.src.task2 as t2

def test_intToFloat():
    assert t2.intToFloat(10) == 10.0

def test_floatToInt():
    assert t2.floatToInt(14.06) == 14

def test_getFinalChar():
    assert t2.getFinalChar("Hello") == "o"

def test_isEqual():
    assert t2.isEqual(116, 116) == True