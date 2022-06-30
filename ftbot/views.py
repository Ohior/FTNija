#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-06-27 15:00:49
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-30 02:06:15
#  \\           //
#   \\         //
#

from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from django.conf import settings
from .models import DictModel, KeyVal


# Create your views here.
# web_url = 'https://trade.mql5.com/trade?servers='
web_url2 = 'https://tradingeconomics.com/currencies/'
staticPath = settings.STATICFILES_DIRS

def indexPage(request):
    key_val = {}
    try:
        # get all data from database
        key_val = DictModel.objects.get()
    except DoesNotExist as dne:
        key_val = {}
        print(dne)
    return render(request, 'index.html', {'context':key_val.json})

def lunchBot(request):
    # scrap the website and get the data
    context = openDestination(web_url2)
    try:
        # delete all data from database
        DictModel.objects.all().delete()
    except AttributeError as ae:
        print(ae)
    # add context data to database
    dm = DictModel.objects.create(key="context", json=context)
    return render(request, 'temp.html', {"context": context})

def openDestination(url):
    context = {}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    result = requests.get(web_url2, headers=headers)
    soup = BeautifulSoup(result.content, 'html.parser')
    tablerows = soup.find_all("tr", {"class": "datatable-row"})
    for tablerow in tablerows:
        row = clean_table_row(tablerow)
        context.update({row[0]: row})
    return context

def clean_table_row(row):
    return row.text.replace("\t", "").replace("\r", "").replace("\n", "").split()
    

