"""Tests for the calculator library."""

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
