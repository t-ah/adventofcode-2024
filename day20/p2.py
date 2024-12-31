from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            solve(format_input(read_input(path)), file_name)


def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


def format_input(s: str):
    return s.split("\n")


def solve(data, file_name) -> None:
    _, _, grid, special_positions = build_grid(data, "#", {"S", "E"}, ".")
    start = special_positions["S"][0]
    distances = flood_grid(grid, start)
    limit = 100 if "test" not in file_name else 50
    cheats = set()
    for pos in distances:
        cheats.update(get_cheats(pos, distances, limit))
    print(len(cheats))
    print(len(list(diamond((0, 0), 20))))


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_cheats(pos, distances, limit):
    cheats = set()
    for nb in diamond(pos, 20):
        if nb in distances:
            if distances[nb] - distances[pos] >= limit + distance(pos, nb):
                cheats.add((pos, nb))
    return cheats


def build_grid(lines: list[str], default_entry, special_items, replace_item):
    grid = defaultdict(lambda: default_entry)
    positions = {item: list() for item in special_items}
    ly, lx = len(lines), len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in special_items:
                positions[c].append((x, y))
                grid[x, y] = c if not replace_item else replace_item
            else:
                grid[x, y] = c
    return lx, ly, grid, positions


def diamond(xy, d):
    sx, sy = xy
    for dx in range(-d, d + 1):
        x = sx + dx
        y_dist = d - abs(dx)
        for dy in range(-y_dist, y_dist + 1):
            y = sy + dy
            yield x, y


def neighbours4(xy, d):
    x, y = xy
    return (x + d, y), (x - d, y), (x, y + d), (x, y - d)


def flood_grid(grid, start):
    distances = {start: 0}
    level = 0
    last_level = {start}
    while last_level:
        level += 1
        new_last_level = set()
        for node in last_level:
            for neighbour in neighbours4(node, 1):
                if grid[neighbour] == "." and neighbour not in distances:
                    new_last_level.add(neighbour)
                    distances[neighbour] = level
        last_level = new_last_level
    return distances


if __name__ == "__main__":
    main()
