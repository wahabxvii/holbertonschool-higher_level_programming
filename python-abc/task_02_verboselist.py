#!/usr/bin/python3
"""Define VerboseList class."""

class VerboseList(list):
    """A class that inherit from list class."""

    def append(self, item):
        """Customize the append method."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Customize the extend method."""
        count = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """Customize the remove method."""
        print(f"Remove {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Customize the pop method."""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
