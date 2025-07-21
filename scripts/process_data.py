import os, json, csv

def extract_mentions(datadir, platform, keywords, out_csv):
    results = []
    for root, _, files in os.walk(datadir):
        for file in files:
            if not file.endswith('.json'): continue
            with open(os.path.join(root, file)) as f:
                try:
                    posts = json.load(f)
                except Exception:
                    continue
                for post in (posts if isinstance(posts, list) else [posts]):
                    text = json.dumps(post)
                    for kw in keywords:
                        if kw in text.lower():
                            results.append([platform, file, kw, text[:120]])
    with open(out_csv, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['platform', 'filename', 'keyword', 'excerpt'])
        writer.writerows(results)

# Example usage
KEYWORDS = ["safety", "party", "solo", "group", "eco", "adventure", "wifi", "event", "deal", "local", "review", "instagrammable"]
extract_mentions("data/instagram/winter", "instagram", KEYWORDS, "output/mentions_instagram_winter.csv")
extract_mentions("data/tiktok/winter", "tiktok", KEYWORDS, "output/mentions_tiktok_winter.csv")
