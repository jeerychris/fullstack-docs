[linux下的find文件查找命令与grep文件内容查找命令](https://www.cnblogs.com/zhangmo/p/3571735.html)

# find vs grep

- find命令是根据**文件的属性**进行查找，如文件名，文件大小，所有者，所属组，是否为空，访问时间，修改时间等。 
- grep是根据**文件的内容进行**查找，会对文件的每一行按照给定的模式(patter)进行匹配查找。

# find

```shell
-type    b/d/c/p/l/f         #查是块设备、目录、字符设备、管道、符号链接、普通文件
-follow                      #如果遇到符号链接文件，就跟踪链接所指的文件
```

## **基本格式：**find  path expression

**1.按照文件名查找**

1. find / **-name** httpd.conf | **xargs** ls -l　　#在根目录下查找文件httpd.conf，表示在整个硬盘查找
2. find /etc **-iname** httpd.conf　　#在/etc目录下文件Httpd.conf
3. find /etc -name '*srm*'　　#使用通配符*(0或者任意多个)。表示在/etc目录下查找文件名中含有字符串‘srm’的文件
4. find . -name 'srm*' 　　#表示当前目录下查找文件名开头是字符串‘srm’的文件

**2.按照文件特征查找** 　　　　

1. find / -amin -10 　　# 查找在系统中最后10分钟访问的文件(access time)
2. find / -atime -2　　 # 查找在系统中最后48小时访问的文件
3. find / -empty 　　# 查找在系统中为空的文件或者文件夹
4. find / -group cat 　　# 查找在系统中属于 group为cat的文件
5. find / -mmin -5 　　# 查找在系统中最后5分钟里修改过的文件(modify time)
6. find / -mtime -1 　　#查找在系统中最后24小时里修改过的文件
7. find / -user fred 　　#查找在系统中属于fred这个用户的文件
8. find / -size +10000c　　#查找出大于10000000字节的文件(c:字节，w:双字，k:KB，M:MB，G:GB)
9. find / -size -1000k 　　#查找出小于1000KB的文件

**3.使用混合查找方式查找文件**

**参数有： ！，-and(-a)，-or(-o)。**

1. find /tmp -size +10000c -and -mtime +2 　　#在/tmp目录下查找大于10000字节并在最后2分钟内修改的文件
2. find / -user fred -or -user george 　　#在/目录下查找用户是fred或者george的文件文件
3. find /tmp ! -user panda　　#在/tmp目录中查找所有不属于panda用户的文件 　　  

## Advanced

```shell
# 查当前目录下的所有普通文件
find . -type f -exec ls -l {} \;

# 查询文件并询问是否要显示
find ./ -mtime -1 -type f -ok ls -l {} \; 

find /usr/ -iname *sql* -type d | xargs ls --full-time --color=auto
```

# **二、grep命令**

## **基本格式：find  expression**

**1.主要参数**

**[options]主要参数：**

**pattern正则表达式主要参数：**

- \： 忽略正则表达式中特殊字符的原有含义。
- ^：匹配正则表达式的开始行。
- $: 匹配正则表达式的结束行。
- \<：从匹配正则表达 式的行开始。
- \>：到匹配正则表达式的行结束。
- [ ]：单个字符，如[A]即A符合要求 。
- [ - ]：范围，如[A-Z]，即A、B、C一直到Z都符合要求 。
- .：所有的单个字符。
- * ：有字符，长度可以为0。

**2.实例**　 

(1) grep 'test' d*　　#显示所有以d开头的文件中包含 test的行
(2) grep ‘test’ aa bb cc 　　 #显示在aa，bb，cc文件中包含test的行
(3) grep ‘[a-z]\{5\}’ aa 　　#显示所有包含每行字符串至少有5个连续小写字符的字符串的行
(4) grep magic /usr/src　　#显示/usr/src目录下的**文件(不含子目录)**包含magic的行
(5) grep -r magic /usr/src　　#显示/usr/src目录下的**文件(包含子目录)**包含magic的行

(6)grep -w pattern files ：只匹配**整个单词**，而不是字符串的一**部分**(如匹配’magic’，而不是’magical’)，

## Advanced

`grep ‘w\(es\)t.*\1′ aa`
如果west被匹配，则es就被存储到内存中，并标记为1，然后搜索任意个字符(.*)，这些字符后面紧跟着 另外一个es(\1)，找到就显示该行。如果用**egrep或grep -E**，就不用”\”号进行转义，直接写成’w(es)t.*\1′就可以了。

[grep-common-usages](http://www.cnblogs.com/end/archive/2012/02/21/2360965.html)
[find-common-usages](https://www.cnblogs.com/archoncap/p/6144369.html)