from find_links import find_links
import ray

@ray.remote
def find_links_task(start_url, base_url, depth=2):
    return find_links(start_url, base_url, depth)

print(f"begin web-scraper...")

base = "https://docs.ray.io/en/latest/"
docs = base + "index.html"
depth = 2

# run six crawlers in parallel, the first three (redundantly) crawl docs.ray.io again, 
# the other three crawl the main entry points of the Ray RLlib, Tune, and Serve libraries, respectively
links = [find_links_task.remote(f"{base}{lib}/index.html", base)
         for lib in ["", "", "", "rllib", "tune", "serve"]]

print(f"web-scraper parallely run on 6 links")

for res in ray.get(links): print(f"{len(res)}")