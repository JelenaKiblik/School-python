"""Create schedule from the given file."""


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""

    file = open(input_filename, "r")
    input_string = file.read()
    file.close()
    file_to_write = open(output_filename, "w")
    file_to_write.write(create_schedule_string(input_string))
    file_to_write.close()


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    pass


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")