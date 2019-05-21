# Python

# Anaconda

**features**
- IPython   "powerful python console"
- conda     "enviroment and package management"

## IPython

### useful commands

```shell
?   # help overview
help()  # python help
obj?
obj??
%quickref

/f a  # force auto paretheses
,f a  # force auto quote    eg: /type 1 # int,  ,type 1 # str
!pwd  # shell command
hist
      # shell history <c-p>/c-n, c-r, shell like
_i    # last input, __i, ___i
_     # last output
_oh   # out hist
```

## Conda

configure file: `~/.condarc`, yaml format

### useful command

```shell
conda --help
conda config --help

# configure domestic channel
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

# env management
conda info -e   # list enviroment, conda env list
conda create -p d:\python\envs\myanaconda3  # create env with specifical path
conda config --add envs_dirs d:\python\envs
conda info -e
activate myanaconda3    # activate

deactivate

# package management
conda search urllib
conda install urllib    # remove, update, list

# 安装不在conda或者acaconda的包，当你安装的包不在conda管理范围的时候可以使用pip来安装
conda install pip  # 首先在当前环境中安装pip
pip install 包名   # 其次在通过PIP命令在当前环境中安装包
```

# Python Syntax

see `D:\python\pycharm-courses\introduction_course`

**helloworld.py**

```python
#!/usr/bin/python3
#coding=UTF-8

print("hello world!!")
```

## data type

str, number, bool, list, tuple, dict, object

```python
type(1)   # int
isinstance(1, object) # True
```

### str

```python
a = 'aaaa'
b = "bbbb"
m = """multi
    line
    """
r = r'c:\a\b'   # row string, like there is b, u string

# format
1 + "2"   # error, not like js, instead str(1) + "2" is used
str(1)    # __str__(self)
"h" * 4   # "hhhh"
name = "python"
format("name = %s" % name)
format("name = {}", name)  # position is used
format("name = {name}", name) # key is used

print("hello, %s" %name, end="")

import string   # for more specific string topic
```

### number, bool
```python
# no ++
9 / 2   # return 4.5, / alway return float, for int, use // instead
9 // 2  # return 4
2 ** 3  # 8

# python bool value, True, False

# logic keyword
# if, elif, else, while  # no switch/case
# is, and, or, None, ==

# def all(iteralbe):
#   for i in iterable:
#     if not i:
#       return False
#     return True
a = list('01234')
all(a)  # False, a must be iterable
any(a)  # True
```

### scope

```python
def demo1():
    # 定义一个局部变量
    # 1> 出生：执行了下方的代码之后，才会被创建
    # 2> 死亡：函数执行完成之后
    num = 10
    print("demo1 num = %d" % num)

def demo2():
    num = 99
    print("demo2 num = %d" % num)
    pass

# 在函数内部定义的变量，不能在其他位置使用
# print("%d" % num)

demo1()
demo2()

# 全局变量
gl_num = 10

def demo3():
    # 希望修改全局变量的值 - 使用 global 声明一下变量即可
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时，就不会创建局部变量
    global gl_num

    gl_num = 99

    print("demo3 gl_num = %d" % gl_num)


def demo4():
    print("demo4 gl_num = %d" % gl_num)

print()
print("gl_num = %d" % gl_num)
demo3()
demo4()
```

### functions

1. primitive type: call by value, obj: call by reference

2. default argument, and call by key, such as print(a, b, end = '\n')

3. multiple returned value, `return a, b`

4. mutable and immutable args, like [] and ()

#### 定义支持多值参数的函数

* `python` 中有 **两种** 多值参数：
    * 参数名前增加 **一个** `*` 可以接收 **元组**
    * 参数名前增加 **两个** `*` 可以接收 **字典**
* 一般在给多值参数命名时，**习惯**使用以下两个名字
    * `*args` —— 存放 **元组** 参数，前面有一个 `*`
    * `**kwargs` —— 存放 **字典** 参数，前面有两个 `*`

* `args` 是 `arguments` 的缩写，有变量的含义
* `kw` 是 `keyword` 的缩写，`kwargs` 可以记忆 **键值对参数**

```python
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)

demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
# 1
# (2, 3, 4, 5)
# {'name': '小明', 'age': 18}

# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# 会把 num_tuple 和 xiaoming 作为元组传递个 args
# demo(gl_nums, gl_xiaoming)
demo(10, *gl_nums, **gl_xiaoming)
```

### iterable

