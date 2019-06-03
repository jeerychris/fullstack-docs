# Dynamic language edit help

Python是一种动态类型语言，这意味着我们在编写代码的时候更为自由，但是与此同时IDE无法向静态类型语言那样分析代码，及时给我们相应的提示。为了解决这个问题，Python 3.6 新增了几个特性**PEP 484**和**PEP 526**，帮助编辑器为我们提供更智能的提示。

**变量注解**

它的语法和某些类型后置的语言类似。

```python
# 变量注解
a: int = 5
b: bool = True
f: float = 5.0
s: str = "abc"
```

声明类型之后，编辑器和IDE就会读取到这个类型注解，然后给予我们相应的提示。程序在运行的时候行为完全不变。

如果是自己编写的类，也可以用作变量注解。
```python
class MyClass:
    def fun1(self):
        print("fun1")

me: MyClass = MyClass()
me.fun1()
```

**对于较复杂的内置类型、泛型、生成器、自定义类型等，需要引入标准库typing**。对于更复杂的类型，请直接参考`typing`标准库文档。


**函数注解**
当使用Python编写复杂的函数时，我们常常为没有合适的提示而苦恼。函数注解可以帮助我们解决这个问题。

```python
def add(a: int, b: int) -> int:
    return a + b
```
为函数添加注解之后，当我们调用这个函数的时候，编辑器就会给予对应的提示。当处理大型项目的时候，这个特性会很有用。

函数注解保存在函数的__annotations__属性中，如果你准备编写程序读取它，可以使用这个属性。

```python
print(add.__annotations__)
```

# multiple task

# multiple thread

module `threading`

> Thread module emulating a subset of Java's threading model.

**主线程会等待所有的子线程结束后才结束**

```python
import time
import threading


def sing():
    """唱歌 5秒钟"""
    for i in range(5):
        print("----正在唱:菊花茶----")
        print(threading.enumerate())
        time.sleep(1)


def dance():
    """跳舞 5秒钟"""
    for i in range(5):
        print("----正在跳舞----")
        print(threading.enumerate())
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
```

## thread synchronize

**problem code**: expect last exist thread output 2000000.

```python
import threading

g_num = 0


def inc(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("%s---%d" % (threading.currentThread().getName(), g_num))


def main():
    threading.Thread(target=inc, args=(1000000,)).start()
    threading.Thread(target=inc, args=(1000000,)).start()


if __name__ == '__main__':
    main()

# output
# Thread-1---1133919
# Thread-2---1259644
```

**NOTE**: trans thread args as a list

### mutex lock

```python
import threading

g_num = 0
mutex = threading.Lock()


def inc(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("%s---%d" % (threading.currentThread().getName(), g_num))


def main():
    threading.Thread(target=inc, args=(1000000,)).start()
    threading.Thread(target=inc, args=(1000000,)).start()


if __name__ == '__main__':
    main()

# output
# Thread-2---1946977
# Thread-1---2000000
```

### dead lock

```python
import threading

g_num = 0
mutexA = threading.Lock()
mutexB = threading.Lock()

def inc(num):
    global g_num
    for i in range(num):
        mutexA.acquire()
        mutexB.acquire()
        g_num += 1
        print("%s---%d" % (threading.currentThread().getName(), g_num))
        mutexB.release()
        mutexA.release()

def dec(num):
    global g_num
    for i in range(num):
        mutexB.acquire()
        mutexA.acquire()
        g_num -= 1
        print("%s---%d" % (threading.currentThread().getName(), g_num))
        mutexA.release()
        mutexB.release()

def main():
    threading.Thread(target=inc, args=(1000000,)).start()
    threading.Thread(target=dec, args=(1000000,)).start()

if __name__ == '__main__':
    main()
```

# multiple process

module `multiprocessing`

- 进程的创建
- 进程pid   `os.getpid()`
- 进程args
- **进程间不同享全局变量**

```python
from multiprocessing import Process
import os
import time

nums = [11, 22]

def work1():
    """子进程要执行的代码"""
    print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))
    for i in range(3):
        nums.append(i)
        time.sleep(1)
        print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))

def work2():
    """子进程要执行的代码"""
    print("in process2 pid=%d ,nums=%s" % (os.getpid(), nums))

if __name__ == '__main__':
    p1 = Process(target=work1)
    p1.start()
    p1.join()

    p2 = Process(target=work2)
    p2.start()

    # output
    # in process1 pid=11349 ,nums=[11, 22]
    # in process1 pid=11349 ,nums=[11, 22, 0]
    # in process1 pid=11349 ,nums=[11, 22, 0, 1]
    # in process1 pid=11349 ,nums=[11, 22, 0, 1, 2]
    # in process2 pid=11350 ,nums=[11, 22]
```

