from sparql import get_outgoing_links

start = "Albert_Einstein"
links = get_outgoing_links(start)

print(f"{start} links to {len(links)} pages.")
print("First 10 links:")
for link in links[:10]:
    print("→", link)
