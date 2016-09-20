"""
CrawlSpider looking into a specific city and pull out content for:
Title, Ad's URL, Post Date, Price, Vehicle Details, Locations and Images.

List of craigslist pages for all cities provided in the url.txt from:
https://sites.google.com/site/clsiteinfo/city-site-code-sort
"""

from scrapy import Spider, Request
from scrapy.selector import Selector
from craigslist_VMMR.items import CraigslistVmmrItem
import urlparse

search_url = '/search/cto' #cta
    
class DemoSpider(Spider):
    name = 'craigslistDemo'
    allowed_urls = ['https://craigslist.org','http://icanhazip.com']
    start_urls = [l.strip() for l in open('urls.txt').readlines()]
       
    def parse(self, response):
        urls = []
        for i in range(4):
            tn = '?s=' + str(100*i)
            url = urlparse.urljoin(response.url, search_url)
            urls.append(urlparse.urljoin(url, tn))
        for url in urls:
            yield Request(url, meta={'start_url': response.url}, callback=self.parse_main_page)
            #yield Request('http://icanhazip.com/', callback=self.check_ip, dont_filter = True)

    def parse_main_page(self, response):
        ids = response.xpath('//*[@class="row"]/@data-pid').extract()
        for id in ids:
            curlink = response.xpath('//*[@data-pid="' + str(id) + '"]/a/@href').extract()[0]
            link = response.meta['start_url'] + str(curlink)
            yield Request(link, callback=self.parse_detail_page)
        
    def parse_detail_page(self, response):
        title = response.xpath('//*[@ id = "titletextonly"]/text()').extract()[0]
        mmr = response.xpath('//*[@class = "attrgroup"]/span/b/text()').extract()[0]
        post_time=response.xpath('//*[@id = "pagecontainer"]/section/section/div[2]/p[2]/time/text()').extract()[0]
        try:                price = response.xpath('//*[@class = "price"]/text()').extract()[0]
        except IndexError:  pass
        try:                location = response.xpath('//small/text()').extract()[0]
        except IndexError:  pass
        image_urls = response.xpath('//*[@id="thumbs"]/a/@href').extract()
        #body = response.xpath('//*[@id = "postingbody"]//text()').extract()
        #body = reduce(lambda x,y: str(x).strip() + ' ' + str(y).strip(), body)

        item = CraigslistVmmrItem()
        item['ad_url'] = response.url;
        item['title'] = str(title)
        item['mmr'] = str(mmr)
        item['post_date']=str(post_time)
        item['price'] = str(price)
        item['location'] = str(location)
        item['image_urls'] = image_urls
        #item['summary'] = body
           
        yield item

    def check_ip(self, response):
        print "Public IP: " + response.body + " ************* \n"

