import re
import os
import requests
import urllib.request

for index in range(1,9):
    url = "http://sdshiyan.jinan.cn/col/col1634/index.html?uid=3512&pageNum="
    url = url + str(index)
    print(url)

    response = urllib.request.urlopen(url)
    response = response.read().decode("utf-8")
    print(response)
    # response = requests.get(url)
    # response = str(response.content)
    # print(response)

    # pat1 = "208px\;\" src=\"[\w\d\s]+\"\>+\s+\<div class=\"caption\"\>+\s+\<h5\>+[\u4e00-\u9fa5]+"
    #<img style="width:190px;height:208px;" src="/picture/0/beeff0c198e64c809939a501d198e9ef.jpg" >            <div class="caption">                <h5>关锋　</h5>            </div>        </a>    </li>	]]></record>
    #\s+<div+\s+class=\"caption\"+\s+\<h5\>+[\u4e00-\u9fa5]+
    pat1 = "208px\;\"+\s+src=\"[\w\d\S]+\s+\>+\s+\<div+\s+class=\"caption\"+\>+\s+\<h5\>+[\u4e00-\u9fa5]+"
    str1 = re.compile(pat1).findall(response)
    # print(str1)
    str1 = list(set(str1))
    # print(str1)
    mylen = len(str1)
    title = []
    for index1 in range(0,mylen):
        mystr = str1[index1]
        # print(mystr)
        pat2 = "[\u4e00-\u9fa5]+"
        title = re.compile(pat2).findall(mystr)
        print(title)


    # picurl = "http://sdshiyan.jinan.cn/picture/0/8b2c06d860a94950883a1304a17da949.jpg"
