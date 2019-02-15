# -*- coding: utf-8 -*-
import json

load_dict={} #存放读取的数据
with open("../data/json/keywords.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)
keywords = []
for key in load_dict:
    keywords.append(key["keywords"])

person_list = []
stop_list = ['不详','明人','清人','丁姓画师','清宫廷画家']
file_object = open('../data/txt/paints.txt', 'r', encoding="utf-8").readlines()
for data in file_object:  # 生成url列表
    names = data.strip('\n').split(" ")[5].replace("、","　")
    names = names.strip("等").split("（")[0]
    for name in names.split("　"):
        if name not in stop_list and name not in person_list:
            print(name)
            person_list.append(name)

'''for name in person_list:
    if name not in keywords and len(name)>1:
        print(name)'''