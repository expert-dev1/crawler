import scrapy

class Myspider(scrapy.Spider):
    name = 'tommy'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        all_divs = response.css('div.quote')

        for quotes in all_divs:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()

            yield {
                'tile': title,
                'author': author,
                'tags': tags
            }

        next_button = response.css('li.next a::attr(href)').get()

        if next_button is not None:
            yield response.follow(next_button, callback=self.parse)