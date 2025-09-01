import pytest
from main import calculate

def test_calculate_basic():
    assert calculate(2, 3) == 6

def test_calculate_zero():
    assert calculate(0, 10) == 0
    assert calculate(10, 0) == 0

def test_calculate_negative():
    assert calculate(-2, 5) == -10
    assert calculate(3, -7) == -21

def test_calculate_both_negative():
    assert calculate(-4, -5) == 20

def test_calculate_large_numbers():
    assert calculate(123456, 789) == 97406784
