# -*- coding: utf-8 -*-
import scrapy
from ..items import QuotetutItem

class AmazonDealsSpider(scrapy.Spider):
    name = 'amazon_deals'
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1559357420&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0']

    def parse(self, response):

        items =QuotetutItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author=response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price:nth-child(1) .a-price-fraction , .a-spacing-top-small .a-price:nth-child(1) .a-price-whole::text').css('::text').extract()
        product_image = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_image'] = product_image


        yield items
