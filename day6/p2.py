from pathlib import Path
from collections import defaultdict


directions = ((-1, 0), (0, 1), (1, 0), (0, -1))


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


# just check for each next position, if an obstacle there would lead to a loop
def solve(lines: list[str]) -> None:
    grid = defaultdict(lambda: "x")
    position = (0, 0)
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == "^":
                grid[x, y] = []
                position = (x, y)
            elif c == ".":
                grid[x, y] = []
            else:
                grid[x, y] = c

    current_direction_index = 0
    count = 0
    while True:
        direction = directions[current_direction_index]
        next_pos = (position[0] + direction[0], position[1] + direction[1])
        match grid[next_pos]:
            case "x":
                break
            case "#":
                current_direction_index = (current_direction_index + 1) % 4
            case []:
                grid[next_pos] = "#"
                if check_loop(grid, position, current_direction_index):
                    count += 1
                grid[next_pos] = []
                grid[position].append(
                    current_direction_index
                )  #  if we leave the same cell in the same direction twice, it's a loop
                position = next_pos
            case _:
                grid[position].append(current_direction_index)
                position = next_pos
    print(count)


def check_loop(grid, pos, dir_i) -> bool:
    overlay = defaultdict(
        lambda: []
    )  # remember additional directions without modifying the original grid
    while True:
        direction = directions[dir_i]
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        match grid[next_pos]:
            case "x":
                break
            case "#":
                dir_i = (dir_i + 1) % 4
            case _:
                if dir_i in grid[pos] or dir_i in overlay[pos]:
                    return True
                overlay[pos].append(dir_i)
                pos = next_pos
    return False


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
