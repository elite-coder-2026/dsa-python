from collections import defaultdict

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def tarjan_util(self, u, low, disc, s, st):
        disc[u] = self.time
        low[u] = self.time
        s[u] = True
        st.append(u)

        for v in self.graph[u]:
            if disc[v] == -1:
                self.tarjan_util(v, low, disc, s, st)

                low[u] = min(low[u], low[v])
            elif s[v]:
                low[u] = min(low[u], disc[v])

        w = -1

        if low[u] == disc[u]:
            while w is not u:
                w = st.pop()
                print(w, end=" ")
                s[w] = False
            print()

    def tarjan(self):
        disc = [-1] * self.nodes
        low = [-1] * self.nodes
        s= [False] * self.nodes
        st = []

        for u in self.nodes:
            if disc[u] == -1:
                self.tarjan_util(u, low, disc, s, st)
