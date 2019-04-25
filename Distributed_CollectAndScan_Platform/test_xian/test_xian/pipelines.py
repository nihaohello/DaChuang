class XianPipeline(object):
    def process_item(self, item, spider):
        temp_news = "%s\n%s\n\n"%(item['title'],item['url'])
        f = open('荣耀西安网帖子5.txt','a+',encoding="utf-8")  #a+表示追加内容
        f.write(temp_news)
        f.close()
        #return item