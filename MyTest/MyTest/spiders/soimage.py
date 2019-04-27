# -*- coding: utf-8 -*-
import scrapy
import json

class SoimageSpider(scrapy.Spider):
    name = 'soimage'
    allowed_domains = ['image.so.com']
    base_url = 'http://image.so.com/zj?ch=beauty&sn={index}&listtype=new&temp=1'
    start_urls = [base_url.format(index=0)]
    start_index = 0
    MAX_DOWNLOAD_NUM = 10


    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index:
            yield scrapy.Request(self.base_url.format(index=self.start_index))
