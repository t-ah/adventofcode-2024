from collections import defaultdict


def build_grid(lines: list[str], default_arg) -> tuple[int, int, defaultdict[tuple[int,int], str]]:
    grid = defaultdict(default_arg)
    x_len, y_len = len(lines), len(lines[0])
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            grid[x, y] = c
    return x_len, y_len, grid
