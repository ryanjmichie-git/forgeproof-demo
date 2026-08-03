"""A small calculator library.

Deliberately minimal — new operations are added via GitHub issues.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""   # <- was: Return the difference of a and b.
    return a - b