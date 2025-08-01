import json

def read_json(path):
    json_data = []
    with open(path, "r") as f:
        json_data = json.load(f)
    return json_data