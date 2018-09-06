"""Hello world."""


def main():
    """Write a function which prints message "Hello world!" to the console."""
    name = input("What's your name? ")
    if name == "":
        print("Name was not inserted!")
    scool = input("Where do you study? ")
    if scool == "":
        print("School was not inserted!")
    if (name != "") and (scool != ""):
        print(f"{name} , welcome to {scool}")

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
