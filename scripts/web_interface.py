from js import document
from pyodide.ffi import create_proxy
from bfs import bfs
from bidirectional import bidirectional_search
import time
import asyncio

# Get and validate input values
def get_input_value(id):
    el = document.getElementById(id)
    print(f"🔍 Looking for element with ID: {id} → Found: {el is not None}")
    if el is None:
        print(f"❌ Element with ID '{id}' not found.")
        return ""
    if not hasattr(el, "value"):
        print(f"❌ Element with ID '{id}' exists but has no 'value' attribute.")
        return ""
    return el.value.strip()

# Set output text in UI
def update_output(id_name, text):
    el = document.getElementById(id_name)
    if el is None:
        print(f"❌ Output element with ID '{id_name}' not found.")
        return
    el.innerText = str(text)

# Run the algorithm and display results
def run_search(start, goal, algorithm_func):
    if not start or not goal:
        update_output("runTime", "Missing input")
        update_output("success", "Got lost in the tides..")
        update_output("num_pages", "0")
        return

    print(f"🌊 Running {algorithm_func.__name__} from '{start}' to '{goal}'")

    start_time = time.time()
    path = algorithm_func(start, goal)
    end_time = time.time()

    run_time = round(end_time - start_time, 2)
    success = "We surfed to our destination!" if path else "Got lost in the tides.."
    num_pages = str(len(path)) if path else "0"

    update_output("runTime", f"{run_time}s")
    update_output("success", success)
    update_output("num_pages", num_pages)

# Button bindings and loading animation
async def algo_bfs(event):
    video = document.getElementById("video-wrapper")
    animation = document.getElementById('animation')
    animation.play()
    video.classList.remove("hidden")
    await asyncio.sleep(0.5)

    video.classList.add("fade") # fade in loading scroll
    await asyncio.sleep(2)

    start = get_input_value("startInput")
    goal = get_input_value("targetInput")
    run_search(start, goal, bfs)

    video.classList.remove("fade") # fade in loading scroll
    await asyncio.sleep(2)
    animation.pause()

    video.classList.add("hidden")

async def algo_bidirectional(event):
    video = document.getElementById("video-wrapper")
    animation = document.getElementById('animation')
    animation.play()
    video.classList.remove("hidden")
    await asyncio.sleep(0.5)

    video.classList.add("fade") # fade in loading scroll
    await asyncio.sleep(3.5)

    start = get_input_value("startInput")
    goal = get_input_value("targetInput")
    run_search(start, goal, bidirectional_search)

    video.classList.remove("fade") # fade in loading scroll
    await asyncio.sleep(3.5)
    animation.pause()

    video.classList.add("hidden")


# Set up button event listeners
bfs_proxy = create_proxy(algo_bfs)
bidir_proxy = create_proxy(algo_bidirectional)

document.getElementById("bfsBtn").addEventListener("click", bfs_proxy)
document.getElementById("bidirectBtn").addEventListener("click", bidir_proxy)