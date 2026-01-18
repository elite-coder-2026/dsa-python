# Topological Sort Documentation

## Overview
This module implements topological sorting using Kahn's Algorithm. Topological sorting is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge (u, v), vertex u comes before vertex v in the ordering.

**Note:** ⚠️ The filename and function name contain a typo - "typology" should be "topological".

---

## Function: `typological_sort(adj)`

Performs topological sorting on a directed acyclic graph using Kahn's Algorithm (BFS-based approach).

**Parameters:**
- `adj` (list of lists): Adjacency list representation of a directed graph where `adj[i]` contains all vertices that node `i` has edges pointing to. The graph is 0-indexed.

**Returns:**
- `list`: A list of vertices in topological order. If the graph has a cycle, the returned list will have fewer vertices than the input graph (cycle detection).

**Algorithm: Kahn's Algorithm**
1. **Calculate indegrees**: Count incoming edges for each vertex
2. **Initialize queue**: Add all vertices with indegree 0 (no dependencies) to a queue
3. **Process vertices**:
   - Remove a vertex from the queue and add it to the result
   - Decrease indegree of all its neighbors
   - If a neighbor's indegree becomes 0, add it to the queue
4. **Return result**: The order in which vertices were removed

**Time Complexity:** O(V + E)
- V = number of vertices
- E = number of edges
- Each vertex and edge is processed exactly once

**Space Complexity:** O(V)
- O(V) for the indegree array
- O(V) for the queue in worst case
- O(V) for the result array

**Cycle Detection:**
If the returned list has fewer elements than the number of vertices (`len(res) < n`), the graph contains a cycle and topological sorting is not possible.

**Use Cases:**
- Task scheduling with dependencies
- Build systems (compile order)
- Course prerequisite planning
- Resolving symbol dependencies in linkers

**Example:**
```python
from collections import deque

# Graph: 0 -> 1 -> 3
#        0 -> 2 -> 3
adj = [
    [1, 2],  # Node 0 points to 1 and 2
    [3],     # Node 1 points to 3
    [3],     # Node 2 points to 3
    []       # Node 3 has no outgoing edges
]

result = typological_sort(adj)
print(result)  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
# Both are valid topological orderings
```

**Cycle Detection Example:**
```python
# Graph with cycle: 0 -> 1 -> 2 -> 0
adj = [
    [1],  # Node 0 points to 1
    [2],  # Node 1 points to 2
    [0],  # Node 2 points to 0 (creates cycle)
]

result = typological_sort(adj)
print(result)  # Output: []
print(len(result) < len(adj))  # True - cycle detected
```

---

## Function: `add_edge(adj, u, v)`

Helper function to add a directed edge to the adjacency list representation of a graph.

**Parameters:**
- `adj` (list of lists): Adjacency list to modify
- `u` (int): Source vertex (starting point of the edge)
- `v` (int): Destination vertex (ending point of the edge)

**Returns:**
- None (modifies `adj` in-place)

**Effect:**
Adds vertex `v` to the adjacency list of vertex `u`, representing a directed edge from `u` to `v`.

**Example:**
```python
# Create adjacency list for 4 vertices
adj = [[] for _ in range(4)]

# Add edges: 0->1, 0->2, 1->3, 2->3
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 3)
add_edge(adj, 2, 3)

print(adj)
# Output: [[1, 2], [3], [3], []]

result = typological_sort(adj)
print(result)  # [0, 1, 2, 3] or [0, 2, 1, 3]
```

---

## Complete Usage Example

```python
from collections import deque

# Build a graph representing course prerequisites
# Courses: 0=Intro CS, 1=Data Structures, 2=Algorithms, 3=AI
num_courses = 4
adj = [[] for _ in range(num_courses)]

# Prerequisites:
# - Must take Intro CS (0) before Data Structures (1)
# - Must take Intro CS (0) before Algorithms (2)
# - Must take Data Structures (1) before AI (3)
# - Must take Algorithms (2) before AI (3)
add_edge(adj, 0, 1)  # 0 -> 1
add_edge(adj, 0, 2)  # 0 -> 2
add_edge(adj, 1, 3)  # 1 -> 3
add_edge(adj, 2, 3)  # 2 -> 3

# Get course order
course_order = typological_sort(adj)

if len(course_order) == num_courses:
    print("Valid course order:", course_order)
    # Possible outputs: [0, 1, 2, 3] or [0, 2, 1, 3]
else:
    print("Error: Circular dependency detected!")
```

---

## Algorithm Details: Kahn's Algorithm

**Why it works:**
- Vertices with indegree 0 have no dependencies, so they can be processed first
- After processing a vertex, we "remove" it by decreasing the indegree of its neighbors
- This may create new vertices with indegree 0, which can then be processed
- If all vertices are processed, we have a valid topological order
- If some vertices remain (stuck with indegree > 0), there's a cycle

**Advantages:**
- Easy to implement
- Natural cycle detection
- BFS-based (uses queue)
- Can be easily modified to return "levels" of independent tasks

**Disadvantages:**
- Requires O(V) extra space for indegree array
- Only works on DAGs (Directed Acyclic Graphs)

**Alternative Approach:**
- DFS-based topological sort: Uses recursion with a stack, also O(V + E)

---

## Implementation Notes

1. **0-indexed**: The implementation uses 0-based indexing for vertices
2. **Cycle Detection**: Check if `len(result) == len(adj)` to verify no cycles
3. **Multiple Valid Orders**: Topological sort is not unique; graphs may have multiple valid orderings
4. **DAG Requirement**: Only works on Directed Acyclic Graphs; will not produce correct results for cyclic graphs

---

## Known Issues

1. **Naming Typo**: Function is named `typological_sort` instead of `topological_sort`
2. **No Explicit Cycle Warning**: The function doesn't explicitly warn when a cycle is detected (returns partial result)
3. **No Input Validation**: Doesn't check for invalid inputs (empty graph, None values, etc.)

## Recommendations

1. Rename function to `topological_sort` for correctness
2. Add cycle detection with explicit error/warning:
   ```python
   if len(res) != n:
       raise ValueError("Graph contains a cycle - topological sort not possible")
   ```
3. Add input validation for edge cases
4. Add docstrings to functions
5. Consider returning both the ordering and a boolean indicating success
