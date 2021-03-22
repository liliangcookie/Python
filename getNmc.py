import re
import requests
import os
import time
import urllib.request
from bs4 import BeautifulSoup
from builtins import str
# http://www.nmc.cn/publish/observations/china/dm/weatherchart-h000.htm
#<div class="col-xs-12 time actived" data-fffmm="000" data-img="http://image.nmc.cn/product/2020/09/16/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_20200916060000000.png?v=1600240483439" data-index="0" data-time="09/16 14:00">
mynum = 1
def getweather():
    url="http://www.nmc.cn/publish/observations/china/dm/weatherchart-h000.htm"
    response = urllib.request.urlopen(url)
    response =  response.read().decode("utf-8")
    myhtml = BeautifulSoup(response,"html.parser")
    img = myhtml.find_all('div',class_='col-xs-12 time actived')
    pat1 = "http://+\S+png"
    str1 = re.compile(pat1).findall(str(img[0]))
   # print(str)
    name = str1[0][79:87]
   # print(name)
   # print(str1[0])
   # f = "../nmc/"+name+".jpg"
    f = name + ".jpg"
    r = requests.get(str1[0])
    with open(f,"wb") as file:
        file.write(r.content)
        file.close
    pass
    print(mynum+1)
    time.sleep(1)

pass
getweather()