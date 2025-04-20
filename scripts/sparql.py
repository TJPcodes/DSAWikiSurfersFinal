import os
import json

# Path to local cache directory
CACHE_DIR = "data/cache"

# Format the cache path safely
def cache_path(title):
    safe_title = title.replace("/", "_").replace(" ", "_")
    return f"{CACHE_DIR}/{safe_title}.json"

# Load from cache
def load_from_cache(title):
    try:
        with open(cache_path(title), "r") as f:
            links = json.load(f)
            print(f"🔗 {title} → {len(links)} links (from cache)")
            return links
    except Exception as e:
        print(f" Could not load cached links for {title}: {e}")
        return None

# Return list of outgoing links from cache or empty list
def get_outgoing_links(page_title):
    cached = load_from_cache(page_title)
    if cached is not None:
        return cached

    print(f" No cached data for: {page_title}")
    return []
