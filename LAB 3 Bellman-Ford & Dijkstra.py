"""
Name: Kshitiz Reddy
Reg No: A26MTAI0008
Subject: Data Structure and Algorithms Lab
"""

import heapq

# Graph represented as edge list for Bellman-Ford
# and adjacency list for Dijkstra

edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5)
]

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

num_vertices = 4


def bellman_ford(source):
    dist = [float('inf')] * num_vertices
    dist[source] = 0

    # relax all edges (V-1) times
    for i in range(num_vertices - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # check for negative weight cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    print("Bellman-Ford distances from source", source)
    for i in range(num_vertices):
        print("Node", i, "->", dist[i])


def dijkstra(source):
    dist = [float('inf')] * num_vertices
    dist[source] = 0
    pq = [(0, source)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    print("Dijkstra distances from source", source)
    for i in range(num_vertices):
        print("Node", i, "->", dist[i])


# ---- Main ----
if __name__ == "__main__":
    bellman_ford(0)
    print()
    dijkstra(0)