### 进程间通信-Queue

`Queue`, `Pipe`

```python
from multiprocessing import Queue, Process, current_process
import random
import time


def write_data(queue: Queue):
    while True:
        if queue.full():
            time.sleep(1)
        else:
            queue.put(random.randint(1, 100))
            print("process %s: size = %d" % (current_process().name, queue.qsize()))


def read_data(queue: Queue):
    while True:
        if queue.empty():
            time.sleep(1)
        else:
            print("process %s: ele = %d" % (current_process().name, queue.get()))


if __name__ == "__main__":
    q = Queue(5)
    Process(target=write_data, args=(q, )).start()
    Process(target=read_data, args=(q, )).start()
```

### process pool

`pool.apply_async(f, (arg1, ))`

```python
import multiprocessing as mp


def info(x: int):
    print("%s---%d" % (mp.current_process().name, x ** 2))


if __name__ == "__main__":
    with mp.Pool(5) as p:
        p.map(info, range(5))
```

# 协程

协程，又称微线程，纤程。英文名**Coroutine**。`Go` programming language

**协程是啥**

<span style="color:#0f0">协程是python个中另外一种实现多任务的方式，只不过比线程更小占用更小执行单元（理解为需要的资源）</span>。 为啥说它是一个执行单元，因为它**自带CPU上下文**。这样只要在合适的时机， 我们可以把一个协程 切换到另一个协程。 只要这个过程中保存或恢复 CPU上下文那么程序还是可以运行的。

通俗的理解：在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外一个函数中执行，注意不是通过调用函数的方式做到的，并且切换的次数以及什么时候再切换到原来的函数都由开发者自己确定

**协程和线程差异**

在实现多任务时, **线程切换**从系统层面**远不止保存和恢复 CPU上下文这么简单。 操作系统为了程序运行的高效性每个线程都有自己缓存Cache等等数据，操作系统还会帮你做这些数据的恢复操作。 所以线程的切换非常耗性能**。但是**协程的切换只是单纯的操作CPU的上下文**，所以一秒钟切换个上百万次系统都抗的住。

## yield简单实现协程

```python
import time


def task_1():
    while True:
        print("---1----")
        yield


def task_2():
    while True:
        print("---2----")
        yield


if __name__ == "__main__":
    t1 = task_1()
    t2 = task_2()
    while True:
        next(t1)
        next(t2)
        time.sleep(1)
```

## greenlet module

`conda install greenlet`

python中的greenlet模块对其封装，从而使得切换任务变的更加简单

```python
from greenlet import greenlet
import time

def test1():
    while True:
        print("---A--")
        gr2.switch()
        time.sleep(0.5)
        print("---A--After sleep")

def test2():
    while True:
        print("---B--")
        gr1.switch()
        time.sleep(0.5)
        print("---A--After sleep")

gr1 = greenlet(test1)
gr2 = greenlet(test2)

#切换到gr1中运行
gr1.switch()
```

## gevent

greenlet已经实现了协程，但是这个还的人工切换，是不是觉得太麻烦了，不要捉急，python还有一个比greenlet更强大的并且能够自动切换任务的模块`gevent`

其原理是当一个greenlet遇到IO(指的是input output 输入输出，比如网络、文件操作等)操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO

`conda install gevent`

```python
import gevent

def f(n):
    for i in range(3):
        print(gevent.getcurrent(), n)

g1 = gevent.spawn(f, 1)
g2 = gevent.spawn(f, 2)
g3 = gevent.spawn(f, 3)
g1.join()
g2.join()
g3.join()
```

3个greenlet是依次运行而不是交替运行

```python
import gevent

def f(n):
    for i in range(3):
        print(gevent.getcurrent(), n)
        #用来模拟一个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)

g1 = gevent.spawn(f, 1)
g2 = gevent.spawn(f, 2)
g3 = gevent.spawn(f, 3)
g1.join()
g2.join()
g3.join()
```

output:

```python
<Greenlet at 0xf186173598: f(1)> 1
<Greenlet at 0xf1861737b8: f(2)> 2
<Greenlet at 0xf1861739d8: f(3)> 3
<Greenlet at 0xf186173598: f(1)> 1
<Greenlet at 0xf1861737b8: f(2)> 2
<Greenlet at 0xf1861739d8: f(3)> 3
<Greenlet at 0xf186173598: f(1)> 1
<Greenlet at 0xf1861737b8: f(2)> 2
<Greenlet at 0xf1861739d8: f(3)> 3
```

### 给程序打补丁

> 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

