import heapq
def basic_shortest_path(a, b, adj):
    n = len(adj)
    inf = 10**9

    dist = [[inf, inf] for _ in range(n)]
    pq = []

    dist[a][0] = 0
    heapq.heappush(pq, (0, a, 0))

    while pq:
        d, node, used = heapq.heappop(pq)

        if d != dist[node][used]:
            continue

        for nxt, w1, w2 in adj[node]:
            if dist[nxt][used] > d + w1:
                dist[nxt][used] = d + w1
                heapq.heappush(pq, (d + w1, nxt, used))

            if used is 0:
                if dist[nxt][1] > d + w2:
                    dist[nxt][1] = d + w2
                    heapq.heappush(pq, (dist[nxt][1], nxt, 1))

    ans = min(dist[b][0], dist[b][1])

    return -1 if ans >= inf else ans

def dijkstra(src, n, adj):
    dist = [10**9] * n
    pq = []
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        d, u = heapq.heappop(pq)

        # Explore all neighbors of u
        for v, straight, curved in adj[u]:

            # Relaxation step
            if dist[v] > d + straight:
                dist[v] = d + straight
                heapq.heappush(pq, (dist[v], v))

    return dist

def dijkstra_shortest_path(a, b, adj):
    n = len(adj)

    da = dijkstra(a, n, adj)
    db = dijkstra(b, n, adj)

    ans = da[b]

    for u in range(n):
        for v, straight, curved in adj[u]:
            ans = min(ans, da[u] + curved + db[v])
            ans = min(ans, db[u] + curved + da[u])

    if ans >= 10**9:
        return -1

    return ans