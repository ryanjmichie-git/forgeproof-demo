"""Tests for the calculator library."""

import pytest

import calculator


def test_add_positive():
    assert calculator.add(2, 3) == 5


def test_add_negative():
    assert calculator.add(-1, -4) == -5


def test_add_zero():
    assert calculator.add(7, 0) == 7


def test_multiply_positive():
    assert calculator.multiply(3, 4) == 12


def test_multiply_by_zero():
    assert calculator.multiply(9, 0) == 0


def test_multiply_negative():
    assert calculator.multiply(-2, 5) == -10


def test_subtract_positive():
    assert calculator.subtract(9, 4) == 5


def test_subtract_negative_result():
    assert calculator.subtract(3, 8) == -5


def test_subtract_zero():
    assert calculator.subtract(7, 0) == 7


def test_divide_whole_result():
    assert calculator.divide(12, 4) == 3


def test_divide_fractional_result():
    assert calculator.divide(7, 2) == 3.5


def test_divide_negative_operand():
    assert calculator.divide(-9, 3) == -3


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        calculator.divide(1, 0)
