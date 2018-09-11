"""Circle info."""
import math


def find_circle_info(d, x, y):
    """Write a function which prints message "Hello world!" to the console."""
    r = d / 2
    perimeter = 2 * math.pi * r
    area = math.pi * (r ** 2)
    c = (x ** 2 + y ** 2) ** 0.5
    if c < r:
        place = "inside"
    elif c == r:
        place = "perimeter"
    else:
        place = "outside"
    return f"Circle with perimeter of {perimeter} units and area of {area} units has point ({x},{y}) on its {place}"
