import json


s_json = input()
s_pyt = json.loads(s_json)

print(type(s_pyt))
print(s_pyt)
