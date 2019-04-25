import scrapy
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.http import Request

class XianSpider(scrapy.Spider):
    name = 'xian'
    allowed_domains = ['ixian.cn']
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    start_urls = ['https://www.ixian.cn/forum-13-1.html']

    url_set = set()
    def parse(self, response):

        #获取荣耀西安论坛城市发展板块所有文章内容及url
        hxs1 = Selector(response).xpath("//div[@class='busforumlist_item_title']/a")
        #print(hxs)
        for item in hxs1:
            #print(item.xpath(".//@href"))
            title = item.xpath(".//text()").extract_first()
            url = item.xpath(".//@href").extract_first()
            #print(title,url)
            from test_xian.items import XianItem
            obj = XianItem(title=title,url=url) #这里参数一定要加上参数名
            yield obj


        #获取所有页码url  分页url
        hxs2 = Selector(response).xpath("//div[@class='pg']/a[re:test(@href,'https://www.ixian.cn/forum-13-\d+.html')]/@href").extract()
        for url in hxs2:
            if url in self.url_set:
                #print("url已收集,重复数据 %s"%url)
                pass
            else:
                self.url_set.add(url)
                print("新增一条url: %s"%url)
                #将新url加入到调度器，进行新的url递归访问并解析
                yield  Request(url=url,callback=self.parse)