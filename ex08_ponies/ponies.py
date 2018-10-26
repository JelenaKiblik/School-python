"""EX08 Ponies."""


def decode(line: str) -> str:
    pass


def extract_information(line: str) -> dict:
    pass


def read(read_file: str) -> list:
    pass


def read(read_file: str) -> list:
    pass


def filter_by_location(ponies: list) -> list:
    pass


def filter_by_kind(ponies: list, kind: str) -> list:
    pass


def get_points_for_color(color: str) -> int:
    pass


def add_points(pony: dict) -> dict:
    pass


if __name__ == '__main__':
    print(extract_information('Maud Pommel         Unicorn             pink                green               cyan                Castle of Friendship'))
    print(add_points({'name': 'Maud Pommel', 'kind': 'Unicorn', 'coat_color': 'pink', 'mane_color': 'green', 'eye_color': 'cyan', 'location': 'Castle of Friendship'}))
