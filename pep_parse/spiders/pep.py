import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAINS]
    start_urls = [f'https://{ALLOWED_DOMAINS}/']

    def parse(self, response):
        links = response.css(
            'section[id=numerical-index] tbody tr a[href^="pep"]'
        )
        for pep_link in links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css(
            'h1.page-title::text'
        ).get().split(' – ')
        num = pep_title[0].split(' ')[1]
        name = pep_title[1]
        data = {
            'number': int(num),
            'name': name,
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
