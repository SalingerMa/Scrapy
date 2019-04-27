# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MatplotlibItem


class MatplotlibSpider(scrapy.Spider):
    name = 'matplotlib'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/']

    def parse(self, response):
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound li.toctree-l2')
        links = le.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse_example)

    def parse_example(self, response):
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        matplot = MatplotlibItem()
        matplot['file_urls'] = [url]
        return matplot