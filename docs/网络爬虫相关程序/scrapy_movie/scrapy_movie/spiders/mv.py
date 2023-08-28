import scrapy
from scrapy_movie.items import ScrapyMovieItem


class MvSpider(scrapy.Spider):
    name = "mv"
    # allowed_domains是允许范围的路径
    allowed_domains = ["dytt8.net"]
    start_urls = ["https://dytt8.net/html/gndy/china/index.html"]

    def parse(self, response):
        #       要第一个名字 和 第二页的图片
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            # 获取第一页的name 和 要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # 第二页的地址是
            url = 'http://www.dytt8.net' + href

            # 对第二页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        # 注意 如果拿不到数据的情况下  一定要查你的xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # 接受到请求的那个meta参数的值
        name = response.meta['name']

        movie = ScrapyMovieItem(src=src, name=name)

        yield movie
