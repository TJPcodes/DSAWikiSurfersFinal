from js import document
from pyodide import create_proxy
from bidirectional import bidirectional_search

def algo_search(event):
    start = document.getElementById("startInput").value.strip()
    goal = document.getElementById("targetInput").value.strip()

    if not start or not goal:
        document.getElementById("runTime").innerText = "Missing input"
        document.getElementById("success").innerText = "False"
        return

    import time
    start_time = time.time()
    path = bidirectional_search(start, goal)
    end_time = time.time()

    run_time = round(end_time - start_time, 2)
    success = bool(path)

    document.getElementById("runTime").innerText = f"{run_time}s"
    document.getElementById("success").innerText = str(success)
    document.getElementById("path").innerText = " → ".join(path) if path else "No path found"

# Set up the event listener
proxy = create_proxy(algo_search)
document.getElementById("submitBtn").addEventListener("click", proxy)
