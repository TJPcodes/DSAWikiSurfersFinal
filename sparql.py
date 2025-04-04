import os
import json
import time
from urllib.parse import quote
from SPARQLWrapper import SPARQLWrapper, JSON

CACHE_DIR = "data/cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def cache_path(title):
    safe_title = title.replace("/", "_")
    return os.path.join(CACHE_DIR, f"{safe_title}.json")

def save_to_cache(title, links):
    with open(cache_path(title), "w") as f:
        json.dump(links, f)
    print(f"💾 Cached: {title} ({len(links)} links)")

def load_from_cache(title):
    try:
        with open(cache_path(title), "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_outgoing_links(page_title):
    cached = load_from_cache(page_title)
    if cached is not None:
        return cached

    # Properly encode the title for URI use
    safe_title = quote(page_title, safe='')  # encode everything

    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    query = f"""
    SELECT ?linkedPage WHERE {{
        <http://dbpedia.org/resource/{safe_title}> <http://dbpedia.org/ontology/wikiPageWikiLink> ?linkedPage .
    }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    # Throttle to avoid rate-limiting
    time.sleep(0.5)

    try:
        results = sparql.query().convert()
        links = [r["linkedPage"]["value"].split("/")[-1] for r in results["results"]["bindings"]]
        save_to_cache(page_title, links)
        return links
    except Exception as e:
        print(f"⚠️  Error querying {page_title}: {e}")
        save_to_cache(page_title, [])  # cache failure so we skip it next time
        return []
