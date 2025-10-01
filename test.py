import pytest
from calculator import StringCalculator

@pytest.fixture
def calc():
    return StringCalculator()


def test_empty_string_returns_zero(calc):
    assert calc.add("") == 0

def test_single_number_returns_value(calc):
    assert calc.add("1") == 1
    assert calc.add("5") == 5

def test_two_numbers_sum(calc):
    assert calc.add("1,2") == 3
    assert calc.add("10,20") == 30


def test_multiple_numbers_sum(calc):
    assert calc.add("1,2,3,4,5") == 15


def test_newline_as_delimiter(calc):
    assert calc.add("1\n2,3") == 6

def test_invalid_newline_position(calc):
    assert calc.add("1,\n2") == 3 


def test_custom_delimiter(calc):
    assert calc.add("//;\n1;2") == 3
    assert calc.add("//|\n1|2|3") == 6


def test_negative_number_raises(calc):
    with pytest.raises(ValueError, match="negative numbers not allowed: -2"):
        calc.add("1,-2,3")

def test_multiple_negatives_raises(calc):
    with pytest.raises(ValueError, match="negative numbers not allowed: -2, -3, -5"):
        calc.add("1,-2,-3,4,-5")


def test_ignore_large_numbers(calc):
    assert calc.add("2,1001") == 2
    assert calc.add("1000,2") == 1002


def test_long_delimiter(calc):
    assert calc.add("//[***]\n1***2***3") == 6


def test_multiple_delimiters(calc):
    assert calc.add("//[*][%]\n1*2%3") == 6

def test_multiple_long_delimiters(calc):
    assert calc.add("//[***][%%]\n1***2%%3") == 6
