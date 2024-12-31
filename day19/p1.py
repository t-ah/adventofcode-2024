from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            solve(read_input(path).split("\n\n"))


def solve(parts: list[str]) -> None:
    patterns = parts[0].split(", ")
    patterns_map = defaultdict(lambda: list())
    for pattern in patterns:
        patterns_map[pattern[0]].append(pattern)
    goals = parts[1].split("\n")
    cache = set()
    reachable_goals = [goal for goal in goals if can_be_constructed(goal, patterns_map, cache)]
    print(len(reachable_goals))


def can_be_constructed(goal, p_map, cache):
    if goal == "" or goal in cache:
        return True
    patterns = p_map[goal[0]]
    for pattern in patterns:
        if pattern == goal[:len(pattern)]:
            if can_be_constructed(goal[len(pattern):], p_map, cache):
                cache.add(goal)
                return True
    return False



def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
