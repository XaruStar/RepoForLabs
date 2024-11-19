import json

# TODO решите задачу
def task(json_file) -> float:
    with open(json_file, 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    for item in data:
        score = item.get('score', 0.0)

        weight = item.get('weight', 0.0)

        product = score * weight

        total_sum += product

    round_sum = round(total_sum, 3)

    return round_sum

json_file = 'input.json'
print(task(json_file))
