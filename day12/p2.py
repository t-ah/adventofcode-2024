from collections import defaultdict
from pathlib import Path


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
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
    region = set()
    while expansion:
        region.update(expansion)
        new_expansion = set()
        for node in expansion:
            relevant_neighbours = [
                xy
                for xy in neighbours4(*node)
                if grid[xy] == r_type and xy not in checked
            ]
            new_expansion.update(relevant_neighbours)
            checked.add(node)
        expansion = new_expansion
    return len(region) * count_sides(region)


def count_sides(region):
    by_x = defaultdict(lambda: list())
    by_y = defaultdict(lambda: list())
    for n in region:
        for offset in [1, -1]:
            if (n[0] + offset, n[1]) not in region:
                by_x[n[0] + (offset / 2)].append(n[1])
            if (n[0], n[1] + offset) not in region:
                by_y[n[1] - (offset / 2)].append(n[0])
    total = 0
    for numbers in by_x.values():
        total += get_contiguous(numbers)
    for numbers in by_y.values():
        total += get_contiguous(numbers)
    return total


def get_contiguous(numbers):
    numbers.sort()
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] > 1:
            count += 1
    return count + 1


def build_grid(
    lines: list[str], default_arg=None
) -> tuple[int, int, dict[tuple[int, int], str]]:
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
