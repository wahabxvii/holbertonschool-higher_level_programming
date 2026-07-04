#!/usr/bin/python3
"""Module that has serialize_and_save_to_file function."""


def serialize_and_save_to_file(data, filename):
    """Serializing function."""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Load and deserialize function."""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
