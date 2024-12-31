from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(line: str) -> None:
    diskmap = []
    is_file = True
    for id, s_length in enumerate(line):
        length = int(s_length)
        item = id // 2 if is_file else -1
        diskmap.extend(length * [item])
        is_file = not is_file
    i = 0
    j = len(diskmap) - 1
    while i < j:
        if diskmap[i] == -1:
            j = last_item_index(diskmap, j)
            if j > i:
                diskmap[i] = diskmap[j]
                diskmap[j] = -1
        i += 1
    print(checksum(diskmap))


def last_item_index(diskmap, j):
    while True:
        if diskmap[j] != -1:
            return j
        j -= 1


def checksum(diskmap):
    checksum = 0
    for i, n in enumerate(diskmap):
        if n == -1:
            break
        checksum += i * n
    return checksum


def read_input(path: Path) -> str:
    with open(path, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
