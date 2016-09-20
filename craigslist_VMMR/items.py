# -*- coding: utf-8 -*-

# Model definitions for scraped items
#

import scrapy
from scrapy.item import Item, Field

class CraigslistVmmrItem(scrapy.Item):
    ad_url = Field()
    title = Field()
    mmr = Field()
    post_date = Field()
    price = Field()
    location = Field()
    image_urls = Field()
    images = Field()
    #summary = Field()
