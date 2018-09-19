"""Süvapython 01 - Jänguru."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """
    Convert point from polar coordinates to cartesian coordinates.

    :param pos1: kui kaugel (mitu ühikut) ta purskkaevust on.
    :param jump_distance1: kui kaugele (mitu ühikut) jänguru ühe hüppega hüppab.
    :param sleep1: peale hüpet tahab jänguru puhata. Näitab, kui kaua (mitu ajaühikut) jänguru puhkab kahe hüppe vahel.
    :param pos2: kui kaugel (mitu ühikut) ta purskkaevust on.
    :param jump_distance2: kui kaugele (mitu ühikut) jänguru ühe hüppega hüppab.
    :param sleep2: peale hüpet tahab jänguru puhata. Näitab, kui kaua (mitu ajaühikut) jänguru puhkab kahe hüppe vahel.

    :return: positsioon, kus nad esimest korda kohtuvad
    """
    if (pos1 >= 0 and pos2 >= 0) and (jump_distance1, jump_distance2 >= 0) and (sleep1, sleep2 > 0):
        janguru1 = (jump_distance1) / sleep1
        janguru2 = (jump_distance2) / sleep2
        if (janguru1 > janguru2) and (pos1 < pos2):
            meet_time = (pos2 - pos1) / (janguru1 - janguru2)
            meet_pos = pos1 + (meet_time * janguru1)
            return round(meet_pos)
        elif (janguru1 < janguru2) and (pos1 < pos2):
            return -1
        elif (janguru1 < janguru2) and (pos1 > pos2):
            meet_time = (pos1 - pos2) / (janguru2 - janguru1)
            meet_pos = pos2 + (meet_time * janguru2)
            return round(meet_pos)
        elif (janguru1 == janguru2) and (pos1 == pos2):
            meet_pos = jump_distance1 * 2
            return round(meet_pos)
    else:
        return -1


if __name__ == '__main__':
    print("start")
    print(meet_me(1, 2, 1, 2, 1, 1))   # => 3
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    print(meet_me(10, 7, 7, 5, 8, 6))   # => 45
    print(meet_me(100, 7, 4, 300, 8, 6))   # => 940
    print(meet_me(1, 7, 1, 15, 5, 1))   # => 50
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
