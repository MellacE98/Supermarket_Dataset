from crawlers.spiders.quotes_spider import QuotesSpiderSpider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(QuotesSpiderSpider)
process.start()
