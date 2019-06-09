# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import ItcastItem

import sys


class Opp2Spider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["deviant.com"]
    start_urls = ['http://www.deviantart/otherchannel/disney.shtml']

    def parse(self, response):
         
        # 存放老师信息的集合
        items = []
        
        for each in response.xpath("//div[@class='li_txt']"):
            #将我们得到的数据封装到目标文件items.py中的ItcastItem类中
            item = ItcastItem()
            
            # extract()函数 返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()
            
            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            
            items.append(item)
            
        return items
