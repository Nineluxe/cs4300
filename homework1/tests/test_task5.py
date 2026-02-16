import pytest
import homework1.src.task5 as t5

def test_printFirstThreeFavs(capsys):
    t5.printFirstThreeFavs()
    output = capsys.readouterr()

    assert output.out == "IT Rosemary's Baby The Divine Farce "

def test_createStudentDatabase():
    assert t5.createStudentDatabase() == {'Bryce': '001', 'Alex': '002', 'Elijah': '003'}