from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
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
    limit = 100 if "test" not in file_name else 4
    cheats = [count_cheats(pos, distances, limit) for pos in distances]
    print(sum(cheats))


def count_cheats(pos, distances, limit):
    count = 0
    for nb in neighbours4(pos, 2):
        if nb in distances:
            if distances[nb] - distances[pos] >= limit + 2:
                count += 1
    return count


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
