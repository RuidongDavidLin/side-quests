# -*- coding: utf-8 -*-
import os

while 1:
    try:
        dir = input("请输入图片文件位置： ")
        # 添加path
        path = os.path.join(dir)
        break
    except (NotADirectoryError, FileNotFoundError):
        print("\n路径错误！")

list_name = []
files = os.listdir(path)  # 采用listdir来读取所有文件
for i in files:
    a = eval(i[4:-4])
    list_name.append(a)
# loss_file_name.sort(key=lambda x: int(x[:x.find("-")]))  # 按照前面的数字字符排序
# print(loss_file_name)
a = 0
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,'blue_top_'+str(list_name[a])+".txt"))
    a += 1
