from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    lx, ly, grid = build_grid(lines, lambda: ".")
    checked = set()
    total_cost = 0
    for x in range(lx):
        for y in range(ly):
            if (x, y) not in checked:
                total_cost += determine_cost(x, y, grid, checked)
    print(total_cost)


def determine_cost(x, y, grid, checked):
    expansion = [(x, y)]
    r_type = grid[x, y]
    area = 0
    perimeter = 0
    while expansion:
        area += len(expansion)
        new_expansion = set()
        for node in expansion:
            relevant_neighbours = [xy for xy in neighbours4(*node) if grid[xy] == r_type]
            perimeter += 4 - len(relevant_neighbours)
            unchecked_neighbours = [n for n in relevant_neighbours if n not in checked]
            new_expansion.update(unchecked_neighbours)
            checked.add(node)
        expansion = new_expansion
    return area * perimeter


def build_grid(lines: list[str], default_arg=None) -> tuple[int, int, dict[tuple[int,int], str]]:
    grid = defaultdict(default_arg) if default_arg else dict()
    y_len, x_len = len(lines), len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = c
    return x_len, y_len, grid


def neighbours4(x, y):
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def read_input(path: Path) -> list[str]:
    with open(path) as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
