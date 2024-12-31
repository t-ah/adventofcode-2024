from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            solve(format_input(read_input(path)), file_name)


def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


def format_input(s: str):
    return s.split("\n")


def solve(data, _) -> None:
    starts = [int(d) for d in data]
    results = [advance(s, 2000) for s in starts]
    print(sum(results))


def advance(n, times):
    for _ in range(times):
        n = next_secret(n)
    return n


def next_secret(n: int) -> int:
    n ^= n * 64
    n %= 16777216
    n ^= n // 32
    n %= 16777216
    n ^= n * 2048
    n %= 16777216
    return n


if __name__ == "__main__":
    main()
