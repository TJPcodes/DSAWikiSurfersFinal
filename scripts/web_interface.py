from js import document
from pyodide.ffi import create_proxy
from bidirectional import bidirectional_search
from bfs import bfs
import time

def update_output(id_name, text):
    document.getElementById(id_name).innerText = str(text)

def run_search(start, goal, algorithm_func):
    if not start or not goal:
        update_output("runTime", "Missing input")
        update_output("success", "False")
        update_output("numPages", "")
        return

    start_time = time.time()
    numPages = algorithm_func(start, goal)
    end_time = time.time()

    run_time = round(end_time - start_time, 2)
    if bool(numPages):
        success = "We surfed to our destination!"
    else:
        success = "Got lost in the tides.."

    update_output("runTime", f"{run_time}s")
    update_output("success", success)
    update_output("numPages", " → ".join(numPages) if numPages else "No path found")

def get_input_value(id):
    el = document.getElementById(id)
    if el is None:
        print(f"Element with id '{id}' not found.")
        return ""
    return el.value.strip()

def algo_bfs(event):
    start = get_input_value("startInput")
    goal = get_input_value("targetInput")
    run_search(start, goal, bfs)

def algo_bidirectional(event):
    start = get_input_value("startInput")
    goal = get_input_value("targetInput")
    run_search(start, goal, bidirectional_search)

bfs_proxy = create_proxy(algo_bfs)
bidir_proxy = create_proxy(algo_bidirectional)

document.getElementById("video-wrapper").classList.toggle("fade") # fade in loading scroll
document.getElementById("bfsBtn").addEventListener("click", bfs_proxy)
document.getElementById("bidirectBtn").addEventListener("click", bidir_proxy)
document.getElementById("video-wrapper").classList.toggle("fade") # fade out loading scroll