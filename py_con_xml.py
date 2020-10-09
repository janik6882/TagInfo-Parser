import json
import xmltodict
import os

document = os.path.join("scans", "Trysil_2019_mod.xml")
x = open(document, "r")
x = xmltodict.parse(x.read())
#json.dump(x, open("out.json", "w"))
data = x["scan"]["section"][3]["subsection"]
data = data[3:]
data = data[0]["block"][:-1]  # [1]["data"]["#text"]

t = [i["data"]["#text"] for i in data]
print t
res = str()
x = [bytearray.fromhex(t[i]) for i in range(len(t))]
for i in x:
    res += str(i)
print res
