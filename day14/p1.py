from pathlib import Path
from collections import Counter


class Robot:
    def __init__(self, line) -> None:
        p, v = [s.split(",") for s in line.split(" ")]
        self.pos = (int(p[0][2:]), int(p[1]))
        self.v = (int(v[0][2:]), int(v[1]))

    def simulate(self, steps, w, h):
        return ((self.pos[0] + (steps * self.v[0])) % w, (self.pos[1] + (steps * self.v[1])) % h)


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    robots = [Robot(line) for line in lines]
    steps, w, h = 100, 101, 103  # w, h = 11, 7 for test
    positions = [robot.simulate(steps, w, h) for robot in robots]
    th_w, th_h = w // 2, h // 2
    quadrants = [get_quadrant(*pos, th_w, th_h) for pos in positions]
    count = Counter(quadrants)
    print(count["ne"] * count["se"] * count["nw"] * count["sw"])


def get_quadrant(x, y, th_w, th_h):
    if x < th_w:
        if y < th_h:
            return "ne"
        if y > th_h:
            return "se"
    if x > th_w:
        if y < th_h:
            return "nw"
        if y > th_h:
            return "sw"
    return "c"

def read_input(path: Path) -> list[str]:
    with open(path) as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
