from collections import defaultdict


def build_grid(
    lines: list[str],
    default_entry: object,
    special_items: set[str],
    replace_item: str | None,
) -> tuple[
    int, int, defaultdict[tuple[int, int], object], dict[str, list[tuple[int, int]]]
]:
    grid = defaultdict(lambda: default_entry)
    positions = {item: list() for item in special_items}
    ly, lx = len(lines), len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in special_items:
                positions[c].append((x, y))
                grid[x, y] = c if not replace_item else replace_item
            else:
                grid[x, y] = c
    return lx, ly, grid, positions


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def neighbours_cross(xy, d):
    x, y = xy
    return (x + d, y), (x - d, y), (x, y + d), (x, y - d)


def neighbours_square(x, y, d):  # TODO use d
    return (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
    )


def neighbvours_diamond(xy, d):
    sx, sy = xy
    for dx in range(-d, d + 1):
        x = sx + dx
        y_dist = d - abs(dx)
        for dy in range(-y_dist, y_dist + 1):
            y = sy + dy
            yield x, y


def flood_grid(grid, start):
    distances = {start: 0}
    level = 0
    last_level = {start}
    while last_level:
        level += 1
        new_last_level = set()
        for node in last_level:
            for neighbour in neighbours_cross(node, 1):
                if grid[neighbour] == "." and neighbour not in distances:
                    new_last_level.add(neighbour)
                    distances[neighbour] = level
        last_level = new_last_level
    return distances


def print_grid(pos, w, h):
    grid = defaultdict(lambda: ".")
    for p in pos:
        grid[p] = "#"
    lines = []
    for y in range(h):
        line = "".join([grid[x, y] for x in range(w)])
        lines.append(line)
    print("\n".join(lines))
