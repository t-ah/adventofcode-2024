from pathlib import Path
from collections import defaultdict


directions = ((-1, 0), (0, 1), (1, 0), (0, -1))


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    grid = defaultdict(lambda: "x")
    position = (0, 0)
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            grid[x, y] = c
            if c == "^":
                grid[x, y] = "."
                position = (x, y)
    current_direction_index = 0
    visited = {position}
    while True:
        direction = directions[current_direction_index]
        next_pos = (position[0] + direction[0], position[1] + direction[1])
        match grid[next_pos]:
            case "x":
                break
            case ".":
                position = next_pos
                visited.add(position)
            case "#":
                current_direction_index = (current_direction_index + 1) % 4
            case _:
                raise Exception("How could this happen")
    print(len(visited))


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
