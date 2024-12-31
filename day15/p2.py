"""
Mamma mia
TODO: extract position stuff, improve grid stuff
"""

from pathlib import Path
from collections import defaultdict


directions = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}
opposites = {"[": "]", "]": "[", ".": "."}


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            blocks = read_input(path)
            solve(blocks)


def solve(blocks: list[str]) -> None:
    lx, ly, grid, pos = build_grid(blocks[0].split("\n"), lambda: "#")
    instructions = blocks[1].replace("\n", "")
    for instr in instructions:
        # print_grid(grid, lx, ly)
        move = directions[instr]
        next_pos = moved(pos, move)

        if instr in ["<", ">"]:
            match grid[next_pos]:
                case "#":
                    continue
                case ".":
                    pos = next_pos
                case "[" | "]":
                    gap = find_gap(grid, next_pos, move)
                    if gap:
                        for p in path(next_pos, gap, move):
                            grid[p] = opposites[grid[p]]
                        grid[next_pos] = "."
                        match instr:
                            case "<":
                                grid[gap] = "["
                            case ">":
                                grid[gap] = "]"
                        pos = next_pos
        else:
            boxes = []
            match grid[next_pos]:
                case "#":
                    continue
                case ".":
                    pos = next_pos
                case "[":
                    boxes = get_affected(grid, next_pos, move)
                case "]":
                    boxes = get_affected(grid, moved(next_pos, directions["<"]), move)
            if boxes:
                for left in boxes:
                    right = moved(left, directions[">"])
                    grid[left] = "."
                    grid[right] = "."
                for left in boxes:
                    right = moved(left, directions[">"])
                    grid[moved(left, move)] = "["
                    grid[moved(right, move)] = "]"
                pos = next_pos
    print(gps(grid, lx, ly))


def get_affected(grid, pos_l, move):
    """find all left parts of affected boxes - spaghetti recursion"""
    pos_r = moved(pos_l, directions[">"])
    affected = []
    for next_pos in [moved(pos_l, move), moved(pos_r, move)]:
        item = grid[next_pos]
        match item:
            case "#":
                return False
            case "[":
                affected.append(next_pos)
            case "]":
                affected.append(moved(next_pos, directions["<"]))
    result = [pos_l]
    for aff in affected:
        further_affected = get_affected(grid, aff, move)
        if not further_affected:
            return False
        result.extend(further_affected)
    return result


def path(pos, target, move):
    while pos != target:
        pos = moved(pos, move)
        yield pos


def gps(grid, lx, ly):
    total = 0
    for x in range(lx):
        for y in range(ly):
            if grid[x, y] == "[":
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


def print_grid(grid, lx, ly):
    lines = []
    for y in range(ly):
        line = "".join([grid[x, y] for x in range(lx)])
        lines.append(line)
    print("\n".join(lines) + "\n")


def moved(pos, move):
    return tuple(pos[i] + move[i] for i in [0, 1])


def build_grid(
    lines: list[str], default_arg
) -> tuple[int, int, defaultdict[tuple[int, int], str], tuple[int, int]]:
    grid = defaultdict(default_arg)
    y_len, x_len = len(lines), len(lines[0])
    start = (0, 0)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                case "#" | ".":
                    grid[2 * x, y] = c
                    grid[2 * x + 1, y] = c
                case "O":
                    grid[2 * x, y] = "["
                    grid[2 * x + 1, y] = "]"
                case "@":
                    grid[2 * x, y] = "."
                    grid[2 * x + 1, y] = "."
                    start = (2 * x, y)
    return 2 * x_len, y_len, grid, start


def read_input(path: Path) -> list[str]:
    with open(path) as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
