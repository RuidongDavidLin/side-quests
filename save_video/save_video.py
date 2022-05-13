if __name__ == '__main__':
    import cv2
    print('请输入要保存的视频的名字:', end="")
    name = input() + '.mkv'
    # 对视频设置的编码解码的方式MPEG-4编码
    fource = cv2.VideoWriter_fourcc(*'DIVX')
    # 采用摄像头采集图像
    video = cv2.VideoCapture(0)  # 如果笔记本有多个摄像头，可设置填入1，2
    # 保存的位置，以及编码解码方式，帧率，视频帧大小
    resulte = cv2.VideoWriter(name, fource, 20.0, (640, 480))
    # 判断是否创建视频流
    while video.isOpened():
        # 将每一张图像保存到变量中
        ret, frame = video.read()
        # 判断是否从对象中读取到了变量
        if ret is True:
            # 反转图像，因为摄像机出来的图片与自己位置相反
            frame = cv2.flip(frame, 2)
            # 将每一帧图像写入到视频中
            resulte.write(frame)
            # 展示视频
            cv2.imshow('video', frame)
            # cv2.waitKey(25)
            # 按q键结束
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
    # 释放并关闭窗口
    video.release()
    resulte.release()
    cv2.destroyAllWindows()