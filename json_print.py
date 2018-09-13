import json

res = open('./sample.json' , 'r')
pr = json.load(res)

print (pr["hoge"][0]["aaa"])
