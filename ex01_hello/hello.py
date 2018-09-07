"""Hello world."""


def main():
    """Write a function which prints message "Hello world!" to the console."""
    name = input("What's your name? ")
    if name == '':
        print("Name was not inserted!")
    else:
        name_school = input("Where do you study? ")
        if name_school == '':
            print("School was not inserted!")
        else:
            print(f"{name}, welcome to {name_school}")
            m = float(input("Mass (kg): "))
            p = float(input("Height (m): "))
            kehamassiindeks = round(m / (p ** 2), 1)

            if kehamassiindeks < 18.5:
                print(f"{kehamassiindeks}, alakaaluline")
            elif (kehamassiindeks >= 18.5) and (kehamassiindeks < 24.9):
                print(f"{kehamassiindeks}, normaalkaal")
            else:
                print(f"{kehamassiindeks}, ülekaaluline")


if __name__ == '__main__':
    main()
