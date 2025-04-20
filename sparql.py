import os
import json

# Path to the local cache directory (relative to index.html)
CACHE_DIR = "data/cache"

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

# Main function used by your algorithms
def get_outgoing_links(page_title):
    cached = load_from_cache(page_title)
    if cached is not None:
        return cached

    print(f" No cached data for: {page_title}")
    return []
