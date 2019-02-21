# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from scrapy.http import HtmlResponse
class JingdongSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    pass


class JSPageMiddleware(object):

    def process_request(self, request, spider):
        if spider.name == "jingdong":
            wait = WebDriverWait(spider.browser,10)
            spider.browser.get(request.url)
            spider.browser.maximize_window()
            time.sleep(2)
            # spider.browser.execute_script(
            #     "window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#content > div.login-wrap > div.w > div > div.login-tab.login-tab-r")))
            login.click()
            time.sleep(10)

            input_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginname')))
            input_name.send_keys("18602718836")
            input_passwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nloginpwd')))
            input_passwd.send_keys("Zhang1991")
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#loginsubmit")))
            submit.click()
            time.sleep(10)

            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8", request=request)









