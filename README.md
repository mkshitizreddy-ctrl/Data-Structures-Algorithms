# Data Structures and Algorithms

This is my **Data Structures and Algorithms (DSA)** lab repository for the M.Tech Artificial Intelligence program at Bennett University.

The repo contains the Python implementations I’ve worked on for the DSA practicals, along with a short reference to the main concepts and complexities covered in each lab.

**Kshitiz Reddy** · A26MTAI0008  
M.Tech Artificial Intelligence · Bennett University

## Labs

| Lab | Topic | Main idea |
|---|---|---|
| Lab 1 | Stack and Queue using Arrays | LIFO, FIFO, array-based implementation |
| Lab 2 | BFS, DFS on a Tree + Count Occurrences | Tree traversal and searching |
| Lab 3 | Bellman-Ford & Dijkstra | Single-source shortest paths |
| Lab 4 | Kruskal's & Prim's Algorithm | Minimum spanning trees and greedy methods |

## Complexity reference

These are the standard bounds for the algorithms used in the labs. The exact cost depends on the implementation and data structure used here.

| Algorithm / Structure | Time complexity in this implementation |
|---|---|
| Stack push / pop / peek | O(1) |
| Queue enqueue / front | O(1) |
| Queue dequeue | O(n) because it uses `pop(0)` on a Python list |
| BFS | O(V²) in this implementation because it uses a list queue and linear visited checks |
| DFS | O(V²) in this implementation because visited checks use a list |
| Bellman-Ford | O(VE) |
| Dijkstra | O((V + E) log V) with `heapq` and an adjacency list |
| Kruskal | O(E log E) |
| Prim | O(E log V) with `heapq` and an adjacency list |

The BFS/DFS implementations are kept as submitted for the lab. The table above reflects their actual Python implementation rather than the ideal complexity of a version using `deque` or a set.

## Files

The labs are kept as separate Python files so that each practical can be opened, understood, and run independently.

```text
Data-Structures-Algorithms/
├── LAB 1 Stack and Queue using Arrays.py
├── LAB 2 BFS & DFS on a Tree + Count Occurrences.py
├── LAB 3 Bellman-Ford & Dijkstra.py
├── LAB 4 Kruskal's & Prim's Algorithm (MST).py
├── README.md
└── .gitignore
```

## What I’m practicing

- Implementing data structures and algorithms in Python
- Tree and graph traversal
- Shortest-path algorithms
- Minimum spanning trees
- Understanding and comparing algorithm complexity

## Author

**Kshitiz Reddy**  
M.Tech Artificial Intelligence  
Bennett University
