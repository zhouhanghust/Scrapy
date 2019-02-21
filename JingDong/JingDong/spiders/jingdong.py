# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['jd.com']
    start_urls = ['https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F']

    def __init__(self):
        # chrome_opt = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_opt.add_experimental_option("prefs", prefs)
        # self.browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_opt)
        self.browser = webdriver.Chrome(executable_path="./chromedriver")
        time.sleep(2)
        super(JingdongSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        print("spider closed")
        self.browser.quit()

    def parse(self, response):
        wait = WebDriverWait(self.browser, 10)
        input_passwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        input_passwd.send_keys("华为P20")
        time.sleep(0.5)
        sear = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#search > div > div.form > button")))
        sear.click()
        time.sleep(10)
