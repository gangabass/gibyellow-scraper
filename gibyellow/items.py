# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

def clear(value):
    
    if value is None:
        value = ""
    
    value = value.strip()
    return value

class GibyellowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field(serializer=clear)
    Address = scrapy.Field(serializer=clear)
    Phone = scrapy.Field(serializer=clear)
    Categories = scrapy.Field(serializer=clear)
    LogoURL = scrapy.Field(serializer=clear)
    
    pass