```python
import gevent
import random
import time

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())	// time.sleep

gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])
```

`time.sleep(1)` **sequence run**

```python
from gevent import monkey
import gevent
import random
import time

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())

gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])
```

## http download snippet

```python
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    with open(img_name, "wb") as f:
        while True:
            img_content = req.read(1024 * 1024)
            if not img_content:
                break
            else:
                f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "vscode.zip", "https://github.com/microsoft/vscode/archive/1.34.0.zip"),
        gevent.spawn(downloader, "4.jpg", "https://rpic.douyucdn.cn/appCovers/2017/09/17/2308890_20170917232900_big.jpg"),
    ])


if __name__ == '__main__':
    main()
```

## 进程、线程、协程对比

### 请仔细理解如下的通俗描述

- 有一个老板想要开个工厂进行生产某件商品（例如剪子）
- 他需要花一些财力物力制作一条生产线，这个生产线上有很多的器件以及材料这些所有的 为了能够生产剪子而准备的资源称之为：进程
- 只有生产线是不能够进行生产的，所以老板的找个工人来进行生产，这个工人能够利用这些材料最终一步步的将剪子做出来，这个来做事情的工人称之为：线程
- 这个老板为了提高生产率，想到3种办法：
    1. 在这条生产线上多招些工人，一起来做剪子，这样效率是成倍増长，即单进程 多线程方式
    2. 老板发现这条生产线上的工人不是越多越好，因为一条生产线的资源以及材料毕竟有限，所以老板又花了些财力物力购置了另外一条生产线，然后再招些工人这样效率又再一步提高了，即多进程 多线程方式
    3. 老板发现，现在已经有了很多条生产线，并且每条生产线上已经有很多工人了（即程序是多进程的，每个进程中又有多个线程），为了再次提高效率，老板想了个损招，规定：如果某个员工在上班时临时没事或者再等待某些条件（比如等待另一个工人生产完谋道工序 之后他才能再次工作） ，那么这个员工就利用这个时间去做其它的事情，那么也就是说：如果一个线程等待某些条件，可以充分利用这个时间去做其它事情，其实这就是：协程方式

### 简单总结

1. 进程是资源分配的单位
2. 线程是操作系统调度的单位
3. 进程切换需要的资源很最大，效率很低
4. 线程切换需要的资源一般，效率一般（当然了在不考虑GIL的情况下）
5. 协程切换任务资源很小，效率高
6. 多进程、多线程根据cpu核数不一样可能是并行的，但是协程是在一个线程中 所以是并发

# http webserver

## http (Hyper Text Transfer Protocol)

### Request

**method**: GET, POST, PUT, DELTE

get sample:

```
GET / HTTP/1.1
Host: 127.0.0.1:8080
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
cookie: blablaaa
cache-control: disable
```

### Response

`response header + blank line + response body`

sample:

```
HTTP/1.1 200 OK
Connection: Keep-Alive
Content-Encoding: gzip
Content-Type: text/html; charset=utf-8

<h1>hello world</h1>
```

### Conclusion

#### HTTP请求

响应代码：**200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误**；

响应类型：由Content-Type指定；

> Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，我们只需要在HTTP请求中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，因此，**一个HTTP请求只处理一个资源(此时就可以理解为TCP协议中的短连接，每个链接只获取一个资源，如需要多个就需要建立多个链接)**

HTTP协议同时具备极强的扩展性，虽然浏览器请求的是`http://www.sina.com`的首页，但是新浪在HTML中可以链入其他服务器的资源，比如`<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png">`，从而将请求压力分散到各个服务器上，并且，一个站点可以链接到其他站点，无数个站点互相链接起来，就形成了World Wide Web，简称WWW。

#### HTTP格式

每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。

HTTP协议是一种文本协议，所以，它的格式也非常简单。

**HTTP GET请求的格式**：

```
    GET /path HTTP/1.1
    Header1: Value1
    Header2: Value2
    Header3: Value3
```

每个Header一行一个，windows 换行符是\r\n。

**HTTP POST请求的格式：**

```
    POST /path HTTP/1.1
    Header1: Value1
    Header2: Value2
    Header3: Value3

    body data goes here...
```

当遇到**连续两个\r\n**(blank line)时，Header部分结束，后面的数据全部是Body。

**HTTP响应的格式**：

```
    HTTP/1.1 200 OK
    Header1: Value1
    Header2: Value2
    Header3: Value3

    body data goes here...
```

HTTP响应如果包含body，也是通过 blank line 来分隔的。

请再次注意，**Body的数据类型由Content-Type头来确定**，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。

当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。

## blocking io

## non blocking io multiplexing