# widnows BAT脚本编写

simple: <https://blog.csdn.net/happydecai/article/details/78794948>

detail: <https://blog.csdn.net/zmken497300/article/details/51814817>

## basic

- `echo`、`@`、`call`、`pause`、rem(小技巧：用`::`代替`rem`)是批处理文件最常用的几个命令，我们就从他们开始学起。 
- `echo` 表示显示此命令后的字符 
- `echo off` 表示在此语句后所有运行的命令都不显示命令行本身 
- `@`与`echo off`相象，但它是加在每个命令行的最前面，表示运行时不显示这一行的命令行（只能影响当前行）。 
- `call` 调用**另一个批处理文件**（如果不用call而直接调用别的批处理文件，那么执行完那个批处理文件后将无法返回当前文件并执行当前文件的后续命令）。 
- `pause` 运行此句会暂停批处理的执行并在屏幕上显示Press any key to continue...的提示，等待用户按任意键后继续 
- `rem` 表示此命令后的字符为解释行（注释），不执行，只是给自己今后参考用的（相当于程序中的注释）

```bat
echo off

REM most used command: echo, @, call, pause, rem, ::
:: this is also a comment
rem this is also comment, bat don't care letter's case

rem %0-9, command line args, %0 is bat file self
dir . > %1
echo this is mybat 

REM call bat1.bat

dir . | findstr %1

pause
del %1
```

### if statement

`if /?` for help

if [not] "参数" == "字符串"
if "%a%" == "aaa" echo aaa
if [not] exist [路径\]文件名 待执行的命令
if errorlevel  <数字> 待执行的命令

>  cmd and batch in diff, use `%i` in cmd, `%%i` instead in batch file,

cmd `for %i in (*.txt) do @echo %i`
batch `for %%i in (1 2 3 4 5) do @echo %%i`


`choice /?`

```bat
ERRORLEVEL 环境变量被设置为从选择集选择的键索引。列出的第一个选
择返回 1，第二个选择返回 2，等等。如果用户按的键不是有效的选择，
该工具会发出警告响声。如果该工具检测到错误状态，它会返回 255 的
ERRORLEVEL 值。如果用户按 Ctrl+Break 或 Ctrl+C 键，该工具会返回 0
的 ERRORLEVEL 值。在一个批程序中使用 ERRORLEVEL 参数时，将参数降
序排列。

示例:
   CHOICE /? 
   CHOICE /C YNC /M "确认请按 Y，否请按 N，或者取消请按 C。"
   CHOICE /T 10 /C ync /CS /D y
   CHOICE /C ab /M "选项 1 请选择 a，选项 2 请选择 b。"
   CHOICE /C ab /N /M "选项 1 请选择 a，选项 2 请选择 b。"
```

```bat
@echo off 
choice /C ABC /M "help msg"

if errorlevel 1 goto A
if errorlevel 2 goto B 
if errorlevel 3 goto C

:A 
echo "here is A"
goto end

:B 
echo "here is B"
goto end

:C 
echo "here is C"
goto end

:end
echo "end message"
```

### CALL

CALL命令可以在批处理执行过程中调用另一个批处理，当另一个批处理执行完后，再继续执行原来的批处理

```bat
CALL command
调用一条批处理命令，和直接执行命令效果一样，特殊情况下很有用，比如变量的多级嵌套，见教程后面。在批处理编程中，可以根据一定条件生成命令字符串，用call可以执行该字符串，见例子。
CALL [drive:][path]filename [batch-parameters]
调用的其它批处理程序。filename 参数必须具有 .bat 或 .cmd 扩展名。
CALL :label arguments
调用本文件内命令段，相当于子程序。被调用的命令段以标签:label开头
以命令goto :eof结尾。
另外，批脚本文本参数参照(%0、%1、等等)已如下改变:
     批脚本里的 `%*` 指出所有的参数(如 %1 %2 %3 %4 %5 …)
     批参数(%n)的替代已被增强。您可以使用以下语法:（看不明白的直接运行后面的例子）
         %~1         - 删除引号(“)，扩充 %1
         %~f1        - 将 %1 扩充到一个完全合格的路径名
         %~d1        - 仅将 %1 扩充到一个驱动器号
         %~p1        - 仅将 %1 扩充到一个路径
         %~n1        - 仅将 %1 扩充到一个文件名
         %~x1        - 仅将 %1 扩充到一个文件扩展名
         %~s1        - 扩充的路径指含有短名
         %~a1        - 将 %1 扩充到文件属性
         %~t1        - 将 %1 扩充到文件的日期/时间
         %~z1        - 将 %1 扩充到文件的大小
   可以组合修饰符来得到多重结果:
         %~dpI       - 仅将 %I 扩展到一个驱动器号和路径
```

