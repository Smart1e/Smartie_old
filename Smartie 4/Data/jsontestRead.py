import json


with open("test.json", "r") as f:
    data = json.load(f)
    print('Succsesfully read file.')

print(data)
