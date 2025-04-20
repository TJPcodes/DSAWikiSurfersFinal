from collections import deque
from sparql import get_outgoing_links

MAX_DEPTH = 12  # Optional: prevent endless traversals

def bfs(start, goal):
    visited = set()
    queue = deque([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        print(f"🔎 Exploring: {current}")

        if current == goal:
            return reconstruct_path(parent, start, goal)

        # Optional: track current depth
        depth = get_depth(current, parent)
        if depth > MAX_DEPTH:
            continue

        for neighbor in get_outgoing_links(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None  # No path found

def get_depth(node, parent):
    depth = 0
    visited = set()
    while node in parent and parent[node] is not None:
        if node in visited:  # catch loops
            return float("inf")
        visited.add(node)
        node = parent[node]
        depth += 1
    return depth

def reconstruct_path(parent, start, goal):
    path = [goal]
    visited = set()

    while True:
        current = path[-1]
        if current == start:
            break
        if current not in parent or parent[current] is None:
            print("⚠️  Path reconstruction failed — parent missing.")
            return None
        if current in visited:
            print("⚠️  Loop detected in parent map!")
            return None
        visited.add(current)
        path.append(parent[current])

    path.reverse()
    return path

