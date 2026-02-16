import pytest
import homework1.src.task3 as t3

# Try the different cases
def test_getSign():
    assert t3.getSign(-14) == "Negative"
    assert t3.getSign(14) == "Positive"
    assert t3.getSign(0) == "Zero"
    assert not t3.getSign("some thing") == "Zero"

# Verify that we generated the proper first 10 prime numbers
def test_printFirst10Primes(capsys):
    t3.printFirst10Primes()
    output = capsys.readouterr()
    assert output.out == "2 3 5 7 11 13 17 19 23 29 "

# Verify that the sum is equal to 5050
def test_sum1To100():
    assert t3.sum1To100() == 5050
