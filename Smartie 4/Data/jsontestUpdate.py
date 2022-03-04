import json

with open("test.json", "r") as f:
    data = json.load(f)
    print('File read.')
    f.close()

data['test1'] = "NotTrue"
print('Updated')
with open("test.json", "w") as f:
    myjson = json.dump(data, f)
    print('Saved update.')
    f.close()
