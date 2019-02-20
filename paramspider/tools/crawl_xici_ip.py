# -- coding:utf-8 --

import requests
from paramspider.settings import MYUSER_AGENTS
import random
from scrapy.selector import Selector
import json


def crawl_ips():
    ua = random.choice(MYUSER_AGENTS)
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Host": "www.xicidaili.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ua
    }
    res = requests.get("https://www.xicidaili.com/nn/", headers=headers)
    selector = Selector(text=res.text)
    all_trs = selector.css("#ip_list  tr")

    ip_list = []
    for tr in all_trs[1:]:
        speed_str = tr.css("td.country div.bar::attr(title)").extract_first()
        speed = None
        if speed_str:
            speed = float(speed_str.strip("秒"))
        if not speed or speed > 2.0:
            continue
        all_text = tr.css("td::text").extract()
        ip = all_text[0]
        port = all_text[1]
        gaoni = all_text[4].strip()
        proxy_type = all_text[5]

        if gaoni != '高匿':
            continue

        if proxy_type == "HTTP":
            proxy_type = "http"
        else :
            proxy_type = "https"

        ip_list.append("{0}://{1}:{2}".format(proxy_type, ip, port))
    return ip_list


ip_list = crawl_ips()
with open('./ips.json', 'w', encoding="utf-8") as outfile:
    json.dump(ip_list, outfile, ensure_ascii=False)



