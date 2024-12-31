from pathlib import Path


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            line = read_input(path)
            solve(line)


def solve(line: str) -> None:
    stones = line.split(" ")
    cache = dict()
    total = sum([simulate(s, 75, cache) for s in stones])
    print(total)


def simulate(s, iterations, cache) -> int:
    if iterations == 0:
        return 1
    if (s, iterations) in cache:
        return cache[s, iterations]
    if s == "0":
        result = simulate("1", iterations - 1, cache)
    elif len(s) % 2 == 0:
        result = simulate(str(int(s[:len(s)//2])), iterations - 1, cache) +  simulate(str(int(s[len(s)//2:])), iterations - 1, cache)
    else:
        result = simulate(str(int(s) * 2024), iterations - 1, cache)
    cache[s, iterations] = result
    return result


def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
