# -*- coding: utf-8 -*-
import json
import tool

load_dict = {}
person_dict = {}
stop_list = ['朝代','性别','享年']
mapping_dict = {}
with open("../data/json/personInfoVec.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)
info_list = ['中文名', '别名', '民族', '信仰', '毕业院校', '出生地', '祖籍', '出生日期', '逝世日期', '职业', '代表作品']
with open("../data/json/allperson.json",'r', encoding="utf-8") as load_person:
    person_dict = json.load(load_person)
for info in person_dict:
    if info["title"] == "error":
        continue
    baseInfo_dict = {}
    baseInfo_dict["detail"] = info["detail"].replace("\xa0","")
    baseInfo_dict["image"] = info["image"]
    print(info["title"])
    tmp_info = []
    baseInfoKeyList = info['baseInfoKeyList'].split("##")
    for i in range(len(baseInfoKeyList)):
        key = baseInfoKeyList[i]
        baseInfoKey = key.replace("\xa0","").strip("：")
        try:
            if baseInfoKey == "民族族群":
                baseInfoKey = "民族"
            if baseInfoKey in ['曾用假名','又号']:
                baseInfoKey = "别名"
            if baseInfoKey in ['本名', '姓名']:
                baseInfoKey = "中文名"
            if baseInfoKey in ['籍贯']:
                baseInfoKey = "祖籍"
            if baseInfoKey in ['出生']:
                baseInfoKey = "出生日期"
            if baseInfoKey in stop_list:
                continue
            if baseInfoKey in info_list:
                tmp_info.append(baseInfoKey)
                baseInfo_dict[baseInfoKey] = info['baseInfoValueList'].split("##")[i]
            elif baseInfoKey in load_dict.keys() and baseInfoKey not in info_list:
                vector_a = load_dict[baseInfoKey]
                max_sim = 0.8
                for basic_info in info_list:
                    if basic_info not in tmp_info:
                        vector_b = load_dict[basic_info]
                        sim = tool.cos_sim(vector_a,vector_b)
                        if sim > 0.8 and sim > max_sim:
                            print(baseInfoKey,basic_info,sim)
                            max_sim = sim
                            baseInfoKey = basic_info
                    # 这个判断条件是错误滴
                    # if baseInfoKey == basic_info:
                    tmp_info.append(basic_info)
                    baseInfo_dict[baseInfoKey] = info['baseInfoValueList'].split("##")[i]
        except Exception as e:
            print(baseInfoKey,e)

    for tmp in info_list:
        if tmp not in tmp_info:
            baseInfo_dict[tmp] = ""
    mapping_dict[info["title"]] = baseInfo_dict
with open('../data/json/mapping.json', 'w', encoding="utf-8") as outfile:
    json.dump(mapping_dict, outfile, ensure_ascii=False)