"""Wat."""


def first(n: int):
    """Function first."""
    if n <= -950:
        return 12
    if (n > -950) and (n <= -628):
        return 11
    if (n > -628) and (n <= - 400):
        return 14
    if (n > -400) and (n <= - 300):
        return 11
    if (n > -300) and (n <= - 150):
        return 14
    if n == -17:
        return 11
    if (n > -150) and (n < -100):
        return 12
    if (n > -100) and (n < -40):
        return 11
    if (n > -40) and (n < -1):
        return 12
    if n == -1:
        return 14
    if n == 0:
        return 16
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 6
    if n == 5:
        return 4
    if n == 6:
        return 6
    if (n > 6) and (n <= 99):
        return 8
    if ((n > 99) and (n <= 444)) or ((n > 900) and (n <= 980)):
        return 12
    if (n > 980) and (n < 1000):
        return 11
    if (n >= 700) and (n <= 900):
        return 12
    if ((n > 445) and (n < 700)) or ((n >= 999) and (n <= 2000)):
        return 8
    if (n > 2000) and (n < 3000):
        return 18


print(first(2343))
