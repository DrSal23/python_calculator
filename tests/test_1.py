import pytest
from src.python_calculator.python_calculator import roman_to_int
from src.python_calculator.python_calculator import main


def test_I():
    res = roman_to_int("I")
    assert res == 1

#def test_IplusI(monkeypatch, capsys):
def test_complex_expression(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['python_calculator', 'X', '+', 'X', '*', 'II'])

    main()
    captured = capsys.readouterr()

    assert captured.out.strip() == 'XXX'
    



def test_1():
    assert 1 == 1

def test_IV(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['python_calculator', 'V', '-', 'I'])

    main()
    captured = capsys.readouterr()

    assert captured.out.strip() == 'IV'


def test_IV_toint():
    res = roman_to_int("IV")
    assert res == 4