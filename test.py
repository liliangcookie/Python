#num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
#for i in num: print("<img src='"+str(i)+".png'></img><br>")
import fitz  # pip install pymupdf
import re
import os
#import sys
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
file_list = check_file("//10.160.228.38/web/book/rwdl")

def find_imag(img_path):
    checkXO = r"/Type(?= */XObject)"
    checkIM = r"/Subtype(?= */Image)"

    pdf = fitz.open("海运网络的脆弱性及风险控制研究.pdf")
    path = "海运网络的脆弱性及风险控制研究.pdf"
    img_count = 0
    len_XREF = pdf._getXrefLength()

    print("文件名:{}, 页数: {}, 对象: {}".format(path, len(pdf), len_XREF - 1))

    for i in range(1, len_XREF):
        text = pdf._getXrefString(i)
        isXObject = re.search(checkXO, text)

        # 使用正则表达式查看是否是图片
        isImage = re.search(checkIM, text)

        # 如果不是对象也不是图片，则continue
        if not isXObject or not isImage:
            continue
        img_count += 1
        # 根据索引生成图像
        pix = fitz.Pixmap(pdf, i)

        new_name = path.replace('\/', '_') + "_img{}.png".format(img_count)
        new_name = new_name.replace(':', '')

        # 如果pix.n<5,可以直接存为PNG
        if pix.n < 5:
            (os.path.join(img_path, new_name))
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.writePNG(os.path.join(img_path, new_name))

        else:
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.writePNG(os.path.join(img_path, new_name))
            print(img_path)
            print("提取了{}张图片".format(img_count))
            pix0 = None

        pix = None




if __name__ == '__main__':
    pdf_path = r'海运网络的脆弱性及风险控制研究.pdf'
    img_path = r'img'
    m = find_imag(img_path)
            # input the path of pdf file