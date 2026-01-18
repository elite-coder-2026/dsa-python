from typing import List, Dict, Tuple, Optional, Any, Callable, Set
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys

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
        pass