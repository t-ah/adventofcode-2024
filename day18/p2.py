"""
combine dijkstra and a simple binary search
"""
from pathlib import Path
import heapq
from collections import defaultdict


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines, file_name)


def solve(lines: list[str], file_name) -> None:
    end = 70 if "test" not in file_name else 6
    obstacles = [tuple([int(s) for s in line.split(",")]) for line in lines]
    lower = 0
    upper = len(obstacles)
    while True:
        center = lower + ((upper-lower) // 2)
        if end_reachable(center, obstacles, end):
            lower = center
        else:
            upper = center
        if lower + 1 == upper:
            print(f"{obstacles[lower][0]},{obstacles[lower][1]}")
            break


def end_reachable(up_to, obstacles, end):
    relevant_obs = set(obstacles[:up_to])
    graph = dict()
    for x in range(end + 1):
        for y in range(end + 1):
            if (x, y) not in relevant_obs:
                graph[x, y] = dict()
                for nxy in neighbours4(x, y):
                    if nxy not in relevant_obs and 0 <= nxy[0] <= end and 0 <= nxy[1] <= end:
                        graph[x, y][nxy] = 1
    _, distances = dijkstra(graph, (0, 0))
    return distances[(end, end)] < float("inf")


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
