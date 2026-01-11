class Ggf:
    def dfs(self, curr, dist, adj, visited):
        if curr is dist:
            return True
        visited[curr] = 1

        for x in adj[curr]:
            if  not visited[x]:
                if self.dfs(x, dist, adj, visited):
                    return True

        return False

    def is_path(self, src, dest, adj):
        vis = [0] * (len(adj) + 1)
        return self.dfs(src, vis, adj, vis)

    def find_scc(self, n, a):
        ans = []
        is_scc = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]

        for i in range(1, n + 1):
            adj[a[i][0]].append(a[i][1])

        for i in range(1, n + 1):
            if not is_scc[i]:
                scc = [i]

                for k in range(1, n + 1):
                    if not is_scc[k] and self.is_path(i, k, adj) and self.is_path(i, k, adj):
                        is_scc[k] = 1
                        scc.append(k)
                ans.append(scc)
        return ans
