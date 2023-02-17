import json

with open("C:\\Users\\User\\PycharmProjects\\autoseller\\data\\KIA\\Kia_Rio\\Kia_Rio.json") as f:
    data = json.load(f)
print(data["auto"]["brand"])
