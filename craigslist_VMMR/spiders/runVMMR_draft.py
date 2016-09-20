"""
CrawlSpider looking into a specific city and pull out content for:
Title, Ad's URL, Post Date, Post Date Specific, Price, Room Details, and Locations.

To change the city: https://sites.google.com/site/clsiteinfo/city-site-code-sort
"""

from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from craigslist_VMMR.items import CraigslistVmmrItem

import csv, re, string

class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/cta"]
    item = []
   
    rules = (
            Rule(LxmlLinkExtractor(allow=(r'sfbay.craigslist.org/search/cta.*'),
                                   #restrict_xpaths=('//a[@class="button next"]'),
                                   #allow=(r'.*/search/cta\?s\=\d+.*'),
                                   #deny = (r'.*format\=rss.*')),
                                   ),
                 callback="parse_items",
                 follow= True,
                ),
            )

    def parse_items(self, response):
        if response.status is not 200:
            print "Error crawling % " % response.url
            return None
        self.logger.info('You are now crawling: %s', response.url)       
        hxs = HtmlXPathSelector(response)
        
        contents = hxs.xpath("//div[@class='rows']/*")
        items = []
        # loop through the postings
        for content in contents:
            item = CraigslistVmmrItem()
            item ["title"] = content.xpath("//p/span[@class='txt']/span[@class='pl']/a/span/text()").extract()[0]
            url_cur = content.xpath("//p/span[@class='txt']/span[@class='pl']/a/@href").extract()[0]
            url = 'https://sfbay.craigslist.org{}'.format(''.join(url_cur))
            item ['ad_url'] = url     
            item ["post_date"] = content.xpath("//p/span/span/time/text()").extract()[0]
            item ["price"] = content.xpath("//p/span/span[@class='l2']/span[@class='price']/text()").extract()[0]
            item ["location"] = content.xpath("//p/span/span[@class='l2']/span[@class='pnr']/small/text()").extract()[0].strip()
            
            #Parse request to follow the posting link into the actual post
            #Request(url=url , meta={'item': item}, callback=self.parse_items_page)
            items.append(item)

        return items
 
    def parse_items_page(self, response):
        hxs = HtmlXPathSelector(response)
        item = response.meta['item']
        #item ["summary"] = hxs.xpath('//section[@id="postingbody"]/text()').extract()
        images = response.xpath("//div[@id='thumbs']/a")
        item["image_urls"] = [image.xpath('@href').extract()[0] 
                              for image in images]
        #item["image_urls"] = response.xpath("//*[@id='thumbs']/a/@href").extract()




