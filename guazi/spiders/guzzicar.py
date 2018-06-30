# -*- coding: utf-8 -*-
import scrapy
from guazi.items import GuaziItem
from scrapy_splash import SplashRequest

class GuzzicarSpider(scrapy.Spider):
    name = 'guzzicar'
    allowed_domains = ['guazi.com']
    start_urls = ['https://www.guazi.com/www/buy/o{}/#bread'.format(i) for i in range(0,10)]

    def start_requests(self):
        for url in self.start_urls:
        # url = "https://www.guazi.com/www/buy/o1/#bread"
            yield SplashRequest(url, callback=self.parse, args={"wait": 1})
    def parse(self, response):
        names = response.xpath('//h2[@class="t"]/text()').extract()
        addres = response.xpath('//div[@class="t-i"]')
        prices = response.xpath('//div[@class="t-price"]/p/text()').extract()

        for name,addr,price in zip(names,addres,prices):
            item = GuaziItem()
            item["name"] = name
            item["addr"] = addr.xpath("string(.)").extract_first()
            item["price"] = price

            yield item
