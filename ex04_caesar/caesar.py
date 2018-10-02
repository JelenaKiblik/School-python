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
    i = 0
    new_message = ""
    number_of_letter_in_message = 0
    letter_of_message = message[number_of_letter_in_message]
    number_of_letter_of_message_in_alphabet = alphabet.index(letter_of_message)
    for number_of_letter_in_message in range(len(message)):
        number_of_letter_of_message_in_alphabet += shift
        new_message = message.replace(letter_of_message, alphabet[number_of_letter_of_message_in_alphabet])
        i += shift
    return new_message


if __name__ == "__main__":
    # simple tests
    print(encode("hello", 1))  # ifmmp
    print(decode("ifmmp", 1))  # hello
