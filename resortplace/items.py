# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ResortplaceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    root_url        = scrapy.Field()
    spot_name       = scrapy.Field()
    spot_addr       = scrapy.Field()
    spot_type       = scrapy.Field()
    spot_theme      = scrapy.Field()
    spot_star       = scrapy.Field()
    spot_info       = scrapy.Field()
    open_time       = scrapy.Field()
    ticket_type     = scrapy.Field()
    ticket_info     = scrapy.Field()
    traffic_info    = scrapy.Field()

class CityLinkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    province        = scrapy.Field()
    city            = scrapy.Field()
    url             = scrapy.Field()
