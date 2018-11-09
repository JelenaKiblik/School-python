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
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 4
    if n == 5:
        return 5
    if n == 6:
        return 6
    if (n > 6) and (n <= 888):
        return 8
    if n > 888:
        return 18


