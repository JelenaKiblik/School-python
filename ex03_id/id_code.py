"""Check if given ID code is valid."""
import math


def check_your_id(id_code: str):
    """
    Check if given ID code is valid and return the result.

    :param id_code: str
    :return: boolean
    """
    if len(id_code) == 11 and id_code.isdecimal():
        gender = int(id_code[0])
        year = int(id_code[1:3])
        month = int(id_code[3:5])
        day = int(id_code[5:7])
        order = int(id_code[7:10])

        if (check_gender_number(gender) is True) and (check_year_number_two_digits(year) is True) and (check_month_number(month) is True) and (check_day_number(year, month, day) is True) and (check_born_order(order) is True) and (check_control_number(id_code) is True):
            return True
        else:
            return False
    else:
        return False


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
    max_days = 28 + (month_number + math.floor(month_number / 8)) % 2 + 2 % month_number + 2 * math.floor(
        1 / month_number)
    if check_leap_year(year_number) is False:
        if (day_number > 0) and (day_number <= max_days):
            return True
        else:
            return False
    if check_leap_year(year_number) is True:
        if month_number == 2:
            if (day_number > 0) and (day_number <= 29):
                return True
            else:
                return False
        else:
            if (day_number > 0) and (day_number <= max_days):
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
        return False
    else:
        return True


def check_born_order(born_order: int):
    """
    Check if given value is correct for born order number in ID code.

    :param born_order: int
    :return: boolean
    """
    if (born_order >= 0) and (born_order < 1000):
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
    kordajad_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    kordajad_2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
    code_list = [int(n) for n in list(id_code)]
    check_numbers1 = list(kordajad_1)
    check_numbers2 = list(kordajad_2)
    multiply = []

    for i in range(0, len(check_numbers1)):
        multiply.append(check_numbers1[i] * code_list[i])
    summa = sum(multiply)
    check_number = summa % 11

    if (check_number >= 0) and (check_number < 10) and (check_number == code_list[-1]):
        return True
    elif check_number == 10:
        for i in range(0, len(check_numbers2)):
            multiply.append(check_numbers2[i] * code_list[i])
        summa2 = sum(multiply)
        check_number2 = summa2 % 11

        if (check_number2 >= 0) and (check_number2 < 10) and (check_number2 == code_list[-1]):
            return True
        elif check_number2 == 10:
            check_number3 = 0
            if check_number3 == code_list[-1]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':

    print(check_control_number("51809070123"))  # -> False
    print(check_control_number("60109200187"))  # -> False, it must be 6


def get_data_from_id(id_code: str):
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a (gender) born on (DD.MM.YYYY).
    :param id_code: str
    :return: str
    """
    if len(id_code) == 11 and id_code.isdecimal():
        gender = int(id_code[0])
        year = int(id_code[1:3])
        month = id_code[3:5]
        day = id_code[5:7]
        if check_your_id(id_code) is True:
            return f"This is a {get_gender(gender)} born on {day}.{month}.{get_full_year(gender, year)}"
        else:
            return "Given invalid ID code!"
    else:
        return False


def get_gender(gender_number: int):
    """
    Define the gender according to the number from ID code.

    :param gender_number: int
    :return: str
    """
    if gender_number == 1 or gender_number == 3 or gender_number == 5:
        return "male"
    if gender_number == 2 or gender_number == 4 or gender_number == 6:
        return "female"


def get_full_year(gender_number: int, year: int):
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year: int
    :return: int
    """
    if gender_number == 1 or gender_number == 2:
        return 1800 + year
    if gender_number == 3 or gender_number == 4:
        return 1900 + year
    if gender_number == 5 or gender_number == 6:
        return 2000 + year


if __name__ == '__main__':
    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998"
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"
