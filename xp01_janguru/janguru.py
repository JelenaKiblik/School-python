"""Süvapython 01 - Jänguru."""
from fractions import Fraction


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Convert point from polar coordinates to cartesian coordinates."""
    if pos1 == pos2:
        pos1 = pos2
    elif (jump_distance1 / sleep1 > jump_distance2 / sleep2 and pos1 > pos2) or (
            jump_distance2 / sleep2 > jump_distance1 / sleep1 and pos2 > pos1):
        pos1 = -1
    elif jump_distance1 / sleep1 == jump_distance2 / sleep2:
        pos1 = -1
    else:
        if pos1 > pos2:
            while pos1 != pos2:
                pos1 += Fraction(jump_distance1, sleep1)
                pos2 += Fraction(jump_distance2, sleep2)
                if pos2 > pos1:
                    pos1 = -1
                    break
        elif pos2 > pos1:
            while pos1 != pos2:
                pos1 += Fraction(jump_distance1, sleep1)
                pos2 += Fraction(jump_distance2, sleep2)
                if pos1 > pos2:
                    pos1 = -1
                    break
    return pos1


if __name__ == '__main__':
    print("start")
    print(meet_me(1, 2, 1, 1, 2, 1))  # => 3
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    print(meet_me(3, 5, 10, 4, 1, 2))  # => 8
    print(meet_me(100, 7, 4, 300, 8, 6))  # => 940
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    print(meet_me(10, 7, 7, 5, 8, 6))   # => 45
    print(meet_me(1, 7, 1, 15, 5, 1))   # => 50
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
