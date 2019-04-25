from scrapy_djangoitem import DjangoItem
from index.models import Feeds


class SeemeispiderItem(DjangoItem):
    django_model = Feeds

