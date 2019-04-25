from django.db import models


# Create your models here.

class Feeds(models.Model):
    
    url = models.CharField(max_length=100, verbose_name='图片链接')

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = verbose_name


