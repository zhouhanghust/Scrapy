from scrapy.cmdline import execute

import sys
import os

pathnow = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pathnow)
execute(['scrapy','crawl','xn'])
