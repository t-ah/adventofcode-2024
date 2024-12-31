from pathlib import Path
import itertools
from grid_builder import build_grid


allowed = ["MS", "SM"]


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    x_len, y_len, grid = build_grid(lines, lambda: ".")
    result = len(
        [
            True
            for x, y in itertools.product(range(x_len), range(y_len))
            if check(grid, x, y)
        ]
    )
    print(result)


def check(grid, x, y):
    if grid[x, y] != "A":
        return False
    w1 = grid[x - 1, y - 1] + grid[x + 1, y + 1]
    w2 = grid[x + 1, y - 1] + grid[x - 1, y + 1]
    if w1 not in allowed or w2 not in allowed:
        return False
    return True


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
