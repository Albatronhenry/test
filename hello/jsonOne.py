import json
dict = {
    'henry':23,'yoshi':33,'albatron':34,'group_ltd':'yonyougov'
}
jstr = json.dumps(dict)
print('dcit:', dict)
print('json:', jstr)
print('==============')
str = json.loads(jstr)
print(str)
print('==============')
with open(r'd:\dict.json','w') as f:
    json.dump(dict,f)
# f = open(r'd:\dict.json','r')
# for i in f:
#     i = f.read()
#     dataj = json.load(i)
#     print(dataj)