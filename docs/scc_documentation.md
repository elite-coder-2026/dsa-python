# Strongly Connected Components (SCC) Documentation

## Overview
The `Ggf` class implements an algorithm to find Strongly Connected Components in a directed graph. A strongly connected component is a maximal set of vertices where every vertex is reachable from every other vertex in the set.

---

## Class: `Ggf`

### Method: `dfs(self, curr, dist, adj, visited)`

Performs a depth-first search to determine if there's a path from a source node to a destination node.

**Parameters:**
- `curr` (int): Current node being visited in the DFS traversal
- `dist` (int): Destination node to reach
- `adj` (list): Adjacency list representation of the graph where `adj[i]` contains all neighbors of node `i`
- `visited` (list): Boolean list tracking which nodes have been visited, where `visited[i]` indicates if node `i` has been visited

**Returns:**
- `bool`: `True` if there exists a path from `curr` to `dist`, `False` otherwise

**Algorithm:**
1. If the current node equals the destination, return `True`
2. Mark the current node as visited
3. Recursively explore all unvisited neighbors
4. If any neighbor can reach the destination, return `True`
5. If no path is found, return `False`

**Time Complexity:** O(V + E) where V is the number of vertices and E is the number of edges

**Space Complexity:** O(V) for the visited array and recursion stack

---

### Method: `is_path(self, src, dest, adj)`

Checks whether a path exists from a source node to a destination node in the graph.

**Parameters:**
- `src` (int): Source node to start from
- `dest` (int): Destination node to reach
- `adj` (list): Adjacency list representation of the graph

**Returns:**
- `bool`: `True` if a path exists from `src` to `dest`, `False` otherwise

**Algorithm:**
1. Initialize a visited array with size `len(adj) + 1` filled with zeros
2. Call DFS starting from the source node

**Note:** ⚠️ There appears to be a bug in the implementation at line 16. The parameters passed to `dfs` are in the wrong order. It should be:
```python
return self.dfs(src, dest, adj, vis)
```
instead of:
```python
return self.dfs(src, vis, adj, vis)
```

---

### Method: `find_scc(self, n, a)`

Finds all strongly connected components in a directed graph using a brute-force approach.

**Parameters:**
- `n` (int): Number of vertices in the graph
- `a` (list): List of edges where `a[i] = [source, destination]` represents a directed edge from `source` to `destination`. The list is 1-indexed.

**Returns:**
- `list`: A list of strongly connected components, where each component is represented as a list of node IDs

**Algorithm:**
1. Initialize an empty result list and a tracking array `is_scc` to mark nodes already in a component
2. Build an adjacency list from the edge list
3. For each unprocessed node `i`:
   - Create a new component starting with node `i`
   - Check all other unprocessed nodes `k` to see if they belong to the same SCC
   - Two nodes belong to the same SCC if there's a path from `i` to `k` AND from `k` to `i`
   - Add qualifying nodes to the current component
4. Add the component to the result list

**Time Complexity:** O(n² × (V + E)) - Very inefficient for large graphs
- O(n²) for checking all pairs of nodes
- O(V + E) for each DFS call

**Space Complexity:** O(V + E) for the adjacency list and auxiliary arrays

**Note:** ⚠️ There's a bug at line 31. The condition:
```python
if not is_scc[k] and self.is_path(i, k, adj) and self.is_path(i, k, adj):
```
should be:
```python
if not is_scc[k] and self.is_path(i, k, adj) and self.is_path(k, i, adj):
```
The current implementation checks the path from `i` to `k` twice instead of checking bidirectional paths.

**Alternative Algorithms:**
This brute-force approach is inefficient. Consider using more efficient algorithms like:
- **Kosaraju's Algorithm:** O(V + E) time complexity using two DFS passes
- **Tarjan's Algorithm:** O(V + E) time complexity using a single DFS pass
- **Path-based strong component algorithm:** O(V + E) time complexity

---

## Usage Example

```python
# Create an instance of the class
scc_finder = Ggf()

# Define a graph with 5 nodes (1-indexed)
n = 5
edges = [
    None,  # Index 0 (unused for 1-indexed)
    [1, 2],
    [2, 3],
    [3, 1],
    [3, 4],
    [4, 5]
]

# Find all strongly connected components
components = scc_finder.find_scc(n, edges)
print(components)
# Expected output: [[1, 2, 3], [4], [5]]
# (assuming bugs are fixed)
```

---

## Known Issues

1. **Parameter Order Bug** in `is_path()` (line 16)
2. **Bidirectional Check Bug** in `find_scc()` (line 31)
3. **Inefficient Algorithm** - O(n² × (V + E)) complexity makes it unsuitable for large graphs

## Recommendations

1. Fix the identified bugs
2. Consider implementing Kosaraju's or Tarjan's algorithm for better performance
3. Add input validation for edge cases (empty graphs, invalid node IDs, etc.)
4. Add unit tests to verify correctness
5. Consider using 0-indexed arrays for consistency with Python conventions
