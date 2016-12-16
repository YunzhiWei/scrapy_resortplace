# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem

# This is Level 5 Spider
_GLB_SPIDER_NAME     = "cncntraffic"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
_GLB_START_URL_LIST  = ["http://datong.cncn.com/jingdian/yungangshiku/jiaotong"]

class CncnTrafficSpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN
    start_urls = _GLB_START_URL_LIST

    def parse(self, response):
        """
        Function:   This function is to parse the search result list

        IN:         response - crawl response
        Out:        NA

        Special:
        """

        print "response: ", response

        for ppp in response.xpath('//div[@class="box670"]/div[@class="txt1"]/p'):
            details = ppp.xpath('.//text()').extract()
            if len(details) > 0:
                for detail in details:
                    print "details: ", detail.replace(u'\xa0', ' ')
