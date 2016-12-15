# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem


_GLB_SPIDER_NAME     = "cncnplace"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
# _GLB_START_POINT_URL = "http://www.neitui.me/index.php?name=neitui&handle=lists&fr=search&keyword="
# _GLB_SEARCH_KEYWORDS = ["Python", "hadoop", "大数据", "技术总监"]
# _GLB_START_URL_LIST  = [_GLB_START_POINT_URL + _keyword for _keyword in _GLB_SEARCH_KEYWORDS]


class CncnPlaceSpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN

    start_urls = ["http://www.cncn.com/place/"] # _GLB_START_URL_LIST

    # todayflag  = datetime.datetime.now().strftime('%m-%d')

    def parse(self, response):
        """
        Function:   This function is to parse the search result list

        IN:         response - crawl response
        Out:        NA

        Special:
        """

        print "response: ", response

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
