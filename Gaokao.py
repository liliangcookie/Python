import os
from bs4 import BeautifulSoup
from goose3 import Goose
from goose3.text import StopWordsChinese

# dir = "N:\gk\\"
# files = os.listdir(dir)
# for file in files:  # 这里得到的是文件名
#     filedir = os.path.join(dir, file)
#     print(filedir)
#     myflie = open(filedir,mode='rb+')
#     f= myflie.read().decode("utf-8")
#     response = str(f)
#     # print(response)
#     soup = BeautifulSoup(response,'html.parser')
    url = 'https://mp.weixin.qq.com/s/RfN_bWh3Cw-KS3bGCGe7Ew'
    g = Goose({'stopwords_class': StopWordsChinese})
    text = g.extract(url=url)
    print (text.cleaned_text[:150])




    # print(soup)
    # myflie.close()
    # break
    # # continue

