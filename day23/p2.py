from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
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
    nodes = list(graph.keys())
    print(",".join(sorted(list(expand_group(set(), nodes, 0, graph)))))


def expand_group(current_nodes: set, all_nodes, index, graph) -> set:
    if index >= len(all_nodes):
        return current_nodes
    # if next node compatible, determine best of with and without it, else continue without next node
    compatible = True
    next_node = all_nodes[index]
    next_node_nb = graph[next_node]
    for node in current_nodes:
        if node not in next_node_nb:
            compatible = False
            break
    if compatible:
        g1 = expand_group(current_nodes | {next_node}, all_nodes, index + 1, graph)
        g2 = expand_group(current_nodes, all_nodes, index + 1, graph)
        if len(g1) > len(g2):
            return g1
        return g2
    return expand_group(current_nodes, all_nodes, index + 1, graph)


def build_graph(data):
    graph = defaultdict(lambda: set())
    for link in data:
        left, right = link.split("-")
        graph[left].add(right)
        graph[right].add(left)
    return graph


if __name__ == "__main__":
    main()
