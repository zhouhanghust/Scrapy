# -*- coding: utf-8 -*-
import json

load_dict={} #存放读取的数据
with open("../data/json/paints.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)
useful_data ={}
id =0
f = open('E:/code/KGQA_painter-master/quotesbot/quotesbot/data/txt/paints.txt','w',encoding="utf-8")

for key in load_dict:
    if key["image"] is not None:
        id = id +1
        #key["id"] = key["href"].split("/")[-1].split(".")[0]
        key["id"] = id
        key["name"] = key["name"].strip('\n').strip(" ").replace("•","·")
        key["classification"] = key["classification"].strip('\n').strip(" ")
        key["epoch"] = key["epoch"].strip('\n').strip(" ")
        key["href"] = "https://www.dpm.org.cn"+key["href"]
        key["image"] = key["image"].strip('\n').strip(" ")
        key["author"] = key["author"].strip('\n').strip(" ")
        if key["author"] is None or key["author"]=="":
            key["author"] = "不详"
        print(key["id"])
        info = str(key["id"]) + " " + str(key["name"]) + " " + str(key["classification"]) + " " + key["image"]+ " " + key["epoch"]+ " " + key["author"]+ " " + key["href"]

        f.write(info+"\n")



f.close()