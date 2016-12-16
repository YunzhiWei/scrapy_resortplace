# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem

# This is Level 4 Spider
_GLB_SPIDER_NAME     = "cncn"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
_GLB_START_URL_LIST  = ["http://hengshui.cncn.com/jingdian/"]

class CncnCitySpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN
    start_urls = _GLB_START_URL_LIST

    # Level 2
    def parse(self, response):

        print "\n\n######### city response: ", response

        # iterate each search result to see if there is any new for today
        for spot in response.xpath('//div[@class="city_spots"]/div[@class="city_spots_list"]/ul/li'):
            # print "spot: ", spot
            link = spot.xpath('a/@href').extract()
            name = spot.xpath('a/div[@class="title"]/b/text()').extract()
            if len(name) > 0 and len(link) > 0:
                print "name: %s @ %s" % (name[0].replace(u'\xa0', ' '), link[0])
                yield scrapy.Request(link[0], callback = self.parse_spot)

        # try to find if there is the next page link in the current search result
        # if yes, try to get the link and invoke this parse to process
        pagelinks = response.xpath('//div[@class="page"]/div[@class="page_con"]/a[@class="num next"]/@href').extract()
        if len(pagelinks) > 0:
            rooturl = response.url[0:response.url.find('jingdian')]
            # print "url: ", rooturl
            nextpageurl = rooturl + "jingdian/" + pagelinks[0].encode('utf-8')
            print "Next @ ", nextpageurl
            yield scrapy.Request(nextpageurl, callback = self.parse)

    # Level 3
    def parse_spot(self, response):

        print "\n\n######### spot response: ", response

        names = response.xpath('//div[@class="content mt20"]/div[@class="box_list"]/div[@class="spots_info_con"]/div[@class="spots_info"]/div[@class="type"]/h1/text()').extract()
        stars = response.xpath('//div[@class="content mt20"]/div[@class="box_list"]/div[@class="spots_info_con"]/div[@class="spots_info"]/div[@class="type"]/h1/em/text()').extract()
        if len(names) > 0 and len(stars) > 0:
            print "%s %s" % (names[0].replace(u'\xa0', ' '), stars[0].replace(u'\xa0', ' '))
        elif len(names) > 0:
            print names[0].replace(u'\xa0', ' ')
        for detail in response.xpath('//div[@class="content mt20"]/div[@class="box_list"]/div[@class="spots_info_con"]/div[@class="spots_info"]/div[@class="type"]/dl'):
            # print "detail: ", detail
            itemkeys = detail.xpath('dt/text()').extract()
            if len(itemkeys) > 0:
                itemkey = itemkeys[0].replace(u'\xa0', ' ')
                itemvalues = detail.xpath('dd/p[@class="more J_why"]')
                if len(itemvalues) > 0:
                    itemvalue = itemvalues.xpath('@detail').extract()[0].replace(u'\xa0', ' ')
                else:
                    itemvalues = detail.xpath('dd/p')
                    if len(itemvalues) > 0:
                        itemvalue = itemvalues.xpath('text()').extract()[0].replace(u'\xa0', ' ')
                    else:
                        itemvalues = detail.xpath('dd/a')
                        if len(itemvalues) > 0:
                            itemvalue = itemvalues.xpath('text()').extract()[0].replace(u'\xa0', ' ')
                        else:
                            itemvalue = detail.xpath('dd/text()').extract()[0].replace(u'\xa0', ' ')
                print "%s %s" % (itemkey, itemvalue)

        yield scrapy.Request(response.url + "profile", callback = self.parse_profile)

    # Level 4
    def parse_profile(self, response):

        print "\n\n######### profile response: ", response

        content = response.xpath('//div[@class="type"]')

        for detail in content.xpath('.//p//text()').extract():  # .//p//text() 会提取 tag <p> 下面所有的 文本内容，可能是属于 tag <p> 的，也可能是嵌套在 <p> 内部的 <span> 等等
            print detail.replace(u'\xa0', ' ')

        # nextpageurl = response.url[0:response.url.find('profile')] + "menpiao"
        # # print "goto @ ", nextpageurl
        # yield scrapy.Request(nextpageurl, callback = self.parse_ticket)
        nextpageurl = response.url[0:response.url.find('profile')] + "jiaotong"
        # print "goto @ ", nextpageurl
        yield scrapy.Request(nextpageurl, callback = self.parse_traffic)

    # Level 5
    def parse_traffic(self, response):

        print "\n\n######### traffic response: ", response

        for ppp in response.xpath('//div[@class="box670"]/div[@class="txt1"]/p'):
            details = ppp.xpath('.//text()').extract()
            if len(details) > 0:
                for detail in details:
                    print detail.replace(u'\xa0', ' ')

        yield scrapy.Request(response.url[0:response.url.find('jiaotong')] + "menpiao", callback = self.parse_ticket)

    # Level 6
    def parse_ticket(self, response):

        print "\n\n######### ticket response: ", response

        for ppp in response.xpath('//div[@class="info_type"]/p'):
            # print "ppp: ", ppp
            itemkey = ppp.xpath('span/text()').extract()[0].replace(u'\xa0', ' ')
            itemvalue = ""
            details = ppp.xpath('.//span[@class="nr"]/text()').extract()
            if len(details) > 0:
                for detail in details:
                    itemvalue += detail.replace(u'\xa0', ' ')
            details = ppp.xpath('.//a//text()').extract()
            if len(details) > 0:
                for detail in details:
                    itemvalue += detail.replace(u'\xa0', ' ')

            print "%s %s" % (itemkey, itemvalue)
