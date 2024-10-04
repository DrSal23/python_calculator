import pytest
from src.python_calculator.python_calculator import roman_to_int
from src.python_calculator.python_calculator import int_to_roman
from src.python_calculator.python_calculator import evaluate_expression
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
    
def test_int_to_roman_negative():
    with pytest.raises(ValueError, match="Negative numbers can't be represented in Roman numerals."):
        int_to_roman(-1)

# Test case for handling zero input in int_to_roman
def test_int_to_roman_zero():
    with pytest.raises(ValueError, match="Negative numbers can't be represented in Roman numerals."):
        int_to_roman(0)

# Test case for handling large numbers in int_to_roman
def test_int_to_roman_large_number():
    with pytest.raises(ValueError, match="You're going to need a bigger calculator."):
        int_to_roman(4000)

# Test case for zero result in evaluate_expression
def test_evaluate_expression_zero_result():
    result = evaluate_expression('I - I')
    assert result == "0 does not exist in Roman numerals."

# Test case for negative result in evaluate_expression
def test_evaluate_expression_negative_result():
    result = evaluate_expression('I - V')
    assert result == "Negative numbers can't be represented in Roman numerals."

# Test case for large result in evaluate_expression
def test_evaluate_expression_large_result():
    result = evaluate_expression('MMM + M')
    assert result == "You're going to need a bigger calculator."

# Test case for fractional result in evaluate_expression
def test_evaluate_expression_fractional_result():
    result = evaluate_expression('V / III')
    assert result == "There is no concept of a fractional number in Roman numerals."

# Test case for invalid Roman numeral syntax
def test_evaluate_expression_invalid_syntax():
    result = evaluate_expression('IIII + V')
    assert result == "I don't know how to read this."

# Test case for division by zero
def test_evaluate_expression_zero_division():
    result = evaluate_expression('X / 0')
    assert result == "I don't know how to read this."

# Test case for handling insufficient arguments in main
def test_main_no_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['python_calculator'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "I don't know how to read this."

# Test case for handling insufficient arguments
def test_main_insufficient_arguments(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['python_calculator', 'V'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "I don't know how to read this."

# Test case for successful Roman numeral conversion from integer
def test_command_line_conversion(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['python_calculator', 'IV'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == '4'


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






