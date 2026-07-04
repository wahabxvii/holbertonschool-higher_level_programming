#!/usr/bin/python3
"""Mudole that has read_file function"""

def read_file(filename=""):
    """Function that reads a text file."""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    print(read_data, end='')