```python
list = []   # list = list(), list(it)
            # mutable
tuple = ()  # tuple = tuple(), tuple(it)
            # immutable
dict = {"name": "jone"}   # dict = dict(), dict(key iterable, value iterable), dict([(k1,v1)])
set = set() # set(it)

for i in list:
  print(i, end=' ')

for i in rang(len(list) - 1):
  print(i, end=' ')

it = iter(list)
for i in it:
  print(i, end=' ')

it = iter(list)
while True:
  try:
    print(next(it))
  except StopIteration:
    break;
```

## file

```python
def read_file(filename):
  """
  print file content to console
  """
  try: 
    file = open(filename, 'r')
  except OSError as err:
    print(err)
  else:
    print(file.read())
    file.close()

def write_file(filename, data):
  """
  write data to filename
  """
  try:
    file = open(filename, 'w')
  except:
    pass
  else:
    if data:
      file.write(data)
    file.close()
```

### 操作文件的函数/方法

- 在 `Python` 中要操作文件需要记住 1 个函数和 3 个方法

| 序号 | 函数/方法 | 说明                           |
| ---- | --------- | ------------------------------ |
| 01   | open      | 打开文件，并且返回文件操作对象 |
| 02   | read      | 将文件内容读取到内存           |
| 03   | write     | 将指定内容写入文件             |
| 04   | close     | 关闭文件                       |

- `open` 函数负责打开文件，并且返回文件对象
- `read`/`write`/`close` 三个方法都需要通过 **文件对象** 来调用

#### 文件指针（知道）

- **文件指针** 标记 **从哪个位置开始读取数据**

- **第一次打开** 文件时，通常 **文件指针会指向文件的开始位置**

- 当执行了`read`方法后，**文件指针**会移动到**读取内容的末尾**
    - 默认情况下会移动到 **文件末尾**

**思考**

- 如果执行了一次 `read` 方法，读取了所有内容，那么再次调用 `read` 方法，还能够获得到内容吗？

**答案**

- 不能
- 第一次读取之后，文件指针移动到了文件末尾，再次调用不会读取到任何的内容

**读取大文件的正确姿势**

```python
# 打开文件
file = open("README")

while True:
    # 读取一行内容
    text = file.readline()

    # 判断是否读到内容
    if not text:
        break

    # 每读取一行的末尾已经有了一个 `\n`
    print(text, end="")

# 关闭文件
file.close()
```

### 文件/目录的常用管理操作

#### 文件操作

| 序号 | 方法名 | 说明       | 示例                              |
| ---- | ------ | ---------- | --------------------------------- |
| 01   | rename | 重命名文件 | `os.rename(源文件名, 目标文件名)` |
| 02   | remove | 删除文件   | `os.remove(文件名)`               |

#### 目录操作

| 序号 | 方法名     | 说明           | 示例                      |
| ---- | ---------- | -------------- | ------------------------- |
| 01   | listdir    | 目录列表       | `os.listdir(目录名)`      |
| 02   | mkdir      | 创建目录       | `os.mkdir(目录名)`        |
| 03   | rmdir      | 删除目录       | `os.rmdir(目录名)`        |
| 04   | getcwd     | 获取当前目录   | `os.getcwd()`             |
| 05   | chdir      | 修改工作目录   | `os.chdir(目标目录)`      |
| 06   | path.isdir | 判断是否是文件 | `os.path.isdir(文件路径)` |

> 提示：文件或者目录操作都支持 **相对路径** 和 **绝对路径**

### 文本文件的编码格式

- 文本文件存储的内容是基于 **字符编码** 的文件，常见的编码有 `ASCII` 编码，`UNICODE` 编码等

> Python 2.x 默认使用 `ASCII` 编码格式
> Python 3.x 默认使用 `UTF-8` 编码格式

#### `UTF-8` 编码格式

- 计算机中使用 **1~6 个字节** 来表示一个 `UTF-8` 字符，涵盖了 **地球上几乎所有地区的文字**
- 大多数汉字会使用 **3 个字节** 表示
- `UTF-8` 是 `UNICODE` 编码的一种编码格式

#### unicode 字符串

- 在 `Python 2.x` 中，即使指定了文件使用 `UTF-8` 的编码格式，但是在遍历字符串时，仍然会 **以字节为单位遍历** 字符串
- 要能够 **正确的遍历字符串**，在定义字符串时，需要 **在字符串的引号前**，增加一个小写字母 `u`，告诉解释器这是一个 `unicode` 字符串（使用 `UTF-8` 编码格式的字符串）

