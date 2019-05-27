# Shell

# Syntax

## variable

```shell
# no space around equal
name="define a variable"
echo $name      # name var

# 在Bash shell环境中，用普通的变量赋值方法定义数值，它会被存储为字符串。因此没法直接做数学运算。
# 这时，可以利用let、(( ))、[]和expr进行整数运算，使用bc进行浮点数，平方，进制转换等运算

# 用普通的变量赋值, if contains space, use "" or ''

# strings
# 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
# 双引号里可以有变量 
# 双引号里可以出现转义字符
echo "name = ${name}"
echo 'name = ${name}'

# 利用let、(( ))、[], 变量名之前可以加$,也可不加$
let a=23
let b=aabb
echo $a $b

no1=16
no2=8
# 利用let执行数学运算。使用let执行运算时，变量名之前不需要添加$
let result=no1\*no2
echo $result
let no1++
echo $no1

# (())
echo $((no1+no2))

# []
echo $[no2 + ++no1]

# expr执行数学运算。expr变量名之前必须加$，且变量名与运算符号之间必须留一个空格，不然不执行算数运算
echo $(expr $no1 + $no2)
echo `expr $no1 + 2`


# for statement
# note backtick

for f in `ls .sh`; do
    echo $f
done

for f in $(ls *.sh) do
    echo $f
done

# use variable inside string: "$var"
# use ${var}, recommend

# for skill in Ada Coff; do
#     echo "i am good at $skill script"
# done

for skill in Ada Python shell; do
    echo "i am good at ${skill}Script"
done

# readonly var

# myurl="baidu.com"
# readonly myurl
# myurl="www.baidu.com"

# unset var

# unset name
# echo $name


# 使用双引号拼接
greeting="hello, "$name" !"

# 获取字符串长度
string="abcd"
echo ${#string} #输出 4

# substring, ${string:startIndex:length}
echo ${greeting::4} # hell


```

## cmd args

shell command line args
like batch cmd args, use `$0-n`, `$0` is self

- `$#`	传递到脚本的参数个数
- `$$`	脚本运行的当前进程ID号
- `$!`	后台运行的最后一个进程的ID号

- `$*`	以一个单字符串显示所有向脚本传递的参数。 如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。
- `$@`	与$*相同，但是使用时加引号，并在引号中返回每个参数。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。

- `$-`	显示Shell使用的当前选项，与set命令功能相同。
- `$?`	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。

```shell
echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done
```

## array

`array=(a b c)`

```shell
ar=(1 2 3)
echo ${ar[0]}   # 1
echo ${ar[@]}   # 1 2 3

# walk through
for i in ${ar[@]}
do
    echo $i
done

i=0
while [ $i -lt ${arr[$i]} ]; do
    echo ${arr[$i]}
    let i++
    # let "i++"
    # $i=$[$i + 1]
done

# arr_len
ar_len=${#ar[@]} && echo $ar_len
ar_len=${#ar[*]} && echo $ar_len

hello_string="hello,everyone my name is xiaoming"
echo $(expr length "$hello_string")
```

## 基本运算

- 算数运算符
- 关系运算符
- 布尔运算符
- 字符串运算符
- 文件测试运算符

原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用。
**expr 是一款表达式计算工具**，使用它能完成表达式的求值操作。

两个数相加(注意使用的是**反引号** 而不是单引号)：

```shell
val=`expr 2 + 2`
echo "两数之和为 : $val" # 两数之和为 : 4

val=`expr $a \* $b` # escape
echo "a * b : $val"
```


**NOTE**:

- **表达式和运算符之间要有空格**，例如 2+2 是不对的，必须写成 2 + 2，这与我们熟悉的大多数编程语言不一样。
- 完整的表达式要被 ` ` 包含，注意这个字符不是常用的单引号，在 Esc 键下边。

乘号(*)前边some time必须加反斜杠(\)才能实现乘法运算；


### 关系运算符

