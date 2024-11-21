# TODO решите задачу
import json
filename = 'input.json'
def task(file) -> float:
    with open(file) as f:
        data = json.load(f)
        result = [dict["score"] * dict["weight"] for dict in data]
        return round(sum(result), 3)

print(task(filename))
