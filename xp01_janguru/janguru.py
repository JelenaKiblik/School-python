"""Süvapython 01 - Jänguru."""
from fractions import Fraction


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Function that returns the position they meet for the first time or -1 if they don't meet."""
    speed_1 = Fraction(jump_distance1, sleep1)
    speed_2 = Fraction(jump_distance2, sleep2)

    if speed_2 >= speed_1:
        slower = 1
    else:
        slower = 2

    distance_between = None

    slower_just_moved = False

    current_position_1 = pos1
    current_position_2 = pos2

    current_sleep_remaining_1 = 0
    current_sleep_remaining_2 = 0

    while True:
        if current_sleep_remaining_1 == 0:
            current_position_1 += jump_distance1
            current_sleep_remaining_1 = sleep1
            if slower == 1:
                slower_just_moved = True

        if current_sleep_remaining_2 == 0:
            current_position_2 += jump_distance2
            current_sleep_remaining_2 = sleep2
            if slower == 2:
                slower_just_moved = True

        current_sleep_remaining_1 -= 1
        current_sleep_remaining_2 -= 1

        if current_position_1 == current_position_2:
            return current_position_1

        if slower_just_moved:
            if slower == 1:
                if current_position_1 < current_position_2:
                    previous_distance_between = distance_between
                    distance_between = current_position_2 - current_position_1
                    if previous_distance_between is not None and distance_between >= previous_distance_between:
                        return -1
            if slower == 2:
                if current_position_2 < current_position_1:
                    previous_distance_between = distance_between
                    distance_between = current_position_1 - current_position_2
                    if previous_distance_between is not None and distance_between >= previous_distance_between:
                        return -1

        slower_just_moved = False


if __name__ == '__main__':
    print("start")
    print(meet_me(1, 2, 1, 2, 1, 1))   # = > 3
    print(meet_me(1, 2, 1, 1, 2, 1))  # => 3
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    print(meet_me(3, 5, 10, 4, 1, 2))  # => 8
    print(meet_me(100, 7, 4, 300, 8, 6))  # => 940
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    print(meet_me(10, 7, 7, 5, 8, 6))   # => 45
    print(meet_me(1, 7, 1, 15, 5, 1))   # => 50
