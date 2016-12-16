# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem

# This is Level 3 Spider
_GLB_SPIDER_NAME     = "cncnspot"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
#_GLB_START_URL_LIST  = ["http://datong.cncn.com/jingdian/yungangshiku/"]
_GLB_START_URL_LIST  = ["http://Hengshui.cncn.com/jingdian/taihuayagewenquandajiudian/"]

class CncnSpotSpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN
    start_urls = _GLB_START_URL_LIST

    def parse(self, response):

        print "response: ", response

        name = response.xpath('//div[@class="content mt20"]/div[@class="box_list"]/div[@class="spots_info_con"]/div[@class="spots_info"]/div[@class="type"]/h1/text()').extract()
        star = response.xpath('//div[@class="content mt20"]/div[@class="box_list"]/div[@class="spots_info_con"]/div[@class="spots_info"]/div[@class="type"]/h1/em/text()').extract()
        if len(name) > 0:
            print "name: ", name[0].replace(u'\xa0', ' ')
        if len(star) > 0:
            print "star: ", star[0]
        for detail in response.xpath('//div[@class="content mt20"]/div[@class="box_list"]/div[@class="spots_info_con"]/div[@class="spots_info"]/div[@class="type"]/dl'):
            # print "detail: ", detail
            itemkey = detail.xpath('dt/text()').extract()
            if len(itemkey) > 0:
                print "itemkey: ", itemkey[0]
                itemvalue = detail.xpath('dd/p[@class="more J_why"]')
                if len(itemvalue) > 0:
                    print "itemvalue: ", itemvalue.xpath('@detail').extract()[0].replace(u'\xa0', ' ')
                else:
                    itemvalue = detail.xpath('dd/p')
                    if len(itemvalue) > 0:
                        print "itemvalue: ", itemvalue.xpath('text()').extract()[0].replace(u'\xa0', ' ')
                    else:
                        itemvalue = detail.xpath('dd/a')
                        if len(itemvalue) > 0:
                            print "itemvalue: ", itemvalue.xpath('text()').extract()[0].replace(u'\xa0', ' ')
                        else:
                            print "itemvalue: ", detail.xpath('dd/text()').extract()[0].replace(u'\xa0', ' ')
