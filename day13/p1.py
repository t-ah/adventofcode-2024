from pathlib import Path
from dataclasses import dataclass


@dataclass
class Machine:
    prize: tuple[int, int]
    btn_a: tuple[int, int]
    btn_b: tuple[int, int]

    def compute_cost(self):
        # bp = self.prize[0] // self.btn_b[0]
        for bp in range(self.prize[0] // self.btn_b[0], -1, -1):
            for ap in range(100):
                x = self.get_x(ap, bp)
                if x > self.prize[0]:
                    break
                if x == self.prize[0] and self.get_y(ap, bp) == self.prize[1]:
                    return 3 * ap + bp
        return 0

    def get_x(self, ap, bp):
        return self.btn_a[0] * ap + self.btn_b[0] * bp

    def get_y(self, ap, bp):
        return self.btn_a[1] * ap + self.btn_b[1] * bp

    def check(self, ap, bp):
        return self.get_x(ap, bp) == self.prize[0] and self.get_y(ap, bp) == self.prize[1]


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(machines: list[Machine]) -> None:
    prizes = 0
    total_cost = 0
    for m in machines: # minimize (ap+bp) | ax * ap + bx * bp = px and ay * ap + by * bp = py
        cost = m.compute_cost()
        if cost != 0:
            total_cost += cost
            prizes += 1
    print(total_cost)


def read_input(path: Path):
    with open(path) as f:
        return [parse_machine(s.split("\n")) for s in f.read().split("\n\n")]


def parse_machine(lines):
    a = lines[0].split(" ")
    b = lines[1].split(" ")
    p = lines[2].split(" ")
    ax = int(a[2][2:-1])
    ay = int(a[3][2:])
    bx = int(b[2][2:-1])
    by = int(b[3][2:])
    px = int(p[1][2:-1])
    py = int(p[2][2:])
    return Machine((px, py), (ax, ay), (bx, by))


if __name__ == "__main__":
    main()
