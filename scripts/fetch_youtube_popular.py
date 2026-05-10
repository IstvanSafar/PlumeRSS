import os, json, requests

API_KEY = os.environ["YOUTUBE_API_KEY"]
BASE = "https://www.googleapis.com/youtube/v3"

CATEGORIES = [
    {"id": "HU_news",     "label": "🇭🇺 Magyar hírek",   "query": "hírek",           "lang": "hu", "region": "HU"},
    {"id": "HU_tech",     "label": "🇭🇺 Magyar tech",     "query": "tech magyarázó",  "lang": "hu", "region": "HU"},
    {"id": "HU_misc",     "label": "🇭🇺 Magyar egyéb",    "query": "podcast magyarázó","lang": "hu", "region": "HU"},
    {"id": "EN_news",     "label": "📰 News",              "query": "news channel",    "lang": "en", "region": "US"},
    {"id": "EN_tech",     "label": "💻 Tech",              "query": "technology",      "lang": "en", "region": "US"},
    {"id": "EN_science",  "label": "🔬 Science",           "query": "science education","lang": "en", "region": "US"},
    {"id": "EN_gaming",   "label": "🎮 Gaming",            "query": "gaming",          "lang": "en", "region": "US"},
    {"id": "EN_finance",  "label": "💼 Finance",           "query": "finance investing","lang": "en", "region": "US"},
]

def fetch_channels(query, lang, region, max_results=12):
    # Search for channels
    r = requests.get(f"{BASE}/search", params={
        "part": "snippet",
        "type": "channel",
        "q": query,
        "relevanceLanguage": lang,
        "regionCode": region,
        "maxResults": max_results,
        "order": "relevance",
        "key": API_KEY,
    })
    r.raise_for_status()
    items = r.json().get("items", [])
    if not items:
        return []

    channel_ids = [i["snippet"]["channelId"] for i in items]

    # Get subscriber counts
    r2 = requests.get(f"{BASE}/channels", params={
        "part": "snippet,statistics",
        "id": ",".join(channel_ids),
        "key": API_KEY,
    })
    r2.raise_for_status()
    details = {c["id"]: c for c in r2.json().get("items", [])}

    results = []
    for cid in channel_ids:
        c = details.get(cid)
        if not c:
            continue
        subs = int(c["statistics"].get("subscriberCount", 0))
        results.append({
            "id": cid,
            "title": c["snippet"]["title"],
            "description": c["snippet"].get("description", "")[:120],
            "thumbnail": c["snippet"]["thumbnails"].get("default", {}).get("url", ""),
            "subscribers": subs,
            "feedUrl": f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}",
        })

    results.sort(key=lambda x: x["subscribers"], reverse=True)
    return results


output = {"updated": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "categories": []}

for cat in CATEGORIES:
    print(f"Fetching: {cat['label']} ...")
    channels = fetch_channels(cat["query"], cat["lang"], cat["region"])
    output["categories"].append({
        "id": cat["id"],
        "label": cat["label"],
        "channels": channels,
    })

out_path = os.path.join(os.path.dirname(__file__), "..", "youtube_popular.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Done. {sum(len(c['channels']) for c in output['categories'])} channels written.")
