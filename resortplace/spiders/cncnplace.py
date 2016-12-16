# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem, CityLinkItem

# This is Level 1 Spider
_GLB_SPIDER_NAME     = "cncnplace"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
_GLB_START_URL_LIST  = ["http://www.cncn.com/place/"]

class CncnPlaceSpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN
    start_urls = _GLB_START_URL_LIST

    def parse(self, response):

        print "response: ", response

        item = CityLinkItem()

        # iterate each search result to see if there is any new for today
        for province in response.xpath('//div[@class="city_all"]/div[@class="tli"]'):
            name0 = province.xpath('div[@class="t"]')
            namea = name0.xpath('a')
            # print "province name0: ", name0
            # print "province namea: ", namea
            if len(namea) == 0:
                name = name0.xpath('text()').extract()
            else:
                name = namea.xpath('text()').extract()
            print "province name:  ", name[0]
            for city in province.xpath('div[@class="li"]/a'):
                link = city.xpath('@href').extract()
                name = city.xpath('text()').extract()
                print "city: ", name[0], link[0]
                item['city'] = name[0]
                item['url']  = link[0]
                yield item
