"""Check if given ID code is valid."""


def check_your_id(id_code: str):
    """
    Check if given ID code is valid and return the result.

    :param id_code: str
    :return: boolean
    """
    pass


def check_gender_number(gender_number: int):
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if gender_number == 0:
        return False
    elif (gender_number >= 1) and (gender_number <= 6):
        return True
    else:
        return False


def check_year_number_two_digits(year_number: int):
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    pass


def check_month_number(month_number: int):
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    pass


def check_day_number(year_number: int, month_number: int, day_number: int):
    """
    Check if given value is correct for day number in ID code.
    Also, consider leap year and which month has 30 or 31 days.

    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    pass


def check_leap_year(year_number: int):
    """
    Check if given year is a leap year.

    :param year_number: int
    :return: boolean
    """
    pass


def check_born_order(born_order: int):
    """
    Check if given value is correct for born order number in ID code.

    :param born_order: int
    :return: boolean
    """
    pass


def check_control_number(id_code: str):
    """
    Check if given value is correct for control number in ID code.
    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    pass


if __name__ == '__main__':
    print("Overall ID check::")
    print(check_your_id("49808270244"))  # -> True
    personal_id = input()  # type your own id in command prompt
    print(check_your_id(personal_id))  # -> True
    print(check_your_id("12345678901"))  # -> False
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {check_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(check_year_number_two_digits(100))  # -> False
    print(check_year_number_two_digits(50))  # -> true
    print("\nMonth number:")
    print(check_month_number(2))  # -> True
    print(check_month_number(15))  # -> False
    print("\nDay number:")
    print(check_day_number(2005, 12, 25))  # -> True
    print(check_day_number(1910, 8, 32))  # -> False
    print(check_leap_year(1804))  # -> True
    print(check_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(check_day_number(1996, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(check_day_number(2099, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(check_day_number(2008, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(check_day_number(1822, 4, 31))  # -> False (April contains max 30 days)
    print(check_day_number(2018, 10, 31))  # -> True
    print(check_day_number(1915, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(check_born_order(0))  # -> True
    print(check_born_order(850))  # -> True
    print("\nControl number:")
    print(check_control_number("49808270244"))  # -> True
    print(check_control_number("60109200187"))  # -> False, it must be 6
