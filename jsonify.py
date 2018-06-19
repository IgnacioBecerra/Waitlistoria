import json

for w in open("./data/CSE100.json"):
	print(w)
	if w == "SE":
		w = '"type": "SE"'