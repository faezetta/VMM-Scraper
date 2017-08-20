Python crawler for Craigslist vehicle ads in all U.S. states using Scrapy

## Prerequisities
* Python 2.x or 3.x
* pip
* Scrapy and all its dependencies

## Running the Project
To modify the code for your own purpose:
* [items.py](/craigslist_VMMR/items.py) includes the items you want to parse in each page. Current version includes the ad URL, posting title, date, location, images and price of the vehicle.
* [runVMMR.py](/craigslist_VMMR/spiders/runVMMR.py) defines the initial URL, how to navigate the pages or follow links and extract and parse the fields defined above for the scraper. In the current setting, only the first 5 pages showing up in search results are visited.
* [settings.py](/craigslist_VMMR/settings.py) defines the directory where you want to save the images and parsed results. You can modify the download delay based on your project. It makes use of different middleware available online such as [this](https://github.com/cnu/scrapy-random-useragent) and [this](https://github.com/alecxe/scrapy-fake-useragent).
* [urls.txt](urls.txt) includes the list craigslist URLS for different US. Cities that the scraper goes through.

To run the scraper, you just need to run the spider: 
```
$ scrapy crawl craigstlistDemo
```
The output is a csv file with the posts found including the target fields. 

## Others
Beware of IP ban from craigslist.
