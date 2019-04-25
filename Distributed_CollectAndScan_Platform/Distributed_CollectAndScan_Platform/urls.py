"""Distributed_CollectAndScan_Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Scan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'indexs', views.indexs),
    url(r'domains', views.domains),
    url(r'ips_scan', views.ips_scan),
    url(r'all_scan', views.all_scan),
    url(r'map', views.map),
    url(r'error', views.error),
    url(r'test_api', views.test_api),
    url(r'collect_urls', views.collect_urls),
    url(r'get_city_from_domain', views.get_city_from_domain),
    url(r'redis_caches',views.redis_caches),
    url(r'cache_test',views.cache_test),
    url(r'cache_html',views.cache_html),
    url(r'Scan_Vuln',views.Scan_Vuln),
]