`-eq, -ne, -gt, -lt, ge, le`

**NOTE**: 条件表达式要放在方括号之间，并且要有空格，例如: [$a==$b] 是错误的，必须写成 [ $a == $b ]。

```shell
a=10
b=20

if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi
```

### 布尔运算符

`!, -o, ||, -a, &&`

### 字符串compare

- `=`	检测两个字符串是否相等，相等返回 true	
- `!=`	检测两个字符串是否相等，不相等返回 true
- `-z`	检测字符串长度是否为0，为0返回 true
- `-n`	检测字符串长度是否为0，不为0返回 true。	
- `$`	检测字符串是否为空，不为空返回 true。	

### 文件测试运算符

- `-b file`	检测文件是否是**块设备文件**，如果是，则返回 true。	[ -b $file ] 返回 false。
- `-c file`	检测文件是否是字符设备文件，如果是，则返回 true。	[ -c $file ] 返回 false。
- `-d file`	检测文件是否是**目录**，如果是，则返回 true。	[ -d $file ] 返回 false。
- `-f file`	检测文件是否是**普通文件**（既不是目录，也不是设备文件），如果是，则返回 true。	[ -f $file ] 返回 true。
- `-g file`	检测文件是否设置了 SGID 位，如果是，则返回 true。	[ -g $file ] 返回 false。
- `-k file`	检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。	[ -k $file ] 返回 false。
- `-p file`	检测文件是否是有名管道，如果是，则返回 true。	[ -p $file ] 返回 false。
- `-u file`	检测文件是否设置了 SUID 位，如果是，则返回 true。	[ -u $file ] 返回 false。
- `-r file`	检测文件是否可读，如果是，则返回 true。	[ -r $file ] 返回 true。
- `-w file`	检测文件是否可写，如果是，则返回 true。	[ -w $file ] 返回 true。
- `-x file`	检测文件是否**可执行**，如果是，则返回 true。	[ -x $file ] 返回 true。
- `-s file`	检测**文件是否为空**（文件大小是否大于0），不为空返回 true。	[ -s $file ] 返回 true。
- `-e file`	检测文件（包括目录）是否存在，如果是，则返回 true。	[ -e $file ] 返回 true。
- `-S` 判断某文件是否 socket。
- `-L` 检测文件是否存在并且是一个符号链接。

### note and conclusion

- 使用 [[ ... ]] 条件判断结构，而不是 [ ... ]，能够防止脚本中的许多逻辑错误。比如，&&、||、< 和 > 操作符能够正常存在于 [[ ]] 条件判断结构中，但是如果出现在 [ ] 结构中的话，会报错。
- 进行数值比较时,OP可以为 -gt、-lt、-ge、-le、-eq、-ne 也可以为 >、<、>=、<=、==、!=
- `>、<、==、!=`也可以进行字符串比较。
- 行字符串比较时，== 可以使用 = 替代。
- `>`和`<`进行字符串比较时，需要使用[[ string1 OP string2 ]] 或者 [ string1 \OP string2 ]。也就是使用 [] 时，> 和 < 需要使用反斜线转义

**字符串比较是否为null**

```shell
a=""
if [ -n $a ]
then
   echo "-n $a : 字符串长度不为 0"
else
   echo "-n $a : 字符串长度为 0"
fi
# -n  : 字符串长度不为 0
```

从结果上看 -n $a 返回 true，这并正确，正确的做法是 $a 这里应该加上双引号，否则 -n $a 的结果永远是 true：

```shell
a=""
if [ -n "$a" ]
then
   echo "-n $a : 字符串长度不为 0"
else
   echo "-n $a : 字符串长度为 0"
fi
# -n  : 字符串长度为 0
```

## shell statements

```shell
if [ condition1 ]
then
    cmds
elif
    cmds
else
    cmds
fi
# 写成一行（适用于终端命令提示符）：
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi;

for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
# 写成一行：
for var in item1 item2 ... itemN; do command1; command2… done;

for((i=1;i<=5;i++));do
    echo "这是第 $i 次调用";
done;

while condition
do
    command
done

int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done

# infinity loop
for (( ; ; ))
```

