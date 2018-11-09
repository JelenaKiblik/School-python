"""Wat."""


def first(n: int):
    """Function first."""
    if n <= -960:
        return 12
    if (n > -960) and (n <= -628):
        return 11
    if (n > -628) and (n <= -1):
        return 14
    if n == 0:
        return 16
    if n == 1:
        return 0
    if (n > 1) and (n <= 6):
        return n
    if (n > 99) and (n <= 444):
        return 12
    if (n > 445) and (n <= 888):
        return 8
    if (n > 899) and (n <= 1000):
        return 11
    if (n > 999) and (n <= 2000):
        return 8
    if n > 2000:
        return 18
