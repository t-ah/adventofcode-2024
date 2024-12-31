from pathlib import Path
from collections import defaultdict


directions = [(0,1), (0,-1), (1,0), (1,1), (1,-1), (-1,0), (-1,-1), (-1,1)]


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    grid = defaultdict(lambda: ".")
    x_len, y_len = len(lines), len(lines[0])
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            grid[x, y] = c
    count = 0
    for x in range(x_len):
        for y in range(y_len):
            count += check(grid, x, y, "XMAS")
    print(count)


def check(grid, x, y, word):
    if grid[x, y] != word[0]:
        return 0
    words = [construct_word(grid, x, y, x_offset, y_offset, len(word)) for x_offset, y_offset in directions]
    return words.count(word)


def construct_word(grid, x, y, x_offset, y_offset, length):
    word = ""
    for i in range(length):
        word += grid[x + (i * x_offset), y + (i * y_offset)]
    return word


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
