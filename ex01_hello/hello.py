"""Hello world."""


def main():
    """Write a function which prints message "Hello world!" to the console."""
    name = input("What's your name? ")
    scool = input("Where do you study? ")
    if name == "":
        print("Name was not inserted!")
    if scool == "":
        print("School was not inserted!")
    else:
        print(name + " , welcome to " + scool)

    m = float(input("How much do you weigh?"))
    p = float(input("How tall are you?"))
    kehamassiindeks = round(m / (p ** 2))

    if kehamassiindeks < 18.5:
        print(str(kehamassiindeks) + " Alakaaluline")
    elif (kehamassiindeks >= 18.5) and (kehamassiindeks < 24.9):
        print(str(kehamassiindeks) + " Normaalkaal")
    else:
        print(str(kehamassiindeks) + " ja üle Ülekaaluline")


if __name__ == '__main__':
    main()
