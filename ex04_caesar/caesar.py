"""Encode and decode Caesar cipher."""


def encode(message: str, shift: int, alphabet: str) -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    new_message = ""
    for i in message:
        if i.isalpha():
            alphabet = ord(i) + shift
            if alphabet > ord('z'):
                alphabet -= 26
            finalLetter = chr(alphabet)
            new_message += finalLetter
    return new_message


def decode(message: str, shift: int, alphabet: str) -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    new_message = ""
    for i in message:
        if i.isalpha():
            alphabet = ord(i) - shift
        if alphabet > ord('z'):
            alphabet += 26
        finalLetter1 = chr(alphabet)
        new_message += finalLetter1
    return new_message
