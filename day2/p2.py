from pathlib import Path


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    reports = [[int(s) for s in line.split(" ")] for line in lines]
    safe_reports = 0
    for report in reports:
        if is_safe(report) or is_safe_with_skip(report):
            safe_reports += 1
    print(safe_reports)


def is_safe(report: list[int]):
    increasing = report[1] > report[0]
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if increasing:
            if diff <= 0:
                return False
        else:
            if diff >= 0:
                return False
        if abs(diff) > 3:
            return False
    return True


# let's try the easy way first
def is_safe_with_skip(report):
    for skip_index in range(len(report)):
        if is_safe(report[:skip_index] + report[skip_index + 1:]):
            return True
    return False


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
