import pprint
import requests
import sys

card = sys.argv[1]
r = requests.get("https://lookup.binlist.net/"+card, headers={'Accept-Version':"3"})
pprint.pprint(r.json())
