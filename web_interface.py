from js import document
from pyodide import create_proxy
from bfs import bfs
from bidirectional import bidirectional_search
import time

def run_search(start, target, algorithm_func):
    if not start or not target:
        document.getElementById("runTime").innerText = "Missing input"
        document.getElementById("success").innerText = "False"
        document.getElementById("path").innerText = ""
        return

    start_time = time.time()
    path = algorithm_func(start, target)
    end_time = time.time()

    run_time = round(end_time - start_time, 2)
    success = bool(path)

    document.getElementById("runTime").innerText = f"{run_time}s"
    document.getElementById("success").innerText = str(success)
    document.getElementById("path").innerText = " → ".join(path) if path else "No path found"

def algo_bidirectional(event):
    start = document.getElementById("startInput").value.strip()
    target = document.getElementById("targetInput").value.strip()
    run_search(start, target, bidirectional_search)

def algo_bfs(event):
    start = document.getElementById("startInput").value.strip()
    target = document.getElementById("targetInput").value.strip()
    run_search(start, target, bfs)

# Hook up both buttons
biDi = create_proxy(algo_bidirectional)
bfsProxy = create_proxy(algo_bfs)

document.getElementById("bidirectBtn").addEventListener("click", biDi)
document.getElementById("bfsBtn").addEventListener("click", bfsProxy)
