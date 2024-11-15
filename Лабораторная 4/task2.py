# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
data = []

def task() -> None:
    with open(INPUT_FILENAME, "r") as inp:
        reader = csv.DictReader(inp)

        for i in reader:
            data.append(i)
            with open(OUTPUT_FILENAME, "w") as out:
                json.dump(data, out, indent=4)





if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
