import pytest


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference when b is subtracted from a."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Returns the division of a by b.
    Raises a ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(number):
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0




@pytest.mark.parametrize("a,b,expected",[
    pytest.param(1,2,3,id="normal addition"),
    pytest.param(1000,2000,3000,id="large numbers"),
    pytest.param('c','v','s',marks=pytest.mark.xfail(reason="String math not supported yet"), id="expected failure"),

])
def test_add(a,b,expected):
    #positive test
    assert add(a, b) == expected

    #Error type test
    # with pytest.raises(TypeError):
    #     add(4,"2")


class Test_Calculator:
    def test_add(self):
        assert add(3,2)
        with pytest.raises(TypeError):
            add(4, "2")
            add("v", [0])

    def test_subtract(self):
        assert subtract(5,5) == 0

        with pytest.raises(TypeError):
            subtract(4, "2")
            subtract("v", [0])





@pytest.mark.parametrize("input_val, expected", [
    pytest.param(1, 2, id="normal addition"),
    pytest.param(99, 100, id="large numbers"),
    pytest.param("a", "b",
                 marks=pytest.mark.xfail(reason="String math not supported yet"),
                 id="expected failure")
])
def test_increment(input_val, expected):
    assert input_val + 1 == expected