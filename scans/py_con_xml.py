import json, xmltodict

document = "Trysil_2019_mod.xml"
x = open(document, "r")
x = xmltodict.parse(x.read())
#json.dump(x, open("out.json", "w"))
data = x["scan"]["section"][3]["subsection"]
data = data[3:]
data = data[0]["block"][:-1]  # [1]["data"]["#text"]
for i in data:
    try:
        pass
        #print i["data"]["#text"]
    except KeyError:
        print i
t = [i["data"]["#text"] for i in data]
print t
x = [bytearray.fromhex(t[i]) for i in range(len(t))]
for i in x:
    print str(i)