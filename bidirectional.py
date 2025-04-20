from collections import deque
from sparql import get_outgoing_links

def bidirectional_search(start, goal):
    if start == goal:
        return [start]

    # Initialize frontiers and visited sets
    front_queue = deque([start])
    back_queue = deque([goal])
    front_visited = {start: None}
    back_visited = {goal: None}

    while front_queue and back_queue:
        # Expand front
        meet_node = expand(front_queue, front_visited, back_visited, direction="forward")
        if meet_node:
            return construct_path(front_visited, back_visited, meet_node)

        # Expand back
        meet_node = expand(back_queue, back_visited, front_visited, direction="backward")
        if meet_node:
            return construct_path(front_visited, back_visited, meet_node)

    return None

def expand(queue, visited, other_visited, direction):
    current = queue.popleft()
    print(f"🌊 {direction.capitalize()} exploring: {current}")
    neighbors = get_outgoing_links(current)

    for neighbor in neighbors:
        if neighbor not in visited:
            visited[neighbor] = current
            queue.append(neighbor)
            if neighbor in other_visited:
                return neighbor
    return None

def construct_path(front_visited, back_visited, meet_node):
    # Reconstruct forward path
    path_front = []
    node = meet_node
    while node:
        path_front.append(node)
        node = front_visited[node]
    path_front.reverse()

    # Reconstruct backward path
    path_back = []
    node = back_visited[meet_node]
    while node:
        path_back.append(node)
        node = back_visited[node]

    return path_front + path_back
