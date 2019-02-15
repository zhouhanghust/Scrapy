# -*- coding: utf-8 -*-
import json
from jieba import analyse

# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags

load_dict={} #存放读取的数据
with open("../data/json/paintsDetail_relation.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)
keyword_list = []
tmp_list = []
for key in load_dict:
     try:
          # 原始文本
          text = load_dict[key]

          # 基于TF-IDF算法进行关键词抽取
          keywords = tfidf(key)
          print("keywords by tfidf:",key)
          # 输出抽取出的关键词
          for keyword in keywords:
               print(keyword)
               tmp_list.append(keyword)
               if "狗" in keyword or "犬" in keyword:
                    keyword = "狗"
               if keyword not in keyword_list:
                    keyword_list.append(keyword)

     except Exception as e:
          print(e)
print(len(keyword_list))
print(keyword_list)
print(len(tmp_list))

