from datetime import datetime

from django.db import models

# Create your models here.


# 废品种类
class Scrap(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='废品名称')
    price = models.FloatField(null=False, blank=False, verbose_name='废品单价')
    delete = models.IntegerField(choices=((0, '未删除'), (1, '已删除')), default=0, verbose_name='是否删除')
    time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '废品种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
