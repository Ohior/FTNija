#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-06-27 15:00:49
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-29 20:42:38
#  \\           //
#   \\         //
#

from jsonfield import JSONField
from django.db import models

# Create your models here.

class DictModel(models.Model):
    key  = models.CharField(max_length=200)
    json = JSONField()

    def __str__(self):
        return self.key

class Dicty(models.Model):
    name      = models.CharField(max_length=70)
    def __str__(self):
        return self.name

class KeyVal(models.Model):
    container = models.ForeignKey(Dicty,on_delete=models.CASCADE, db_index=True)
    key       = models.CharField(max_length=200, db_index=True)
    value     = models.CharField(max_length=200, db_index=True)
    def __str__(self):
        return self.containerFF