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
    pass


if __name__ == '__main__':
    print("start")
    meet_me(1, 2, 1, 2, 1, 1)   # => 3
    meet_me(1, 2, 3, 4, 5, 5)   # => -1
    meet_me(10, 7, 7, 5, 8, 6)   # => 45
    meet_me(100, 7, 4, 300, 8, 6)   # => 940
    meet_me(1, 7, 1, 15, 5, 1)   # => 50
    meet_me(0, 1, 1, 1, 1, 1)   # => -1
