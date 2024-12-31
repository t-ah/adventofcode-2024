from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            solve(format_input(read_input(path)), file_name)


def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


def format_input(s: str):
    parts = s.split("\n\n")
    return (
        [x.split(": ") for x in parts[0].split("\n")],
        [x.split(" ") for x in parts[1].split("\n")],
    )


def solve(data, _) -> None:
    values = defaultdict(lambda: -1)
    for w, val in data[0]:
        values[w] = int(val)
    unfired_rules = data[1]
    while unfired_rules:
        rules = unfired_rules
        unfired_rules = []
        for rule in rules:
            inA, inB = rule[0], rule[2]
            if inA in values and inB in values:
                match rule[1]:
                    case "AND":
                        values[rule[4]] = values[inA] and values[inB]
                    case "OR":
                        values[rule[4]] = values[inA] or values[inB]
                    case "XOR":
                        values[rule[4]] = values[inA] ^ values[inB]
            else:
                unfired_rules.append(rule)
    print(get_result(values))


def get_result(values):
    result = []
    for key in sorted(list(values.keys())):
        if key[0] == "z":
            result.append(str(values[key]))
    return int("".join(reversed(result)), 2)


if __name__ == "__main__":
    main()
