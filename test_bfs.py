from bfs import bfs

start = "Star_Wars"
goal = "George_Lucas"

print(f"Searching for path from {start} to {goal}...\n")
path = bfs(start, goal)

if path:
    print(f"Path found in {len(path)-1} steps:\n")
    for step in path:
        print("→", step)
else:
    print("No path found.")
