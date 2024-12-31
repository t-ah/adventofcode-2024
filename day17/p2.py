from pathlib import Path


class OpMachine:
    def __init__(self, program) -> None:
        self.program = program

    def run(self, a):
        self.r = [a, 0, 0]
        self.ip = 0
        self.output = []
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
                    # self.out(self.combo(op) % 8)
                    self.output.append(self.combo(op) % 8)
                    # if self.program[self.output] != self.combo(op) % 8:
                    #     return False
                    # self.output += 1
                case 6:  # bdv
                    self.r[1] = self.r[0] // pow(2, self.combo(op))
                case 7:  # cdv
                    self.r[2] = self.r[0] // pow(2, self.combo(op))
            self.ip += 2
        return self.output

    def combo(self, op):
        match op:
            case op if op <= 3:
                return op
            case _:
                return self.r[op - 4]


def main():
    for file_name in ["p2-tesst.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    """ok we can somehow incrementally determine the number"""
    program = [int(x) for x in lines[4].split(" ")[1].split(",")]
    m = OpMachine(program)
    a = find(m, 0, program, 0)
    print(a, m.run(a))


def find(m, i, program, status):
    """
    find the right addition to the current status to generate the item at i-th pos from the back of the program
    the first number found may not be the right one, so we need some backtracking (multiple additions can yield the same list item)
    """
    if i == len(program):
        return status
    status *= 8
    for offset in range(8):
        check = status + offset
        if m.run(check) == program[-(i+1):]:
            next = find(m, i + 1, program, check)
            if next:
                return next
    return False


def read_input(path: Path) -> list[str]:
    with open(path) as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
