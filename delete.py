import os
mydir = "G:\BaiduNetdiskDownload\\"
os.chdir(mydir)
cwd = os.getcwd()
print('----这是分割线------')
def deleteNullFile():
    # '''删除所有大小为0的文件'''
    files = os.listdir(os.getcwd())
    for file in files:
        if os.path.getsize(file)  < 10000:   #获取文件大小
            os.remove(file)
            print(file + " deleted.")
    return
while True:
    deleteNullFile()

else:
    print("没有可以删除的了")
# print(3*2^20)

