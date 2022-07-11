import scrapy
import read_write as rw

class MercadonaSpider(scrapy.Spider):
    name = 'mercadona'
    
    def start_requests(self, keys):
        url = keys['mercadona']['site']
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        filename = 'mercadona.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

keys = rw.load_credentials()
prueba = MercadonaSpider()
prueba.start_requests(keys)