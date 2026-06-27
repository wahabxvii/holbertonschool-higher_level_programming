#!/usr/bin/python3
"""Define MyList class."""


class MyList(list):
    """A class that inherite from list class."""

    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
