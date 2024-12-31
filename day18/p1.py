from pathlib import Path
import heapq
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines, file_name)


def solve(lines: list[str], file_name) -> None:
    end_pos = 70 if "test" not in file_name else 6
    rel_len = 1024 if "test" not in file_name else 12

    start = (0, 0)
    end = (end_pos, end_pos)
    obstacles = [tuple([int(s) for s in line.split(",")]) for line in lines]

    relevant_obs = set(obstacles[:rel_len])
    graph = dict()
    for x in range(end_pos + 1):
        for y in range(end_pos + 1):
            if (x, y) not in relevant_obs:
                graph[x, y] = dict()
                for nxy in neighbours4(x, y):
                    if nxy not in relevant_obs and 0 <= nxy[0] <= end_pos and 0 <= nxy[1] <= end_pos:
                        graph[x, y][nxy] = 1
    _, distances = dijkstra(graph, start)
    print(distances[end])


def dijkstra(graph, start):
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    unvisited = []
    predecessors = {}
    heapq.heappush(unvisited, (0, start))
    while unvisited:
        shortest_distance, node = heapq.heappop(unvisited)
        for neighbour in graph[node]:
            if graph[node][neighbour] != 0 and distances[neighbour] > shortest_distance + graph[node][neighbour]:
                new_distance = shortest_distance + graph[node][neighbour]
                distances[neighbour] = new_distance
                predecessors[neighbour] = node
                heapq.heappush(unvisited, (new_distance, neighbour))
    return predecessors, distances


def neighbours4(x, y):
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def read_input(path: Path) -> list[str]:
    with open(path) as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
