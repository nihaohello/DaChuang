import requests
requrl = "http://localhost:6800/listjobs.json?project=SeeMeiSpider"
print(requests.get(requrl).text)
