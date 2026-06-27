#!/usr/bin/python3
"""Define CountedIterator class."""


class CountedIterator:
    """Define CountedIterator class."""

    def __init__(self, iterable):
        """Initiat CountedIterator with iterable."""

        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator."""
        return self

    def __next__(self):
        """Return the next item."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Count the items iterated."""
        return self.count
