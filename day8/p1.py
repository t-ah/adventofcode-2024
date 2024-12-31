from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    x_len, y_len, grid, lookup = build_grid(lines, lambda: ".")
    locations = set()
    for key, nodes in lookup.items():
        for i in range(len(nodes)):
            for j in range (i + 1, len(nodes)):
                node = nodes[i]
                other = nodes[j]
                x_diff = node[0] - other[0]
                y_diff = node[1] - other[1]
                locations.add((node[0] + x_diff, node[1] + y_diff))
                locations.add((other[0] - x_diff, other[1] - y_diff))
    locations_in_bounds = [loc for loc in locations if 0 <= loc[0] < x_len and 0 <= loc[1] < y_len]
    print(len(locations_in_bounds))


def build_grid(lines: list[str], default_arg) -> tuple[int, int, defaultdict[tuple[int,int], str], dict[str, tuple[int, int]]]:
    grid = defaultdict(default_arg)
    lookup = defaultdict(lambda: list())
    y_len, x_len = len(lines), len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = c
            if c != ".":
                lookup[c].append((x, y))
    return x_len, y_len, grid, lookup


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
