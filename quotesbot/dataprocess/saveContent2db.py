# -*- coding: utf-8 -*-
import json
import pymysql
import tool

conn = pymysql.connect(
    host='localhost',  # mysql服务器地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='123456',  # 密码
    db='kg_painter_demo',  # 数据库名称
    charset='utf8',  # 连接编码，根据需要填写
)
cur = conn.cursor()  # 创建并返回游标

load_dict = {}
keyword_list = []
with open("../data/json/content.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)
for dict in load_dict:
    if dict["keywords"] is None:
        continue

    sql = 'insert into content (content_id,content_name,content_info) values (%s, %s, %s)' \
          % (dict["content_id"], tool.add_str(dict["keywords"]), tool.add_str(dict["keydetail"]))

    sql2 = 'insert into paint_to_content (paint_id,content_id) values (%s, %s)' \
           % (dict["paint_id"], dict["content_id"])
    try:
        if str(dict["keywords"]) not in keyword_list:
            cur.execute(sql)  # 执行上述sql命令
        cur.execute(sql2)  # 执行上述sql命令
        conn.commit()
        keyword_list.append(dict["keywords"])
    except Exception as e:
        print("==================", dict["keywords"], e)
conn.close()
