import scrapy
from ..items import MytutItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls  = ['http://quotes.toscrape.com']

    def parse(self,response):
        items = MytutItem()

        all_div_quotes = response.css("div.quote")

        for qt in all_div_quotes :

            title = qt.css("span.text::text").extract()
            author = qt.css(".author::text").extract()
            tag = qt.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] =tag

            yield items
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
             yield response.follow(next_page_url,callback=self.parse)
