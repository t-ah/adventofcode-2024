"""
OK, we check all grid cells, if the path from one end to it plus from the start to it equals the shortest distance.
Then we realise that there is some problem because of the turning and apply some corrections.
"""
from pathlib import Path
from collections import defaultdict
import heapq


directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


def main():
    for file_name in ["p2-test.txt", "p2-test2.txt", "p2-input.txt"]:
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
    pred, from_start_dist = dijkstra(graph, (start[0], start[1], 0))
    start_to_end_dist = [from_start_dist[end[0], end[1], i] for i in range(4)]
    min_dist = min(start_to_end_dist)
    end_dijkstra = [
        dijkstra(graph, (end[0], end[1], i)) for i in range(4)
    ]  # get distances from all 4 ends to the start
    from_end_pred = [end_dijkstra[i][0] for i in range(4)]
    from_end_dist = [end_dijkstra[i][1] for i in range(4)]
    tiles = set()
    for x in range(lx):
        for y in range(ly):
            if grid[x, y] != ".":
                continue
            for i in range(4):
                for end_index in range(4):
                    #  if same pred: add 2000, elif preds have same x or y: sub 2000
                    modifier = 0
                    if (x, y, i) in from_end_pred[end_index]:
                        pred1 = from_end_pred[end_index][x, y, i]
                        if pred1[0] == x and pred1[1] == y:  # 1 turn
                            if pred1 in from_end_pred[end_index]:
                                pred2 = from_end_pred[end_index][pred1]
                                if pred2[0] == x and pred2[1] == y:  # 2 turns
                                    modifier = -2000
                        else:
                            modifier = 0
                    if (
                        from_start_dist[x, y, i]
                        + from_end_dist[end_index][x, y, i]
                        + modifier
                        == min_dist
                    ):
                        tiles.add((x, y))
                    # try also shortest path into opposite direction and check if directly entered (i.e. pred is different)
                    # otherwise, another "shortest" path might be preferred that doesn't require two additional turns to get into the same position
                    if (
                        from_start_dist[x, y, i]
                        + from_end_dist[end_index][x, y, (i + 2) % 4]
                        == min_dist
                    ):
                        pred1 = from_end_pred[end_index][x, y, i]
                        if pred1[0] != x or pred1[1] != y:
                            tiles.add((x, y))
    print(len(tiles))


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
