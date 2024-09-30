import scrapy

class ExampleSpider(scrapy.Spider):
    name = "pakwheels"
    start_urls = ['https://www.pakwheels.com/']

    def parse(self, response):
        title = response.css('div.col-md-6.line.or li::text').getall()
        title2 = response.css('div.col-md-6 li::text').getall()
        title3 = response.css('div.col-md-6.mb20 a::attr(href)')[1].getall()
        
        yield {
            'title': title,
            'title2': title2,
            'title3': title3,
        }
