from src.math_utils import add, subtract, multiply, power, modulo

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_power():
    assert power(2, 3) == 8

def test_power_zero():
    assert power(5, 0) == 1

def test_modulo():
    assert modulo(10, 3) == 1
