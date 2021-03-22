import re
import requests
import os
import urllib.request
import time
# url="http://book.sciencereading.cn/shop/main/Login/shopFrame.do"
# 方案1 抓取网络内容
# url="http://book.sciencereading.cn/shop/book/Booksimple/list.do?showQueryModel.bookGroupName=%E7%8E%AF%E5%A2%83%E5%AD%A6%E7%B3%BB%E5%88%97%E4%B8%9B%E4%B9%A6"
# response = urllib.request.urlopen(url)
# response =  response.read().decode("utf-8")
# 方案2 另存为包含重要信息的本地文件
filedir = "1.html"
myflie = open(filedir,encoding='utf-8')
response = str(myflie.read())

# response  = requests.get(url)

# response = str(response.content)
print(response)
pat1 = "\?id=B[\w\d]+\"+\s+target=\"_blank\"+\s+class=\"hightlight\"\>\<b+\s+class=\"kc_title keyContent\"\>+[\u4e00-\u9fa5]+"      #获得ID和Title的正则表达式
# pat2 = "show.do\?id=B[\w\s]+\"\s target=\"_blank\" class=\"hightlight\"\>\<b\s class=\"kc_title keyContent\"\>[\u4e00-\u9fa5\S]\<\/b"
str = re.compile(pat1).findall(response)    #从获得的HTMl页面中进去选取所需的ID和Title
# str2 = re.compile(pat2).findall(response)
print(str)
# print(str2)
str = list(set(str))                #进行数组的去重操作
mylen = len(str)        #获取数组长度，接就是图书的数量，后面用作循环的次数
id = []     #声明一个数组，方便提取到ID
title = []
for index in range(0,mylen):         #(1,mylen) 分别是开始位置和循环次数的参数
    page = 1                        #每一本书的开始页码
    mystr = str[index]              #利用指针，获取本次循环出来的ID截取内容
    #id = re.sub("\?id=B","B",mystr) #获取只需要的id
    id = mystr[4:40]
    pat2 = "[\u4e00-\u9fa5]+"

    title= re.compile(pat2).findall(mystr)
    # title = re.sub("", "", title)
    title = title[0]
    deldir = "N:\Python\Project\\"
    mydir3 = deldir + title
    mydir = os.mkdir(mydir3)
    print(mydir)
    # print(id)
    # print(title)
    myurl = "http://159.226.29.160/knReader/request/TebReadHandler.ashx?b=url&p=&page="
    myurl = re.sub("url",id,myurl)
    headers = {
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    while (page<600):
        download = myurl +"%d"%page
        print(download)
        r = requests.get(download,headers=headers,timeout= 800)
        name = mydir3+"/"+"%d"%page+".gif"
        print(name)
        with open(name,"wb") as f:
            f.write(r.content)
            f.close()
        page = page+1
    time.sleep(60)
    deldir = "N:\Python\Project\\"
    mydir1 = deldir +title
    print(mydir1)
    os.chdir(mydir1)
    cwd = os.getcwd()
    print('----这是分割线------')
    def deleteNullFile():
        # '''删除所有大小为0的文件'''
        files = os.listdir(os.getcwd())
        for file in files:
            if os.path.getsize(file) == 0:  # 获取文件大小
                os.remove(file)
                print(file + " deleted.")
        return


    while True:
        deleteNullFile()
        break
    else:
        print("没有可以删除的了")

