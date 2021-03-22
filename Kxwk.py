import os
import re
import requests
import urllib
# http://book.sciencereading.cn/shop/book/Booksimple/list.do
# showQueryModel.bookclcId:
# showQueryModel.dp1Value:7dee8d8a889211e7a2df00163e2ed6f9 地球科学
# 75e48243889111e7a2df00163e2ed6f9 数理
# 57ed86a0889211e7a2df00163e2ed6f9 材料化学
# 6a4dcb6a889211e7a2df00163e2ed6f9 生命
# 8ab2fb16889211e7a2df00163e2ed6f9 资源环境
# 99603fad889211e7a2df00163e2ed6f9 农林
# a95a1a87889211e7a2df00163e2ed6f9 医药
# c57f833d889211e7a2df00163e2ed6f9 信息
# d97783da889211e7a2df00163e2ed6f9 工程
# e689625e889211e7a2df00163e2ed6f9 管理
# 1208204e889311e7a2df00163e2ed6f9 教育传播

# showQueryModel.dp1Name:
# showQueryModel.dp2Value:
# showQueryModel.dp2Name:
# showQueryModel.dp3Value:'170' 地球科学 420 测绘科学技术 html xueke ="210" 农学
# showQueryModel.dp3Name: 学科名字
# showQueryModel.nameIsbnAuthor: 自然地理
# showQueryModel.keywords1:作者
# showQueryModel.keywords2:名称
# showQueryModel.keywords3:ISBN
# showQueryModel.keywords4:简介
# showQueryModel.pattern2:
# showQueryModel.pattern3:
# showQueryModel.pattern4:
# showQueryModel.keycolumns1:
# showQueryModel.keycolumns2:
# showQueryModel.keycolumns3:
# showQueryModel.keycolumns4:
# showQueryModel.bookType:'专著' 教育-大学 科普 参考工具书 教育-职业 图集   报告  大众-科普 大众 大众-通俗
# showQueryModel.publishYear:'2018'
# showQueryModel.bookGroupName:地球信息科学基础丛书 厦门大学新世纪教材大系
# showQueryModel.nameIsbnAuthor2:结果中搜索
# showQueryModel.readPermission: 0所有 1有权限
# showQueryModel.bookOrderColumn: -1  booksimple.publishDate desc 出版日期降序 booksimple.publishDate 出版日期升序 booksimple.name 升序 booksimple.author 作者升序
# pageSplit.nowPageNumber: 2
# pageSplit.showRow: 10
# showQueryModel.keywords1: 自然地理
# 结构化数据提取
from bs4 import BeautifulSoup
# keyword = ''
url = 'http://book.sciencereading.cn/shop/book/Booksimple/list.do?showQueryModel.nameIsbnAuthor=%E5%9C%B0%E8%B4%A8%E5%AD%A6&pageSplit.nowPageNumber=1&pageSplit.showRow=10'
# url = 'https://mp.weixin.qq.com/s/qNRC0wtXzbw7aW5Tj7_Ijw'
response = urllib.request.urlopen(url)
response =  response.read().decode("utf-8")
# soup = BeautifulSoup(response)
soup = BeautifulSoup(response)
# print(response)
soup = soup.text
soup = BeautifulSoup(soup)
print(soup)