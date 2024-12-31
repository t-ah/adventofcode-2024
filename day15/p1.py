from pathlib import Path
from collections import defaultdict


directions = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            blocks = read_input(path)
            solve(blocks)


def solve(blocks: list[str]) -> None:
    lx, ly, grid, pos = build_grid(blocks[0].split("\n"), lambda: "#")
    instructions = blocks[1].replace("\n", "")
    for instr in instructions:
        move = directions[instr]
        next_pos = moved(pos, move)
        match grid[next_pos]:
            case "#":
                continue
            case ".":
                pos = next_pos
            case "O":
                gap = find_gap(grid, next_pos, move)
                if gap:
                    grid[gap] = "O"
                    grid[next_pos] = "."
                    pos = next_pos
    print(gps(grid, lx, ly))


def gps(grid, lx, ly):
    total = 0
    for x in range(lx):
        for y in range(ly):
            if grid[x, y] == "O":
                total += x + 100 * y
    return total


def find_gap(grid, pos, move):
    while True:
        pos = moved(pos, move)
        match grid[pos]:
            case "#":
                return False
            case ".":
                return pos


def moved(pos, move):
    return tuple(pos[i] + move[i] for i in [0,1])


def build_grid(lines: list[str], default_arg) -> tuple[int, int, defaultdict[tuple[int,int], str], tuple[int, int]]:
    grid = defaultdict(default_arg)
    y_len, x_len = len(lines), len(lines[0])
    start = (0, 0)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = c
            if c == "@":
                grid[x, y] = "."
                start = (x, y)
    return x_len, y_len, grid, start


def read_input(path: Path) -> list[str]:
    with open(path) as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
