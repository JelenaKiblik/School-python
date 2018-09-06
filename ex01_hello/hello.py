"""Hello world."""


def main():
    """Write a function which prints message "Hello world!" to the console."""
    name = input("What's your name? ")
    if name == "":
        print("Name was not inserted!")
    scool = input("Where do you study? ")
    if scool == "":
        print("School was not inserted!")
    else:
        print(name + " , welcome to " + scool)

    m = float(input("How much do you weigh?"))
    p = float(input("How tall are you?"))
    kehamassiindeks = round(m / (p ** 2))

    if kehamassiindeks < 18.5:
        print(str(kehamassiindeks) + ", alakaaluline")
    elif (kehamassiindeks >= 18.5) and (kehamassiindeks < 24.9):
        print(str(kehamassiindeks) + ", normaalkaal")
    else:
        print(str(kehamassiindeks) + ", ülekaaluline")


if __name__ == '__main__':
    main()
