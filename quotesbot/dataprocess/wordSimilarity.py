# -*- coding: utf-8 -*-
from word_similarity import WordSimilarity2010
import json

ws_tool = WordSimilarity2010()

b_a = "抄袭"
b_b = "克隆"
sim_b = ws_tool.similarity(b_a, b_b)
print(b_a, b_b, '相似度为', sim_b)
#抄袭 克隆 最终的相似度为 0.585642777645155

w_a = '人民'
sample_list = ["国民", "群众", "党群", "良民", "同志", "成年人", "市民", "亲属", "志愿者", "先锋" ]

for s_a in sample_list:
    sim_a = ws_tool.similarity(w_a,s_a)
    print(w_a, s_a, '相似度为', sim_a)

b_a = "出生日期"
b_b = "出生时间"
sim_b = ws_tool.similarity(b_a, b_b)
print(b_a, b_b, '相似度为', sim_b)

info_list = ['中文名', '别名', '民族', '信仰', '学校', '出生地', '祖籍', '出生日期', '死亡日期', '职业', '代表作品']
load_dict={} #存放读取的数据
baseInfoKeyList=set()
with open("../data/json/allperson.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)

for dict in load_dict:
    print(dict["title"])
    for key in dict['baseInfoKeyList'].split("##"):
        info = key.replace("\xa0","").strip("：")
        for basic_info in info_list:
            sim_a = ws_tool.similarity(info, basic_info)
            print(info, basic_info, '相似度为', sim_a)




