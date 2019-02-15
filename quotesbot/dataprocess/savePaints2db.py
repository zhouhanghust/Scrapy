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
with open("../data/json/paintsDetail_relation.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)
with open('../data/txt/paints.txt','r',encoding="utf-8") as f:
    paints_list = f.readlines()
    for paints in paints_list:
        #print(paints.strip("\n"))
        paints = paints.strip("\n").split(" ")
        sql = 'insert into paint (paint_id,name,image,detail,theme_type,epoch,location)' \
              ' values (%s, %s, %s,%s, %s, %s,%s)' \
            % (paints[0], tool.add_str(paints[1]), tool.add_str(paints[3]), tool.add_str(load_dict[paints[1]]), \
               tool.add_str(paints[2]),  tool.add_str(paints[4]), tool.add_str('故宫博物院'))

        #print(sql)
        try:
            cur.execute(sql) # 执行上述sql命令
            conn.commit()
        except Exception as e:
            print("==================",paints[1],e)
conn.close()