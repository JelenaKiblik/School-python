"""Hello world."""


def main():
    """
        Write a function which prints message "Hello world!" to the console.

        The function should not return anything or do anything else except printing the specified message.
        """
    print("Welcome to McDonald's!")
    drink = input("What do you want to drink?")
    print(drink + " with ice cubes is my favorite too!")
    order = input("Can I take your order?")

    if order == "Big Mac":
        print("Big Mac meal coming right up!")
    elif order == "Salad":
        print("Hmm, that's weird.")
    else:
        print("We only serve junk food.")
