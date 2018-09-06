"""Hello world."""


def main():
    """Write a function which prints message "Hello world!" to the console."""
    name = input("What's your name? ")
    name_scool = input("Where do you study? ")

    if (name == "") and (name_scool != ""):
        print("Name was not inserted!")
    elif (name_scool == "") and (name != ""):
        print("School was not inserted!")
    elif (name_scool == "") and (name == ""):
        print("Name was not inserted!")
        print("School was not inserted!")
    else:
        print(f"{name} , welcome to {name_scool}")

    m = int(input("Mass (kg): "))
    p = int(input("Height (m): "))
    kehamassiindeks = round(m / (p ** 2), 1)

    if kehamassiindeks < 18.5:
        print(f"{kehamassiindeks}, alakaaluline")
    elif (kehamassiindeks >= 18.5) and (kehamassiindeks < 24.9):
        print(f"{kehamassiindeks}, normaalkaal")
    else:
        print(f"{kehamassiindeks}, ülekaaluline")


if __name__ == '__main__':
    main()
