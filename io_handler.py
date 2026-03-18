import json 
with open ("data/resources-e01a.json","r") as xd: 
    recursos= json.load(xd)

print(recursos)
print("--------------------------------------------------------------")

with open ("data/works-e01a.json","r") as w: 
    trabajo= json.load(w)
print(trabajo)
    