# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from resortplace.items import ResortplaceItem

# This is Level 4 Spider
_GLB_SPIDER_NAME     = "cncn"
_GLB_ALLOWED_DOMAIN  = ["cncn.com"]
_GLB_CITY_URL_LIST   = [
    # "http://beijing.cncn.com",
    # "http://shanghai.cncn.com"
    # "http://tianjin.cncn.com"
    # "http://chongqing.cncn.com"

    # "http://hongkong.cncn.com",
    # "http://macao.cncn.com",
    # "http://taiwan.cncn.com"
    ###################################### 2016-12-17 6:00 - 8:00
    # "http://shijiazhuang.cncn.com",
    # "http://tangshan.cncn.com",
    # "http://qinhuangdao.cncn.com",
    # "http://handan.cncn.com",
    # "http://xingtai.cncn.com",
    # "http://baoding.cncn.com",
    # "http://zhangjiakou.cncn.com",
    # "http://chengde.cncn.com",
    # "http://cangzhou.cncn.com",
    # "http://langfang.cncn.com",
    # "http://hengshui.cncn.com"
    ####################################### 2016-12-17 8:12 - 10:55
    # "http://taiyuan.cncn.com",
    # "http://datong.cncn.com",
    # "http://yangquan.cncn.com",
    # "http://changzhi.cncn.com",
    # "http://jincheng.cncn.com",
    # "http://shuozhou.cncn.com",
    # "http://jinzhong.cncn.com",
    # "http://yuncheng.cncn.com",
    # "http://xinzhou.cncn.com",
    # "http://linfen.cncn.com",
    # "http://lvliang.cncn.com",
    #
    # "http://huhehaote.cncn.com",
    # "http://baotou.cncn.com",
    # "http://wuhai.cncn.com",
    # "http://chifeng.cncn.com",
    # "http://tongliao.cncn.com",
    # "http://ordos.cncn.com",
    # "http://hulunbuir.cncn.com",
    # "http://bayannur.cncn.com",
    # "http://ulanqab.cncn.com",
    # "http://hinggan.cncn.com",
    # "http://xilingol.cncn.com",
    # "http://alashan.cncn.com"
    ################################## 2016-12-17 13:20 - 16:30
    # "http://shenyang.cncn.com",
    # "http://dalian.cncn.com",
    # "http://anshan.cncn.com",
    # "http://fushun.cncn.com",
    # "http://benxi.cncn.com",
    # "http://dandong.cncn.com",
    # "http://jinzhou.cncn.com",
    # "http://yingkou.cncn.com",
    # "http://fuxin.cncn.com",
    # "http://liaoyang.cncn.com",
    # "http://panjin.cncn.com",
    # "http://tieling.cncn.com",
    # "http://chaoyang.cncn.com",
    # "http://huludao.cncn.com",
    #
    # "http://changchun.cncn.com",
    # "http://jilinshi.cncn.com",
    # "http://siping.cncn.com",
    # "http://liaoyuan.cncn.com",
    # "http://tonghua.cncn.com",
    # "http://baishan.cncn.com",
    # "http://songyuan.cncn.com",
    # "http://baicheng.cncn.com",
    # "http://yanbian.cncn.com",
    #
    # "http://harbin.cncn.com",
    # "http://qiqihar.cncn.com",
    # "http://jixi.cncn.com",
    # "http://hegang.cncn.com",
    # "http://shuangyashan.cncn.com",
    # "http://daqing.cncn.com",
    # "http://yichun.cncn.com",
    # "http://jiamusi.cncn.com",
    # "http://qitaihe.cncn.com",
    # "http://mudanjiang.cncn.com",
    # "http://heihe.cncn.com",
    # "http://suihua.cncn.com",
    # "http://daxinganling.cncn.com"
    ######################################### 2016-12-17 16:45 - 2:30
    # "http://nanjing.cncn.com",
    # "http://wuxi.cncn.com",
    # "http://xuzhou.cncn.com",
    # "http://changzhou.cncn.com",
    # "http://suzhou.cncn.com",
    # "http://nantong.cncn.com",
    # "http://lianyungang.cncn.com",
    # "http://huaian.cncn.com",
    # "http://yancheng.cncn.com",
    # "http://yangzhou.cncn.com",
    # "http://zhenjiang.cncn.com",
    # "http://jstaizhou.cncn.com",
    # "http://suqian.cncn.com",
    #
    # "http://hangzhou.cncn.com",
    # "http://ningbo.cncn.com",
    # "http://wenzhou.cncn.com",
    # "http://jiaxing.cncn.com",
    # "http://huzhou.cncn.com",
    # "http://shaoxing.cncn.com",
    # "http://jinhua.cncn.com",
    # "http://quzhou.cncn.com",
    # "http://zhoushan.cncn.com",
    # "http://taizhou.cncn.com",
    # "http://lishui.cncn.com",
    #
    # "http://hefei.cncn.com",
    # "http://wuhu.cncn.com",
    # "http://bengbu.cncn.com",
    # "http://huainan.cncn.com",
    # "http://maanshan.cncn.com",
    # "http://huaibei.cncn.com",
    # "http://tongling.cncn.com",
    # "http://anqing.cncn.com",
    # "http://huangshan.cncn.com",
    # "http://chuzhou.cncn.com",
    # "http://fuyang.cncn.com",
    # "http://ahsuzhou.cncn.com",
    # "http://chaohu.cncn.com",
    # "http://luan.cncn.com",
    # "http://bozhou.cncn.com",
    # "http://chizhou.cncn.com",
    # "http://xuancheng.cncn.com"
    ################################ 2016-12-18 6:10 - 12:56
    # "http://fuzhou.cncn.com",
    # "http://xiamen.cncn.com",
    # "http://putian.cncn.com",
    # "http://sanming.cncn.com",
    # "http://quanzhou.cncn.com",
    # "http://zhangzhou.cncn.com",
    # "http://nanping.cncn.com",
    # "http://longyan.cncn.com",
    # "http://ningde.cncn.com",
    #
    # "http://nanchang.cncn.com",
    # "http://jingdezhen.cncn.com",
    # "http://pingxiang.cncn.com",
    # "http://jiujiang.cncn.com",
    # "http://xinyu.cncn.com",
    # "http://yingtan.cncn.com",
    # "http://ganzhou.cncn.com",
    # "http://jian.cncn.com",
    # "http://jxyichun.cncn.com",
    # "http://jxfuzhou.cncn.com",
    # "http://shangrao.cncn.com",
    #
    # "http://jinan.cncn.com",
    # "http://qingdao.cncn.com",
    # "http://zibo.cncn.com",
    # "http://zaozhuang.cncn.com",
    # "http://dongying.cncn.com",
    # "http://yantai.cncn.com",
    # "http://weifang.cncn.com",
    # "http://jining.cncn.com",
    # "http://taian.cncn.com",
    # "http://weihai.cncn.com",
    # "http://rizhao.cncn.com",
    # "http://laiwu.cncn.com",
    # "http://linyi.cncn.com",
    # "http://dezhou.cncn.com",
    # "http://liaocheng.cncn.com",
    # "http://binzhou.cncn.com",
    # "http://heze.cncn.com"
    ##################################### 2016-12-18 14:45 - 2:18
    # "http://zhengzhou.cncn.com",
    # "http://kaifeng.cncn.com",
    # "http://luoyang.cncn.com",
    # "http://pingdingshan.cncn.com",
    # "http://anyang.cncn.com",
    # "http://hebi.cncn.com",
    # "http://xinxiang.cncn.com",
    # "http://jiaozuo.cncn.com",
    # "http://puyang.cncn.com",
    # "http://xuchang.cncn.com",
    # "http://luohe.cncn.com",
    # "http://sanmenxia.cncn.com",
    # "http://nanyang.cncn.com",
    # "http://shangqiu.cncn.com",
    # "http://xinyang.cncn.com",
    # "http://zhoukou.cncn.com",
    # "http://zhumadian.cncn.com",
    #
    # "http://wuhan.cncn.com",
    # "http://huangshi.cncn.com",
    # "http://shiyan.cncn.com",
    # "http://yichang.cncn.com",
    # "http://xiangfan.cncn.com",
    # "http://ezhou.cncn.com",
    # "http://jingmen.cncn.com",
    # "http://xiaogan.cncn.com",
    # "http://jingzhou.cncn.com",
    # "http://huanggang.cncn.com",
    # "http://xianning.cncn.com",
    # "http://suizhou.cncn.com",
    # "http://enshi.cncn.com",
    #
    # "http://changsha.cncn.com",
    # "http://zhuzhou.cncn.com",
    # "http://xiangtan.cncn.com",
    # "http://hengyang.cncn.com",
    # "http://shaoyang.cncn.com",
    # "http://yueyang.cncn.com",
    # "http://changde.cncn.com",
    # "http://zhangjiajie.cncn.com",
    # "http://yiyang.cncn.com",
    # "http://chenzhou.cncn.com",
    # "http://yongzhou.cncn.com",
    # "http://huaihua.cncn.com",
    # "http://loudi.cncn.com",
    # "http://xiangxi.cncn.com",
    #
    # "http://guangzhou.cncn.com",
    # "http://shaoguan.cncn.com",
    # "http://shenzhen.cncn.com",
    # "http://zhuhai.cncn.com",
    # "http://shantou.cncn.com",
    # "http://foshan.cncn.com",
    # "http://jiangmen.cncn.com",
    # "http://zhanjiang.cncn.com",
    # "http://maoming.cncn.com",
    # "http://zhaoqing.cncn.com",
    # "http://huizhou.cncn.com",
    # "http://meizhou.cncn.com",
    # "http://shanwei.cncn.com",
    # "http://heyuan.cncn.com",
    # "http://yangjiang.cncn.com",
    # "http://qingyuan.cncn.com",
    # "http://dongguan.cncn.com",
    # "http://zhongshan.cncn.com",
    # "http://chaozhou.cncn.com",
    # "http://jieyang.cncn.com",
    # "http://yunfu.cncn.com",
    #
    # "http://nanning.cncn.com",
    # "http://liuzhou.cncn.com",
    # "http://guilin.cncn.com",
    # "http://wuzhou.cncn.com",
    # "http://beihai.cncn.com",
    # "http://fangchenggang.cncn.com",
    # "http://qinzhou.cncn.com",
    # "http://guigang.cncn.com",
    # "http://yulin.cncn.com",
    # "http://baise.cncn.com",
    # "http://hezhou.cncn.com",
    # "http://hechi.cncn.com",
    # "http://laibin.cncn.com",
    # "http://chongzuo.cncn.com",
    #
    # "http://haikou.cncn.com",
    # "http://sanya.cncn.com",
    # "http://sansha.cncn.com"
    ################################## 2016-12-19 10:02 - 17:02
    # "http://chengdu.cncn.com",
    # "http://zigong.cncn.com",
    # "http://panzhihua.cncn.com",
    # "http://luzhou.cncn.com",
    # "http://deyang.cncn.com",
    # "http://mianyang.cncn.com",
    # "http://guangyuan.cncn.com",
    # "http://suining.cncn.com",
    # "http://neijiang.cncn.com",
    # "http://leshan.cncn.com",
    # "http://nanchong.cncn.com",
    # "http://meishan.cncn.com",
    # "http://yibin.cncn.com",
    # "http://guangan.cncn.com",
    # "http://dazhou.cncn.com",
    # "http://yaan.cncn.com",
    # "http://bazhong.cncn.com",
    # "http://ziyang.cncn.com",
    # "http://aba.cncn.com",
    # "http://ganzi.cncn.com",
    # "http://liangshan.cncn.com",
    #
    # "http://guiyang.cncn.com",
    # "http://liupanshui.cncn.com",
    # "http://zunyi.cncn.com",
    # "http://anshun.cncn.com",
    # "http://tongren.cncn.com",
    # "http://qianxinan.cncn.com",
    # "http://bijie.cncn.com",
    # "http://qiandongnan.cncn.com",
    # "http://qiannan.cncn.com"
    ################################# 2016-12-19 20:30 - 23:01
    # "http://kunming.cncn.com",
    # "http://qujing.cncn.com",
    # "http://yuxi.cncn.com",
    # "http://baoshan.cncn.com",
    # "http://zhaotong.cncn.com",
    # "http://lijiang.cncn.com",
    # "http://puer.cncn.com",
    # "http://lincang.cncn.com",
    # "http://chuxiong.cncn.com",
    # "http://honghe.cncn.com",
    # "http://wenshan.cncn.com",
    # "http://xishuangbanna.cncn.com",
    # "http://dali.cncn.com",
    # "http://dehong.cncn.com",
    # "http://nujiang.cncn.com",
    # "http://diqing.cncn.com",
    #
    # "http://lhasa.cncn.com",
    # "http://changdu.cncn.com",
    # "http://shannan.cncn.com",
    # "http://xigaze.cncn.com",
    # "http://nagqu.cncn.com",
    # "http://ngari.cncn.com",
    # "http://nyingchi.cncn.com"
    ################################## 2016-12-20 8:43 - 18:48
    # "http://xian.cncn.com",
    # "http://tongchuan.cncn.com",
    # "http://baoji.cncn.com",
    # "http://xianyang.cncn.com",
    # "http://weinan.cncn.com",
    # "http://yanan.cncn.com",
    # "http://hanzhong.cncn.com",
    # "http://sxyulin.cncn.com",
    # "http://ankang.cncn.com",
    # "http://shangluo.cncn.com",
    #
    # "http://lanzhou.cncn.com",
    # "http://jiayuguan.cncn.com",
    # "http://jinchang.cncn.com",
    # "http://baiyin.cncn.com",
    # "http://tianshui.cncn.com",
    # "http://wuwei.cncn.com",
    # "http://zhangye.cncn.com",
    # "http://pingliang.cncn.com",
    # "http://jiuquan.cncn.com",
    # "http://qingyang.cncn.com",
    # "http://dingxi.cncn.com",
    # "http://longnan.cncn.com",
    # "http://linxia.cncn.com",
    # "http://gannan.cncn.com",
    #
    # "http://xining.cncn.com",
    # "http://haidong.cncn.com",
    # "http://haibei.cncn.com",
    # "http://huangnan.cncn.com",
    # "http://hainanzhou.cncn.com",
    # "http://golog.cncn.com",
    # "http://yushu.cncn.com",
    # "http://haixi.cncn.com",
    #
    # "http://yinchuan.cncn.com",
    # "http://shizuishan.cncn.com",
    # "http://wuzhong.cncn.com",
    # "http://guyuan.cncn.com",
    # "http://zhongwei.cncn.com",
    #
    # "http://urumqi.cncn.com",
    # "http://karamay.cncn.com",
    # "http://tulufan.cncn.com",
    # "http://hami.cncn.com",
    # "http://changji.cncn.com",
    # "http://bortala.cncn.com",
    # "http://bayingolin.cncn.com",
    # "http://akesu.cncn.com",
    # "http://kizilsukirgiz.cncn.com",
    # "http://kashi.cncn.com",
    # "http://hetian.cncn.com",
    # "http://yili.cncn.com",
    # "http://tacheng.cncn.com",
    # "http://altay.cncn.com"
]

