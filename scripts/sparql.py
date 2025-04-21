import json
from pyodide.http import pyfetch  # Pyodide browser fetch

# Hosted GitHub Pages dataset
BASE_URL = "https://tjpcodes.github.io/wiki-surfers-data/data/cache/"

# Asynchronously fetch outgoing links for a page
async def get_outgoing_links(page_title):
    try:
        url = f"{BASE_URL}{page_title}.json"
        resp = await pyfetch(url)
        text = await resp.string()
        links = json.loads(text)
        print(f" {page_title} → {len(links)} links (fetched)")
        return links
    except Exception as e:
        print(f" Failed to fetch {page_title}: {e}")
        return []

# Build a safe filename for each cached page
def cache_path(title):
    safe_title = title.replace("/", "_").replace(" ", "_")
    return f"{CACHE_DIR}/{safe_title}.json"

# Load links from cache if available
def load_from_cache(title):
    try:
        with open(cache_path(title), "r") as f:
            links = json.load(f)
            print(f" {title} → {len(links)} links (from cache)")
            return links
    except Exception as e:
        print(f" Could not load cached links for {title}: {e}")
        return None

