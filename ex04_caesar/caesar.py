"""Encode and decode Caesar cipher."""


def encode(message: str, shift: int, alphabet: str) -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    message = message.lower()
    new_message = ""
    for i in message:
        if i in alphabet:
            number = ord(i)
            number += shift
            if number > ord("z"):
                number -= 26
            elif number < ord("a"):
                number += 26
            new_message = new_message + chr(number)
        else:
            new_message = new_message + i
    return new_message


def decode(message: str, shift: int, alphabet: str) -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    message = message.lower()
    new_message = ""
    for i in message:
        if i in alphabet:
            number = ord(i)
            number -= shift
            if number > ord("z"):
                number -= 26
            elif number < ord("a"):
                number += 26
            new_message = new_message + chr(number)
        else:
            new_message = new_message + i
    return new_message


if __name__ == "__main__":
    # simple tests
    print(encode("Hello world", 1, alphabet="abcdefghijklmnopqrstuvwxyz"))  # ifmmp xpsme
    print(decode("ifmmp", 1, alphabet="abcdefghijklmnopqrstuvwxyz"))  # hello
