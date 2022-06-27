import os
from PIL import Image
import cv2
import json
import retinex

# 填写需要的增强的数据集所在的文件夹名
data_path = 'data'
# 将文件夹下的文件名写入列表
img_list = os.listdir(data_path)
# 获取当前路径
save_path = os.getcwd() + "/data/"
# 检验文件夹是否为空文件夹
if len(img_list) == 0:
    print('Data directory is empty.')
    exit()

# 读取参数文件
with open('config.json', 'r') as f:
    config = json.load(f)

# 开始循环
for img_name in img_list:
    if img_name == '.gitkeep':
        continue
    # 读取图片并存入数组
    img = cv2.imread(os.path.join(data_path, img_name))

    print('msrcr processing......')
    # 调用MSRCR方法进行数据增强
    img_msrcr = retinex.MSRCR(
        img,
        config['sigma_list'],
        config['G'],
        config['b'],
        config['alpha'],
        config['beta'],
        config['low_clip'],
        config['high_clip']
    )
    # 显示增强后的图像，按q退出
    # cv2.imshow('MSRCR retinex', img_msrcr)
    # 将numpy数组处理后进行保存
    # img_msrcr = Image.fromarray(img_msrcr)
    img_msrcr.save(os.path.join(save_path, img_name.replace('.', '_msrcr.')))

    print('amsrcr processing......')
    # 调用AMSRCR方法进行数据增强
    img_amsrcr = retinex.automatedMSRCR(
        img,
        config['sigma_list']
    )
    # 显示增强后的图像，按q退出
    # cv2.imshow('autoMSRCR retinex', img_amsrcr)
    # 将numpy数组处理后进行保存
    # img_amsrcr = Image.fromarray(img_amsrcr)
    img_amsrcr.save(os.path.join(save_path, img_name.replace('.', '_amsrcr.')))

    print('msrcp processing......')
    # 调用MSRCP方法进行数据增强
    img_msrcp = retinex.MSRCP(
        img,
        config['sigma_list'],
        config['low_clip'],
        config['high_clip']
    )

    shape = img.shape
    # img_msrcp = Image.fromarray(img_msrcp)
    # cv2.imshow('MSRCP', img_msrcp)
    img_msrcp.save(os.path.join(save_path, img_name.replace('.', '_msrcp.')))
    cv2.waitKey()
