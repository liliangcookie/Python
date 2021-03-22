import urllib.parse
import os
def check_file(file_path):
    os.chdir(file_path)
   # print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    for f in all_file:
        if os.path.isdir(f):
            files.extend(check_file(file_path+'\\'+f))
            os.chdir(file_path)
        else:
            files.append(f)
    return files
file_list = check_file("//10.160.228.38/web/book/rwdl")  #便利文件下的文件名称，并存入数组返回

for i in range(len(file_list)):
    filename = file_list[i]
    name = urllib.parse.unquote(filename)
    name = name.replace('&ldquo;','')
    name = name.replace('&rdquo;','')
    srcFile = '//10.160.228.38/web/book/rwdl/' + filename
    dstFile = '//10.160.228.38/web/book/rwdl/' + name
    #print(name)
    try:
        os.rename(srcFile, dstFile)
    except Exception as e:
        print(e)
        print('改名失败\r\n')
    else:
        print(srcFile+'更改为：'+dstFile)