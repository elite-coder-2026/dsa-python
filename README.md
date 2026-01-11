# DSA Python

A comprehensive collection of Data Structures and Algorithms implemented in Python.

## Overview

This repository contains Python implementations of fundamental data structures and algorithms, organized by category for easy navigation and reference.

## Structure

### Arrays
- **is_palindrome.py** - Check if an array/string is a palindrome
- **rev_arr.py** - Array reversal implementation
- **sum_of_digits.py** - Calculate sum of digits

### Search Algorithms
- **binary_search.py** - Standard binary search implementation
- **unbounded_binary_search.py** - Binary search for unbounded/infinite arrays

### Sorting Algorithms
- **sort_algorithms.py** - Collection of sorting algorithm implementations
- **built-in-sort.py** - Python built-in sort examples

### Graph Algorithms
- **bfs.py** - Breadth-First Search
- **tarjan.py** - Tarjan's algorithm for strongly connected components
- **typology_sort.py** - Topological sorting
- **print_level.py** - Level-order graph traversal
- **scc.py** - Strongly Connected Components
- **bellman_ford/** - Bellman-Ford algorithm for shortest paths with negative weights
  - print_neg_weight_directed_graph.py
- **dijkstra/** - Dijkstra's shortest path algorithm
  - shortest_path.py

### Tree Data Structures
- **red_black_tree.py** - Self-balancing Red-Black Tree implementation
- **tst.py** - Ternary Search Tree

### Sparse Tables
- **build_sparse_table.py** - Construct sparse table for range queries
- **range_min_query.py** - Range minimum query using sparse tables

### Math
- **is_prime.py** - Primality testing

## Usage

Each file contains standalone implementations that can be run or imported independently. Navigate to the specific algorithm or data structure you need and refer to the code comments for usage examples.

```python
# Example: Using binary search
from binary_search import binary_search

arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)
```

## Requirements

- Python 3.x

## Contributing

Feel free to contribute additional algorithms or improvements to existing implementations.

## License

This project is open source and available for educational purposes.