**NOTE**: `:eof` system defined lable, `%0` cmd self, a exe, bat file or lable

```bat
@echo off
Echo 产生一个临时文件 > tmp.txt
Rem 下行先保存当前目录，再将c:\windows设为当前目录
pushd c:\windows
Call :sub tmp.txt
Rem 下行恢复前次的当前目录
Popd
Call :sub tmp.txt
Del tmp.txt
goto :eof

:sub
echo %0 %1 %2 %3 %4
echo %*
Echo 删除引号： %~1
Echo 扩充到路径： %~f1
Echo 扩充到一个驱动器号： %~d1
Echo 扩充到一个路径： %~p1 
Echo 扩充到一个文件名： %~n1
Echo 扩充到一个文件扩展名： %~x1
Echo 扩充的路径指含有短名： %~s1 
Echo 扩充到文件属性： %~a1 
Echo 扩充到文件的日期/时间： %~t1 
Echo 扩充到文件的大小： %~z1 
Goto :eof
```

### errorlevel

IF ERRORLEVEL 是用来测试它的**上一个DOS命令的返回值**的，注意只是上一个命令的返回值，而且返回值必须依照从大到小次序顺序判断。**通常用非零值表示错误**
因此下面的批处理文件是错误的：

**ERROR**

```bat
@ECHO OFF 
XCOPY C:\AUTOEXEC.BAT D:\ 
IF ERRORLEVEL 0 ECHO 成功拷贝文件 
IF ERRORLEVEL 1 ECHO 未找到拷贝文件 
IF ERRORLEVEL 2 ECHO 用户通过ctrl-c中止拷贝操作 
IF ERRORLEVEL 3 ECHO 预置错误阻止文件拷贝操作 
IF ERRORLEVEL 4 ECHO 拷贝过程中写盘错误
```

### setlocal and variable delay

see `set /?`

```bat
rem setlocal and variable delayed

    set VAR=before
    if "%VAR%" == "before" (
        set VAR=after
        if "%VAR%" == "after" @echo If you see this, it worked
    )

would never display the message, Similarly, the following example
will not work as expected:

    set LIST=
    for %i in (*) do set LIST=%LIST% %i
    echo %LIST%

 the actual FOR loop we are executing is:

    for %i in (*) do set LIST= %i

which just keeps setting LIST to the last file found.

    setlocal enabledelayedexpansion

    set VAR=before
    if "%VAR%" == "before" (
        set VAR=after
        if "!VAR!" == "after" @echo If you see this, it worked
    )

    set LIST=
    for %i in (*) do set LIST=!LIST! %i
    echo %LIST%
```

### for statement

`for /?` for help

cmd `for %i in (*.txt) do @echo %i`
batch `for %%i in (1 2 3 4 5) do @echo %%i`

- /D match only dir
- /R recursive
- 

```bat
for /r %%i in (*.exe) do echo %%i
for /r c:\ %%i in (boot.int) do echo %%i

FOR /L %%variable IN (start,step,end) DO command [command-parameters]
    该集表示以增量形式从开始到结束的一个数字序列。
    因此，(1,1,5) 将产生序列 1 2 3 4 5，(5,-1,1) 将产生
    序列 (5 4 3 2 1)。
```

## common special chars

- `@`  命令行回显屏蔽符
- `%`  批处理变量引导符
- `>`   重定向符
- `>>`  重定向符
- `<、>&、<&` 重定向符
- `|`  命令管道符
- `^`  转义字符
- `&`  组合命令
- `&&` 组合命令
- `||`  组合命令
- `“` 字符串界定符
- , 逗号
- ; 分号
- `()` 括号
- ! 感叹号
- : （略）
   - CR(0D) 命令行结束符 
   - Escape(1B) ANSI转义字符引导符 
   - Space(20) 常用的参数界定符 
   - Tab(09) ; = 不常用的参数界定符 
   - + COPY命令文件连接符 
   - `* ?` 文件通配符 
   - `/` 参数开关引导符 
   - `:` 批处理标签引导符 


