from pathlib import Path
from collections import defaultdict
import heapq


directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]) -> None:
    lx, ly, grid, start, end = build_grid(lines, lambda: "#")
    graph = dict()
    for x in range(lx):
        for y in range(ly):
            if grid[x, y] == ".":
                for i in range(4):
                    graph[x, y, i] = {
                        (x, y, (i + 1) % 4): 1000,
                        (x, y, (i + 3) % 4): 1000,
                    }
                    nx, ny = moved((x, y), i)
                    if grid[nx, ny] == ".":
                        graph[x, y, i][nx, ny, i] = 1
    pred, dist = dijkstra(graph, (start[0], start[1], 0))
    end_dist = [dist[end[0], end[1], i] for i in range(4)]
    print(end_dist)
    print(min(end_dist))


def moved(pos, dir_index):
    offset = directions[dir_index]
    return pos[0] + offset[0], pos[1] + offset[1]


def build_grid(lines: list[str], default_arg):
    grid = defaultdict(default_arg)
    ly, lx = len(lines), len(lines[0])
    start, end = (0, 0), (0, 0)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                case "S":
                    start = (x, y)
                    grid[x, y] = "."
                case "E":
                    end = (x, y)
                    grid[x, y] = "."
                case _:
                    grid[x, y] = c
    return lx, ly, grid, start, end


def neighbours4(x, y):
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def dijkstra(graph, start):
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    unvisited = []
    predecessors = {}
    heapq.heappush(unvisited, (0, start))
    while unvisited:
        shortest_distance, node = heapq.heappop(unvisited)
        for neighbour in graph[node]:
            if (
                graph[node][neighbour] != 0
                and distances[neighbour] > shortest_distance + graph[node][neighbour]
            ):
                new_distance = shortest_distance + graph[node][neighbour]
                distances[neighbour] = new_distance
                predecessors[neighbour] = node
                heapq.heappush(unvisited, (new_distance, neighbour))
    return predecessors, distances


def read_input(path: Path) -> list[str]:
    with open(path) as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
