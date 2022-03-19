# 如何修改ssh 的默认端口
## 修改原因
提交GitHub代码的时候，因为仓库名更换了，但是git add remote处没有更换
导致多次尝试失败，最终 SSH 默认的22端口被当作黑客端口封禁了
## 解决办法
修改 SSH 提交的默认端口
## 修改步骤
修改下面这个文件（Git默认安装目录）（我自己的软件习惯安装在D盘）
下面是我的安装路径
> D:\Git\etc\ssh\ssh_config 
下面是默认安装路径
> C:\Program Files\Git\etc\ssh\ssh_config

添加以下代码
```
Host github.com
User 814099377@qq.com
Hostname ssh.github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
Port 443
```
> 814099377@qq.com是我的GitHub账号注册邮箱，替换成自己的就可以了
其中443为HTTPS转发端口（具体有啥影响的话，我目前还没发现）