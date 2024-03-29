"""Circle info."""
import math


def find_circle_info(d, x, y):
    """
    Write a function which finds perimeter, area and where given point is placed in relation to the circle with diameter d.

    Place: inside, perimeter, outside.

    The function should print "Circle with perimeter of {perimeter} unts and area of {area} units has point ({x}, {y}) on its {place}".
    :return: None
    """
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
    print(f"Circle with perimeter of {perimeter} units and area of {area} units has point ({x}, {y}) on its {place}")


if __name__ == '__main__':
    find_circle_info(10, 9, 8)
