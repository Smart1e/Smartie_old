import json

settings = {
    "system" : "2",
    "user" : "Loukas",
    "test1" : "True",
    "test2" : "False",
}


with open("test.json", "w") as f:
    json.dump(settings, f)
    print('Settings implemented.')
