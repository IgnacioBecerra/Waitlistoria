import json

with open('./class_codes.json') as f:
    data = json.load(f)

for e in data:
	print(e)