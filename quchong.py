import os
import hashlib
import time
import sys


# 搞到文件的MD5
def get_ms5(filename):
    m = hashlib.md5()
    mfile = open(filename, "rb")
    m.update(mfile.read())
    mfile.close()
    md5_value = m.hexdigest()
    return md5_value


# 搞到文件的列表
def get_urllist():
    base = ("G:\BaiduNetdiskDownload\\")  # 这里就是你要清缴的文件们了
    list = os.listdir(base)
    urllist = []
    for i in list:
        url = base + i
        urllist.append(url)

    return urllist


# 主函数
if __name__ == '__main__':
    md5list = []
    urllist = get_urllist()
    print("test1")
    for a in urllist:
        md5 = get_ms5(a)
        if (md5 in md5list):
            os.remove(a)
            print("重复：%s" % a)
        else:
            md5list.append(md5)
            print("一共%s张照片" % len(md5list))