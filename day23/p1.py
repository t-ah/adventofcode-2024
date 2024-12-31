from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            solve(format_input(read_input(path)), file_name)


def read_input(path: Path) -> str:
    with open(path) as f:
        return f.read()


def format_input(s: str):
    return s.split("\n")


def solve(data, _) -> None:
    graph = build_graph(data)
    triples = find_triples(graph)
    relevant_triples = [triple for triple in triples if one_starts_with_t(triple)]
    print(len(relevant_triples))


def find_triples(graph):
    triples = set()
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            for second_neighbour in graph[neighbour]:
                if second_neighbour in graph[node]:
                    triples.add(tuple(sorted([node, neighbour, second_neighbour])))
    return triples


def one_starts_with_t(nodes):
    return "t" in [node[0] for node in nodes]


def build_graph(data):
    graph = defaultdict(lambda: set())
    for link in data:
        left, right = link.split("-")
        graph[left].add(right)
        graph[right].add(left)
    return graph


if __name__ == "__main__":
    main()
