"""Assessment 3.4 - Graph for the last name PLARISAN
Vertices: unique letters P, L, A, R, I, S, N
Edges (undirected): letters next to each other in the name, and the last
letter N connects back to the first-used A:
    P-L, L-A, A-R, R-I, I-S, S-A, A-N
"""
from collections import deque


class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, start):
        """Breadth-First Search using a queue."""
        visited, order, queue = {start}, [], deque([start])
        while queue:
            v = queue.popleft()
            order.append(v)
            for n in self.adj[v]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return order

    def dfs(self, start):
        """Depth-First Search using a stack (recursion)."""
        visited, order = set(), []

        def visit(v):
            visited.add(v)
            order.append(v)
            for n in self.adj[v]:
                if n not in visited:
                    visit(n)

        visit(start)
        return order


if __name__ == "__main__":
    g = Graph()
    for u, v in [("P", "L"), ("L", "A"), ("A", "R"), ("R", "I"),
                 ("I", "S"), ("S", "A"), ("A", "N")]:
        g.add_edge(u, v)

    print("Adjacency list:")
    for k, v in g.adj.items():
        print(f"  {k}: {v}")
    print("BFS from P:", " ".join(g.bfs("P")))
    print("DFS from P:", " ".join(g.dfs("P")))