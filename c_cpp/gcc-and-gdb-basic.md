# Gcc

- gcc 支持源码格式
    - `.c` 	C源程序;  
    - `.C`, `.cc`, `.cxx`, `.cpp` 	C++源程序;  
    - `.m` 	Objective-C源程序;  
    - `.i` 	预处理后的C文件;  
    - `.ii` 预处理后的C++文件;  
    - `.s` 	汇编语言源程序; 
    - `.S` 	汇编语言源程序;
    - `.h` 	预处理器文件;
    - `.o`  目标文件(Object file)

## source to excutable

- 预处理(Pre-Processing)

根据预处理命令（#开头）修改源文件, `gcc -E hello.c -o hello.i`

- 编译(Compiling)

语法检查，并将源文件翻译成汇编文件  `gcc -S hello.i -o hello.s`

- 汇编(Assembling)

将汇编文件转换为目标文件（二进制）  `gcc -c hello.s -o hello.o`

- 链接(Linking)

编址和符号链接，生成可执行文件      `gcc hello.o -o hello`

**Problem**: **头文件**不在标准目录下

- gcc的选项 -I, 它的作用是把一个路径加入到系统路径, **作用于编译阶段**

> 对于有头文件在多个目录时,可以在编译时多次使用用-I参数加入头文件所在目录.
> 例如test_link.c需要用到 /usr/include, 当前目录(.),/home/hxy目录下的头文件.则如下编译
>     `gcc  -I. -I/usr/include -I/home/hxy -c test_link.c –o test_link`

- gcc的选项`-D`, 定义宏，most common use， DEBUG & RELEASE, 分别生成编译与发行版

>     `gcc -o app -DDEBUG *.c`

```cpp
#ifdef DEBUG
    // debug logic
#else
    // release logic
#endif
```

## gcc使用第三方库

- 找**头文件**并编译

`-I` option, **编译阶段**, `gcc -o hello.s -S -I{incluude_dir1} -I{include_dir2} hello.c`

- 找**库文件**链接

`-L` option, **汇编阶段**，`gcc -o hello.o -c -L{lib_dir} -llib hello.s`



### 库 

库是一组目标文件的包，就是一些最常用的代码编译成目标文件后打包存放。而最常见的库就是运行时库（Runtime Library）,如C运行库CRT.

库一般分为两种:静态库（`.a` 、`.lib`）动态库（`.so` 、`.dll` ）所谓**静态、动态是指链接过程**。 

静态库有两个重大缺点：

- 1）空间浪费

- 2）静态链接对程序的更新、部署和发布会带来很多麻烦。一旦程序中有任何模块更新，整个程序就要重新链接，发布给用户。

动态链接的基本思想：把程序按照模块拆分成各个相对独立的部分，在程序运行时才将它们链接在一起形成一个完整的程序，而不是想静态链接一样把所有的程序模块都链接成一个单独的可执行文件。

特点：

- 1）代码共享，所有引用该动态库的可执行目标文件共享一份相同的代码与数据。

- 2）程序升级方便，应用程序不需要重新链接新版本的动态库来升级，理论上只要简单地将旧的目标文件覆盖掉。

- 3）在运行时可以动态地选择加载各种应用程序模块

#### Linux库的命名

linux库的命名有一个特殊的要求,即要以lib打头,以.so或.a结尾

- libc.so         #标准C库,动态链接库
- libpthread.a #线程库,的静态链接库版本.

在一般使用时,为防止不同版本库互相覆盖,一般还在系统库名后加入版本号.

- libm. 6. so #math库 ver 6.0版本
- libc-2.3.2.so #标准C ver 2.3.2动态库

linux一般把系统库放在 /lib下. 这是大部分库命名的习惯

### gcc链接库

gcc -l参数 用来链接库标准表达式方式.

> -l接的库名,是**去掉lib和后缀名**(.so,.a)剩下的部分,
>       `gcc foo.c -lpthread -o foo` 
> 构造foo,链接库pthread . -lpthread 表示 链接 libpthread.so 

- 去掉后缀名,gcc –l是如何知道链接是动态库还是静态库的?,gcc有如下规则:

