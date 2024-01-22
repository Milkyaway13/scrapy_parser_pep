import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        tr_tags = response.css('section[id=numerical-index] tbody tr')
        links = tr_tags.css('a[href^="pep"]')
        for pep_link in links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css(
            'h1.page-title::text').get().split(' – ')
        num = pep_title[0].split(' ')[1]
        name = pep_title[1]
        data = {
            'number': int(num),
            'name': name,
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
