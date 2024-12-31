from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            solve(format_input(read_input(path)), file_name)


def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


def format_input(s: str):
    return [x.split("\n") for x in s.split("\n\n")]


def solve(data, _) -> None:
    locks = []
    keys = []
    for item in data:
        if item[0][0] == "#":
            locks.append(parse_lock(item))
        else:
            keys.append(parse_key(item))
    total = 0
    for lock in locks:
        for key in keys:
            if not overlaps(lock, key):
                total += 1
    print(total)


def overlaps(lock, key):
    for a, b in zip(lock, key):
        if a + b > 5:
            return True
    return False


def parse_lock(item):
    heights = 5 * [0]
    for y in range(1, 6):
        for x in range(5):
            if item[y][x] == "#":
                heights[x] = y
    return tuple(heights)


def parse_key(item):
    heights = 5 * [0]
    for y in range(5, 0, -1):
        for x in range(5):
            if item[y][x] == "#":
                heights[x] = 6 - y
    return tuple(heights)


if __name__ == "__main__":
    main()
