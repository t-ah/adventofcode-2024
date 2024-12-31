from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            parts = read_input(path)
            solve(parts)


def solve(parts: list[str]):
    rules = [[int(x) for x in rule.split("|")] for rule in parts[0].split("\n")]
    updates = [[int(x) for x in update.split(",")] for update in parts[1].split("\n")]

    rule_book = defaultdict(lambda: list())
    for rule in rules:
        rule_book[rule[1]].append(rule[0])

    result = 0
    for update in updates:
        if reorder(update, rule_book):
            result += update[len(update) // 2]
    print(result)


def reorder(update, rule_book):
    i = 0
    reordered = False
    while i < len(update):
        head = update[i]
        constraints = rule_book[head]
        reordered_iteration = False
        for constraint in constraints:
            if constraint in update[i + 1 :]:
                reordered_iteration = True
                reordered = True
                update.remove(constraint)
                update.insert(i, constraint)
        if not reordered_iteration:
            i += 1
    return reordered


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
