# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem

# This is Level 2 Spider
_GLB_SPIDER_NAME     = "cncncity"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
_GLB_START_URL_LIST  = ["http://hengshui.cncn.com/jingdian/"]

class CncnCitySpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN
    start_urls = _GLB_START_URL_LIST

    def parse(self, response):

        print "response: ", response

        # iterate each search result to see if there is any new for today
        for spot in response.xpath('//div[@class="city_spots"]/div[@class="city_spots_list"]/ul/li'):
            print "spot: ", spot
            link = spot.xpath('a/@href').extract()
            name = spot.xpath('a/div[@class="title"]/b/text()').extract()
            print "name: ", name[0], link[0]

        # try to find if there is the next page link in the current search result
        # if yes, try to get the link and invoke this parse to process
        pagelinks = response.xpath('//div[@class="page"]/div[@class="page_con"]/a[@class="num next"]/@href').extract()
        if len(pagelinks) > 0:
            rooturl = response.url[0:response.url.find('jingdian')]
            print "url: ", rooturl
            nextpageurl = rooturl + "jingdian/" + pagelinks[0].encode('utf-8')
            print "Next @ ", nextpageurl
            yield scrapy.Request(nextpageurl, callback = self.parse)
