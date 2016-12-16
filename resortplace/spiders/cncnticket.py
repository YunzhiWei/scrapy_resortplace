# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem

# This is Level 5 Spider
_GLB_SPIDER_NAME     = "cncnticket"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
# _GLB_START_POINT_URL = "http://www.neitui.me/index.php?name=neitui&handle=lists&fr=search&keyword="
# _GLB_SEARCH_KEYWORDS = ["Python", "hadoop", "大数据", "技术总监"]
# _GLB_START_URL_LIST  = [_GLB_START_POINT_URL + _keyword for _keyword in _GLB_SEARCH_KEYWORDS]


class CncnTicketSpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN

    start_urls = ["http://datong.cncn.com/jingdian/yungangshiku/menpiao"] # _GLB_START_URL_LIST

    # todayflag  = datetime.datetime.now().strftime('%m-%d')

    def parse(self, response):
        """
        Function:   This function is to parse the search result list

        IN:         response - crawl response
        Out:        NA

        Special:
        """

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
