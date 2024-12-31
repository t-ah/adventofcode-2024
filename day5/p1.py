from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
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
        middle = update[len(update) // 2]
        if is_valid_update(update, rule_book):
            result += middle
    print(result)


def is_valid_update(update, rule_book):
    while update:
        head = update.pop(0)
        constraints = rule_book[head]
        for constraint in constraints:
            if constraint in update:
                return False
    return True


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
