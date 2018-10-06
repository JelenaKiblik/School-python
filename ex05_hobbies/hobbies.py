"""Hobbies."""
import csv


def create_list_from_file(file):
    """
    Collect lines from given file into list.

    :param file: original file path
    :return: list of lines
    """
    file = open("hobbies_database.txt", "r")
    new_list = file.readlines()
    return new_list


def create_dictionary(file):
    """
    Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2].

    :param file: original file path
    :return: dict
    """
    pass


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    pass


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    pass


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    pass


def find_least_popular_hobby(file):
    """
    Find the least popular hobby.

    :param file: original file path
    :return: list
    """
    pass


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        # your code goes here

# These examples are based on a given text file from the exercise.


if __name__ == '__main__':
    dic = create_dictionary("hobbies_database.txt")
    print(len(create_list_from_file("hobbies_database.txt")))  # -> 100
    # print("Check presence of hobbies for chosen person:")
    # print("shopping" in dic["Wendy"])  # -> True
    # print("fitness" in dic["Sophie"])  # -> False
    # print("gaming" in dic["Peter"])  # -> True
    # print("Check if hobbies - person relation is correct:")
    # print("Check if a person(people) with the biggest amount of hobbies is(are) correct:")
    # print(find_person_with_most_hobbies("hobbies_database.txt"))  # -> ['Jack']
    # print(len(dic["Jack"]))  # ->  12
    # print(len(dic["Carmen"]))  # -> 10
    # print("Check if a person(people) with the smallest amount of hobbies is(are) correct:")
    # print(find_person_with_least_hobbies("hobbies_database.txt"))  # -> ['Molly']
    # print(len(dic["Molly"]))  # -> 5
    # print(len(dic["Sophie"]))  # -> 7
    # print("Check if the most popular hobby(ies) is(are) correct")
    # print(find_most_popular_hobby("hobbies_database.txt"))  # -> ['gaming', 'sport', 'football']
    # print("Check if the least popular hobby(ies) is(are) correct")
    # print(find_least_popular_hobby("hobbies_database.txt"))  # -> ['tennis', 'dance', 'puzzles', 'flowers']
    # write_corrected_database("hobbies_database.txt", 'correct_hobbies_database.csv')
