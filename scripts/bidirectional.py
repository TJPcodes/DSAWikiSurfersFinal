from collections import deque
from sparql import get_outgoing_links

async def bidirectional_search(start, goal):
    if start == goal:
        return [start]

    front_queue = deque([start])
    back_queue = deque([goal])
    front_visited = {start: None}
    back_visited = {goal: None}

    while front_queue and back_queue:
        # Expand forward
        meet_node = await expand(front_queue, front_visited, back_visited, direction="forward")
        if meet_node:
            return len(front_visited) + len(back_visited)

        # Expand backward
        meet_node = await expand(back_queue, back_visited, front_visited, direction="backward")
        if meet_node:
            return len(front_visited) + len(back_visited)

    return None

async def expand(queue, visited, other_visited, direction):
    if not queue:
        return None

    current = queue.popleft()
    print(f" {direction.capitalize()} exploring: {current}")
    neighbors = await get_outgoing_links(current)

    for neighbor in neighbors:
        if neighbor not in visited:
            visited[neighbor] = current
            queue.append(neighbor)
            if neighbor in other_visited:
                return neighbor
    return None
from collections import deque
from sparql import get_outgoing_links

async def bidirectional_search(start, goal):
    if start == goal:
        return [start]

    front_queue = deque([start])
    back_queue = deque([goal])
    front_visited = {start: None}
    back_visited = {goal: None}

    while front_queue and back_queue:
        # Expand forward
        meet_node = await expand(front_queue, front_visited, back_visited, direction="forward")
        if meet_node:
            print(f" Met in forward search at {meet_node}")
            return len(front_visited) + len(back_visited)

        # Expand backward
        meet_node = await expand(back_queue, back_visited, front_visited, direction="backward")
        if meet_node:
            print(f" Met in backward search at {meet_node}")
            return len(front_visited) + len(back_visited)

    return None

async def expand(queue, visited, other_visited, direction):
    if not queue:
        return None

    current = queue.popleft()
    print(f" {direction.capitalize()} exploring: {current}")
    neighbors = await get_outgoing_links(current)

    for neighbor in neighbors:
        if neighbor not in visited:
            visited[neighbor] = current
            queue.append(neighbor)
            if neighbor in other_visited:
                return neighbor
    return None

