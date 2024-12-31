from pathlib import Path
from collections import Counter

def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    ids = [line.split("   ") for line in lines]
    left, right = [int(id[0]) for id in ids], [int(id[1]) for id in ids]
    counter = Counter(right)
    result = sum([counter[l_id] * l_id for l_id in left])
    print(result)


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
