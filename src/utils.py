import json


def read_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    return data


def write_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    return data


def write_file(path: str, data: str) -> None:
    with open(path, 'r', encoding='urf-8') as f:
        for line in data.splitlines():
            f.write(line+"\n")