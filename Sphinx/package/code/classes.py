"""This module contains a demo class

The Class has four methods
- __init__
- add
- subtract
- operations_completed

>>> from classes import Foo
>>> foo = Foo()
>>> foo.add(2, 4)
6
>>> foo.subtract(5,2)
3
>>> foo.operations_completed()
2
"""

class Foo(object):
    """The Foo object!"""

    def __init__(self):
        """Constructor - set completed operations to 0"""
        self.completed_operations = 0

    def add(self, x, y):
        """Add two objects - increment completed operations"""
        result = x + y
        self.completed_operations += 1
        return result

    def subtract(self, x, y):
        """Subtract two objects - increment completed operations"""
        result = x - y
        self.completed_operations += 1
        return result

    def operations_completed(self):
        """Return the number of operations this class has completed"""
        return self.completed_operations
