import urllib2, json, codecs, urlparse

try:
    fp = codecs.open("parsed_manifests.json", encoding="utf8")
    manifests = json.load(fp)
    fp.close()
except:
    manifests = {}

try:
    fp = codecs.open("fetched_data.json", encoding="utf8")
    fetched_data = json.load(fp)
    fp.close()
except:
    fetched_data = {}

def fetch(murl):
    print "Fetching manifest", murl
    if murl in manifests: return
    try:
        fp = urllib2.urlopen(murl, timeout=4)
    except:
        manifests[murl] = {"success": False, "error": "Manifest URL fetch error"}
    else:
        try:
            data = json.load(fp)
        except:
            manifests[murl] = {"success": False, "error": "Manifest JSON parse error"}
        else:
            if "launch_path" not in data:
                manifests[murl] = {"success": False, "error": "No launch path in manifest"}
            else:
                fp.close()
                app_url = urlparse.urljoin(murl, data["launch_path"])
                manifests[murl] = {"app_url": app_url, "name": data.get("name", app_url), "success": True}
    fp = codecs.open("parsed_manifests.json", mode="w", encoding="utf8")
    json.dump(manifests, fp)
    fp.close()

for d in fetched_data.values():
    for murl in d["manifests"]:
        fetch(murl)