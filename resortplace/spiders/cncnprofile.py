# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem

# This is Level 4 Spider
_GLB_SPIDER_NAME     = "cncnprofile"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
_GLB_START_URL_LIST  = ["http://datong.cncn.com/jingdian/yungangshiku/profile"]

class CncnProfileSpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN
    start_urls = _GLB_START_URL_LIST

    def parse(self, response):

        print "response: ", response

        content = response.xpath('//div[@class="type"]')

        for detail in content.xpath('.//p//text()').extract():  # .//p//text() 会提取 tag <p> 下面所有的 文本内容，可能是属于 tag <p> 的，也可能是嵌套在 <p> 内部的 <span> 等等
            print "detail: ", detail.replace(u'\xa0', ' ')
