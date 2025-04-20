from bidirectional import bidirectional_search

start = "Big_bang_theory"
goal = "Rice"

print(f"Searching for path from {start} to {goal}...\n")
path = bidirectional_search(start, goal)

if path:
    print("\n Path found in", len(path) - 1, "steps:\n")
    for step in path:
        print("→", step)
else:
    print("\n❌ No path found.")
