# -- coding:utf-8 --

import time
from selenium import webdriver
from scrapy.selector import Selector

# 设置不加载图片
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_opt.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_opt)
browser.get("https://www.jd.com/")
browser.maximize_window()
time.sleep(2)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(2)

t_selector = Selector(text=browser.page_source)
browser.quit()