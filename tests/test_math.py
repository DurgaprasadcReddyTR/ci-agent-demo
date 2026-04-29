from src.math_utils import add, subtract, multiply, absolute_value

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_absolute_value_positive():
    assert absolute_value(5) == 5

def test_absolute_value_negative():
    assert absolute_value(-7) == 7
