"""Check if given ID code is valid."""
import math


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
    if (year_number >= 0) and (year_number <= 99):
        return True
    else:
        return False


def check_month_number(month_number: int):
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if (month_number > 0) and (month_number <= 12):
        return True
    else:
        return False


def check_day_number(year_number: int, month_number: int, day_number: int):
    """
    Check if given value is correct for day number in ID code.
    Also, consider leap year and which month has 30 or 31 days.

    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """

    # x номер месяца
    # y количество дней

    y = 28 + (x + math.floor(x/8)) % 2 + 2 % x + 2 * math.floor(1/x);



    if month_number == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if day_number == 31:
            return True
        else:
            return False
    elif month_number == 4 or 6 or 9 or 11:
        if day_number == 30:
            return True
        else:
            return False
    elif (month_number == 2) and (check_leap_year is True):
        if day_number == 29:
            return True
        else:
            return False



def check_leap_year(year_number: int):
    """
    Check if given year is a leap year.

    :param year_number: int
    :return: boolean
    """
    if year_number % 4 != 0 or (year_number % 100 == 0 and year_number % 400 != 0):
        return True
    else:
        return False


def check_born_order(born_order: int):
    """
    Check if given value is correct for born order number in ID code.

    :param born_order: int
    :return: boolean
    """
    if (born_order) > 0 and (born_order < 1000):
        return True
    else:
        return False


def check_control_number(id_code: str):
    """
    Check if given value is correct for control number in ID code.
    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    total = 0
    kordajad_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    kordajad_2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
    for element in id_code:
        for i in kordajad_1:
            total += int(element) * i
        return total
    if total / 11 != 10:
        return total / 11
    else:
        for element in id_code:
            for i in kordajad_2:
                total += int(element) * i
            return total
        if total / 11 != 10:
            return total / 10
        else:
            return 0





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

def get_data_from_id(id_code: str):
    """
    Get possible information about the person.
    Use given ID code and return a short message.
    Follow the template - This is a (gender) born on (DD.MM.YYYY).
    :param id_code: str
    :return: str
    """
    pass

def get_gender(gender_number: int):
    """
    Define the gender according to the number from ID code.

    :param gender_number: int
    :return: str
    """
    pass


def get_full_year(gender_number: int, year: int):
    """
    Define the 4-digit year when given person was born.
    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year: int
    :return: int
    """
    pass


if __name__ == '__main__':
    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998"
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