```python
# *-* coding:utf8 *-*

# 在字符串前，增加一个 `u` 表示这个字符串是一个 utf8 字符串
hello_str = u"你好世界"

print(hello_str)

for c in hello_str:
    print(c)
```

## module

`import re`, import re, use re.compile("this")
`from re import *`, import * inside re module, use compile("this")

```python
import re
pattern = re.compile("\d+")
result =  pattern.findall("today is 2019 08 12")

# match, search, sub, 
# re.RegFlags, I, M
# re.Match group, span

import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))   # 2019-05-21 00:20:15
print(time.strptime('2018-9-30 11:32:23', '%Y-%m-%d %H:%M:%S')) # parse str to time.struc_time
print(time.mktime(time.strptime('2018-9-30 11:32:23', '%Y-%m-%d %H:%M:%S')))  # 1538278343.0
```

## lambda

```python
arr = list(range(1, 5))

new_list = filter(is_odd, arr)
for ele in new_list:
    print(ele, end=' ')
print()

power_list = map(lambda x: x ** 2, arr)
while True:
    try:
        print(next(power_list), end=' ')
    except:
        break
print()

from functools import reduce
print(reduce(lambda x,y: x+y, arr))
```

## OOP

### basic

单下划线、双下划线、头尾双下划线说明：

* __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
* _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
* __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

Python 中，并没有 真正意义 的 私有

在给 属性、方法 命名时，实际是对 名称 做了一些特殊处理，使得外界无法访问到
处理方式：在 名称 前面加上 _类名 => _类名__名称

```python
class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 伪私有属性，在外界不能够被直接访问
print(xiaofang._Women__age)
# 伪私有方法，同样不允许在外界直接访问
xiaofang._Women__secret()
```

`dir()`
```python
class A:
  pass

dir(A())
"""
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']
 """
```

### multiple inheritance

```python
class A:
    def demo(self):
        print("A --- demo 方法")

class B:
    def test(self):
        print("B --- test 方法")

class C(B, A):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass

# 创建子类对象
c = C()
c.test()
c.demo()

# 确定C类对象调用方法的顺序
print(C.__mro__)
```

#### Python 中的 MRO —— 方法搜索顺序（知道）

- `Python` 中针对 **类** 提供了一个 **内置属性** `__mro__` 可以查看 **方法** 搜索顺序
- MRO 是 `method resolution order`，主要用于 **在多继承时判断 方法、属性 的调用 路径**

```python
print(C.__mro__)
```

**输出结果**

```python
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

- 在搜索方法时，是按照 `__mro__` 的输出结果 **从左至右** 的顺序查找的
- 如果在当前类中 **找到方法，就直接执行，不再搜索**
- 如果 **没有找到，就查找下一个类** 中是否有对应的方法，**如果找到，就直接执行，不再搜索**
- 如果找到最后一个类，还没有找到方法，程序报错

### 2.2 新式类与旧式（经典）类

> `object` 是 `Python` 为所有对象提供的 **基类**，提供有一些内置的属性和方法，可以使用 `dir` 函数查看

- **新式类**：以 `object` 为基类的类，**推荐使用**
- **经典类**：不以 `object` 为基类的类，**不推荐使用**
- 在 `Python 3.x` 中定义类时，如果没有指定父类，会 **默认使用** `object` 作为该类的 **基类** —— `Python 3.x` 中定义的类都是 **新式类**
- 在 `Python 2.x` 中定义类时，如果没有指定父类，则不会以 `object` 作为 **基类**

> **新式类** 和 **经典类** 在多继承时 —— **会影响到方法的搜索顺序**

为了保证编写的代码能够同时在 `Python 2.x` 和 `Python 3.x` 运行！
今后在定义类时，**如果没有父类，建议统一继承自 object**

### class members

#### class property

```python
class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    def __init__(self, name):
        self.name = name
        # 让类属性的值+1
        Tool.count += 1

# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 2. 输出工具对象的总数
tool2.count = 99
print("工具对象总数 %d" % tool2.count)  # 工具对象总数 99
print("===> %d" % Tool.count)   # ===> 2
```

在 Python中*属性的获取*存在一个*向上查找机制*:

get `tool2.count`

> 1. find in instance's properties
> 2. find in class propeties

- 因此，要访问类属性有两种方式：
    1. **类名.类属性**
    2. **对象.类属性** （不推荐）

**注意**

- 如果使用 `对象.类属性 = 值` 赋值语句，只会 **给对象添加一个属性**，而不会影响到 **类属性的值**

#### class method

*类方法*就是针对*类对象*定义的方法
- 在*类方法*内部*only*可以直接访问*类属性*或者调用其他的*类方法*

```python
class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        # 让类属性的值+1
        Tool.count += 1

Tool.show_tool_count()
```

- 类方法需要用 **修饰器** `@classmethod` 来标识，**告诉解释器这是一个类方法**
- 类方法的第一个参数应该是`cls` 
    - 由 **哪一个类** 调用的方法，方法内的 `cls` 就是 **哪一个类的引用**
    - 这个参数和 **实例方法** 的第一个参数是 `self` 类似
    - **提示** 使用其他名称也可以，不过习惯使用 `cls`

- 通过 **类名.** 调用 **类方法**，**调用方法时**，不需要传递 `cls` 参数

#### static method

- 在开发时，如果需要在 **类** 中封装一个方法，这个方法：
    - 既 **不需要** 访问 **实例属性** 或者调用 **实例方法**
    - 也 **不需要** 访问 **类属性** 或者调用 **类方法**
- 这个时候，可以把这个方法封装成一个 **静态方法**

```python
class Dog(object):
    @staticmethod
    def run():
        # 不访问实例属性/类属性
        print("小狗要跑...")

# 通过类名.调用静态方法 - 不需要创建对象
Dog.run()
```

## singleton

##  `__new__` 方法

- 使用 **类名()** 创建对象时，`Python` 的解释器 **首先** 会 调用 `__new__` 方法为对象 **分配空间** 
- `__new__` 是一个 由 `object` 基类提供的内置的静态方法 ，主要作用有两个：

    - 1) 在内存中为对象 **分配空间**
    - 2) **返回** 对象的引用

- `Python` 的解释器获得对象的 **引用** 后，将引用作为 **第一个参数**，传递给 `__init__` 方法

> 重写 `__new__` 方法 的代码非常固定！

- 重写 `__new__` 方法 **一定要** `super().__new__(cls)`
- 否则 Python 的解释器 **得不到** 分配了空间的 **对象引用**，**就不会调用对象的初始化方法**
- 注意：`__new__` 是一个静态方法，在调用时需要 **主动传递** `cls` 参数

**problem**: multiple init(), may change the `instance property`

```python
class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    __instance = None

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.__instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.__instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.__instance

    def __init__(self, *args, **kwargs):
        self.name = args[0]

    # solution for multiple init
    # __init_flag = False
    # def __init__(self, *args, **kwargs):
    #     if not MusicPlayer.__init_flag:
    #         MusicPlayer.__init_flag = True
    #         self.name = args[0]

# 创建多个对象
player1 = MusicPlayer("player1")
print(player1.name)     # player1

player2 = MusicPlayer("player2")
print(player2.name)     # player2
print(player1.name)     # player2
```

## exception

### 异常捕获完整语法

- 在实际开发中，为了能够处理复杂的异常情况，完整的异常语法如下：

> 提示：
>
> - 有关完整语法的应用场景，在后续学习中，**结合实际的案例**会更好理解
> - 现在先对这个语法结构有个印象即可

```python
try:
    # 尝试执行的代码
    pass
except 错误类型1:
    # 针对错误类型1，对应的代码处理
    pass
except 错误类型2:
    # 针对错误类型2，对应的代码处理
    pass
except (错误类型3, 错误类型4):
    # 针对错误类型3 和 4，对应的代码处理
    pass
except Exception as result:
    # 打印错误信息
    print(result)
else:
    # 没有异常才会执行的代码
    pass
finally:
    # 无论是否有异常，都会执行的代码
    print("无论是否有异常，都会执行的代码")
```

- `else` 只有在没有异常时才会执行的代码
- `finally` 无论是否有异常，都会执行的代码
- 之前一个演练的 **完整捕获异常** 的代码如下：

```python
try:
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
except ZeroDivisionError:
    print("除 0 错误")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("正常执行")
finally:
    print("执行完成，但是不保证正确")
```

### 抛出异常

- `Python` 中提供了一个 `Exception` **异常类**

- 在开发时，如果满足特定业务需求时，希望抛出异常，可以： 
    1. **创建** 一个 `Exception` 的 **对象**
    2. 使用 `raise` **关键字** 抛出 **异常对象**

```python
def input_password(pwd):
    # 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) < 8:
        raise Exception("密码长度不够", pwd, "should ge 8")
    else:
        return pwd

