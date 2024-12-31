from pathlib import Path
import re

def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    msum = 0
    for line in lines:
        mults = re.findall(r"mul\((\d+),(\d+)\)", line)
        msum += sum([int(x) * int(y) for x,y  in mults])
    print(msum)


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
