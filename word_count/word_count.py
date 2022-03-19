# 将要读取的文件和本程序放在同一个文件夹下
# 将 kind.txt 修改为自己的文件名
# 运行此程序即可得到输出结果
filename = "关键词.txt"
number = {}

with open(filename,encoding="UTF-8") as file:
    for line in file:
        if not number.get(line.strip()):
            number[line.strip()] = 1
        else:
            number[line.strip()] += 1

#reverse = True 为降序排列，False 为升序排列
number_sorted = {word:num for word, num in sorted(number.items(), key = lambda num: num[1], reverse= True)}

for word, num in number_sorted.items():
    print(f"word:{word} num:{num}\n")