_GLB_START_URL_LIST  = [_url + "/jingdian/" for _url in _GLB_CITY_URL_LIST]
# _GLB_START_URL_LIST  = [
#     # "http://hengshui.cncn.com/jingdian/",
#     # "http://tongliao.cncn.com/jingdian/",
#     "http://changchun.cncn.com/jingdian/"
# ]


class CncnCitySpider(scrapy.Spider):

    name = _GLB_SPIDER_NAME
    allowed_domains = _GLB_ALLOWED_DOMAIN
    start_urls = _GLB_START_URL_LIST

    # Level 2
    def parse(self, response):

        print "\n\n######### city response: ", response, response.url
        metadata = {}
        metadata['root_url'] = response.url

        # iterate each search result to see if there is any new for today
        for spot in response.xpath('//div[@class="city_spots"]/div[@class="city_spots_list"]/ul/li'):
            # print "spot: ", spot
            link = spot.xpath('a/@href').extract()
            name = spot.xpath('a/div[@class="title"]/b/text()').extract()
            if len(name) > 0 and len(link) > 0:
                # print "name: %s @ %s" % (name[0].replace(u'\xa0', ' '), link[0])
                yield scrapy.Request(link[0], meta = metadata, callback = self.parse_spot)

        # try to find if there is the next page link in the current search result
        # if yes, try to get the link and invoke this parse to process
        pagelinks = response.xpath('//div[@class="page"]/div[@class="page_con"]/a[@class="num next"]/@href').extract()
        if len(pagelinks) > 0:
            rooturl = response.url[0:response.url.find('jingdian')]
            # print "url: ", rooturl
            nextpageurl = rooturl + "jingdian/" + pagelinks[0].encode('utf-8')
            # print "Next @ ", nextpageurl
            yield scrapy.Request(nextpageurl, callback = self.parse)

    # Level 3
    def parse_spot(self, response):

        print "\n\n######### spot response: ", response

        metadata = response.meta
        names = response.xpath('//div[@class="content mt20"]/div[@class="box_list"]/div[@class="spots_info_con"]/div[@class="spots_info"]/div[@class="type"]/h1/text()').extract()
        stars = response.xpath('//div[@class="content mt20"]/div[@class="box_list"]/div[@class="spots_info_con"]/div[@class="spots_info"]/div[@class="type"]/h1/em/text()').extract()
        if len(names) > 0 and len(stars) > 0:
            metadata[u'景点名称'] = names[0].replace(u'\xa0', ' ')
            metadata[u'景点星级'] = stars[0].replace(u'\xa0', ' ')
            # print meta['name'], meta['star']
        elif len(names) > 0:
            metadata[u'景点名称'] = names[0].replace(u'\xa0', ' ')
            # print meta['name']
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
                # print "%s %s" % (itemkey, itemvalue)
                itemkey = itemkey.replace(u'：', '')
                itemkey = itemkey.replace(u':', '')
                itemkey = itemkey.replace(u' ', '')
                metadata[itemkey] = itemvalue

        # for kk in metadata.keys():
        #     print kk, metadata[kk]

        yield scrapy.Request(response.url + "profile", meta = metadata, callback = self.parse_profile)

    # Level 4
    def parse_profile(self, response):

        print "\n\n######### profile response: ", response
        metadata = response.meta
        # for kk in metadata.keys():
        #     print kk, metadata[kk]

        content = response.xpath('//div[@class="type"]')
        profile = ""

        for detail in content.xpath('.//p//text()').extract():  # .//p//text() 会提取 tag <p> 下面所有的 文本内容，可能是属于 tag <p> 的，也可能是嵌套在 <p> 内部的 <span> 等等
            profile += detail.replace(u'\xa0', ' ')

        metadata[u'详细介绍'] = profile

        # nextpageurl = response.url[0:response.url.find('profile')] + "menpiao"
        # # print "goto @ ", nextpageurl
        # yield scrapy.Request(nextpageurl, callback = self.parse_ticket)
        nextpageurl = response.url[0:response.url.find('profile')] + "jiaotong"
        # print "goto @ ", nextpageurl
        yield scrapy.Request(nextpageurl, meta = metadata, callback = self.parse_traffic)

    # Level 5
    def parse_traffic(self, response):

        print "\n\n######### traffic response: ", response
        metadata = response.meta
        # for kk in metadata.keys():
        #     print kk, metadata[kk]

        traffic = ""
        for ppp in response.xpath('//div[@class="box670"]/div[@class="txt1"]/p'):
            details = ppp.xpath('.//text()').extract()
            if len(details) > 0:
                for detail in details:
                    traffic += detail.replace(u'\xa0', ' ')

        metadata[u'交通信息'] = traffic

        yield scrapy.Request(response.url[0:response.url.find('jiaotong')] + "menpiao", meta = metadata, callback = self.parse_ticket)

    # Level 6
    def parse_ticket(self, response):

        print "\n\n######### ticket response: ", response
        metadata = response.meta
        # for kk in metadata.keys():
        #     print kk, metadata[kk]

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

            itemkey = itemkey.replace(u'：', '')
            itemkey = itemkey.replace(u':', '')
            itemkey = itemkey.replace(u' ', '')
            metadata[itemkey] = itemvalue

        print "########## Here is the final result: #############"

        keyslookupdict = {
            'root_url': 'root_url',
            u'景点名称': 'spot_name',
            u'景点地址': 'spot_addr',
            u'景点类型': 'spot_type',
            u'景点主题': 'spot_theme',
            u'景点星级': 'spot_star',
            u'详细介绍': 'spot_info',
            u'开放时间': 'open_time',
            u'门票分类': 'ticket_type',
            u'门票信息': 'ticket_info',
            u'交通信息': 'traffic_info'
        }

        item = ResortplaceItem()

        for kk in metadata.keys():
            if keyslookupdict.has_key(kk):
                # print kk, ":::", metadata[kk]
                item[keyslookupdict[kk]] = metadata[kk] #.encode('utf-8','ignore')

        yield item
