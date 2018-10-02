"""Encode and decode Caesar cipher."""


def encode(message: str, shift: int, alphabet: str) -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    default_alphabet = "abcdefghijklmnopqrstuvwxyz"

    def func(alphabet=default_alphabet):
        """Function for alphabet."""
        return alphabet

    new_message = ""
    for i in message:
        if i in func(alphabet):
            number = ord(i)
            number += shift
            if number > ord(func(alphabet[-1])):
                number -= len(func())
            elif number < ord(func(alphabet[0])):
                number += len(func())
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
    default_alphabet = "abcdefghijklmnopqrstuvwxyz"

    def func(alphabet=default_alphabet):
        """Function for alphabet."""
        return alphabet

    new_message = ""
    for i in message:
        if i in func():
            number = ord(i)
            number -= shift
            if number > ord(func(alphabet[-1])):
                number -= len(func())
            elif number < ord(func(alphabet[0])):
                number += len(func())
            new_message = new_message + chr(number)
        else:
            new_message = new_message + i
    return new_message
