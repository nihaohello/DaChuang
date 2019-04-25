from scrapy.spiders import CrawlSpider
from SeeMeiSpider.items import SeemeispiderItem
import re
import requests
from urllib.parse import urlparse
from urllib import parse
import sys
import os
import vthread
import random
import threading
import time

class MzSpider(CrawlSpider):
    name = 'test1'
    start_urls = ['http://www.qq.com']
    #self.url=t=start_urls[0]
    def __init__(self):
        start_urls = ['http://www.qq.com']
        self.crawl(start_urls[0],0)

    def crawl(self,url,num):
        start_urls = ['http://www.qq.com']
        self.Is_url = self.deal_url(start_urls[0])[1]
        temp_urls = self.deal_url(start_urls[0])
        try:
            temp_url = temp_urls[0] + "://" + temp_urls[1]
        except Exception:
            pass
        #img_list = response.xpath('/html/body/div[1]/div[3]/div/ul/li[4]/a')
        response=requests.get(url=url)
        s=response
        try:
                urls1 = re.findall('href=".*?"', s.text)
                urls2 = re.findall("href=\'.*?\'", s.text)
                urls3 = re.findall('src=".*?"', s.text)
                urls4 = re.findall("src=\'.*?\'", s.text)
                # urls=re.findall('.*?'+self.Is_url+".*?",s.text)
                urls = urls1 + urls2 + urls3 + urls4
                urls = list(set(urls))
                if urls:
                    print(len(urls))
                    for i in urls:
                        if self.Is_url in i:
                            i = self.deal_href_src(i)
                            if "http" not in i:
                                i = "http://" + i
                        #print(i)
                        if self.Is_url not in i:
                            i = self.deal_href_src(i)
                            if "http" not in i:
                                i = temp_url + "/" + i
                        if "javascript" not in i and "JavaScript" not in i:
                            if ((not i.endswith(".png")) and (not i.endswith("jpg")) and \
                                    (not i.endswith("gif")) and (".css" not in i) and ((".js" not in i) or \
                                                                                       (".json" in i)) and (
                                            ".ico" not in i) and "/css/" not in i and "/js/" \
                                    not in i and \
                                    "jpeg" not in i and ".svg" not in i and "ä" not in i):
                                        #print(i)
                                        item = SeemeispiderItem()
                                        item['url'] = i
                                        #yield Request.requests(i,callback=self.parse(num))
                                        yield item
                #time.sleep(10)       
        except:
            pass
    def deal_url(self, url):
        return urlparse(url)

    def deal_href_src(self, i):
        i = parse.unquote(i)
        if "href=" in i:
            i = i.rstrip("\"").lstrip('href=')
            i = i.rstrip("\'").lstrip('href=')
            i = i.strip("\"")
            i = i.rstrip("/")
        if "src" in i:
            i = i.lstrip("src=").rstrip("\"")
            i = i.lstrip("\"")
            i = i.rstrip("/")
        i = i.replace("'", "")
        i = i.strip(".").strip("/")
        return i

                                #self.crawl(i, num)
            
        '''
        for img in img_list:
            title = 'test'
            img_url = img.xpath('@href').extract_first()
            item = SeemeispiderItem()
            item['title'] = title
            item['image_url'] = img_url
            yield item
        '''
