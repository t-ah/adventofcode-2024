from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    lx, ly, grid = build_grid(lines, lambda: -1)
    total = 0
    for x in range(lx):
        for y in range(ly):
            total += get_score(x, y, grid)
    print(total)


def get_score(x, y, grid):
    if grid[x, y] != 0:
        return 0
    current_level = set()
    current_level.add((x, y))
    for i in range(1, 10):
        if len(current_level) == 0:
            return 0
        nodes = current_level
        current_level = set()
        for node in nodes:
            for n in neighbours4(*node):
                if grid[n] == i:
                    current_level.add(n)
    return len(current_level)


def neighbours4(x, y):
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def build_grid(lines: list[str], default_arg) -> tuple[int, int, defaultdict[tuple[int,int], str]]:
    grid = defaultdict(default_arg)
    y_len, x_len = len(lines), len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = int(c)
    return x_len, y_len, grid


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
