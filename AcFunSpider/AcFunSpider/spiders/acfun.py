import scrapy


class AcfunSpider(scrapy.Spider):
    name = 'acfun'
    allowed_domains = ['acfun.cn']
    start_urls = ['http://www.acfun.cn/u/21616835']

    def parse(self, response):
        pass
