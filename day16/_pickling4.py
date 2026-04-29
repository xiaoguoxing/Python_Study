import json
with open('./2.txt','r') as f:
    d = json.load(f)
    print(d)