import scrapy
from ..items import QuotetutItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items=QuotetutItem()

        all_div_quotes=response.css('div.quote')

        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()

            items['title']=title
            items['author'] = author
            items['tags'] = tags

            yield items




