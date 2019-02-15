# -*- coding: utf-8 -*-
import numpy as np
import json
info_list = ['中文名', '国籍', '民族', '出生地', '出生日期', '逝世日期', '职业', '主要成就', '朝代', '本名', '字号', '所处时代', '出生时间', '去世时间', '主要作品', '别名', '代表作品', '别称', '民族族群', '官职', '追赠', '谥号', '荣誉', '信仰', '外文名', '毕业院校', '祖籍', '字', '号', '性别', '生前官职', '谥名', '学历', '现居住地', '作品润格', '父亲', '逝世地', '在位时间', '姓名', '籍贯', '擅长', '庙号', '陵号', '年号', '头衔', '出生年月', '绰号', '登场作品', '登场回目', '出身', '上山前身份', '所用兵器', '梁山位次', '对应星号', '梁山职司', '陵寝', '艺术风格', '星座', '血型', '身高', '体重', '经纪公司', '作品', '出生', '中文名称', '临床职称', '好友', '王爵', '书名', '作者', '类别', '出版社', '记载朝代', '卷数', '画派', '号称', '原名', '死因', '尊称', '拼音', '反义词', '近义词', '封爵', '作品收藏', '驻锡寺院', '民系', '享年', '年代', '教学职称', '丈夫', '年龄', '曾用假名', '政治面貌', '别号', '僧名', '兄长', '成就', '官位', '又号', '归隐地', '草草', '职称', '在位', '陵墓', '妻子', '时间', '国家领袖', '都城', '主要城市', '官方语言', '货币', '人口数量', '主要民族', '国土面积', '开创者', '政治制度', '选官制度', '政治体制', '科技成就', '前任', '继任', '亲属', '解释', '读音', '所处年间', '相关典故', '时代']
have_list = []
person_dict = {}
#file_object = open('E:/code/KGQA_painter-master/quotesbot/quotesbot/data/txt/wordVec.txt','w',encoding="utf-8")
with open(r'D:\tool\Tencent_AILab_ChineseEmbedding.txt','r',encoding="utf-8") as f:
    data = f.readline()
    print(data)
    index = 0
    size = 0
    while(1):
        data = f.readline()
        size +=1
        try:
            type = data.split(" ")[0]
            if type in info_list:
                index += 1
                have_list.append(data.split(" ")[0])
                person_dict[type] = data.strip(type+" ").split(" ")
                #file_object.write(data.strip("\n"))
                print(size,index,data)
            if index == 110:
                break
        except ValueError:
            print("==========================")
for info in info_list:
    if info not in have_list:
        print(info)
with open('../data/json/personInfoVec.json', 'w', encoding="utf-8") as outfile:
    json.dump(person_dict, outfile, ensure_ascii=False)