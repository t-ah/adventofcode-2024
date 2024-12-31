from pathlib import Path


class OpMachine:
    def __init__(self, a, b, c, program) -> None:
        self.r = [a, b, c]
        self.program = program
        self.ip = 0
        self.output = []

    def run(self):
        while True:
            if self.ip >= len(self.program):
                break
            op = self.program[self.ip + 1]
            match self.program[self.ip]:
                case 0:  # adv
                    self.r[0] = self.r[0] // pow(2, self.combo(op))
                case 1:  # bxl
                    self.r[1] = self.r[1] ^ op
                case 2:  # bst
                    self.r[1] = self.combo(op) % 8
                case 3:  # jnz
                    if self.r[0] != 0:
                        self.ip = op
                        continue
                case 4:  # bxc
                    self.r[1] = self.r[1] ^ self.r[2]
                case 5:  # out
                    self.out(self.combo(op) % 8)
                case 6:  # bdv
                    self.r[1] = self.r[0] // pow(2, self.combo(op))
                case 7:  # cdv
                    self.r[2] = self.r[0] // pow(2, self.combo(op))
            self.ip += 2

    def combo(self, op):
        match op:
            case op if op <= 3:
                return op
            case _:
                return self.r[op - 4]

    def out(self, v):
        self.output.append(int(v))


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    a = int(lines[0].split(" ")[2])
    b = int(lines[1].split(" ")[2])
    c = int(lines[2].split(" ")[2])
    program = [int(x) for x in lines[4].split(" ")[1].split(",")]
    m = OpMachine(a, b, c, program)
    m.run()
    print(",".join([str(n) for n in m.output]))


def read_input(path: Path) -> list[str]:
    with open(path) as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
