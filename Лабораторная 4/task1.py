# TODO решите задачу
import json
filename = 'input.json'
def task(file) -> float:
    sum_ = 0
    with open(file) as f:
        data = json.load(f)
        for dict in data:
            sum_ += dict["score"] * dict["weight"]
        return round(sum_, 3)

print(task(filename))
