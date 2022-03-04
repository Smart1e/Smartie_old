def write(settings, file='settings.json'):
    import json
    
    #settings = {
    #    "system" : "2",
    #    "user" : "Loukas",
    #    "test1" : "True",
    #    "test2" : "False",
    #}
    myJSON = json.dumps(settings)

    with open(file, "w") as f:
        f.write(myJSON)


def update(key, newfig, file='settings.json'):
    import json

    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    data[key] = newfig
    with open(file, "w") as f:
        myjson = json.dump(data, f)

        f.close()

def read(file='settings.json', key='all'):
    import json
    if key == 'all':

        with open(file, "r") as f:
            data = json.load(f)

        f.close()
        return data
    else:
        with open(file, "r") as f:
            data = json.load(f)

        f.close()
        return data[key]
