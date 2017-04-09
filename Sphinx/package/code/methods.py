"""This module contains methods!

If we write our docstrings as ReST, we get nice documentation
"""

def add(x, y):
    """Add two objects and return the result
    >>> from methods import add
    >>> add(2, 4)
    6
    >>> add('Cheese', 'burger')
    'Cheeseburger'
    """

    return x + y

def subtract(x, y):
    """Subtract two objects and return the result
    >>> from methods import subtract
    >>> subtract(2, 1)
    1
    """

    return x - y
