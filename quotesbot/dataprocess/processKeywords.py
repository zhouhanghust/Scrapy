# -*- coding: utf-8 -*-
import json

load_dict={} #存放读取的数据
with open("../data/json/keywords.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)

with open('../data/txt/paints.txt','r',encoding="utf-8") as f:
    paints_list = f.readlines()
content_list = []
content_dict = {}
content_id = 0
for dict in load_dict:
    if dict["keywords"] is None:
        continue
    for paints in paints_list:
            paint = paints.strip('\n').split(" ")
            if dict["href"] == paint[-1]:
                dict["paint_id"] = paint[0]
                if str(dict["keywords"]) in content_dict:
                    dict["content_id"] = content_dict[dict["keywords"]]
                else:
                    content_id += 1
                    dict["content_id"] = content_id
                    content_dict[dict["keywords"]] = content_id
                break
    #print(dict['keywords'])
    #print(dict)
print(content_dict)
with open('../data/json/content.json', 'w', encoding="utf-8") as outfile:
    json.dump(load_dict, outfile, ensure_ascii=False)