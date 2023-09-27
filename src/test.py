import json

with open("../expenses.txt", "r") as file:
    data = json.load(file)

print(data.get("vechile", []))