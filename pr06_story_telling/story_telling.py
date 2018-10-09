"""Collect story parts from a messy text."""


def read_file(file) -> str:
    """
    Read the text from given file into string.

    :param file: file path
    :return: string
    """
    file = open(file, "r")
    my_string = file.read()
    return get_clean_text(my_string)


def get_clean_text(messy_text: str) -> str:
    """
    Process given text, remove unneeded symbols and retrieve a story.

    :param messy_text: string
    :return: clean string
    """
    new_text = ""
    replace = {
        "*": "\"",
        "!": "?",
        "/": ',',
        "?": "!"
    }
    remove = "1234567890&@#$%^()_+|><~"
    pls_do_upper = False
    for l in messy_text:
        if l in replace:
            new_text += replace[l]
        elif l not in remove:
            if pls_do_upper:
                new_text += l.upper()
            else:
                new_text += l
    return new_text
