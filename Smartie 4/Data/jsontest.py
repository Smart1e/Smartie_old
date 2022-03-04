import json

settings = {
    "system" : "2",
    "user" : "Loukas",
    "test1" : "True",
    "test2" : "False",
}
myJSON = json.dumps(settings)

with open("test.json", "w") as f:
    f.write(myJSON)
    print('Settings implemented.')
