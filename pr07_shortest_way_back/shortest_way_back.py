"""Find the shortest way back in a taxicab geometry."""


def shortest_way_back(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    path_back = ""
    x, y = helper(path)
    for i in range(abs(x)):
        if x > 0:
            path_back += "S"
        elif x < 0:
            path_back += "N"
    for i in range(abs(y)):
        if y > 0:
            path_back += "W"
        elif y < 0:
            path_back += "E"
    return path_back


def helper(path: str):
    """Find location."""
    x = 0
    y = 0
    for i in path:
        if i == "N":
            x += 1
        elif i == "S":
            x -= 1
        elif i == "W":
            y -= 1
        elif i == "E":
            y += 1
    return x, y


if __name__ == '__main__':
    assert shortest_way_back("NNN") == "SSS"
    assert shortest_way_back("SS") == "NN"
    assert shortest_way_back("E") == "W"
    assert shortest_way_back("WWWW") == "EEEE"

    assert shortest_way_back("") == ""
    assert shortest_way_back("NESW") == ""

    assert shortest_way_back("NNEESEW") in ["SWW", "WSW", "WWS"]
