import pytest
import homework1.src.task3 as t3

def test_getSign():
    assert t3.getSign(-14) == "Negative"

def test_printFirst10Primes(capsys):
    t3.printFirst10Primes()
    output = capsys.readouterr()
    assert output.out == "2 3 5 7 11 13 17 19 23 29 "

def test_sum1To100():
    assert t3.sum1To100() == 5050