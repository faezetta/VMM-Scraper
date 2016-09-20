# -*- coding: utf-8 -*-

# Scrapy settings for craigslist_VMMR project
#

BOT_NAME            = 'craigslist_VMMR'

IMAGES_EXPIRES      = 90
DOWNLOAD_DELAY      = 19.0
SPIDER_MODULES      = ['craigslist_VMMR.spiders']
NEWSPIDER_MODULE    = 'craigslist_VMMR.spiders'
DEFAULT_ITEM_CLASS  = 'craigslist_VMMR.items.CraigslistVmmrItem'
ITEM_PIPELINES      = {
                      'craigslist_VMMR.pipelines.CraigslistVmmrPipeline': 1,
                      'craigslist_VMMR.pipelines.WriteToCsv': 10
                      #'scrapy.pipelines.images.ImagesPipeline' : 20
                      }
IMAGES_STORE = 'images/'
csv_file_path = 'items.csv'

# maximum concurrent requests by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1   

# Specify the min height and width of the image to download
IMAGES_MIN_HEIGHT = 100
IMAGES_MIN_WIDTH  = 100

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Retry many times since proxies often fail
RETRY_TIMES = 2
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 90,
    'random_useragent.RandomUserAgentMiddleware': 80,
    #'scrapy-proxies-master.randomproxy.RandomProxy': 100,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

PROXY_LIST = 'list.txt'

# Enable or disable spider middlewares
#SPIDER_MIDDLEWARES = {
#    'craigslist_VMMR.middlewares.MyCustomSpiderMiddleware': 543,
#}

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

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
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
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
