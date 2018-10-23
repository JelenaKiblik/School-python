"""Create schedule from the given file."""
import re


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
    schedule = []
    converted_time = convert_time(input_string)
    if len(create_dictionary(input_string)) == 0:
        line = f"{'-' * 18}"
        schedule.append(line)
        schedule.append(f"|  time | items  |")
        schedule.append(line)
        schedule.append(f"| No items found |")
        schedule.append(line)
    else:
        time_len = get_length_time(input_string)
        word_len = get_length(input_string)
        line = f"--{'-' * (time_len - 4)}{'-' * 12}{'-' * (word_len - 5)}--"
        schedule.append(line)
        schedule.append(f"| {' ' * (time_len - 4)}time | items{' ' * (word_len - 5)} |")
        schedule.append(line)
        for time in converted_time:
            word = ', '.join(converted_time.get(time))
            if word_len < 5:
                schedule.append(f"| {time} {' ' * (time_len - len(time))}| {word}{' ' * (5 - len(word))} |")
            else:
                schedule.append(f"| {' ' * (time_len - len(time))}{time} | {word}{' ' * (word_len - len(word))} |")
        schedule.append(line)
    return "\n".join(schedule)


def create_dictionary(input_string: str):
    """Create dictionary from the given input string."""
    dictionary = {}
    for match in re.finditer(r"\s(\d{1,2})\D(\d{1,2})\s+([a-zA-Z]+)", input_string):
        activity = match.group(3).lower()
        minute = f"{int(match.group(2)):02}"
        hour = f"{int(match.group(1)):02}"
        if 00 <= int(hour) <= 23 and 00 <= int(minute) <= 59:
            dictionary.setdefault(f"{hour}:{minute}", [])
            if activity not in dictionary[f"{hour}:{minute}"]:
                dictionary[f"{hour}:{minute}"].append(activity)
    return dictionary


def get_length(input_string: str):
    """Get the length of the longest word."""
    max_length = 0
    new_time = convert_time(input_string)
    for key in new_time:
        word_length = len(', '.join(new_time.get(key)))
        if word_length > max_length:
            max_length = word_length
    return max_length


def get_length_time(input_string: str):
    """Get the length of the biggest time."""
    max_length = 0
    for key in convert_time(input_string):
        if len(key) > max_length:
            max_length = len(key)
    return max_length


def convert_time(input_string):
    """Convert time function."""
    dictionary = create_dictionary(input_string)
    for key in sorted(dictionary.items()):
        minute = (key[0])[3:5]
        hour = int((key[0])[0:2]) % 24
        isAM = (hour >= 0) and (hour < 12)
        if isAM:
            new_time = f"12:{minute} AM" if (hour == 0) else f"{(key[0])[0:2]}:{minute} AM"
        else:
            new_time = f"{key[0]} PM" if (hour == 12) else f"{int(hour) - 12}:{minute} PM"
        dictionary[new_time.lstrip("0")] = dictionary.pop(key[0])
    return dictionary


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
