# 将要读取的文件和本程序放在同一个文件夹下
# 将 kind.txt 修改为自己的文件名
# 运行此程序即可得到输出结果

filename = "220627-新业态-关键词.txt"
number = {}
check_num = 0
total_num = 0
with open(filename,encoding="UTF-8") as file:
    for line in file:
        check_num += 1
        if not number.get(line.strip()):
            number[line.strip()] = 1
        else:
            number[line.strip()] += 1

#reverse = True 为降序排列，False 为升序排列
number_sorted = {word:num for word, num in sorted(number.items(), key = lambda num: num[1], reverse= True)}

for word, num in number_sorted.items():
    total_num += num
    sentence = f"{word} {num}"
    with open(filename.replace('.txt', '_统计结果.txt'),'w',encoding='utf-8') as f:
        f.write(sentence)
        f.write('\n')
if total_num == check_num:
    print("数目校验正确,一共有{}个词汇".format(total_num))
else:
    print("数目校验不正确")

