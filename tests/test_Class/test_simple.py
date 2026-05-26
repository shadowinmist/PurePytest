# test_example.py
import pytest

# 1. The functions we want to test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# 2. The test functions
def test_add():
    # The 'assert' keyword checks if the condition is True
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # Verify that the correct exception is raised when dividing by zero
    with pytest.raises(ValueError):
        divide(10, 0)