```bat
%0  %1  %2  %3  %4  %5  %6  %7  %8  %9  %*为命令行传递给批处理的参数
%0 批处理文件本身，包括完整的路径和扩展名
%1 第一个参数
%9 第九个参数
%* 从第一个参数开始的所有参数
参数%0具有特殊的功能，可以调用批处理自身，以达到批处理本身循环的目的，也可以复制文件自身等等。
例：最简单的复制文件自身的方法
copy %0 d:\wind.bat

>>  重定向符
输出重定向命令
这个符号的作用和>有点类似，但他们的区别是>>是传递并在文件的末尾追加，而>是覆盖

<，输入重定向命令，从文件中读入命令输入，而不是从键盘中读入。
echo 2005-05-01>temp.txt
date < temp.txt

句柄0：标准输入stdin，键盘输入
句柄1：标准输出stdout，输出到命令提示符窗口（console，代码为CON）
句柄2：标准错误stderr，输出到命令提示符窗口（console，代码为CON）

set /p str=<%0
echo %str%

error redirect
&2>1 && 1>out.txt

|  命令管道符
格式：第一条命令 | 第二条命令 [| 第三条命令…]
将第一条命令的结果作为第二条命令的参数来使用，记得在unix中这种方式很常见。
echo y|format a: /s /q /v:system

^  转义字符
^是对特殊符号<,>,&的前导字符，在命令中他将以上3个符号的特殊功能去掉，仅仅只把他们当成符号而不使用他们的特殊意义。
比如
echo test ^>1.txt
结果则是：test > 1.txt

转义字符还可以用作续行符号。
举个简单的例子：
@echo off
echo 英雄^
是^
好^
男人

& 当第一个命令执行失败了，也不影响后边的命令执行
dir z:\ & diz c:\

&& 第一个命令失败时，后边的命令也不会执行
|| 当一条命令失败后才执行第二条命令

" 双引号允许在字符串中包含空格，进入一个特殊目录可以用如下方法
cd “program files”
cd progra~1
cd pro*

, 逗号
逗号相当于空格，在某些情况下“,”可以用来当做空格使
比如
dir,c:\

() 括号
小括号在批处理编程中有特殊的作用，左右括号必须成对使用，括号中可以包括多行命令，这些命令将被看成一个整体，视为一条命令行。
    括号在for语句和if语句中常见，用来嵌套使用循环或条件语句，其实括号()也可以单独使用，请看例子。
命令：echo 1 & echo 2 & echo 3
可以写成：
(
echo 1
echo 2
echo 3
)

! 感叹号
没啥说的，在变量延迟问题中，用来表示变量，即%var%应该表示为!var!
```
## useful env variables

```bat
%cd%
%home%
%time%
%date%
%path%
%userprofile%
```

## useful command

cmd help, `cmd /?`, like `findstr /?`, `set ? > help.txt`

The **ELSE clause** must occur on the **same line** as the command after the IF.

`setlocal enabledelayedexpansion`

```bat
rem 简单批处理内部命令简介 
@echo off
echo on
@
echo hello bat
goto
rem
pause
call

rem set global variable, 不能有空格等号两边
set a=1
set /A a=(24*60)
set /P a="input prompt msg"

rem access var
%a%


IF [NOT] ERRORLEVEL number command
IF [/i]  [NOT] string1==string2 command
IF [NOT] EXIST filename command
IF DEFINED variable command

IF [/I] string1 compare-op string2 command

    EQU - equal
    NEQ - not equal
    LSS - less than
    LEQ - less than or equal
    GTR - greater than
    GEQ - greater than or equal

IF EXIST filename (
   del filename
) ELSE (
   echo filename missing
)


rem 调用外部程序，所有的DOS命令和命令行程序都可以由start命令来调用,/min /max
start   

rem choice /c YN /m "msg prompt"
choice   

findstr
find

rem show all env var
set   
rem show all enviroment var with prefix p
set p  

rem show path
set path || echo %path%

tasklist | findstr -i pycharm
taskkill

cls
type file

mkdir
rmdir
echo "# new file" > tmp.txt
del
```

## sample

```bat
@echo off
cls
title 终极多功能修复
:menu
cls
color 0A
echo.
echo                 ==============================
echo                 请选择要进行的操作，然后按回车
echo                 ==============================
echo.
echo              1.网络修复及上网相关设置,修复IE,自定义屏蔽网站
echo.
echo              2.病毒专杀工具，端口关闭工具,关闭自动播放
echo.
echo              3.清除所有多余的自启动项目，修复系统错误
echo.
echo              4.清理系统垃圾,提高启动速度
echo.
echo              Q.退出
echo.
echo.
:cho
set choice=
set /p choice=          请选择:
IF NOT “%choice%”==”” SET choice=%choice:~0,1%
if /i “%choice%”==”1” goto ip
if /i “%choice%”==”2” goto setsave
if /i “%choice%”==”3” goto kaiji
if /i “%choice%”==”4” goto clean
if /i “%choice%”==”Q” goto endd
echo 选择无效，请重新输入
echo.
goto cho
```