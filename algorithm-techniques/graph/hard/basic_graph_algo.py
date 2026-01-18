from collections import deque

def bfs(graph: dict, start:int) -> list:
    visited = set()
    q = deque([start])
    result = []


    while q:
        node = q.popleft()

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)
    return result

def dfs(graph: dict, start: int, visited: set = None) -> list:
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result
