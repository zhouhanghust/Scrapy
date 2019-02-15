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

with open('../data/txt/paints.txt','r',encoding="utf-8") as f:
    paints_list = f.readlines()
    for paints in paints_list:
        #print(paints.strip("\n"))
        paints = paints.strip("\n").split(" ")
        if paints[5] == "不详":
            continue
        sql = 'insert into person_to_paint (person_id,paint_id) values ' \
              '( (select t.person_id from person t  where t.name = %s),%s )' \
            % (tool.add_str(paints[5]), paints[0])

        print(sql)
        try:
            cur.execute(sql) # 执行上述sql命令
            conn.commit()
        except Exception as e:
            print("==================",paints[1],e)
conn.close()