from pathlib import Path
from collections import deque, defaultdict


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


def solve(data, _) -> None:
    starts = [int(d) for d in data]
    lookups = [advance(s, 2000) for s in starts]
    keys = set()
    for l in lookups:
        keys.update(l.keys())
    max_value = 0
    for key in keys:
        max_value = max(sum([l[key] for l in lookups]), max_value)
    print(max_value)


def advance(n, times):
    lookup = defaultdict(lambda: 0)
    diffs = deque(4 * ["-"])
    for i in range(4):
        n_neu = next_secret(n)
        diffs.append(str((n_neu % 10) - (n % 10)))
        diffs.popleft()
        n = n_neu

    for i in range(4, times):
        n_neu = next_secret(n)
        value = n_neu % 10
        diff = str((value) - (n % 10))
        diffs.append(diff)
        diffs.popleft()
        key = "".join([d for d in diffs])
        if key not in lookup:
            lookup[key] = value
        n = n_neu
    return lookup


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
