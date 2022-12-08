#!/usr/bin/env python3
#!/usr/bin/python

import json
from jsonschema import validate

schema = {
    "list_of_integers": {"type": "string"},
    "target": {"type": "number"}
}

def getPairs(list: list, target_int: int):
    result = []
    len_list = len(list)
    sorted_list = sorted(list)
    i, j = 0, len_list-1
    while (i < j):
        if sorted_list[i] + sorted_list[j] == target_int:
            result.append([sorted_list[i], sorted_list[j]])
            i+=1
            j-=1
        elif sorted_list[i] + sorted_list[j] < target_int:
            i+=1
        else:
            j-=1
    return result

def launchApp():
    try:
        with open("inputs.json") as json_data_file:
            try:
                data = json.load(json_data_file)
                validate(instance=data, schema=schema)
            
                list = data['list_of_integers'].split(',')
                target = data['target']

                list_of_integers = [int(item) for item in list]
                
                print(getPairs(list_of_integers, target))
            except Exception as e:
                print("invalid JSON")
    except IOError:
        print("Could not open file!")
