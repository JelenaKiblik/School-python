"""Encode and decode Caesar cipher."""


def encode(message: str, shift: int, alphabet: str) -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    return helper(message, shift, alphabet)


def decode(message: str, shift: int, alphabet: str) -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    return helper(message, -shift, alphabet)


# def func(alphabet="abcdefghijklmnopqrstuvwxyz"):
#     """Function for alphabet."""
#     return alphabet


def helper(message, shift, alphabet):
    """
    Helper for encode and decode.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: new_message.
    """
    # message = message.lower()
    new_message = ""
    # alphabet = func()
    for i in message:
        if i in alphabet:
            number = ord(i)
            number += shift
            if number > ord("z"):
                number -= len(alphabet)
            elif number < ord("a"):
                number += len(alphabet)
            new_message = new_message + chr(number)
        else:
            new_message = new_message + i
    return new_message


if __name__ == "__main__":
    # simple tests
    print(encode("hello world", 2, alphabet="abcdefghijklmnopqrstuvwxyz"))  # ifmmp xpsme
    print(decode("ifmmp", 25, alphabet="abcdefghijklmnopqrstuvwxyz"))  # hello
