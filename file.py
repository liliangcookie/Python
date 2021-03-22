import os
import re
import shutil

# myfile = "test.txt"
#
# os.mknod(myfile)
#
# with open(myfile,'w') as f:  # 参数 w:写入 d:
#     f.write("Hello World")
#     f.close()
# 体验文件的基本操作
# file  = "test1.txt"
# f = open(file,'w')
# f.write("Hello World")
# f.close()

# 遍历文件下所有的文件
def fund(filepath,keyword):
    files = os.listdir(filepath)
    keyword = keyword

    for file in files: # 这里得到的是文件名
     if re.compile(keyword).findall(file):

        filedir = os.path.join(filepath,file)
        refile = os.path.join(filepath,"$RECYCLE.BIN")
        syfile = os.path.join(filepath,"System Volume Information")
        othfile = os.path.join(filepath, "共享文件")
        # print(filedir)
        if os.path.isdir(filedir) and filedir!= refile and  filedir!= syfile and  filedir!= othfile:
            if os.access(filedir, os.R_OK):
              # print(filedir)
              fund(filedir)
            else:
               break
        else:
         print("文件来自于："+filedir)
         fname = os.path.splitext(filedir)
         # for
         type = fname[1]
         # docfile = ['.pdf','.doc','.docx','.ppt','.pptx']

         docfile = ['.mkv','.mp4','.avi','.rmvb','.js']

         i=0
         while i < len(docfile):
            if type == docfile[i]:


                # print(file+"///")
                # print(filedir) #fname[1]+
                if os.path.exists(filedir) and os.path.getsize(filedir)>1000000000 : # 1000 为1K 1000000为1M
                    filedir = os.path.join(filepath, file)
                    # 用于文件读取
                    # filecon = os.read(filedir).decode("utf-8")
                    # print(filecon)
                    # if type == '.doc' or type=='.docx':
                    #  newname = "H:\\教学资料\\2020步步高一轮复习Word版文档\\2020步步高一轮复习Word版文档"+file   #关键的存储位置
                    # elif type == '.ppt' or type == '.pptx':
                    #  newname = "F:\PPT\\" + file  # 关键的存储位置
                    # elif type =='.pdf':
                    #  newname = "F:\PDF\\" + file

                    newname = "U:\\" + file

                    # 建立新文件格式
                    # fname = os.path.splitext(filedir)
                    # newfile = fname[0]+".jpg"
                    # newfiledir = os.path.join(filepath,newfile)
                    # with open(newfiledir, "wb") as f:
                    #     f.write(r.content)
                    #     f.close()
                    # print(newfiledir)
                    # shutil.copy(filedir,newname)
                    if(os.path.exists(newname)) :
                        print("文件已存在")
                        # shutil.copy(filedir, newname)
                    else:
                        # shutil.move(filedir, newname)
                        print("转移到" + newname)
                        shutil.move(filedir, newname)
                        # shutil.copy(filedir, newname)
                        # os.remove(newname)
                        # shutil.move(filedir, newname)
                     # else:
                     #    shutil.move(filedir,newname)

            i=i+1
            continue
         # for type in docfile:
         #     print(type+filedir)
         # if fname[1] == ".pdf":
         #    # print(fname)
         #    print(filedir)
         #    #print("---分割线----")
         # else:
         #    # print(fname)
         #     continue
         pass
# fund("N:\\待分类\\")
# fund("N:\\待管理\\")
# fund("M:\\待整理\\")

# fund("H:\\教学资料\\2020步步高一轮复习Word版文档\\2020步步高一轮复习Word版文档")
# fund("H:\\待分类\\")
# fund("G:\\待整理\\")
fund("H:\\高考\\2014-2019\\",'*')

# fund("N:\\待管理\\")
# fund("M:\\待整理\\")

