import urllib, json, codecs, urlparse

try:
    fp = codecs.open("fetched_data.json", encoding="utf8")
    fetched_data = json.load(fp)
    fp.close()
except:
    fetched_data = {}

def fetch(url):
    print "Fetching Mozilla Marketplace API URL", url
    if url in fetched_data:
        next = fetched_data[url]["next"]
        if next == url: return False
        return next
    fp = urllib.urlopen(url)
    data = json.load(fp)
    fp.close()
    next = urlparse.urljoin(url, data["meta"]["next"])
    if next == url: return False
    manifests = [o["manifest_url"] for o in data["objects"]]
    fetched_data[url] = {"next": next, "manifests": manifests}
    fp = codecs.open("fetched_data.json", mode="w", encoding="utf8")
    json.dump(fetched_data, fp)
    fp.close()
    return next

if __name__ == "__main__":
    next = "https://marketplace.firefox.com/api/v1/apps/search/?app_type=hosted&format=JSON"
    while True:
        next = fetch(next)
        if not next:
            break

