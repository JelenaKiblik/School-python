import re
import math

regex_a = r'(-?\d+)x2'
regex_b = r'([+-] ?\d+)x'
regex_c = r'([+-] ?\d+)$'


def square_finder(equation, eq_pos):
    """Find square number."""
    p = re.compile(regex_a)
    square = p.search(equation)
    if square is not None:
        square_pos = square.start(0)
        square = square.group().strip()
        if square[-1] == '+' or square[-1] == '-' or square[-1] == '=':
            square = square[:-1].strip()
        if square[0] == '=':
            square = square[1:].strip()
        if square[0] != '-' and square[0] != '+':
            square = '+' + square
        square = one_checker(space_insert(square).strip())
        if square_pos > eq_pos:
            square = side_swapper(square)
        square = zero_checker(square)
    else:
        square = ''
    print(square)
    return square


def linear_finder(equation, eq_pos):
    """Find linear number."""
    p = re.compile(regex_b)
    linear = p.search(equation)
    if linear is not None:
        linear_pos = linear.start(0)
        linear = linear.group().strip()
        if linear[-1] == '+' or linear[-1] == '-' or linear[-1] == '=':
            linear = linear[:-1].strip()
        if linear[0] == '=':
            linear = linear[1:].strip()
        if linear[0] != '-' and linear[0] != '+':
            linear = '+' + linear
        linear = one_checker(space_insert(linear).strip())
        if linear_pos > eq_pos:
            linear = side_swapper(linear)
        linear = zero_checker(linear)
    else:
        linear = ''
    print(linear)
    return linear


def free_number_finder(equation, eq_pos):
    """Find free number."""
    p = re.compile(regex_c)
    free = p.search(equation)
    if free is not None:
        free_pos = free.start()
        free = free.group().strip()
        if free[-1] == '+' or free[-1] == '-' or free[-1] == '=':
            free = free[:-1].strip()
        if free[0] == '=':
            free = free[1:].strip()
        if free[0] != '-' and free[0] != '+':
            free = '+' + free
        free = space_insert(free)
        if free_pos > eq_pos:
            free = side_swapper(free)
        free = free.strip()
    else:
        free = ''
    print(free)
    return free


def space_insert(checked):
    """Insert space."""
    p = re.compile('(\+|-)')
    var1 = p.search(checked)
    if var1 is not None and checked[1] != ' ':
        checked = checked[0] + ' ' + checked[1:]
    return checked


def one_checker(checked):
    """Checker."""
    d = re.compile('r(\s)1x2?')
    if d.search(checked) is not None:
        if checked[0] == '-' or checked[0] == '+':
            checked = checked[:2] + checked[3:]
        else:
            checked = checked[1:]
    return checked


def zero_checker(checked):
    """Check zero."""
    try:
        if checked[0] == '0' or checked[2] == '0':
            checked = ''
    except IndexError:
        pass
    return checked


def side_swapper(var1):
    """Swap side."""
    if var1[0] != '-':
        if var1[0] == '+':
            var1 = '-' + var1[1:]
        else:
            var1 = '- ' + var1
    else:
        var1 = '+' + var1[1:]
    return var1


def minus(square, linear, free):
    """Find minus"""
    if square != '':
        if square[0] == '-':
            square = side_swapper(square)
            if linear != '':
                linear = side_swapper(linear)
            if free != '':
                free = side_swapper(free)
    return square, linear, free


def check_space(equation):
    """Space check."""
    for i in range(len(equation) - 1, 0, -1):
        if equation[i] == ' ' and equation[i + 1] == ' ':
            equation = equation[:i + 1] + equation[i + 2:]
    return equation


def solve(square, linear, free):
    """Solve ready."""
    if square != '':
        if square[2] == 'x':
            a = 1
        elif square[0] == '-':
            a = int(square[0] + square[2:-2])
        else:
            a = int(square[2:-2])
    else:
        a = 0
    if linear != '':
        if linear[2] == 'x':
            b = 1
        elif linear[0] == '-':
            b = int(linear[0] + linear[2:-1])
        else:
            b = int(linear[2:-1])
    else:
        b = 0
    if free == '':
        c = 0
    else:
        c = int(free[0] + free[2:])
    return a, b, c


def normalize_equation(equation):
    """Normalize equation."""
    eq_pos = re.search('=', equation).start()
    equation = ' ' + equation + ' '
    square_finder(equation, eq_pos)
    linear_finder(equation, eq_pos)
    free_number_finder(equation, eq_pos)
    square, linear, free = minus(square_finder(equation, eq_pos), linear_finder(equation, eq_pos),
                                 free_number_finder(equation, eq_pos))
    equation = '{} {} {} = 0'.format(square, linear, free).strip()
    equation = check_space(equation)
    if equation[0] == '+':
        equation = equation[2:]
    return equation


def solve_equation(equation):
    a_str = (re.search(r'(-?\d+)x2', equation)).group()
    a = int(a_str[0])
    b_str = (re.search(r'([+-] ?\d+)x', equation)).group()
    b = int(b_str[2])
    c_str = (re.search(r'([+-] ?\d+)  ?', equation)).group()
    c = int(c_str[2])
    d = int((b * b) + (4 * a * c))
    x1 = (-b + math.sqrt(d)) / (2 * 2)
    x2 = (-b - math.sqrt(d)) / (2 * 2)
    return x1, x2


if __name__ == '__main__':
    # def print_regex_results(regex, f):
    #     for match in re.finditer(regex, f):
    #         print(match.group(1))
    #
    #
    # f = "3x2 - 4x + 1"
    #
    # print_regex_results(regex_a, f)  # 3
    # print_regex_results(regex_b, f)  # - 4
    # print_regex_results(regex_c, f)  # 1

    print(normalize_equation("x2 + 2x = 3"))  # = > "x2 + 2x - 3 = 0"
    #
    # print(solve_equation("2x2 + 3x - 2 = 0"))  # = > "x1 = -2.0, x2 = 0.5"
