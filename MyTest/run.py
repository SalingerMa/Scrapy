# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', 'book'])
# execute(['scrapy', 'crawl', 'matplotlib', '--nolog', '-o', 'exporter/matplot.json'])
execute('scrapy crawl matplotlib -o exporter/matplot.json'.split())