`case` statement

case工作方式如上所示。取值后面必须为单词in，**每一模式必须以右括号结束**。取值可以为**变量或常数**。匹配发现取值符合某一模式后，其间**所有命令开始执行直至 `;;`**。

取值将检测匹配的每一个模式。**一旦模式匹配，则执行完匹配模式相应命令后不再继续其他模式**。如果无一匹配模式，使用**星号 * 捕获**该值，再执行后面的命令。

```shell
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
```

`break`, `continue`

## shell function

linux shell 可以用户定义函数，然后在shell脚本中可以随便调用。

shell中函数的定义格式如下：

```shell
[ function ] funname [()]
{
    action;
    [return int;]
}
```

- 可以带function fun() 定义，也可以直接fun() 定义,不带任何参数。
- 参数返回，可以显示加：return 返回，**如果不加，将以最后一条命令运行结果**，作为返回值。 **return后跟数值**n(0-255)
- 函数返回值在调用该函数后通过 `$?` 来获得。
- $10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。

```shell
demoFun(){
    echo "这是我的第一个 shell 函数!"
}
demoFun

funWithReturn(){
    aNum=1
    anotherNum=2
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return "hello"
}
funWithReturn
echo "输入的两个数字之和为 $? !"

funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
```

# useful commands

```shell
# interactive
echo
printf
read -p msg

. filename   # 注意点号(.)和文件名中间有一空格
source filename
```

# Samples

## zookeeper service

```bash
#!/usr/bin/bash
# chkconfig:2345 20 90
# description:zookeeper
# processname:zookeeper

export JAVA_HOME=/usr/local/src/java/jdk1.8.0_192/jre
export ZOO_LOG_DIR=/usr/local/zookeeper-3.4.12
EXEC=/usr/local/zookeeper-3.4.12/bin/zkServer.sh

case "$1" in
    start) 
        $EXEC start
        ;;
    stop) 
        $EXEC stop
        ;;
    status) 
        $EXEC status
        ;;
    restart)
        $EXEC restart
        ;;
    *) 
        echo "require start|stop|status|restart" >&2 
        exit 1
        ;;
esac
```

> `# chkconfig:2345 20 90` chkconfig enabled

## redis service

```bash
#!/usr/bin/bash
# chkconfig: 2345 10 90  
# description: Start and Stop redis   
  
PATH=/usr/local/bin:/sbin:/usr/bin:/bin   
REDISPORT=6379  
EXEC=/usr/local/redis/bin/redis-server
REDIS_CLI=/usr/local/redis/bin/redis-cli   
 
PIDFILE=/var/run/redis.pid   
CONF="/usr/local/redis/bin/redis.conf"  
AUTH="1234"  

case "$1" in   
    start)   
        if [ -f $PIDFILE ]   
        then   
            echo "$PIDFILE exists, process is already running or crashed."  
        else  
            echo "Starting Redis server..."  
            $EXEC $CONF   
        fi   
        if [ "$?"="0" ]   
        then   
            echo "Redis is running..."  
        fi   
        ;;   
    stop)   
        if [ ! -f $PIDFILE ]   
        then   
            echo "$PIDFILE exists, process is not running."  
        else  
            PID=$(cat $PIDFILE)   
            echo "Stopping..."  
            $REDIS_CLI -p $REDISPORT  SHUTDOWN    
            sleep 2  
            while [ -x $PIDFILE ]   
            do  
                echo "Waiting for Redis to shutdown..."  
                sleep 1  
            done   
            echo "Redis stopped"  
        fi   
        ;;   
    restart|force-reload)   
        ${0} stop   
        ${0} start   
        ;;   
    *)   
        echo "Usage: /etc/init.d/redis {start|stop|restart|force-reload}" >&2  
        exit 1  
esac
```

