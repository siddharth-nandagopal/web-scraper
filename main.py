from find_links import find_links

print(f"begin web-scraper...")

base = "https://docs.ray.io/en/latest/"
docs = base + "index.html"
depth = 2

links = find_links(docs, base, depth)
print(f"number of links scraped from base {docs} till depth {depth}: {len(links)}")