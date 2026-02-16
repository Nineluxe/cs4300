import pytest
from homework1.src.task1 import helloWorld

def testHW(capsys):
    helloWorld() # Run the original function
    output = capsys.readouterr() # capsys.readouterr() captures .err and .out, which is the stdout
    assert output.out == "Hello, World!\n" # verify that the output matches

