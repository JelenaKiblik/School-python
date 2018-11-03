"""EX08 Ponies."""
import base64


def decode(line: str) -> str:
    """Decode str."""
    return base64.b64decode(line).decode("UTF-8")


def extract_information(line: str) -> dict:
    """Read the pony data line after decoding. Returns dictionary data.."""
    ponies_list = line.split()
    ponies_dict = dict()
    new_list = []
    for i in range(len(ponies_list)):
        if ponies_list[i] != " " or "":
            new_list.append(ponies_list[i])
    ponies_dict["name"] = new_list[0] + " " + new_list[1]
    ponies_dict["kind"] = new_list[2]
    ponies_dict["coat_color"] = new_list[3]
    ponies_dict["mane_color"] = new_list[4]
    ponies_dict["eye_color"] = new_list[5]
    ponies_dict["location"] = " ".join(new_list[6:])
    return ponies_dict


def read(read_file: str) -> list:
    """Read file information from the file by line, decodes, reads data and saves."""
    try:
        with open(read_file, "r") as f:
            pony_list = []
            next(f)
            next(f)
            for line in f.readlines():
                pony_list.append(extract_information(decode(line)))
        return pony_list
    except Exception:
        raise FileNotFoundError("File not found!")


def filter_by_location(ponies: list) -> list:
    """Remove ponies from a predefined order whose assessment location is not specified ('None')."""
    sort_location = []
    for i in range(len(ponies)):
        if ponies[i]["location"] != "None":
            sort_location.append(ponies[i])
    return sort_location


def filter_by_kind(ponies: list, kind: str) -> list:
    """Filter the pony list so that only ponies whose key 'kind' is the corresponding variable is left."""
    same_ponies_kind = []
    for i in range(len(ponies)):
        if ponies[i]["kind"] == kind:
            same_ponies_kind.append(ponies[i])
    return same_ponies_kind


def get_points_for_color(color: str) -> int:
    """Return the estimated value per color. Colors in the color sequence are the first color with the largest number of points (10)."""
    colors = ['magenta', 'pink', 'purple', 'orange', 'red', 'yellow', 'cyan', 'blue', 'brown', 'green']
    if color not in colors:
        return None
    if colors.index(color) < 6:
        return 10 - colors.index(color)


def add_points(pony: dict) -> dict:
    """The pony dictionary inserts the key 'points' and the value, which is the result judged by the judges."""
    evaluation_locations = {
        'coat_color': ['Town Hall', 'Theater', 'School of Friendship'],
        'mane_color': ['Schoolhouse', 'Crusaders Clubhouse', 'Golden Oak Library'],
        'eye_color': ['Train station', 'Castle of Friendship', 'Retirement Village']
    }
    if pony["location"] in evaluation_locations["coat_color"]:
        pony["points"] = get_points_for_color(pony["coat_color"])
    elif pony["location"] in evaluation_locations['mane_color']:
        pony["points"] = get_points_for_color(pony["mane_color"])
    elif pony["location"] in evaluation_locations["eye_color"]:
        pony["points"] = get_points_for_color(pony["eye_color"])
    return pony


def evaluate_ponies(ponies: list) -> list:
    """Add to each ponies the result obtained in the contest using the add_points function."""
    list_with_points = []
    for i in range(len(ponies)):
        list_with_points.append(add_points(ponies[i]))
    return list_with_points


def sort_by_name(ponies: list) -> list:
    """Sort the ponies so that the names of the 'A' are above. Hint: sorted (key = ..)."""
    return sorted(ponies, key=lambda x: x["name"])


def sort_by_points(ponies: list) -> list:
    """Sort the ponies so that ponies with higher score are above and the ponies with the result of None are excluded."""
    return sorted(ponies, key=lambda x: x["points"], reverse=True)


def format_line(pony: dict, place: int) -> str:
    """Return the string to be printed in a new file per pony."""
    return str(place) + " " * (10 - len(str(place))) + str(pony["points"]) + " " * (10 - len(str(pony["points"]))) + str(pony["name"]) + " " * (20 - len(str(pony["name"]))) + str(pony["kind"]) + " " * (20 - len(str(pony["kind"]))) + str(pony["coat_color"]) + " " * (20 - len(str(pony["coat_color"]))) + str(pony["mane_color"]) + " " * (20 - len(str(pony["mane_color"]))) + str(pony["eye_color"]) + " " * (20 - len(str(pony["eye_color"]))) + str(pony["location"])


def write(input_file: str, kind: str):
    """Pony is written in a regular format (format_line) text file."""
    filtered_list = sort_by_name(evaluate_ponies(filter_by_kind(filter_by_location(read(input_file)), kind)))
    remove_none = []
    for i in range(len(filtered_list)):
        if filtered_list[i]["points"] is not None:
            remove_none.append(filtered_list[i])
    finally_sorted = sort_by_points(remove_none)
    with open("results_for_" + kind + ".txt", "w") as f:
        f.write(
            "PLACE" + " " * 5 + "POINTS" + " " * 4 + "NAME" + " " * 16 + "KIND" + " " * 16 + "COAT COLOR" + " " * 10 + "MANE COLOR" + " " * 10 + "EYE COLOR" + " " * 11 + "LOCATION\n" + "-" * 128 + "\n")
        for i in range(len(finally_sorted)):
            if i > 0:
                f.write("\n")
            f.write(format_line(finally_sorted[i], i + 1))


write("sisendfail.txt", "Unicorn")


if __name__ == '__main__':
    print(decode('TWF1ZCBQb21tZWwgICAgICAgICBVbmljb3JuICAgICAgICAgICAgIHBpbmsgICAgICAgICAgICAgICAgZ3JlZW4gICAgICAgICA'
                 + 'gICAgICBjeWFuICAgICAgICAgICAgICAgIENhc3RsZSBvZiBGcmllbmRzaGlw'))
