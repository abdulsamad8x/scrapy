import scrapy

class ExampleSpider(scrapy.Spider):
    name = "pakwheels"
    start_urls = ['https://www.pakwheels.com/']

    def parse(self, response):
        title = response.css('div.col-md-6.line.or li::text').getall()
        
        yield {
            'title': title,
        }
