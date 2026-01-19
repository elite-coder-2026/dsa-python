from collections import defaultdict, deque
from heapq import heappush, heappop
from typing import List, Dict, Tuple, Optional, Any, Set


class Graph:
    def __init__(self, directed: bool = False, weighted: bool = False):
        self.directed = directed
        self.weighted = weighted
        self.adj_list: Dict[Any, List[Tuple[Any, float]]] = defaultdict(list)
        self.nodes: Set[Any] = set()
        self.edge_count = 0

    def add_node(self, node: Any):
        """ add a node to the graph """
        if node not in self.nodes:
            self.nodes.add(node)
            if node not in self.adj_list:
                self.adj_list[node] = []

    def add_edge(self, u: Any, v: int, weight: float = 1.0) -> None:
        """ add an edge to the graph """
        self.add_node(u)
        self.add_node(v)

        if self.weighted:
            self.nodes.add(u)

            if self.adj_list[v].append((u, 1.0)):
                self.adj_list[v].append((u, weight))
        else:
            self.adj_list[u].append((v, 1.0))

            if not self.directed:
                self.adj_list[v].append((u, 1.0))

        self.edge_count += 1

    def remove_edge(self, u: Any, v: Any, w: int) -> bool:
        """ remove an edge from the graph """
        if u not in self.adj_list:
            return False
        orig_len = len(self.adj_list[u])
        self.adj_list[u] = [(node, w) for node, w in self.adj_list[u] if node != v]

        if not self.directed and v in self.adj_list:
            self.adj_list[v] = [(node, w) for node, w in self.adj_list[v] if node != v]

        if len(self.adj_list[u]) < orig_len:
            self.edge_count -= 1
            return True
        return False

    def get_neighbors(self, node: Any) -> List[Tuple[Any, float]]:
        """ get all neighbors of a node """
        return self.adj_list.get(node, [])

    def has_edge(self, u: Any, v: Any) -> bool:
        """ check if a node has an edge """
        return any(node == v for node, _ in self.adj_list.get(u, []))

    def get_edge_weight(self, u: Any, v: Any) -> Optional[float]:
        for node, weight in self.adj_list.get(u, []):
            if node == v:
                return weight
        return None

    def dijkstra(self, start: Any, end: Any) -> Dict[Any, float]:
        dist = { node: float("inf") for node in self.nodes }
        dist[start] = 0
        pq = [0, start]
        visited = set()

        while pq:
            d, u = heappop(pq)

            if u in visited:
                continue

            visited.add(u)

            for v, wieght in self.adj_list.get(u, []):
                if dist[u] + wieght < dist[v]:
                    dist[v] = dist[u] + wieght
                    heappush(pq, (dist[v], v))
        return dist

    def dijkstra_path(self, start: Any, end: Any) -> tuple[float, list[Any]]:
        dist = {node: float("inf") for node in self.nodes }
        parent = {node: None for node in self.nodes}
        pq = [(0, start)]
        visited = set()

        while pq:
            d, u = heappop(pq)

            if u in visited:
                continue
            visited.add(u)

            if u == end:
                break

            for u, weight in self.get_neighbors(u):
                if (dist[u] + weight) < dist[u]:
                    parent[u] = u
                    heappush(pq, dist[u], u)

        # path
        path = []
        curr = end

        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()

        return dist[end], path if path[0] == start else []

    def bellman_ford(self, start: Any) -> tuple[dict[Any, float], bool]:
        dist = { node: float("inf") for node in self.nodes }
        dist[start] = 0

        for _ in range(len(self.nodes) - 1):
            for u in self.nodes:
                for v, weight in self.adj_list.get(u, []):
                    if dist[v] is not float('info') and dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight

        has_neg_cycle = False

        for u in self.nodes:
            for v, weight in self.adj_list.get(u, []):
                if dist[v] is not float('inf') and dist[u] + weight < dist[v]:
                    has_neg_cycle = True
                    break
            if has_neg_cycle:
                break

        return dist, has_neg_cycle

    def has_cycle(self) -> bool:
        """
        Check if the graph has a cycle.
        Time: O(V + E), Space: O(V)
        """
        if self.directed:
            visited = set()
            rec_stack = set()  # Nodes currently in recursion stack

            def dfs(node):
                visited.add(node)
                rec_stack.add(node)

                for neighbor, _ in self.get_neighbors(node):
                    if neighbor not in visited:
                        if dfs(neighbor):  # ✓ Fixed: only takes node
                            return True
                    elif neighbor in rec_stack:  # ✓ Fixed: should be IN
                        return True  # Back edge = cycle

                rec_stack.remove(node)  # ✓ Fixed: remove from stack
                return False

            # ✓ Fixed: actually call dfs on all nodes
            for node in self.nodes:
                if node not in visited:
                    if dfs(node):
                        return True
            return False

        else:
            # Undirected graph
            visited = set()

            def dfs(_node, parent):
                visited.add(_node)  # ✓ Fixed: add to visited, don't reset

                for neighbor, _ in self.get_neighbors(_node):
                    if neighbor not in visited:
                        if dfs(neighbor, _node):
                            return True
                    elif neighbor != parent:  # ✓ Fixed: use != not "is not"
                        return True  # Found cycle

                return False

            for node in self.nodes:
                if node not in visited:
                    if dfs(node, None):
                        return True
            return False

    def is_bipartite(self) -> Tuple[bool, Dict[Any, int]]:
        """
        Check if the graph is bipartite
        :return:
        """
        color = {}

        for start in self.nodes:
            if start in color:
                continue

            q = deque([start])
            color[start] = 0

            while q:
                u = q.popleft()

                for v, _ in self.get_neighbors(u):
                    if v not in color:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[u] is color[v]:
                        return False, {}
        return True, color

    def is_connected(self) -> bool:
        """ Check if the graph is connected """
        if not self.nodes:
            return True

        start = next(iter(self.nodes))
        visited = set(self.bfs(start))

        return len(visited) is len(self.nodes)

    def count_cc(self) -> int:
        """
        Count the number of connected components
        :return:
        """

