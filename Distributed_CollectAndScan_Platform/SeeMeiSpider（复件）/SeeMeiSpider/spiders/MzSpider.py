from scrapy.spiders import CrawlSpider
from SeeMeiSpider.items import SeemeispiderItem


class MzSpider(CrawlSpider):
    name = 'spider'
    start_urls = ['http://www.lolmz.com/hot.php']

    def parse(self, response):
        img_list = response.xpath('//div[@class="chroma-gallery mygallery"]//img')
        for img in img_list:
            title = img.xpath('@alt').extract_first()
            img_url = img.xpath('@src').extract_first()
            item = SeemeispiderItem()
            item['title'] = title
            item['image_url'] = img_url
            yield item

