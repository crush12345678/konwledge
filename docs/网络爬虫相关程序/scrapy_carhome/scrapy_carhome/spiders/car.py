import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    #注意如果你的请求的接口是html为结尾的  那么是不需要加/的
    start_urls = ["https://car.autohome.com.cn/price/list-0-0-0-0-0-0-0-0-15-0-0-0-0-0-0-1.html"]

    def parse(self, response):
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//div[@class="main-lever"]//span/span/text()')
        print('==================================================')

        for i in range(len(name_list)):
            name=name_list[i].extract()
            price=price_list[i].extract()
            print(name,price)