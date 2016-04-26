# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100) #文章标题
    date = models.DateTimeField(auto_now_add=True) #文章创建时间
    category = models.CharField(max_length = 50, blank = True)  #文章分类
    content = models.TextField(blank = True, null = True)  #博客文章正文





    #python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date']
# Create your models here.
