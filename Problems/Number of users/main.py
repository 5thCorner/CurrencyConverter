# import json
#
#
with open('users.json', 'r') as f:
    lst = json.load(f)

print(len(lst['users']))
