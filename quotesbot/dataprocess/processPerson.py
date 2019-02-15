# -*- coding: utf-8 -*-
import json

load_dict={} #存放读取的数据
baseInfoKeyList= []
with open("../data/json/allperson.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)
'''person_list = []
for dict in load_dict:
    person_list.append(dict["title"].strip("'"))
print(person_list)
file_object = open('../data/txt/painter.txt', 'r', encoding="utf-8").readlines()
for person in file_object:  # 生成url列表
    if person.strip("\n") not in person_list:
        print(person.strip("\n"))'''


info_list = ['中文名', '别名', '民族', '信仰', '学校', '出生地', '祖籍', '出生日期', '逝世日期', '职业', '代表作品']
person_list = []
for dict in load_dict:
    print(dict["title"])
    for key in dict['baseInfoKeyList'].split("##"):
        info = key.replace("\xa0","").strip("：")
        if info !="" and info not in baseInfoKeyList:
            baseInfoKeyList.append(info)
print(baseInfoKeyList)
print(len(baseInfoKeyList))