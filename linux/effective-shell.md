# Bash shortcuts

## 移动

==ctrl + a==      将光标移动到命令行开头相当于VIM里shift+^
==ctrl + e==      将光标移动到命令行结尾处相当于VIM里shift+$
ctrl + f      光标向后移动一个字符相当于VIM里l
ctrl + b      光标向前移动一个字符相当于VIM里h



## Edit

ctrl + k      删除光标后面所有字符相当于VIM里d shift+$
==ctrl + h==      删除光标所在位置前的字符相当于VIM里hx或者dh
ctrl + u      删除光标前面所有字符相当于VIM里d shift+^
==ctrl + w==      删除光标前一个单词相当于VIM里db
ctrl + y      copy上次执行时删除的字符

==ctrl + ?==      撤消前一次输入

## 历史命令编辑

ctrl + p   返回上一次输入命令字符

ctrl + n

==ctrl + r==       输入单词搜索历史命令, cooperate with `ctrl+h`

==history |  less==

**!n 编号为n的历史命令**

不用再复制粘贴，或者照着历史记录敲了。**执行历史命令记录里面的某个命令**，只需要 ! + 这条命令记录前的序号，比如

```shell
!767
```

**!! 上一条命令**

!! 表示上一条命令，相当于 !-1 。

**!keyword 查找包含该keyword的历史命令**

如果想查找包含某个关键字的历史命令，可以这样做

查找包含keyword的历史命令，然后**回车就能执行这条历史命令**

**history | grep keyword 列出所有符合条件的命令**

Ctrl + R 无疑是最方便常用的历史记录搜索方式，但是当然也可以用 history | grep keyword 来查找所有的符合条件的记录，然后再结合刚刚的! 方法完成命令。

## 其它
Tab		can double
ctrl + s      stop screen print
ctrl + q      resume screen print
==ctrl + l==        清屏相当于命令clear
==Ctrl + C==	这个键可不是用来复制的，在中端下，按下Ctrl+C就代表结速当前终端执行的程序，按下的时候一定要慎重。
==Ctrl + Z==	把当前进程送到后台处理。
`bg`
`fg`

# tools

## fzf

> like windows **everything**, a linux **fuzzy find** tool, fast and powerfull

