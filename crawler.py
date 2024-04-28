from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

Class HorseSpider(CrawlSpider):

    name = "whirlaway"

    allowed_domains = ['treehouse-projects.github.io']

    start_urls = ['https://treehouse-projects.github.io/horse-land/index.html']

    rules = [Rule(LinkExtractor(allow=r'.*'),
                callback='parse_horses',
                follow=True)]

    def parse_horses(self, response):
        url = response.url
        title = response.css('title::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))