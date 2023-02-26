import json

data = {
    "start": ((0, 0), (1, 1)),
    "goal": ((4, 2), (3, 2)),
    "k": 2,
    "N": 5
}

with open("data.json", "w") as f:
    json.dump(data, f)