> 如果gcc所能找到库目录同时有两种版本,优先链接动态链接库版本
> 如果gcc所能找到库目录只有静态版本,则采用静态版本
> 如果加上 `-static` 参数,gcc 则强制链接静态版本
>       `gcc foo.c -static -lpthread  -o foo ` -lpthread 表示 链接 libpthread.a

- gcc所编译的目标文件和库通常不是在同一个目录下, 从哪一个目录加载库?

gcc在链接时采用`-L`参数来指明从哪一个目录加载库

> 例如，如果在/home/hxy/lib/目录下有链接时所需要的库文件libfoo.so, 则
>   `gcc foo.c -L/home/hxy/lib -lfoo -o foo`

**一个gcc语句可以包含多个-L参数**

**在编译目标文件时使用-L无效**

**标准库,gcc能自行找到,无需使用-L参数**

- 在一些应用中,链接多个库是有顺序的,但大部分情况无所谓

> 如在系统中liba.a 使用libpthread.a中的函数,而可执行程序同时使用两个库,则使用者liba.a的链接语句放在被使用者libpthread.a的前面, 
>       `gcc foo.c -L/home/hxy/lib –la -lpthread -o foo`

### gcc创建库

- gcc不能直接**创建静态库**.必须要用归档命令`ar`来创建

ar用于建立、修改、提取档案文件(archive)。archive是一个包含多个被包含文件的单一文件（也称之为库文件），其结构保证了可以从中检索并得到原始的被包含文件（称之为archive中的member）。

ar可以把任何文件归在一起,但通常是用来把gcc编译的目标文件(.o),合在一个静态库中

**静态库创建**

`gcc -Wall -c file1.c file2.c file3.c`  #一次性编译三个.o
`ar rv libname.a file1.o file2.o file3.o` #把三个o合在一起

> r：在库中插入模块(替换)。当插入的模块名已经在库中存在，则替换同名的模块
> v: verbose

**动态链接库创建**

1. 编译目标文件,必须带上`-fpic` 标志,使输出的对象模块是按照**可重定位地址**方式生成的。

`gcc -c mystrlen.c -fpic`
`gcc -c myshow.c -fpic`

2. 将加入动态库的目标文件合并在一起,必须带上-shared ,明确表示是动态链接库

`gcc -shared mystrlen.o myshow.o -o libstr.so`

> 两步可以合并成一步,但一般不建议这样做
> `gcc -fpic -shared mystrlen.c myshow.c -o libstr.so`
> so是Shared Object 的缩写

### 运行中使用动态链接库

一个使用动态链接库的程序运行时,要做一下设置.否则应用程序会报**找不到动态库的错误**

如果让程序运行时能找动态链接库,Linux有如下几种方法.

- 把库所在路径加入/etc/ld.so.conf,程序加载时首先到这里路径查找
- 设置环境变量LD_LIBRARY_PATH,把库所在路径加入这个变量中,这是最常用的方法

`export LD_LIBRARY_PATH=/home/new/test/liba`

**Tips**:
    - can use **wildcard** `*`: eg `gcc -o hello *.c`


# static library and dynamical linked library

C++静态库与动态库: <https://blog.csdn.net/qq_41786318/article/details/79545018>

# windows DLL

static: `.lib`
dynamic: `.dll`

- 1）lib是**编译时用到**的，**dll是运行**时用到的。如果要完成源代码的编译，只需要lib；如果要使动态链接的程序运行起来，只需要dll。

- 2）如果有dll文件，那么lib一般是一些**索引信息**，记录了dll中**函数的入口和位置**，dll中是函数的**具体内容**；如果只有lib文件，那么这个lib文件是静态编译出来的，索引和实现都在其中。使用静态编译的lib文件，在运行程序时不需要再挂动态库，缺点是导致应用程序比较大，而且失去了动态库的灵活性，发布新版本时要发布新的应用程序才行。

- 3）动态链接的情况下，有两个文件：一个是LIB文件，一个是DLL文件。LIB包含被DLL导出的函数名称和位置，DLL包含实际的函数和数据，应用程序使用LIB文件链接到DLL文件。在应用程序的可执行文件中，存放的不是被调用的函数代码，而是DLL中相应函数代码的地址，从而节省了内存资源。DLL和LIB文件必须随应用程序一起发行，否则应用程序会产生错误。如果不想用lib文件或者没有lib文件，可以用WIN32 API函数`LoadLibrary`、`GetProcAddress`装载