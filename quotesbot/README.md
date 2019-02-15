数据准备步骤
绘画数据
1.爬取故宫绘画基本数据
scrapy crawl paints-xpath -o json\paints.json
process_paints.py  paints.txt
2.绘画详情
scrapy crawl paintsDetail-xpath -o json\paintsDetai.json
process_paintsDetail.py 处理得到paintsDetail.txt ,paintsDetail_relation.json
3.绘画关键词
scrapy crawl keywords-xpath -o json\keywords.json
keywords.json
4.人物数据
scrapy crawl allperson-xpath -o json\allperson.json
挑战：
人名还可以继续优化，处理同义名字
https://baike.baidu.com/item/华岩/23889?fromtitle=华喦&fromid=2612331
人名同名不同人的处理，
5.根据相似度匹配，mapping.py 得到 mapping.json
6.person存入mysql
TypeError: can't concat tuple to bytes
字符串拼接方法 可以避免+拼接问题
1 str = 'There are %s, %s, %s on the table.' % (fruit1,fruit2,fruit3) 
7.paint存入mysql
'\ufffd' 需要' 改为 ’
"Data too long for column 'detail' at row 1"
8.person_to_paint存入mysql
        sql = 'insert into person_to_paint (person_id,paint_id) values ' \
              '( (select t.person_id from person t  where t.name = %s),%s )' \
            % (tool.add_str(paints[5]), paints[0])
9.content存入mysql
saveContent2db.py 处理contend，paint_to_content两张表
