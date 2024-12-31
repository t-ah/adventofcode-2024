from pathlib import Path


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    total = 0
    for line in lines:
        parts = line.split(": ")
        result = int(parts[0])
        values = [int(x) for x in parts[1].split(" ")]
        if check(result, values[0], values[1:]):
            total += result
    print(total)


def check(result: int, current, values: list[int]) -> bool:
    if len(values) == 1:
        return result == current + values[0] or result == current * values[0] or result == concat(current, values[0])
    return check(result, current + values[0], values[1:]) or check(result, current * values[0], values[1:]) or check(result, concat(current, values[0]), values[1:])


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
