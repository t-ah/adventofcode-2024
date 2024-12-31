from dataclasses import dataclass
from pathlib import Path


@dataclass
class Space:
    index: int
    length: int


@dataclass
class BlockFile:
    f_id: int
    index: int
    length: int


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(line: str) -> None:
    files = []
    spaces = []
    index = 0
    for i, n_str in enumerate(line):
        n = int(n_str)
        if i % 2 == 0:  # if FILE
            files.append(BlockFile(i // 2, index, n))
        else:  # SPACE
            spaces.append(Space(index, n))
        index += n
    for f in files[::-1]:  # from the back
        s = find_space(f, spaces)
        if s:
            f.index = s.index
            s.index += f.length
            s.length -= f.length
    print(checksum(files))


def find_space(f, spaces):
    for s in spaces:
        if s.index > f.index:
            return None
        if s.length >= f.length:
            return s


def checksum(files):
    checksum = 0
    for f in files:
        for i in range(f.index, f.index + f.length):
            checksum += i * f.f_id
    return checksum


def read_input(path: Path) -> str:
    with open(path, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
