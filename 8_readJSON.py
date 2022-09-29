import json

with open("7_JSONSample.json", mode="r", encoding="utf-8") as _file:
    _data= json.load(_file)
    print(_data["name"])


    