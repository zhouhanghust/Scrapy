# -*- coding: utf-8 -*-
import json

load_dict={} #存放读取的数据
with open("../data/json/paintsDetail.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)

paintsDetail_dict = {}
for key in load_dict:
    if key["name"] is not None:
        name = key["name"].strip('\n').strip(" ").replace("•", "·").strip("【").strip("】").strip(" ")
        detail = ''.join([str(i) for i in key["detail"]]).strip(" ").strip('\n').replace("•", "·")
        paintsDetail_dict[name] = detail.replace("'","‘")

with open('../data/json/paintsDetail_relation.json', 'w', encoding="utf-8") as outfile:
    json.dump(paintsDetail_dict, outfile, ensure_ascii=False)