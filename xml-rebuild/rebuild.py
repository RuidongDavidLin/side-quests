import os
import os.path
import xml.dom.minidom
file_path=input('请输入文件路径(结尾加上/)：')   
files = os.listdir(file_path)  # 返回文件夹中的文件名列表
# print(files)
count = 0
for xmlFile in files:
    if not os.path.isdir(xmlFile):  # os.path.isdir()用于判断对象是否为一个目录
        # 如果不是目录，则直接打开
        # name1 = xmlFile.split('.')[0]
        # print(name1)
        dom = xml.dom.minidom.parse(file_path + xmlFile)
        # print(dom)
        root = dom.documentElement
        newfilename = root.getElementsByTagName('object')
        print(newfilename)
        # newfilename[0].firstChild.data = newfilename[0].firstChild.data.replace('jpeg', 'jpg')
        # print(newfilename[0].firstChild.data)
        
        # newpath = root.getElementsByTagName('path')
        # # newpath[0].firstChild.data = newpath[0].firstChild.data.replace('jpeg', 'jpg')
        # print(newpath[0].firstChild.data)
        # # print(root.nodeName)
        # # newpath = root.getElementsByTagName('path')
        # # newfilename = root.getElementsByTagName('filename')
        # # newfilename[0].firstChild.data = name1
        # with open(os.path.join(file_path, xmlFile), 'w', encoding='utf-8') as fh:
        #     dom.writexml(fh)
            #print('写入name/pose OK!')
        count = count + 1
