import csv
from collections import defaultdict
import heapq
from typing import List, Tuple, Optional, Set

def read_matrix(filename: str) -> List[List[int]]:
    matrix = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                matrix.append(list(map(int, row)))
    return matrix

def print_initial_graph(matrix: List[List[int]]) -> None:
    print("Початковий граф (ребра з вагами):")
    N = len(matrix)
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] != 0:
                print(f"{i} — {j} (довжина: {matrix[i][j]})")

def draw_graph_as_tree_dfs(matrix: List[List[int]], node: int,
                           visited: Optional[Set[int]] = None, prefix: str = "") -> None:
    if visited is None:
        visited = set()
    visited.add(node)
    print(prefix + str(node))
    neighbors = [i for i, w in enumerate(matrix[node]) if w != 0 and i not in visited]
    for i, neighbor in enumerate(neighbors):
        if i == len(neighbors) - 1:
            connector = "└── "
            new_prefix = prefix + "    "
        else:
            connector = "├── "
            new_prefix = prefix + "│   "
        print(prefix + connector, end="")
        draw_graph_as_tree_dfs(matrix, neighbor, visited, new_prefix)

def build_tree(parent: List[int]) -> defaultdict:
    tree = defaultdict(list)
    for child, p in enumerate(parent):
        if p != -1:
            tree[p].append(child)
    return tree

def draw_binary_tree(node: int, tree: defaultdict, prefix: str = "", is_left: bool = True,
                     visited: Optional[Set[int]] = None) -> None:
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)

    children = tree.get(node, [])

    if len(children) > 1:
        draw_binary_tree(children[1], tree, prefix + ("    " if is_left else "│   "), False, visited)

    print(prefix + ("└── " if is_left else "┌── ") + str(node))

    if len(children) > 0:
        draw_binary_tree(children[0], tree, prefix + ("    " if is_left else "│   "), True, visited)

def is_connected(matrix: List[List[int]]) -> bool:
    N = len(matrix)
    visited = set()
    def dfs(v: int):
        visited.add(v)
        for u, w in enumerate(matrix[v]):
            if w != 0 and u not in visited:
                dfs(u)
    dfs(0)
    return len(visited) == N

def prim_mst(graph: List[List[int]]) -> Tuple[List[int], int]:
    N = len(graph)
    used = [False] * N
    min_edge = [float('inf')] * N
    parent = [-1] * N
    min_edge[0] = 0
    heap = [(0, 0)]
    total_weight = 0

    while heap:
        weight, v = heapq.heappop(heap)
        if used[v]:
            continue
        used[v] = True
        total_weight += weight

        for to in range(N):
            w = graph[v][to]
            if w != 0 and not used[to] and w < min_edge[to]:
                min_edge[to] = w
                parent[to] = v
                heapq.heappush(heap, (w, to))

    if not all(used):
        raise ValueError("Граф не є зв’язним, MST не існує.")

    print("\nРебра мінімального остовного дерева (MST):")
    for i in range(1, N):
        if parent[i] != -1:
            print(f"{parent[i]} — {i} (довжина: {graph[parent[i]][i]})")

    return parent, total_weight

def main():
    filename = "c:/IT/lab8.2semestr/island.csv"
    matrix = read_matrix(filename)

    print_initial_graph(matrix)

    print("\nПочатковий граф у вигляді дерева")
    draw_graph_as_tree_dfs(matrix, 0)

    parent, total_weight = prim_mst(matrix)
    mst_tree = build_tree(parent)

    print("\nMST у вигляді дерева:")
    draw_binary_tree(0, mst_tree)

    print(f"\nЗагальна мінімальна довжина кабелів: {total_weight}")

if __name__ == "__main__":
    main()

