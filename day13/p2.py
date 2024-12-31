from pathlib import Path
import z3


class Machine:
    def __init__(self, lines):
        a = lines[0].split(" ")
        b = lines[1].split(" ")
        p = lines[2].split(" ")
        self.btn_a = (int(a[2][2:-1]), int(a[3][2:]))
        self.btn_b = (int(b[2][2:-1]), int(b[3][2:]))
        self.prize = (10000000000000 + int(p[1][2:-1]), 10000000000000 + int(p[2][2:]))

    def solve(self):
        ap = z3.Int('ap')
        bp = z3.Int('bp')
        s = z3.Solver()
        s.add(self.btn_a[0] * ap + self.btn_b[0] * bp == self.prize[0], ap >= 0, bp >= 0)
        s.add(self.btn_a[1] * ap + self.btn_b[1] * bp == self.prize[1], ap >= 0, bp >= 0)
        if s.check() == z3.sat:
            m = s.model()
            return 3 * m[ap].as_long() + m[bp].as_long()
        return 0


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(machines: list[Machine]) -> None:
    total_cost = 0
    for m in machines: # minimize (ap+bp) | ax * ap + bx * bp = px and ay * ap + by * bp = py
        total_cost += m.solve()
    print(total_cost)


def read_input(path: Path):
    with open(path) as f:
        return [Machine(s.split("\n")) for s in f.read().split("\n\n")]


if __name__ == "__main__":
    main()
