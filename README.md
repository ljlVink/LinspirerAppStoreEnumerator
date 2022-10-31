# LinspirerAppStoreEnumerator

### 介绍

勇士 欢迎来到**领创应用商店**

本Python脚本将帮助你**获取指定ID区间内的app包名**

#### 领创的大专生们看这里哦 就算你们怎么改api都已经没用了哦 全部的apk及其信息已经保存了不知道多少份 扩散到不知道哪里去了哦
#### 就算你们更新apk 我们也有数不清的方法获取哦

### 使用

`是人就会`

**LASEr2.py** 倾向于爬取快速爬管控包而打造 

```
python LASEr2.py 起始id 终止id 线程数(可以开到50) 设备swdid(sn/mac) 管控账号
```

e.g

```
python LASEr2.py 1 100000 50 aa:bb:cc:dd:dd:ff abc@abc.abc
```

### 其他

本脚本在下载apk后会**自动删除之**

如需保留 仅需**注释下面这行代码**

```python
os.system("rm ./packages/"+str(id)+".apk")
```

### Contributor
**ljlVink**

LASEr2

>比原版快1000倍

>action也能跑

>跑完可以停止