# 提示用户输入密码
try:
    print(input_password("passwd"))
except Exception as result:
    print(result)
```

## module and package sys

### 模块的概念

> **模块是 Python 程序架构的一个核心概念**

- 每一个以扩展名 `py` 结尾的 `Python` 源代码文件都是一个 **模块**
- **模块名** 同样也是一个 **标识符**，需要符合标识符的命名规则
- 在模块中定义的 **全局变量** 、**函数**、**类** 都是提供给外界直接使用的 **工具**
- **模块** 就好比是 **工具包**，要想使用这个工具包中的工具，就需要先 **导入** 这个模块

**hm_01_测试模块1.py**

```python
# 全局变量
title = "模块1"

# 函数
def say_hello():
    print("我是 %s" % title)

# 类
class Dog(object):
    pass
```

**hm_02_测试模块2**

```python
# 全局变量
title = "模块1"

# 函数
def say_hello():
    print("我是 %s" % title)

# 类
class Dog(object):
    pass
```

```python
import os, sys    # 

from functools import reduce  # import only functools.reduce
from functools import *       # import all functools's `tool`

# alias, for name conflict
from hm_02_测试模块2 import say_hello  as module2_say_hello
from hm_01_测试模块1 import say_hello
say_hello()
module2_say_hello()
```

**使用 `as` 指定模块的别名**

> **如果模块的名字太长**，可以使用 `as` 指定模块的名称，以方便在代码中的使用

```python
import 模块名1 as 模块别名
```

> 注意：**模块别名** 应该符合 **大驼峰命名法**

**注意**

> 如果 **两个模块**，存在 **同名的函数**，那么 **后导入模块的函数**，会 **覆盖掉先导入的函数**

### 模块的搜索顺序[扩展]

`Python` 的解释器在 **导入模块** 时，会：

1. 搜索 **当前目录** 指定模块名的文件，**如果有就直接导入**
2. 如果没有，再搜索 **系统目录**

> 在开发时，给文件起名，不要和 **系统的模块文件** **重名**

`Python` 中每一个模块都有一个内置属性 `__file__` 可以 **查看模块** 的 **完整路径**

模块搜索路径存储在system模块的`sys.path`变量, eg:

```markdown
D:\python\pycharm-courses\introduction_course\grocery
D:\python\envs\myanaconda3\Scripts
D:\python\envs\myanaconda3\python37.zip
D:\python\envs\myanaconda3\DLLs
D:\python\envs\myanaconda3\lib
D:\python\envs\myanaconda3
D:\python\envs\myanaconda3\lib\site-packages
```

```python
import random

print(random.__file__)  # 'D:\\python\\envs\\myanaconda3\\lib\\random.py'
# 生成一个 0～10 的数字
rand = random.randint(0, 10)
```

> 注意：如果当前目录下，存在一个 `random.py` 的文件，程序就无法正常执行了！

- 这个时候，`Python` 的解释器会 **加载当前目录** 下的 `random.py` 而不会加载 **系统的** `random` 模块

### 原则 (Unit Test)

**每一个文件都应该是可以被导入的**

- 一个 **独立的 Python 文件** 就是一个 **模块**
- ==在导入文件时，文件中 **所有没有任何缩进的代码** 都会被执行一遍！==

#### `__name__` 属性

> - `__name__` 属性可以做到，测试模块的代码 **只在测试情况下被运行**，而在 **被导入时不会被执行**！

- `__name__` 是 `Python` 的一个内置属性，记录着一个 **字符串**
- 如果 **是被其他文件导入的**，`__name__` 就是 **模块名**
- 如果 **是当前执行的程序** `__name__` 是 **__main__**

**在很多 Python 文件中都会看到以下格式的代码**：

```python
# 导入模块
# 定义全局变量
# 定义类
# 定义函数

# 在代码的最下方
def main():
    # ...
    pass

# 根据 __name__ 判断是否执行下方代码
if __name__ == "__main__":
    main()
