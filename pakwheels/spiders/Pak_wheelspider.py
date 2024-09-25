import scrapy

class ExampleSpider(scrapy.Spider):
    name = "pakwheels"
    start_urls = ['https://www.pakwheels.com/']

    def parse(self, response):
        title = response.css('h1::text').getall()
        
        yield {
            'title': title,
        }
