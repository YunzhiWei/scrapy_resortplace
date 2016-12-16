# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem

# This is Level 6 Spider
_GLB_SPIDER_NAME     = "cncnticket"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
_GLB_START_URL_LIST  = ["http://datong.cncn.com/jingdian/yungangshiku/menpiao"]

class CncnTicketSpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN
    start_urls = _GLB_START_URL_LIST

    def parse(self, response):

        print "response: ", response

        for ppp in response.xpath('//div[@class="info_type"]/p'):
            # print "ppp: ", ppp
            print "itemkey: ", ppp.xpath('span/text()').extract()[0]
            details = ppp.xpath('.//span[@class="nr"]/text()').extract()
            if len(details) > 0:
                for detail in details:
                    print "itemvalue: ", detail.replace(u'\xa0', ' ')
            details = ppp.xpath('.//a//text()').extract()
            if len(details) > 0:
                for detail in details:
                    print "itemvalue: ", detail.replace(u'\xa0', ' ')
