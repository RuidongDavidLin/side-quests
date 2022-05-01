import random
import time
import datetime
import numpy as np

weather = ['Snowy','Rainy','Windy','Typhoon','Sunny','Cloudy']
signal = ['➕','➖','✖','➗']
point = ['操场','停车场','篮球场','足球场','教学楼','环校路1号','环校路2号','环校路3号','环校路4号']
state = ['继续充电','继续工作','返回仓库']

while True:
    print('正在获取当前机器人状态')
    print('Loading...')
    for i in range(11):
        time.sleep(random.uniform(0,0.3))
        print('\r当前进度：{0}{1}%'.format('▉'*i,(i*10)), end='')
    print("")
    print ("当前系统日期和时间是: ")
    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print("")
    print("Weather Condition : " + weather[random.randint(0,5)])
    time.sleep(0.3)
    battery = '当前机器人的电量为' + str(random.randint(0, 100)) + '%'
    predict_power = '预测15min内发电量为' + str(random.uniform(0, 100)) + 'J'
    print(battery + '\n')
    time.sleep(0.5)
    print(predict_power + '\n')
    time.sleep(0.5)
    print("Working Place : " + point[random.randint(0, 8)])
    for i in range(0,3):
        print(str(np.random.randn(4,6)) + signal[random.randint(0,3)] + str(np.random.randn(4,6)))
        time.sleep(0.5)
    print("After a short-time predict:\n")
    print(state[random.randint(0,2)] + str(random.randint(10,20)) + "min\n\n")
    time.sleep(2)
    # T1 = time.time()
    # T2 = time.time()