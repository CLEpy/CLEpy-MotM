#!/usr/bin/env python

import fire

class Calculator(object):
    """A simple calculator class."""

    def add(self, number1, number2):
        """Add two numbers."""
        return number1 + number2

    def double(self, number):
        """Multiply input x2."""
        return 2 * number


if __name__ == '__main__':
    fire.Fire(Calculator)
