"""Circle info."""
import math


def find_circle_info(d, x, y):
    """
        Summary of the func.

        Description of the func. This function takes one parameter and does nothing.
        :return: What the function returns, data type
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
    return f"Circle with perimeter of {perimeter} units and area of {area} units has point ({x},{y}) on its {place}"


if __name__ == "__main__":
    print(find_circle_info(10, 9, 8))  # Circle with perimeter of 31.41592653589793 units and area of 78.53981633974483
    # units has point (9.0,8.0) on its outside
