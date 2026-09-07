"""
Name: Kshitiz Reddy
Reg No: A26MTAI0008
Subject: Data Structure and Algorithms Lab
"""

import heapq

# Graph as edge list for Kruskal, adjacency list for Prim
edges = [
    (0, 1, 4),
    (0, 2, 4),
    (1, 2, 2),
    (1, 0, 4),
    (2, 3, 3),
    (2, 5, 2),
    (2, 4, 4),
    (3, 4, 3),
    (5, 4, 3)
]

graph = {
    0: [(1, 4), (2, 4)],
    1: [(0, 4), (2, 2)],
    2: [(0, 4), (1, 2), (3, 3), (4, 4), (5, 2)],
    3: [(2, 3), (4, 3)],
    4: [(2, 4), (3, 3), (5, 3)],
    5: [(2, 2), (4, 3)]
}

num_vertices = 6


# ---- Kruskal's Algorithm ----

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot == yroot:
        return

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal():
    result = []
    sorted_edges = sorted(edges, key=lambda x: x[2])

    parent = [i for i in range(num_vertices)]
    rank = [0] * num_vertices

    for u, v, w in sorted_edges:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            result.append((u, v, w))
            union(parent, rank, x, y)

    print("Kruskal's MST:")
    total = 0
    for u, v, w in result:
        print(u, "-", v, ":", w)
        total += w
    print("Total weight:", total)


# ---- Prim's Algorithm ----

def prim(start=0):
    visited = [False] * num_vertices
    min_heap = [(0, start, -1)]  # (weight, node, parent)
    result = []
    total = 0

    while min_heap:
        w, u, parent = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total += w
        if parent != -1:
            result.append((parent, u, w))

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v, u))

    print("Prim's MST:")
    for u, v, w in result:
        print(u, "-", v, ":", w)
    print("Total weight:", total)


# ---- Main ----
if __name__ == "__main__":
    kruskal()
    print()
    prim()