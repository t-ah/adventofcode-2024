from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    ids = [line.split("   ") for line in lines]
    left, right = [int(id[0]) for id in ids], [int(id[1]) for id in ids]
    left.sort()
    right.sort()
    distances = [abs(b - a) for a, b in zip(left, right)]
    print(sum(distances))


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
