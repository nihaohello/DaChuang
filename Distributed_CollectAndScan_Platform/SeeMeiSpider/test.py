import requests
 
url = 'http://localhost:6800/schedule.json'
data = {'project':'SeeMeiSpider', 'spider':'spider'}
 
print(requests.post(url=url,data=data))
