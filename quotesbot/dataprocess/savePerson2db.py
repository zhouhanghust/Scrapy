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

person_dict = {}
load_dict = {}
with open("../data/json/mapping.json",'r',encoding="utf-8") as load_f:
     load_dict = json.load(load_f)
person_id = 0
for name in load_dict:
    person_id+=1
    person_dict = load_dict[name]
    sql = 'insert into person (person_id,name,image,alias,race,belief,school,birth_place,native_place,birth_date,death_date,occupation,rep_works,brief_intro)' \
          ' values (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s)' \
        % (person_id, tool.add_str(name), tool.add_str(person_dict['image']), tool.add_str(person_dict['别名']), \
           tool.add_str(person_dict['民族']),  tool.add_str(person_dict['信仰']), tool.add_str(person_dict['毕业院校']), \
           tool.add_str(person_dict['出生地']),tool.add_str(person_dict['祖籍']), tool.add_str(person_dict['出生日期']), \
           tool.add_str(person_dict['逝世日期']), tool.add_str(person_dict['职业']),tool.add_str(person_dict['代表作品']), \
           tool.add_str(person_dict['detail']))

    #print(sql)
    cur.execute(sql) # 执行上述sql命令
    conn.commit()

conn.close()