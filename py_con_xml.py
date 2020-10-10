# -*- coding: utf-8 -*-
import xmltodict
import os


def get_data(path):
    x = open(path, "r")
    x = xmltodict.parse(x.read())
    data = x["scan"]["section"][3]["subsection"]
    data = data[3:]
    data = data[0]["block"][:-1]
    t = [i["data"]["#text"] for i in data]
    res = str()
    x = [bytearray.fromhex(t[i]) for i in range(len(t))]
    for i in x:
        res += str(i)
    return res


def main():
    p1 = os.path.join("scans", "SFL_2012.xml")
    p2 = os.path.join("scans", "SFL_2017.xml")
    p3 = os.path.join("scans", "SFL_2018_adv_night.xml")
    x2012 = get_data(p1)
    x2017 = get_data(p2)
    x2018 = get_data(p3)
    print len(x2012)
    print x2012
    print len(x2017)
    print x2017
    print len(x2018)
    print x2018


if __name__ == '__main__':
    main()
