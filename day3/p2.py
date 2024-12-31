import re
from pathlib import Path


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    msum = 0
    text = "".join(lines)
    index = 0
    while index < len(text):
        disable = re.search(r"don't\(\)", text[index:])
        if disable:
            disable_index = index + disable.end()
            msum += find_mults_in(text, index, disable_index)
            enable = re.search(r"do\(\)", text[disable_index:])
            if enable:
                index = disable_index + enable.end()
            else:  # never enabled again
                break
        else:
            msum += find_mults_in(text, index, len(text))
            break
    print(msum)


def find_mults_in(text, i, j):
    mults = re.findall(r"mul\((\d+),(\d+)\)", text[i:j])
    return sum([int(x) * int(y) for x, y in mults])


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
