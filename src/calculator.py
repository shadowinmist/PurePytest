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



