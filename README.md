# 树莓派心得

## 2021/07/02(金)

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

### 小灯泡(blinkLed_cz)

如果是输出，设置以什么方式读取引脚，```GPIO.BOARD```的话是物理坐标（括号里的），```GPIO.BCM```的话是名字（绿字）

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
### 距离传感器(UltrasonicRanging_cz.py)

trigPin是输出，它来发出超声波

echoPin是输入，来接收超声波

trigPin每0.00001秒就发出超声波

echoPin去接收超声波，距离上一次没接收到超声波的时候相比隔了多久，用声速进行计算，就是现在的距离

----------


## 2021/07/03(土)

### 按钮(button_cz.py)

按钮要卡在河道上当个桥梁（我在说什么啊）

一端连引脚，一端连地（一开始以为连电源，导致摁了没反应，还以为怎么了呢）

说明书给的代码，在初始设定引脚的输入输出时，又设定了一个触发事件，事件内容写在了```callback```里

顺便一说，如果事先不把```pull_up_down```设成```GPIO.PUD_UP```的话，跑出来它就不受控制一直在疯狂被摁的状态

```
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(ButtonPin, GPIO.FALLING, callback=swLed)
```

然后循环里什么都不写（好家伙）

我灵机一动想写朋友家门口的黄闪的灯，在有行人摁按钮以后，马路上的黄闪就会先变绿变黄再变红

用触发事件和在循环里写黄闪，它俩不关联，硬要说有种叠加的作用，和我想要的效果不一样

所以参考了昨天超声波测距的代码，在循环里写了个条件语句，当捕捉到按钮的低频时，执行绿黄红的操作

结果就很符合我的想法

可能又更好的解决方法吧，玩泥巴第二天也只能想到这个了

由于原理上和参考的代码长得不一样，姑且把两个都放上来了


### 1位数码管(8segment_digital_tube_cz.py)

其实就是引脚比较多，8个点8个控制而已，以前数电实验也写过，1的话哪两个亮，其他不亮，和别的输出差不多。说明书给的代码没有设初始值，但我给设了初始值显示是0

加了个按键，按一下+1

关于按钮的抖动问题，真的是老生常谈，大学就说，现在指导本科生FPGA的时候也有提到，到树莓派果然还有这个问题

从网上抄了一份答案，果然我觉得触发事件那句话还是尽量少用吧，要不然想额外干啥都不让干

在循环里加上
```
if GPIO.input(pinButton) == GPIO.LOW:
	time.sleep(0.02) #等0.02秒
	if GPIO.input(pinButton)==GPIO.LOW: #0.02秒之后还被摁，那就是真的被摁了
		while GPIO.input(pinButton)==GPIO.LOW: #等待按键被抬起
			pass #占位符
		#这里写摁按键会执行的操作
```


然后加了个小灯，摁按键会亮0.2秒，操作和之前类似

-------

## 2021/07/04(金)

### 显示屏(I2C LCD的文件夹里)

事先根据说明书，安装东西又开启权限之类的，总之很复杂

其实代码内容我也没太搞明白怎么回事，但```input```就是把屏幕的值传给别的接口，```output```就是把值写进显示器的接口里，注意这里的编码是```GPIO.setmode(GPIO.BOARD)```

在尝试把LED灯和按键接进去时才发现，只是LED显示屏的话，是不需要初定义什么东西的，奇妙

总之还是有点云里雾里

不过把LED灯和按键接进去，把昨天用数码管做到的+1装置，又做出来了一遍，感觉离计算器不远了

