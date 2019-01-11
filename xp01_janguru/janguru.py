"""Süvapython 01 - Jänguru."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Convert point from polar coordinates to cartesian coordinates."""
    if (pos1 != pos2) and (jump_distance1 - jump_distance2 != 0) and ((sleep1 % sleep2 != 0) and (sleep2 % sleep1 != 0)):
        x = abs(pos1 - pos2) / abs(jump_distance1 - jump_distance2)
        if (((sleep2 * x) - 1) <= ((sleep1 * x) - 1)) and (((sleep2 * x) - 1) >= (sleep1 * (x - 1))):
            # print("code1")
            return int(pos1 + (jump_distance1 * x))
        else:
            y = abs((pos2 - pos1)/(jump_distance2 - (jump_distance1 * (sleep2/sleep1))))
            return int(pos2 + y * jump_distance2)
    elif (pos1 != pos2) and (jump_distance1 - jump_distance2 != 0) and ((sleep1 % sleep2 == 0) or (sleep2 % sleep1 == 0)):
        # x = abs(pos1 - pos2) / abs(jump_distance1 - jump_distance2)
        if sleep1 > sleep2:
            y = sleep1 / sleep2
            pos = pos2 + jump_distance2 * (y - 1)
            # print("code4")
            return int(pos)
    elif (pos1 == pos2) and (jump_distance1 == jump_distance2):
        # print("code3")
        return pos1 + jump_distance1
    else:
        return -1


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
