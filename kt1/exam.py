def capitalize_string(s: str) -> str:
    """
    Return capitalized string. The first char is capitalized, the rest remain as they are.
    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    if len(s) >= 1:
        return s[0].upper() + s[1:]
    else:
        return ""


def sum_half_evens(nums: list) -> int:
    """
    Return the sum of first half of even ints in the given array.
    If there are odd number of even numbers, then include the middle number.

    sum_half_evens([2, 1, 2, 3, 4]) => 4
    sum_half_evens([2, 2, 0, 4]) => 4
    sum_half_evens([1, 3, 5, 8]) => 8
    sum_half_evens([2, 3, 5, 7, 8, 9, 10, 11]) => 10
    """
    pass


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    pass

print(capitalize_string("abc"))
print(capitalize_string("ABc"))
print(capitalize_string(""))