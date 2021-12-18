import json

f = open('databaseFiles/default.json')
data = json.load(f)

for i in data["google"]:
    print(i["username"])
        