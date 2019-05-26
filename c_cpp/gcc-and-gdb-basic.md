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

# A Simple Makefile Tutorial

A simple tutorial: http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/

GNU Make: https://www.gnu.org/software/make/manual/make.html

Makefiles are a simple way to organize code compilation. 

syntax:

```makefile
task: dep1 dep2
    cmd arg1 arg2
    cmd2 args
```

**A Simple Example**

Let's start off with the following three files, `hellomake.c`, `hellofunc.c`, and `hellomake.h`, which would represent a typical main program, some functional code in a separate file, and an include file, respectively.

`hellofunc.c`

```c
#include <hellomake.h>

int main() {
  // call a function in another file
  myPrintHelloMake();
  return 0;
}
```

`hellomake.c`

```c
#include <stdio.h>
#include <hellomake.h>

void myPrintHelloMake(void) {
  printf("Hello makefiles!\n");
  return;
}
```

`hellomake.h`

```c
/*
example include file
*/
void myPrintHelloMake(void);
```

Normally, you would compile this collection of code by executing the following command:

`gcc -o hellomake hellomake.c hellofunc.c -I.`

Unfortunately, this approach to compilation has **two downfalls**. First, if you lose the compile command or switch computers you have to **retype** it from scratch, which is inefficient at best. Second, if you are **only making changes to one .c file, recompiling all** of them every time is also time-consuming and inefficient. So, it's time to see what we can do with a makefile.

## simplest makefile

**makefile 1**

```makefile
hellomake: hellomake.c hellofunc.c
     gcc -o hellomake hellomake.c hellofunc.c -I.
```

If you put this rule into a file called `Makefile` or `makefile` and then **type make** on the command line it will execute the compile command as you have written it in the makefile. 

Note that **make with no arguments executes the first rule in the file**. Furthermore, by putting the list of files on which the command **depends** on the first line after the :, **make knows that the rule hellomake needs to be executed if any of those files change**. Immediately, you have solved problem #1.

One very important thing to note is that there is a tab before the gcc command in the makefile. **There must be a tab at the beginning of any command**, and make will not be happy if it's not there.

**Makefile 2**

```makefile
CC=gcc
CFLAGS=-I.

hellomake: hellomake.o hellofunc.o
     $(CC) -o hellomake hellomake.o hellofunc.o
```

So now we've **defined some constants `CC` and `CFLAGS`**. It turns out these are special constants that communicate to make how we want to compile the files hellomake.c and hellofunc.c. In particular, the macro CC is the C compiler to use, and CFLAGS is the list of flags to pass to the compilation command. **By putting the object files--`hellomake.o` and `hellofunc.o`--in the dependency list and in the rule, make knows it must first compile the .c versions individually, and then build the executable hellomake.**

Using this form of makefile is sufficient for most small scale projects. However, there is one thing missing: **dependency on the include files**. If you were to make a change to hellomake.h, for example, make would not recompile the .c files, even though they needed to be. In order to fix this, we need to tell make that **all .c files depend on certain .h files**. We can do this by writing a simple rule and adding it to the makefile.

### wildcard * and %

Makefile中的%标记和系统通配符*的区别: https://www.cnblogs.com/warren-wong/p/3979270.html

如果你想编译一个文件夹下的所有.c文件，你可能会这样写：

```makefile
%.o:%.c
    gcc -o $@ $<
```
> Make： *** target not found. stop.

要知道原因，我们先来看看另一个makefile的运行过程，例如有Makefile如下：

```makefile
%.o:%.c
    gcc -o $@ $<

all：test1.o test2.o
```
如果没有指定输出项目的时候Make会自动找到makefile中第一个目标中没有通配符的目标进行构造，所以步骤是：

- 构造all，发现需要test1.o和test2.o
- 这个时候他就会在Makefile文件中找到目标能匹配test1.o和test2.o的规则。
- 找到test1.o的规则并且知道test1.c存在，运行下面的命令。
- 同步骤三构造出test2.o
- 现在构造all的源文件已经齐全，构建all

所以通配符`%`的意思是：

- 我要找test1.o的构造规则，看看Makefile中那个规则符合。
- 然后找到了%.o:%.c，
- 来套一下来套一下：
- %.o 和我要找的 test1.o 匹配
- 套上了，得到%=test1。
- 所以在后面的%.c就表示test1.c了。
 
通配符`*`的意思是：

我不知道目标的名字，系统该目录下中所有后缀为.c的文件都是我要找的。
然后遍历目录的文件，看是否匹配。找出所有匹配的项目。

```makefile
all:$(subst .c,.o,$(wildcard *.c))

%.o:%.c
    gcc -o $@ $<
```

`$@`: 目标的名字
`$^`: 构造所需文件列表所有所有文件的名字
`$<`: 构造所需文件列表的第一个文件的名字

**Makefile 3**

```makefile
CC=gcc
CFLAGS=-I.
DEPS = hellomake.h

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

hellomake: hellomake.o hellofunc.o 
	$(CC) -o hellomake hellomake.o hellofunc.o 
```
This addition first creates the macro DEPS, which is the set of .h files on which the .c files depend. Then we define a rule that applies to **all files ending in the .o suffix**. The rule says that the .o file depends upon the .c version of the file and the .h files included in the DEPS macro. 

The rule then says that to generate the .o file, make needs to compile the .c file using the compiler defined in the CC macro. The -c flag says to generate the object file, the -o `$@` says to put the output of the compilation in the **file named on the left side of the :**, the `$<` is the **first item in the dependencies list**, and the CFLAGS macro is defined as above.

As a final simplification, let's use the special macros $@ and `$^`, which are the left and **right sides of the :**, respectively, to make the overall compilation rule more general. In the example below, all of the include files should be listed as part of the macro DEPS, and all of the object files should be listed as part of the macro OBJ.

**Makefile 4**

```makefile
CC=gcc
CFLAGS=-I.
DEPS = hellomake.h
OBJ = hellomake.o hellofunc.o 

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

hellomake: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
```

So what if we want to start putting our .h files in an **include directory**, our source code in a **src directory**, and some **local libraries** in a lib directory? Also, can we somehow hide those **annoying .o files** that hang around all over the place? The answer, of course, is yes. The following makefile defines paths to the include and lib directories, and places the object files in an obj subdirectory within the src directory. It also has a macro defined for any libraries you want to include, such as the math library -lm. This makefile should be located in the src directory. Note that it also includes a rule for cleaning up your source and object directories if you type make clean. The .PHONY rule keeps make from doing something with a file named clean.

**Makefile 5**

```makefile
IDIR =../include
CC=gcc
CFLAGS=-I$(IDIR)

ODIR=obj
LDIR =../lib

LIBS=-lm

_DEPS = hellomake.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = hellomake.o hellofunc.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


$(ODIR)/%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

hellomake: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ 
```
So now you have a perfectly good makefile that you can modify to manage small and medium-sized software projects. You can add multiple rules to a makefile; you can even create rules that call other rules. For more information on makefiles and the make function, check out the GNU Make Manual, which will tell you more than you ever wanted to know (really).