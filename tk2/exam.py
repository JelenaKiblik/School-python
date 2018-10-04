"""Test 2 (N8)."""


def make_ends(nums):
    """
    Given an array of ints, return a new array length 2 containing the first and last elements from the original array.

    The original array will be length 1 or more.

    make_ends([1, 2, 3]) → [1, 3]
    make_ends([1, 2, 3, 4]) → [1, 4]
    make_ends([7, 4, 6, 2]) → [7, 2]

    :param nums: List of integers.
    :return: List with the first and the last element from the input list.
    """
    new_nums = [nums[0], nums[-1]]
    return new_nums


def caught_speeding(speed, is_birthday):
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) → 0
    caught_speeding(65, False) → 1
    caught_speeding(65, True) → 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if is_birthday is True:
        if speed <= 65:
            return 0
        elif (speed > 65) and (speed <= 85):
            return 1
        else:
            return 2
    else:
        if speed <= 60:
            return 0
        elif (speed > 60) and (speed <= 80):
            return 1
        else:
            return 2


def combo_string(s1, s2):
    """
    Return a new string of the form short + long + short.

    Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') → 'hiHellohi'
    combo_string('hi', 'Hello') → 'hiHellohi'
    combo_string('aaa', 'b') → 'baaab'

    :param s1:
    :param s2:
    :return:
    """
    string_one = len(s1)
    string_two = len(s2)
    if string_one > string_two:
        return s2 + s1 + s2
    else:
        return s1 + s2 + s1


def min_index_value(nums):
    """
    Take the first and the last element as indices of two elements and return the smaller of those elements.

    If at least one index is out of range, return -1.
    All the values are non-negative integers.

    min_index_value([1, 2, 3]) => -1 (3 is out of range)
    min_index_value([1, 2, 1]) => 2 (both elements point to 2)
    min_index_value([1, 2, 0]) => 1 (have to take minimum of 2 and 1)

    :param nums: List of non-negative integers.
    :return: Minimum value of two elements at positions of the first and the last element value.
    """
    first_number_index = nums[0]
    second_number_index = nums[-1]
    list_length = len(nums) - 1
    if (first_number_index >= list_length) or (second_number_index >= list_length):
        return -1
    else:
        if nums[first_number_index] == nums[second_number_index]:
            return nums[second_number_index]
        elif nums[first_number_index] > nums[second_number_index]:
            return nums[second_number_index]
        else:
            return nums[first_number_index]


def max_duplicate(nums):
    """
    Return the largest element which has at least one duplicate.

    If no element has duplicate element (an element with the same value), return None.

    max_duplicate([1, 2, 3]) => None
    max_duplicate([1, 2, 2]) => 2
    max_duplicate([1, 2, 2, 1, 1]) => 2

    :param nums: List of integers
    :return: Maximum element with duplicate. None if no duplicate found.
    """
    sorted_nums = sorted(nums, reverse=True)
    for i in range(len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i + 1]:
            result = sorted_nums[i]
        else:
            result = None
        return result
