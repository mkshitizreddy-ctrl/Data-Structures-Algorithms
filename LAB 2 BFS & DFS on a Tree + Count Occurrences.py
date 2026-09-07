"""
Name: Kshitiz Reddy
Reg No: A26MTAI0008
Subject: Data Structure and Algorithms Lab
"""

# Simple tree using dictionary (adjacency list)
# Each node has a unique ID, but the "value" stored at each node
# can repeat -- that's what we search/count.

tree = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7],
    5: [],
    6: [],
    7: []
}

# value stored at each node (id -> value)
node_value = {
    1: 10,
    2: 20,
    3: 30,
    4: 20,   # repeated value
    5: 40,
    6: 20,   # repeated value
    7: 50
}


def bfs(start, target_value):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node_value[node] == target_value:
                print("Found value", target_value, "at node", node, "using BFS")
                return True
            queue.extend(tree[node])

    print("Value", target_value, "not found using BFS")
    return False


def dfs(start, target_value, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    if node_value[start] == target_value:
        print("Found value", target_value, "at node", start, "using DFS")
        return True

    for child in tree[start]:
        if child not in visited:
            if dfs(child, target_value, visited):
                return True

    return False


def count_occurrences(root, value):
    count = 0
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.append(node)

        if node_value[node] == value:
            count += 1

        stack.extend(tree[node])

    return count


# ---- Main ----
if __name__ == "__main__":
    bfs(1, 20)
    dfs(1, 20)

    val = 20
    print(f"Value {val} occurs {count_occurrences(1, val)} times in the tree")