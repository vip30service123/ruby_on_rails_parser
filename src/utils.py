import json


def read_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    return data


def write_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)