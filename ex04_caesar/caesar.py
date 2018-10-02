"""Encode and decode Caesar cipher."""


def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    return helper(message, shift, alphabet)


def decode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    return helper(message, -shift, alphabet)


def helper(message: str, shift: int, alphabet: str):
    """Helper function for the cipher.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: New message.
    """
    new_message = ""
    if shift == 0:
        return message
    else:
        for i in message:
            if i in alphabet:
                number = ord(i)
                number += shift
                if number > ord(alphabet[-1]):
                    number -= len(alphabet)
                elif number < ord(alphabet[0]):
                    number += len(alphabet)
                new_message = new_message + chr(number)
            else:
                new_message = new_message + i
        return new_message


if __name__ == "__main__":
    # simple tests
    print(encode("hello", 1))  # ifmmp
    print(decode("ifmmp", 1))  # hello
