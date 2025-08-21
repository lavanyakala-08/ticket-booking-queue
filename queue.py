# queue.py

class Queue:
    """A simple implementation of a Queue data structure using a Python list."""

    def __init__(self):
        """Initializes a new, empty queue."""
        self.items = []

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self.items

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.

        Args:
            item: The item to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The item from the front of the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        """
        Returns the number of items currently in the queue.

        Returns:
            int: The number of items.
        """
        return len(self.items)

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.items[0]
        return None

    def __repr__(self):
        """
        Provides a string representation of the queue.
        """
        return f"Queue({self.items})"


