"""
This code doesn't solve the problem, but I used it somehow to solve it manually.
"""

from pathlib import Path


def main():
    for file_name in ["p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            solve(format_input(read_input(path)), file_name)


def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


def format_input(s: str):
    parts = s.split("\n\n")
    return [tuple(x.split(" ")) for x in parts[1].split("\n")]


def solve(data, _) -> None:
    # for i in range(45):
    #     y = bin_str(0)
    #     x = bin_str(pow(2, i))
    #     print(f"{i}:")
    #     run(x, y, data)
    # Problems: 15, 21, 30, 34
    # cqk,fph,gds,jrs,wrk,z15,z21,z34
    print_rules("x34", data)


def print_rules(start, data):
    rules = find_rules(start, data)
    targets = [rule[4] for rule in rules]
    for _ in range(4):
        new_targets = []
        for t in targets:
            new_rules = find_rules(t, data)
            rules.update(new_rules)
            for rule in new_rules:
                new_targets.append(rule[4])
        targets = new_targets
    for rule in sorted(rules):
        print(" ".join(rule))


def find_rules(start, rules):
    return set([rule for rule in rules if start == rule[0] or start == rule[2]])


def bin_str(n):
    s = bin(n)[2:]
    padding = "".join((45 - len(s)) * ["0"])
    return (padding + s)[::-1]


def run(x_str, y_str, unfired_rules):
    # x_str, y_str = bin_str(x), bin_str(y)
    # x_str = "".join(44 * ["0"])
    # y_str = bin_str(pow(2, 40))
    values = dict()
    for i, d in enumerate(x_str):
        if i < 10:
            values[f"x0{i}"] = int(d)
        else:
            values[f"x{i}"] = int(d)
    for i, d in enumerate(y_str):
        if i < 10:
            values[f"y0{i}"] = int(d)
        else:
            values[f"y{i}"] = int(d)
    while unfired_rules:
        l = len(unfired_rules)
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
        if len(unfired_rules) == l:
            break
    expected = bin(int(x_str[::-1], 2) + int(y_str[::-1], 2))[2:][::-1]
    padding = "".join((45 - len(expected)) * ["0"])
    print(expected + padding)
    print(get_result(values))


def get_result(values):
    result = []
    for key in sorted(list(values.keys())):
        if key[0] == "z":
            result.append(str(values[key]))
    return "".join(result)


if __name__ == "__main__":
    main()
