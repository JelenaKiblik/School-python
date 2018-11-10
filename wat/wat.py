"""Wat."""


def first(n: int):
    """Function first."""
    if n <= -950:
        return 12
    if ((n > -960) and (n <= -628)) or ((n >950) and (n <= 1000)):
        return 11
    if (n > -628) and (n <= - 150):
        return 14
    if (n > -150) and (n <= -1):
        return 12
    if n == 0:
        return 16
    if n == 1:
        return 0
    if n == 2:
        return
    if n == 3:
        return 4
    if n == 5:
        return 6
    if n == 6:
        return 6
    if n > 6:
        return 8
    if ((n > 99) and (n <= 444)) or ((n > 900) and (n <= 950)):
        return 12
    if ((n > 445) and (n <= 900)) or ((n > 999) and (n <= 2000)):
        return 8
    if n > 2000:
        return 18
