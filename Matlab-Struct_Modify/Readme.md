# 对Matlab类型：Struct进行结构调整

### 需求描述 (:laughing:)
我需要删除Matlab结构体中的指定行
但是单纯依赖Python并不能很好的解决这个需求，原因在于Struct结构在Scipy库读取后是成为一种Numpy的结构,由于水平有限，故没能实现删减
![这是图片](struct%E7%BB%93%E6%9E%84%E7%A4%BA%E6%84%8F%E5%9B%BE.jpg)

### 解决过程(:stuck_out_tongue_winking_eye:)
#### 先在Matlab内部进行处理，将结构体转为表格形式(Table),具体代码如下
```matlab
% struct2table将struct转化为table,PV为结构体名称
table = struct2table("PV");

% 我的需求是将correction=1的行删去
todelete = table.correction==1;

% 将todelete置为空[]
table(todelete,:) =[];

% 转化为struct
PV = table2struct(PV);
```

#### 解决初步需求，但是发现新问题(:sweat:)
转化出的结构体为 452x1 struct，很原有数据结构有差别(原有是1xM)
#### 经过摸索，发现可以重新放回Python环境下进行Numpy数组改造
##### 主要解决思想
> Python调用Scipy库读取.mat文件后，可以利用numpy数组的reshape方法进行重构

#### 代码(Python)
```Python
import scipy.io
import numpy as np

data = scipy.io.loadmat('process_data.mat')
print(data.keys())  # 了解.mat文件内部结构

print(data["PV"].shape)
# 将原有(452,1)转化为(1,452)
data["PV"] = data["PV"].reshape(1,452)
# 保存
scipy.io.savemat("Process.mat",data)
```

### 效果展示
![效果图2](%E6%95%88%E6%9E%9C%E5%9B%BE2.jpg)
![效果图1](%E6%95%88%E6%9E%9C%E5%9B%BE1.jpg)