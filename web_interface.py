from js import document
from pyodide import create_proxy
from bidirectional import bidirectional_search
from bfs import bfs
import time

def update_output(id_name, text):
    document.getElementById(id_name).innerText = str(text)

def run_search(start, goal, algorithm_func):
    if not start or not goal:
        update_output("runTime", "Missing input")
        update_output("success", "False")
        update_output("path", "")
        return

    start_time = time.time()
    path = algorithm_func(start, goal)
    end_time = time.time()

    run_time = round(end_time - start_time, 2)
    success = bool(path)

    update_output("runTime", f"{run_time}s")
    update_output("success", success)
    update_output("path", " → ".join(path) if path else "No path found")

def algo_bfs(event):
    start = document.getElementById("startInput").value.strip()
    goal = document.getElementById("targetInput").value.strip()
    run_search(start, goal, bfs)

def algo_bidirectional(event):
    start = document.getElementById("startInput").value.strip()
    goal = document.getElementById("targetInput").value.strip()
    run_search(start, goal, bidirectional_search)

bfs_proxy = create_proxy(algo_bfs)
bidir_proxy = create_proxy(algo_bidirectional)

document.getElementById("bfsBtn").addEventListener("click", bfs_proxy)
document.getElementById("bidirectBtn").addEventListener("click", bidir_proxy)
