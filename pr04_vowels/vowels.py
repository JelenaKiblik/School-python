"""Sorting."""


def number_of_vowels(string: str):
    """
    Find the number of vowels(a, e, i, o, u) in word.

    :param string:
    :return: number of vowels in string
    """
    count = 0
    for letter in string:
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            count += 1
    return count


def word_with_most_vowels(string_list: list):
    """
    Find and return the string with most vowels in the list.

    :param string_list:
    :return: The string with most vowels in the list.
    """
    max_count = 0
    string_index = 0
    for i, string in enumerate(string_list):
        vowels = number_of_vowels(string)
        if max_count < vowels:
            max_count = vowels
            string_index = i

    return string_list[string_index]


def sort_list(string_list: list):
    """
    Sort the list by the number of vowels in the string.

    :param string_list: List of strings that need to be sorted.
    :return: List of strings sorted by the number of vowels.
    """
    return sorted(string_list, key=number_of_vowels, reverse=True)
