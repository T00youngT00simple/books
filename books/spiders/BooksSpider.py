
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from books.items import BookItem
class book_spider(scrapy.Spider):
    name = 'books'
    allowed_domains = ["toscrape.com/"]
    start_urls  = ['http://books.toscrape.com/']

    def parse(self,response):
        for book in response.selector.xpath("//li/article[@class = 'product_pod']"):
            item = BookItem()
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.xpath('./div/p[1]/text()').extract_first()
            item['name'] = name
            item['price'] = price
            yield item
        # next_url = response.selector.xpath('//li[@class = "next"]/a/@href').extract_first()
        # #http://books.toscrape.com/catalogue/page-2.html
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(next_url,callback=self.parse)

        le = LinkExtractor(restrict_xpaths='//li[@class = "next"]/a')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url,callback=self.parse)




