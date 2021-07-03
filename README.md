# 树莓派心得

### 2021/07/02(金)

从官网下载助手，然后在自己电脑上操作，把系统写进烧录卡里

然后就启动了

目前的ip地址是10.30.82.109

大概每次进去都要登陆一下，有些麻烦

``` pinout ``` 可以查看引脚

引入包

```
import RPi.GPIO as GPIO
import time
```

- 小灯泡

如果是输出，设置以什么方式读取引脚，```GPIO.BOARD```的话是物理坐标（括号里的），```GPIO.BC```的话是名字（绿字）

然后设置对应引脚是输出，并且设定初始值是```GPIO.HIGH```

```
LedPin = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)
```

然后把要做的操作写进```try```里,停止的部分写在```except```里

```
try:
    loop()
except KeyboardInterrupt:
    destroy()
```

然后在循环```loop()```里写上以下改变引脚电流状态的代码，别忘了加个sleep
```
GPIO.output(LedPin, GPIO.LOW)
GPIO.output(LedPin, GPIO.HIGH)
time.sleep(1)
```

最后写上在停止的时候的操作```destroy()```

```
GPIO.output(LedPin, GPIO.HIGH)
GPIO.cleanup() 
```
- 距离传感器

trigPin是输出，它来发出超声波

echoPin是输入，来接收超声波

trigPin每0.00001秒就发出超声波

echoPin去接收超声波，距离上一次没接收到超声波的时候相比隔了多久，用声速进行计算，就是现在的距离

### 2021/07/03(土)

- 