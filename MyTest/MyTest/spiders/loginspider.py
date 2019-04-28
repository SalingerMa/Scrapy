# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

class LoginspiderSpider(scrapy.Spider):
    name = 'loginspider'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/profile?_next=/places/default/index']
    login_url = 'http://example.webscraping.com/places/default/user/login'

    def parse(self, response):
        keys = response.css('table label::text').re('(.*?):')
        values = response.css('table td.w2p_fw::text').extract()
        print(keys, values)

        yield dict(zip(keys, values))

        # login

    def start_requests(self):
        yield Request(self.login_url, callback=self.login)

    def login(self, response):
        fd = {'email': 'ms@a.com', 'password': '123456'}
        yield FormRequest.from_response(response, formdata=fd, callback=self.parse_login)

    def parse_login(self, response):
        if 'Welcome Sai' in response.text:
            yield from super().start_requests()

