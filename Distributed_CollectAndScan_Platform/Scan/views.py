#coding=utf-8
from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
import socket
from django.views.decorators.cache import cache_page
import requests
import json
from Scan.common import test
from Scan.collect.collect_urls import crawl
from Scan.Scan.Scan import Scan

# Create your views here.
def indexs(request):
    return render(request,'indexs.html')
def domains(request):
    return render(request,'domains.html')
def ips_scan(request):
    return render(request,'ips_scan.html')
def all_scan(request):
    return render(request,'all_scan.html')
def map(request):
    return render(request,'map.html')
def error(request):
    return render(request,'404.html')

#collect url函数
def collect_urls(request):
    if request.is_ajax() and request.method == 'GET':
        url=request.GET.get("url")
        #crawl(url).run()
    return HttpResponse("aaa")

#由网址得到城市名的函数
def get_city_from_domain(request):
    url=request.GET.get("url").lstrip("http://").lstrip("https://")
    ip = socket.gethostbyname(url)
    url = "http://ip.taobao.com/service/getIpInfo.php?ip=" + ip
    s = requests.get(url=url)
    print(s.text)
    city = json.loads(s.text)["data"]["city"]
    return HttpResponse(city)

#调试api函数
def test_api(request):
    if request.is_ajax() and request.method == 'GET':
        data=[]
        for key in request.GET:
            valuelist = request.GET.getlist(key)
            data.append(valuelist)
        print(data[0])
        #print(request.body)
        return HttpResponse("aaa")
        #return  render(request, "indexs.html", {"data":data[0]})


#cache的测试函数
def cache_test(request):
    if request.GET.get("url"):
        get_url=request.GET.get("url")
        print(get_url)
    if cache.has_key("url"):
        return HttpResponse(cache.get("url"))
    else:
        cache.set("url",get_url)
#cache html
def cache_html(request):
    return render(request,"cache_html.html")

#redis缓存的三个函数
def redis_caches():
    def _deco(func):
        def __deco(*args, **kwargs):
            obj, request = args
            if request.method == 'GET':  # 如果请求是已Get方式请求的，则调用get方式的方法
                data = request.GET.dict()
            elif request.method == 'POST':  # 如果是post则调用这个方式
                data = request.POST.dict()

            class_name = obj.__class__.__name__
            cache = read_from_cache()
            if cache:
                print('%s to  cache' % class_name)
                result = cache
            else:
                print('%s to  view' % class_name)
                result = obj.process(data, request)
                print('func  return  ', result)
                write_to_cache('test1_public', result)
            return HttpResponse(result)

        return __deco

    return _deco

# read cache user id
def read_from_cache(user_name='public'):
    """
    读取缓存
    :param user_name:
    :return:
    """
    key = 'test1_'+user_name
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return data


def write_to_cache(key, value):
    """
    写入缓存
    :param value:
    :param user_name:
    :return:
    """
    cache.set(key, json.dumps(value), settings.REDIS_TIMEOUT)


#Scan_Vuln
def Scan_Vuln(request):
    #return HttpResponse("aaaaaa")
    if request.GET.get("url"):
        url=request.GET.get("url")
        a=Scan(url)
        a.run()
    return HttpResponse("aaaa")
