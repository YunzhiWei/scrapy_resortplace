# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem

# This is Level 4 Spider
_GLB_SPIDER_NAME     = "cncnprofile"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
# _GLB_START_POINT_URL = "http://www.neitui.me/index.php?name=neitui&handle=lists&fr=search&keyword="
# _GLB_SEARCH_KEYWORDS = ["Python", "hadoop", "大数据", "技术总监"]
# _GLB_START_URL_LIST  = [_GLB_START_POINT_URL + _keyword for _keyword in _GLB_SEARCH_KEYWORDS]


class CncnProfileSpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN

    start_urls = ["http://datong.cncn.com/jingdian/yungangshiku/profile"] # _GLB_START_URL_LIST

    # todayflag  = datetime.datetime.now().strftime('%m-%d')

    def parse(self, response):
        """
        Function:   This function is to parse the search result list

        IN:         response - crawl response
        Out:        NA

        Special:
        """

        print "response: ", response

        content = response.xpath('//div[@class="type"]')

        for detail in content.xpath('.//p//text()').extract():  # .//p//text() 会提取 tag <p> 下面所有的 文本内容，可能是属于 tag <p> 的，也可能是嵌套在 <p> 内部的 <span> 等等
            print "detail: ", detail.replace(u'\xa0', ' ')
