"""Exam example."""


def segment_number(first_number, last_number):
    """
    Return list with elements dividable by 5 but not dividable by 3 between (inclusive) two arguments.

    Return list of numbers where only numbers between first_number
    and last_number (both inclusive) which divide by 5 but do not divide by 3
    are used.

    #1

    :param first_number: the lowest possible candidate
    :param last_number: the highest possible candidate
    :return: list of numbers
    """
    new_list = []
    for i in range(first_number, last_number + 1):
        if (i % 5 == 0) and (i % 3 != 0):
            new_list.append(i)
    return new_list


def add_or_subtract(numbers):
    """
    Return the sum of all numbers in a list.

    The sum is calculated according to following rules:
        -always start by adding all the numbers together.
        -if you find a 0, start subtracting all following numbers until you find another 0, then start adding again.
        -there might be more than two 0 in a list - change +/- with every 0 you find.

    For example:
        [1, 2, 0, 3, 0, 4] -> 1 + 2 - 3 + 4 = 4
        [0, 2, 1, 0, 1, 0, 2] -> -2 - 1 + 1 - 2 = -4
        [1, 2] -> 1 + 2 = 3
        [4, 0, 2, 3] = 4 - 2 - 3 = -1

    #2

    :param numbers: the list of number given.
    :return: the sum of all numbers.
    """
    null = False
    summa = 0
    for i in numbers:
        if i == 0 and null is False:
            null = True
            continue
        if i == 0 and null is True:
            null = False
            continue
        if i != 0 and null is False:
            summa += i
            continue
        if i != 0 and null is True:
            summa -= i
            continue
    return summa


def should_get_up_early(is_weekday, really_tired, first_class_is_programming):
    """
    Decide if you should get up early.

    You should only even consider getting up early if it is a weekday, on weekends you should never get up early.
    If it is a weekday you should typically get up early, unless you are really tired.
    But if it is a weekday and you are really tired but the first class is a programming class you should still get up
    early ignoring you being tired.

    #3

    :param is_weekday: is it a weekday or not, boolean
    :param really_tired: are you really tired, boolean
    :param first_class_is_programming: is the first class a programming class, boolean
    :return: True if you should get up early, otherwise False
    """
    if not is_weekday:
        return False
    else:
        if really_tired is True and first_class_is_programming is False:
            return False
        if really_tired is True and first_class_is_programming is True:
            return True
        else:
            return True


def pear_fear(pears, people):
    """
    Return how many pears non-pear-fearers get.

    Every 3rd person fears pears, so they won't get any.
    How many pears will each get?
    Everyone who is not afraid of pears gets equal number of pears.
    Only whole pears will be used, so some pears may remain.

    #4

    :param pears:
    :param people:
    :return:
    """
    if pears == 0 or people == 0:
        return 0
    else:
        fears_pears = people // 3
        non_pear_fear = people - fears_pears
        return pears // non_pear_fear


def string_between_string(word1, word2):
    """
    Insert reversed word2 to the center of word1.

    word1 length is always even.

    #5

    :param word1: Initial word. String.
    :param word2: Word to reverse and insert. String.
    :return: New word as string.
    """
    return word1[0:len(word1) // 2] + word2[::-1] + word1[len(word1) // 2:]


def get_padded_string(string1, string2):
    """
    Pad the longer of two strings with the shorter one on both sides.

    If both strings are the same length, consider string1 as the longer one.
    For example when string1 is "pizza" and string2 is "bbq", this should return "bbqpizzabbq".

    #6

    :param string1: String one
    :param string2:  String two
    :return: Padded string
    """
    if len(string1) >= len(string2):
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1


def remove_duplicate(number_list):
    """
    Return list where consecutive duplicates are removed.

    Go though given list and remove all
    occurrences of two or more of the same
    numbers appearing after one another.
    Remove all but one of the duplicates.

    #7

    :param number_list: input list
    :return: new list
    """
    i = 0
    while i < len(number_list) - 1:
        if number_list[i] == number_list[i + 1]:
            del number_list[i]
        else:
            i = i + 1
    return number_list


def who_called(calls, name):
    """
    You are given a dictionary of calls and a name.

    Determine who called that name.
    If nobody called the person, return -1.

    #8

    :param calls: dictionary of all the calls
    :param name: name of the receiver
    :return: name of the caller
    """
    for k in calls:
        if name in calls[k]:
            return k
    else:
        return -1


def remove_lowest_digit(number):
    """
    Given a non-negative integer, remove the first occurrence of the lowest digit and return a new number.

    123 => 23
    223 => 23
    232 => 32
    1 => 0
    :param number: non-negative integer
    :return: non-negative integer
    """
    new_list = []
    for digit in str(number):
        new_list.append(digit)
    new_list.remove(min(new_list))
    if len(new_list) >= 1:
        return int("".join(new_list))
    else:
        return 0


def show_highest_grade(grade1, grade2):
    """
    Print "Highest grade: GRADE" where GRADE is the higher of two inputs.

    grade1, grade2 are both non-negative integers.

    3, 4 => "Highest grade: 4"

    #10

    :param grade1:
    :param grade2:
    :return:
    """
    if grade1 > grade2:
        print(f"Highest grade: {grade1}")
    else:
        print(f"Highest grade: {grade2}")


if __name__ == '__main__':
    #
    # print(segment_number(1, 11))  # == [5, 10]
    # print(segment_number(1, 4))  # == []
    # print(segment_number(-20, 20))  # == [-20, -10, -5, 5, 10, 20]
    #
    # print(add_or_subtract([1, 2, 0, 3]))  # == 0
    # print(add_or_subtract([0, 1, 2]))  # == -3
    # print(add_or_subtract([1, 2, 0, 2, 0, 4]))  # == 5
    #
    # print(should_get_up_early(True, True, True))  # is True
    # print(should_get_up_early(False, True, False))  # is False
    #
    # print(pear_fear(10, 3))  # == 5
    # print(pear_fear(10, 5))  # == 2
    # print(pear_fear(0, 3))  # == 0
    # print(pear_fear(17, 2))  # == 8
    # print(pear_fear(21, 10))  # == 3
    #
    # print(string_between_string("ho", "lle"))  # == "hello"
    # assert string_between_string("", "yas") == "say"
    # assert string_between_string("smrt", "a") == "smart"
    # assert string_between_string("w  d", " ro ") == "w  or  d"
    # assert string_between_string(".,", ",.") == "..,,"
    #
    # assert get_padded_string("pizza", "bbq") == "bbqpizzabbq"
    # assert get_padded_string("dog", "cat") == "catdogcat"
    # assert get_padded_string("geoff", "giraffe") == "geoffgiraffegeoff"
    #
    # print(remove_duplicate([1, 1, 2, 2, 3, 3]))  # == [1, 2, 3]
    # assert remove_duplicate([1, 2, 3]) == [1, 2, 3]
    # assert remove_duplicate([1, 1, 1, 1, 1, 2, 1, 1, 3]) == [1, 2, 1, 3]

    # assert who_called({}, "Nathan") == -1
    # assert who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Alex") == "James"
    # assert who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Olaf") == -1
    #
    # print(remove_lowest_digit(12131))   # == 2131
    # print(remove_lowest_digit(1000))  # == 100
    print(remove_lowest_digit(71))   # == 7
    # print(remove_lowest_digit(171))  # == 71

    # assert show_highest_grade(10, 14) is None
    # prints:
    # Highest grade: 14