```

> `def`, `if __name__ == "__main__"` 未缩进，执行

### 包（Package）

- **包** 是一个 **包含多个模块** 的 **特殊目录**
- 目录下有一个 **特殊的文件** `__init__.py`
- 包名的 **命名方式** 和变量名一致，**小写字母** + `_`

**好处**

- 使用 `import 包名` 可以一次性导入 **包** 中 **所有的模块**

#### demo

1. 新建一个 `hm_message` 的 **包**
2. 在目录下，新建两个文件 `send_message` 和 `receive_message`
3. 在 `send_message` 文件中定义一个 `send` 函数
4. 在 `receive_message` 文件中定义一个 `receive` 函数
5. 在外部直接导入 `hm_message` 的包

#### `__init__.py`

- 要在外界使用 **包** 中的模块，需要在 `__init__.py` 中指定 **对外界提供的模块列表**

```python
# 从 当前目录 导入 模块列表
from . import send_message
from . import receive_message
```

### 发布模块

#### `setup.py`

- `setup.py` 的文件

```python
from distutils.core import setup

setup(name="hm_message",  # 包名
      version="1.0",  # 版本
      description="itheima's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="itheima",  # 作者
      author_email="itheima@itheima.com",  # 作者邮箱
      url="www.itheima.com",  # 主页
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"])
```

有关字典参数的详细信息，可以参阅官方网站：

<https://docs.python.org/2/distutils/apiref.html>

**构建模块**

```bash
$ python3 setup.py build
```

**生成发布压缩包**

```bash
$ python3 setup.py sdist
```

> 注意：要制作哪个版本的模块，就使用哪个版本的解释器执行！

**安装模块**

```bash
$ tar -zxvf hm_message-1.0.tar.gz 
$ sudo python3 setup.py install
```

**卸载模块**

直接从安装目录下，把安装模块的 **目录** 删除就可以

```python
$ cd /usr/local/lib/python3.5/dist-packages/
$ sudo rm -r hm_message*
```

## more built in functions 

### sorted

```python
a = [5, 7, 6, 3, 4, 1, 2]
b = sorted(a)  # 保留原列表
print(a)        # [5, 7, 6, 3, 4, 1, 2]
print(b)        # [1, 2, 3, 4, 5, 6, 7]

L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
# sorted(L, cmp=lambda x, y: cmp(x[1], y[1]))  # 利用cmp函数, python 2

import operator
# print(sorted(L, lambda x, y: operator.gt(x, y)))    # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print(sorted(L, key=lambda x: x[1]))                    # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(students, key=lambda s: s[2])  # 按年龄排序 [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(students, key=lambda s: s[2], reverse=True)  # 按降序 [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

```

# The vscode python tutorial

<https://code.visualstudio.com/docs/python/python-tutorial>

## the vscode python extension

## python interpreter

# `vscode` folder

## `code .`

> use code open a folder, vscode make this a workspace. and create  `.vscode` automatically

- setting.json
    workspace scope vscode setting
- keybinding.json

- launch.json
    if use debug

# pip

<http://www.pianshen.com/article/5331129106/>

the python package installer, use PyPI(The Python Package Index), the standard repository of software for the python programming language.

## help 

```shell
D:\python\hello>pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
```

```shell
D:\python\hello>pip help install

Usage:
  pip install [options] <requirement specifier> [package-index-options] ...
  pip install [options] -r <requirements file> [package-index-options] ...
  pip install [options] [-e] <vcs project url> ...
  pip install [options] [-e] <local project path> ...
  pip install [options] <archive url/path> ...

Description:
  Install packages from:

  - PyPI (and other indexes) using requirement specifiers.
  - VCS project urls.
  - Local project directories.
  - Local or remote source archives.

  pip also supports installing from "requirements files", which provide
  an easy way to specify a whole environment to be installed.

Install Options:
  -r, --requirement <file>    Install from the given requirements file. This option can be used multiple times.
  -c, --constraint <file>     Constrain versions using the given constraints file. This option can be used multiple times.
  --no-deps                   Don't install package dependencies.
```


# Use a virtual environment

A best practice among Python developers is to avoid installing packages into a **global interpreter environment**, as we did in the previous section. You instead use a **project-specific virtual environment** that **contains a copy of a global interpreter**. Once you activate that environment, any packages you then install are isolated from other environments. Such isolation reduces many complications that can arise from conflicting package versions.

## Django Tutorial in Visual Studio Code

<https://code.visualstudio.com/docs/python/tutorial-django>
<https://docs.djangoproject.com/en/2.1/intro/tutorial01/>

Django is a high-level Python framework designed for rapid, secure, and scalable web development. Django includes rich support for URL routing, page templates, and working with data.