# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import random

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'zhihu.middlewares.MyCustomDownloaderMiddleware': 543,
   'zhihu.middlewares.ProxyMiddleware': 554,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihu.pipelines.ZhihuPipeline': 300,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#UA文件
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 
    'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36',
]

USER_AGENT = random.choice(USER_AGENT_LIST)

#数据库文件
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = 3306
MYSQL_DB = 'test'

#headers
headers = {
    'cookie': 'd_c0="AEACagcEdguPTuI-xvKbwbrymWD3Qz_hjTg=|1489678463"; _zap=c59a21e5-6ba7-454b-b55d-f49d4bb2514d; q_c1=f3a6b725fa0740809d3fbfa7b27a0a82|1504404590000|1489678461000; __DAYU_PP=VnRZaAbVjF2Y72i2Ibze2f45defbc60a; q_c1=f3a6b725fa0740809d3fbfa7b27a0a82|1526799064000|1489678461000; _xsrf=d7d544b2-f692-4d25-b8c9-9596553cc79f; capsion_ticket="2|1:0|10:1528538306|14:capsion_ticket|44:YjM0ZDY2YmZkMDBlNGQ1MDhmOWM5MDY0MTdiZjFlNWY=|50084dc7d6e0a99cbe565ec7431e0aea7a4dd015a714aa7cf0e6d70eff4a3fe3"; l_n_c=1; n_c=1; __utma=51854390.1250038235.1508418197.1512663574.1528548346.6; __utmc=51854390; __utmz=51854390.1528548346.6.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|2=registration_date=20161215=1^3=entry_date=20170316=1; tgw_l7_route=7139e401481ef2f46ce98b22af4f4bed; l_cap_id="OWY1YzIzMTc2NmUyNDVkMGE2ZDdhZjBkNTQ5NTA2MDA=|1528553906|fdee998e61c248ed46fa7a158aba49000c34b7f8"; r_cap_id="NTRkZDJjNjBkMzQ2NDNhOWE1YzUyYjlkNTYwODJkNzk=|1528553906|73e734318ebeef1f7c7cce30b23fa4b50dc8d87b"; cap_id="MjAwNmFlOGFmZTYzNDhkODg0MDc4MzY2NDViOTAzYWI=|1528553906|d208c0cc516c188780b1795cc1317660916b48c8"',
    'origin': 'https://www.zhihu.com',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'referer': 'https://www.zhihu.com/topics',
    'authority': 'www.zhihu.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrftoken': 'd7d544b2-f692-4d25-b8c9-9596553cc79f',
}

#log
LOG_FILE = "mySpider.log"
LOG_LEVEL = "ERROR"