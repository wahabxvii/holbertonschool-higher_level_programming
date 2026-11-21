#!/usr/bin/python3
"""Returns "Python", one more copy on every call to the function."""


def magic_string(words=[]):
    """Return "Python" joined as many times as the function has been called."""
    words += ["Python"]
    return ", ".join(words)
