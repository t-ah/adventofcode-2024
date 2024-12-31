from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            solve(read_input(path).split("\n\n"))


def solve(parts: list[str]) -> None:
    patterns = parts[0].split(", ")
    patterns_map = defaultdict(lambda: list())
    for pattern in patterns:
        patterns_map[pattern[0]].append(pattern)
    goals = parts[1].split("\n")
    cache = dict()
    reachable_goals = [can_be_constructed(goal, patterns_map, cache) for goal in goals]
    print(sum(reachable_goals))


def can_be_constructed(goal, p_map, cache):
    count = 0
    if goal == "":
        return 1
    if goal in cache:
        return cache[goal]
    patterns = p_map[goal[0]]
    for pattern in patterns:
        if pattern == goal[:len(pattern)]:
            ways = can_be_constructed(goal[len(pattern):], p_map, cache)
            count += ways
    cache[goal] = count
    return count



def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
