A couple of very noddy Python scripts to get the app URLs for all hosted web apps listed in the Mozilla Marketplace. We hit the Marketplace API to get the manifest URL for each hosted app, then hit each manifest URL to get its actual app URL. Run `get-all-mm-hosted.py` first, then `fetch_parse_manifests.py`, then `python -c "import json; d=json.load(open('parsed_manifests.json')); win=[x for x in d.values() if x['success']]; print json.dumps([{'name':x['name'],'url':x['app_url']} for x in win], indent=2)" > app_list.json` to get a final list. The scripts pick up where they left off if they're interrupted, at least in theory. 

On 27th August 2014, there were 1876 hosted apps listed in the Marketplace; fetching the manifests, 1534 worked, and 342 didn't. List of working apps with names in app_list.json.
