import os
path= os.getcwd()  #待读取的文件夹
path_list=os.listdir(path)
path_standard = {'1.txt' : 0, 
                 '2.txt' : 0, 
                 '3.txt' : 0, 
                 '4.txt' : 0, 
                 '5.txt' : 0, 
                 '6.txt' : 0, 
                 '7.txt' : 0}
for filename in path_list:
	if filename in path_standard:
		path_standard[filename] = 1
for word in path_standard:
    if path_standard[word] == 0:
        print(word + "没交")
        