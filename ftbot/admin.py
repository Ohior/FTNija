#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-06-27 15:00:49
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-28 15:31:59
#  \\           //
#   \\         //
#

from django.contrib import admin
from .models import DictModel, Dicty, KeyVal

# Register your models here.
# Register your models here.
admin.site.register(Dicty)
admin.site.register(KeyVal)
admin.site.register(DictModel)