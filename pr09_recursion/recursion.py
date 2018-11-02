def recursive_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using recursion.
    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    pass


def loop_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using loops.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    my_sum = 0
    for i in numbers:
        if i % 2 == 0:
            my_sum = my_sum + i
            i += 1
    return my_sum


def loop_reverse(s: str) -> str:
    """Reverse a string using a loop.

    :param s: string
    :return: reverse of s
    """
    a = ""
    for i in range(1, len(s) + 1):
        a += s[len(s) - i]
    return a


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    :param s: string
    :return: reverse of s
    """
    if s == "":
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]


if __name__ == '__main__':
    print(recursive_sum([1, 3, 5, 7, 9]))
    print(recursive_sum([2, 4, 5, 8]))
    print(loop_sum([1, 3, 5, 7, 9]))
    print(loop_sum([2, 4, 5, 8]))

