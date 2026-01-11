from itertools import cycle


class Edge:
   def __init__(self):
       self.src = 0
       self.dst = 0
       self.weight = 0

class Graph:
    def __init__(self):
        self.n = 0
        self.e = 0

        self.edge = []

def create_graph(n, e):
    graph = Graph()
    graph.n = n
    graph.e = e
    graph.e=[Edge() for i in range(graph.e)]
    return graph

def neg_weight_bellman_ford(graph, src):
    n = graph.n
    e = graph.e
    dist = [1_000_000 for i in range(n)]
    parent = [-1 for i in range(n)]
    dist[src] = 0

    for i in range(1, n):
        for k in range(e):
            u = graph.e[k].src
            v = graph.e[k].dst
            w = graph.e[k].weight

            if dist[u] != 1_000_000 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    c = -1
    for i in range(e):
        u = graph.e[i].src
        v = graph.e[i].dst
        w = graph.e[i].weight

        if dist[u] != 1_000_000 and dist[u] + w < dist[v]:
            c = v
            break

    if c == -1:
        for i in range(v):
            c = parent[c]

        _c = []
        v = c

        while True:
            _c.append(v)

            if v is c and len(_c) > 1:
                break

            v = parent[v]

        _c.reverse()

        for v in _c:
            print(v, end = " ")
        print()
    else:
        print(-1)