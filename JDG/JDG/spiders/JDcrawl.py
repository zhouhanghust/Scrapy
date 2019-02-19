# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class JdcrawlSpider(scrapy.Spider):
    name = 'JDcrawl'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAP20&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=%E5%8D%8E%E4%B8%BAP20&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&page=1&s=1&click=0']

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="./chromedriver")
        self.wait = WebDriverWait(self.browser, 10)
        time.sleep(2)
        self.browser.maximize_window()
        super().__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        print("spider closed")
        self.browser.quit()

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        self.browser.get(url)
        time.sleep(1)
        return scrapy.Request(url, meta={'pn': 1},dont_filter=True)


    def parse(self, response):
        pn = response.meta['pn']
        # self.browser.execute_script(
        #     "window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight*5/6);")
        time.sleep(1)
        if pn < 50:
            next = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_bottomPage > span.p-num > a.pn-next")))
            next.click()
            pn += 1
            time.sleep(1)
            yield scrapy.Request(self.browser.current_url, meta={'pn': pn}, callback=self.parse)


