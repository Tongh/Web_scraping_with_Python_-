from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from wikiSpider.items import Article


class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page"]
    rules = [Rule(SgmlLinkExtractor(allow = ('(/wiki/)((?!:).)*$'), ), callback = "parse_item", follow = True)]

    def parse_item(self, respnse):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is : " + title)
        item['title'] = title
        return item

    """
    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is : " + title)
        item['title'] = title
        return item
    """
