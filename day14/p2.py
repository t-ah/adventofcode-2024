from pathlib import Path
from collections import defaultdict
from PIL import Image


class Robot:
    def __init__(self, line) -> None:
        p, v = [s.split(",") for s in line.split(" ")]
        self.pos = [int(p[0][2:]), int(p[1])]
        self.v = (int(v[0][2:]), int(v[1]))

    def step(self, w, h):
        self.pos = ((self.pos[0] + self.v[0]) % w, (self.pos[1] + self.v[1]) % h)
        return self.pos


def main():
    for file_name in ["p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    robots = [Robot(line) for line in lines]
    w, h = 101, 103
    step = 0
    while True:
        step += 1
        print(step)
        positions = [robot.step(w, h) for robot in robots]
        img = Image.new('RGB', (w, h), color = 'black')
        pixels = img.load()
        for p in positions:
            pixels[p] = (255, 255, 255)
        img.save(f'img/{step}.png')



def print_grid(pos, w, h):
    grid = defaultdict(lambda: ".")
    for p in pos:
        grid[p] = "#"
    lines = []
    for y in range(h):
        line = "".join([grid[x, y] for x in range(w)])
        lines.append(line)
    print("\n".join(lines))


def read_input(path: Path) -> list[str]:
    with open(path) as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
