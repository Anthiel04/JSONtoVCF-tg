import json


def getFile(path):
    with open(path, "r") as file:
        data = json.load(file)

    return data["contacts"]["list"]
