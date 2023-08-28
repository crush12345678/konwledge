import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook.items import ScrapyReadbookItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1188_1.html"]

    rules = (Rule(LinkExtractor(allow=r"/book/1188_\d+\.html"),  # allow后面是正则 \.是防止点转译
                  callback="parse_item",
                  follow=True),)
    #注意事项
    #【1】callback只能写函数名字符串，callback="parse_item"
    #【2】在基本的spider中，如果重新发送请求，那里的callback写的是  callback=self.parse_item
    #[注——稍后看]follow-ture 是否跟进 就是按照提取链接规则进行提取

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            name = img.xpath('./@data-original').extract_first()
            src = img.xpath('./@alt').extract_first()

            book = ScrapyReadbookItem(name=name, src=src)
            yield book
