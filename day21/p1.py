from pathlib import Path

num_pad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [" ", "0", "A"]]

dir_pad = [[" ", "^", "A"], ["<", "v", ">"]]

x_offset2direction = {-2: "<<", -1: "<", 0: "", 1: ">", 2: ">>"}

y_offset2direction = {-3: "^^^", -2: "^^", -1: "^", 0: "", 1: "v", 2: "vv", 3: "vvv"}


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            solve(format_input(read_input(path)), file_name)


def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


def format_input(s: str):
    return s.split("\n")


def solve(data, file_name) -> None:
    num_coords = dict()
    for y in range(len(num_pad)):
        for x in range(len(num_pad[0])):
            num_coords[num_pad[y][x]] = (x, y)
    num_blocked = {(0, 3)}

    dir_coords = dict()
    for y in range(len(dir_pad)):
        for x in range(len(dir_pad[0])):
            dir_coords[dir_pad[y][x]] = (x, y)
    dir_blocked = {(0, 0)}

    num_cache = {"": "A"}
    dir_cache = {"": "A"}

    total = 0
    dir_pads = 2
    for code in data:
        tf = shortest_sequence(code, num_coords, num_cache, num_blocked)
        l = sum(
            [
                get_length(x + "A", dir_coords, dir_cache, dir_blocked, dir_pads)
                for x in tf[:-1].split("A")
            ]
        )
        result = l * int(code[:-1])
        total += result
    print(f"Total: {total}")


def shortest_sequence(sequence, coords, cache, blocked):
    sections = sequence[:-1].split("A")
    new_sequence = "".join(
        [expand_once(section, coords, cache, blocked) for section in sections]
    )
    return new_sequence


def expand_once(section, coords, cache, blocked):
    if section in cache:
        return cache[section]
    pos = coords["A"]
    complete_path = ""
    for btn in section + "A":
        coord = coords[btn]
        path = generate_path(pos, coord, blocked)
        complete_path += path
        pos = coord
    cache[section] = complete_path
    return complete_path


def get_length(section, coords, cache, blocked, times):
    if (section, times) in cache:
        return cache[section, times]
    pos = coords["A"]
    if times == 1:
        l = 0
        for btn in section:
            coord = coords[btn]
            path = generate_path(pos, coord, blocked)
            l += len(path)
            pos = coord
        cache[section, 1] = l
        return l
    length = 0
    for btn in section:
        coord = coords[btn]
        path = generate_path(pos, coord, blocked)
        length += get_length(path, coords, cache, blocked, times - 1)
        pos = coord
    cache[section, times] = length
    return length


def generate_path(start, end, blocked):
    if start == end:
        return "A"
    sx, sy = start
    ox, oy = (end[0] - sx, end[1] - sy)
    can_start_x = True
    can_start_y = True
    if ox != 0:
        ox_normal = ox // abs(ox)
        for x in range(sx + ox_normal, sx + ox + ox_normal, ox_normal):
            if (x, sy) in blocked:
                can_start_x = False
                break
    if oy != 0:
        oy_normal = oy // abs(oy)
        for y in range(sy + oy_normal, sy + oy + oy_normal, oy_normal):
            if (sx, y) in blocked:
                can_start_y = False
                break
    if not can_start_x or (ox > 0 and can_start_y):
        return y_offset2direction[oy] + x_offset2direction[ox] + "A"
    return x_offset2direction[ox] + y_offset2direction[oy] + "A"


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == "__main__":
    main()
