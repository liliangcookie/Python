import os
import re
import requests
import urllib.request
import time

newurl = 'http://159.226.29.160/knReader/request/TebReadHandler.ashx?b=BC6F90A78F76640639CF40EF81A06554C000&p=&page=147'
c = requests.get(newurl).status_code
c = requests.get(newurl).encoding
print(c)

# if f !=null:
# f = requests.get(url).status_code
# print(f)
def isurl(url):
    c = requests.get(url).status_code
    return c
pass

def geturl(url):
    # url  = str(url)
    if isurl(url)==200:
     response = urllib.request.urlopen(url)
     response =  response.read().decode("utf-8")
     pat1 = 'href=[\'\"]+[^\s]+html'
     str = re.compile(pat1).findall(response)
     i=0
     while i<= len(str):
        u = str[i][6:]
        newurl = "http://sdfuen.com/"+u
        newurl = 'http://159.226.29.160/knReader/request/TebReadHandler.ashx?b=BC6F90A78F76640639CF40EF81A06554C000&p=&page=1147'
        c = requests.get(newurl).status_code
        print(newurl)
        i += 1
        if c == 200:
         print('--page is get---')
         # geturl(newurl)
        elif c == 404:
         print('--page is lost---')
         break
        else:
         continue
        # geturl(newurl)
pass

murl = "http://www.fuenchina.com/news1.html"
geturl(murl)

# print(requests.codes("http://www.fuenchina.com/news1.html"))
#
# def getall(url):
#  url = str(url)
#  response = urllib.request.urlopen(url)
#  response =  response.read().decode("utf-8")
# # print(response)
#  pat1 = 'href=[\'\"]+[^\s]+html'
# # pat2 = 'src=\"+[^\s]+'
#  str = re.compile(pat1).findall(response)
# # print(str)
#  i= 0
#  while i < len(str):
#     text  = str[i][6:]
#     newurl =  "http://sdfuen.com/"+text
#     with requests.urlopen(newurl) as f:
#      print(f.status)
#      print(newurl)

#     i +=1
# getall('http://www.fuenchina.com/news1.html')