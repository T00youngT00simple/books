# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):

    # define the fields for your item here like:
    # id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()

# class BookItem_ex(BookItem):
#     url = scrapy.Field()
