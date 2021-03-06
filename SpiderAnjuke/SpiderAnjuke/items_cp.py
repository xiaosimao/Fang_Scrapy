# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderlianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    houseTitle = scrapy.Field()
    houseCity = scrapy.Field()
    houseCityURL = scrapy.Field()
    houseName = scrapy.Field()
    housePublishedTime = scrapy.Field()
    housePrice = scrapy.Field()
    houseHistoryPrice = scrapy.Field()
    houseArea = scrapy.Field()
    houseAddress = scrapy.Field()
    houseDistrict = scrapy.Field()
    houseBaiduLongitude = scrapy.Field()
    houseBaiduLatitude = scrapy.Field()

    pass
