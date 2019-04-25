from django.db import models

# Create your models here.
class Recruit(models.Model):

    resource = models.CharField('信息来源', max_length=255)
    url = models.URLField('信息链接', default='')
    # ...

class Firm(models.Model):
    # 公司相关信息
    firm_introduction = models.TextField('公司简介')
    # ...
