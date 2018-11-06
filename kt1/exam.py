"""Kontrolltoo."""


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
    new_list = []
    list = []
    for i in nums:
        if i % 2 == 0:
            new_list.append(i)
    if len(new_list) % 2 == 0:
        a = len(new_list) // 2
        for i in range(a):
            list.append(new_list[i])
    else:
        a = len(new_list) // 2
        for i in range(a + 1):
            list.append(new_list[i])
    return sum(list)


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    count = 1
    string = s.lower()
    if len(string) == 0:
        return 0
    else:
        for i in range(0, len(string) - 1):
            if string[i] == string[i + 1]:
                count += 1
        return count


print(max_block("hoopla"))
print(max_block(""))
print(max_block("abbCCCddBBBxx"))
