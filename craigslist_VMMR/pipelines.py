# -*- coding: utf-8 -*-

# Item pipeline definition
#

from scrapy.pipelines.images import ImagesPipeline, ImageException
from scrapy.http import Request
from scrapy.exceptions import DropItem
from cStringIO import StringIO
from craigslist_VMMR import settings
from craigslist_VMMR.items import CraigslistVmmrItem
import csv
import os.path
      
class CraigslistVmmrPipeline(ImagesPipeline):
       
    def get_media_requests(self, item, info):
        print"\n Reading images *************"
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})  

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Items contains no images')
        return item

    # Using image url and mmr instead of hash
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]
        image_name = item['mmr'] + '_' + image_guid
        return 'full/%s' % (image_name)
    
    # Override the convert_image method to disable image conversion    
    def convert_image(self, image, size=None):
        buf = StringIO()        
        try:
            image.save(buf, image.format)
        except Exception, ex:
            raise ImageException("Cannot process image. Error: %s" % ex)

        return image, buf

# To add a process_item module and save data to csv with headers from items
class WriteToCsv(object):
       
    def __init__(self):
        if not os.path.isfile(settings.csv_file_path):
            writer = csv.writer(open(settings.csv_file_path, 'wb'), lineterminator='\n')
            header_keys = CraigslistVmmrItem.fields.keys()
            writer.writerow(header_keys)

    def process_item(self, item, spider):
        print "Save data ************* \n"
        writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
        writer.writerow([item[key] for key in item.keys()])
        return item
