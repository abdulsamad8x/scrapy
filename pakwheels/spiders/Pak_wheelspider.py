import scrapy

class ExampleSpider(scrapy.Spider):
    name = "pakwheels"
    start_urls = ['https://www.pakwheels.com/']

    def parse(self, response):
        title = response.css('div.col-md-6.line.or li::text').getall()
        title2 = response.css('div.col-md-6 li::text').getall()
        
        yield {
            'title': title,
            'title2' : title2
        }
