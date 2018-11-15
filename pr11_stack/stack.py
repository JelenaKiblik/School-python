"""PR11 - Stack, introduction to classes."""
from typing import Any


class StackOverflowException(Exception):
    """Exception."""

    def __init__(self):
        """Exception, which is raised when a full stack is attempted to put an element."""
        super().__init__()


class StackUnderflowException(Exception):
    """Exception."""

    def __init__(self):
        """Exception, which is lifted when an empty stack is attempted to take an element."""
        super().__init__()


class Stack:
    """Simple stack implementation."""

    def __init__(self, capacity: int) -> None:
        """
        Initialise the stack.

        :param capacity: the maximum number of objects that stack can hold.
        """
        self.items = []
        self.capacity = capacity
        self.count = 0

    def push(self, item: Any) -> None:
        """
        Add the element to the collection.

        If stack has no more room, raises StackOverflowException.
        """
        self.items.append(item)
        self.count += 1

    def pop(self) -> Any:
        """
        Remove the most recently added element that was not yet removed.

        If stack is empty, raises StackUnderflowException.
        """
        self.count -= 1
        return self.items.pop()

    def peek(self) -> Any:
        """
        Show the most recently added element without removing it from the stack.

        If stack is empty returns None.
        """
        if self.items.count == 0:
            return None
        else:
            return self.items[len(self.items) - 1]

    def is_empty(self) -> bool:
        """Return the brace that the stack is empty."""
        if self.items.count != 0:
            return False
        else:
            return True

    def is_full(self) -> bool:
        """Return the brawl value of the stack is full."""
        if self.items.count != 0:
            return True
        else:
            return False

    def __str__(self) -> str:
        """
        Get string representation of stack.

        If top element is present should return:
            "Stack(capacity={capacity}, top_element={top_element})"
        Else
            "Stack(capacity={capacity})"
        """
        pass


if __name__ == '__main__':
    # Define some items
    item_1 = "first item"
    item_2 = "second item"
    item_3 = "third item"
    stack_capacity = 5
    my_stack = Stack(stack_capacity)

    my_stack.push(item_1)
    my_stack.push(item_2)
    my_stack.push(item_3)