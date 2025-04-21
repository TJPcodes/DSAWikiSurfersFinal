from collections import deque
from sparql import get_outgoing_links

MAX_DEPTH = 12  # Optional: prevent endless traversals

async def bfs(start, goal):
    visited = set()
    queue = deque([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        print(f"🔎 Exploring: {current}")

        if current == goal:
            return len(visited)


        # Optional: track current depth
        depth = get_depth(current, parent)
        if depth > MAX_DEPTH:
            continue

        neighbors = await get_outgoing_links(current)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return 0  # No path found

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



