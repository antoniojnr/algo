import json

with open('meujson', 'r') as f:
    cont = json.load(f)
    print json.dumps(cont, sort_keys=True, indent=4)
