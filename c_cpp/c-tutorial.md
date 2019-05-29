# C

https://www.runoob.com/cprogramming/

C语言最初是用于系统开发工作

- 操作系统
- 语言编译器
- 汇编器
- 文本编辑器
- 打印机
- 网络驱动器
- 现代程序
- 数据库
- 语言解释器
- 实体工具

# syntax

## C关键字：

按年份起始：

- `auto` `break` `case` `char` `const` `continue` `default` `do` 
- `double` `else` `enum` `extern` `float` `for` `goto` `if` 
- `int` `long` `register` `return` `short` `signed` `sizeof` `static` 
- `struct` `switch` `typedef` `union` `unsigned` `void` `volatile` `while`

1999年12月16日，ISO推出了C99标准，该标准新增了5个C语言关键字：

`inline` `restrict` `_Bool` `_Complex` `_Imaginary`

2011年12月8日，ISO发布C语言的新标准**C11**，该标准新增了7个C语言关键字：

`_Alignas` `_Alignof` `_Atomic` `_Static_assert` `_Noreturn` `_Thread_local` `_Generic`

## data type

C 中的类型可分为以下几种：

| 序号 | 类型与描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | **基本类型：** 它们是算术类型，包括两种类型：整数类型和浮点类型。 |
| 2    | **枚举类型：** 它们也是算术类型，被用来定义在程序中只能赋予其一定的离散整数值的变量。 |
| 3    | **void 类型：** 类型说明符 *void* 表明没有可用的值。         |
| 4    | **派生类型：** 它们包括：**指针类型**、**数组类型**、**结构类型**、**共用体类型**和**函数类型**。 |

**NOTE**
- 表达式 `sizeof(type)` 得到对象或类型的存储字节大小
- the essence of type: **the size when memory allocate**
- 类型**自动转换, 高精度>低精度**, like `int a = 2.0`,  else must transformed explicitly

### void 类型

void 类型指定没有可用的值。它通常用于以下三种情况下：

- **函数返回为空** C 中有各种函数都不返回值，或者您可以说它们返回空。不返回值的函数的返回类型为空。例如 **void exit (int status);**
- **函数参数为空** C 中有各种函数不接受任何参数, can ignore。不带参数的函数可以接受一个 void。例如 **int rand(void);**
- **指针指向 void** 类型为 void * 的指针代表对象的地址，而不是类型。例如，内存分配函数 **void \*malloc( size_t size );** 返回指向 void 的指针，可以转换为任何数据类型。

## variable

### declare and define

- declare, only let the compiler know the var's existance, there can go through compile phase, **no memory allocated**
- define, equal to declare plus **memory allocate**
- **除非有extern关键字，否则都是变量的定义**。

```c
extern int i; //声明，不是定义
int i; //声明，也是定义
```

### 初始化局部变量和全局变量

当**局部变量被定义时，系统不会对其初始化**，您必须自行对其初始化。定义全局变量时，系统会自动对其初始化，如下所示：

| 数据类型 | 初始化默认值 |
| -------- | ------------ |
| int      | 0            |
| char     | '\0'         |
| float    | 0            |
| double   | 0            |
| pointer  | NULL         |

正确地初始化变量是一个良好的编程习惯，否则有时候程序可能会产生意想不到的结果，因为未初始化的变量会导致一些在内存位置中已经可用的垃圾值。

### lvalue and rvalue

C 中有两种类型的表达式：

1. **左值（lvalue）：****指向内存位置的表达式**被称为左值（lvalue）表达式。左值可以出现在赋值号的左边或右边。
2. **右值（rvalue）：**术语右值（rvalue）指的是**存储在内存中某些地址的数值**。右值是不能对其进行赋值的表达式，也就是说，右值可以出现在赋值号的右边，但不能出现在赋值号的左边。

变量是左值，因此可以出现在赋值号的左边。数值型的字面值是右值，因此不能被赋值，不能出现在赋值号的左边。

```c
int g = 20;
10 = 20
```

### const and #define

在 C 中，有两种简单的定义常量的方式：

- 使用 `#define` 预处理器。
- 使用 `const` 关键字。

**NOTE**: 请注意，把常量定义为大写字母形式，是一个很好的编程实践, like `#define PI 3.141596`

### 两者的区别

**(1) 编译器处理方式不同**

- \#define 宏是在**预处理阶段**展开。
-  const 常量是**编译运行阶段**使用。

**(2) 类型和安全检查不同**

-  \#define 宏没有类型，不做任何类型检查，**仅仅是char substitute**。
-  const 常量**有具体的类型**，**在编译阶段会执行类型检查**。

**(3) 存储方式不同**

- \#define宏仅仅是展开，有多少地方使用，就展开多少次，不会分配内存。（宏定义不分配内存，变量定义分配内存。）
- const常量会在内存中分配(可以是堆中也可以是栈中)。

**(4) const 可以节省空间，避免不必要的内存分配。 例如：**

```c
#define NUM 3.14159 //常量宏
const doulbe Num = 3.14159; //此时并未将Pi放入ROM中 ......
double i = Num; //此时为Pi分配内存，以后不再分配！
double j = Num; //没有内存分配
double I= NUM; //编译期间进行宏替换，分配内存
double J = NUM; //再进行宏替换，又一次分配内存！
```

const 定义常量从汇编的角度来看，只是给出了对应的内存地址，而不是象 #define 一样给出的是立即数，所以，const 定义的常量在程序运行过程中只有一份拷贝（因为是全局的只读变量，存在静态区），而 #define 定义的常量在内存中有若干个拷贝。

**(5) 提高了效率。 编译器通常不为普通const常量分配存储空间，而是将它们保存在符号表中，这使得它成为一个编译期间的常量，没有了存储与读内存的操作，使得它的效率也很高。**

宏预编译时就替换了，程序运行时，并不分配内存。

### #define  “边缘效应”

例：`#define N 2+3`, N 的值是 5。

```c
int a = N/2
```

在编译时我们预想 **a=2.5**，实际打印结果是 **3.5** 原因是在预处理阶段，编译器将 a=N/2 处理成 a=2+3/2，这就是 **define** 宏的边缘效应，所以我们应该写成 `#define N (2+3)`

## operator

```c
#define max(a, b) ((a>b) ? a : b)
```

## condition

no bool type in c, 0 is false, not 0 is true

## loop

for, while, do..while,

<kbd>Ctrl</kbd>+<kbd>C</kbd> to stop infinity loop: `for(;;){}`

## function

args transformed by value

```c
// allocate mem outside function
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

**内部函数**

如果一个函数只能被本文件中其他函数所调用，它称为内部函数。在定义内部函数时，在函数名和函数类型的前面加 `static`.

**外部函数**

如果在定义函数时，在函数的首部的最左端加关键字 `extern`，则此函数是外部函数，可供其它文件调用

> C 语言规定，如果在定义函数时省略 `extern`，则默认为外部函数。

**内联函数**

内联函数是指用`inline`关键字修饰的函数。在类内定义的函数被默认成内联函数。内联函数从源代码层看，有函数的结构，而在编译后，却不具备函数的性质。

内联扩展是用来**消除函数调用时的时间开销**。它通常用于频繁执行的函数，对于小内存空间的函数非常受益。

使用内联函数的时候要注意：

- 递归函数不能定义为内联函数

- 内联函数一般适合于不存在while和switch等复杂的结构且只有1~5条语句的小函数上，否则编译系统将该函数视为普通函数。

- 内联函数只能先定义后使用，否则编译系统也会把它认为是普通函数。

- 对内联函数不能进行异常的接口声明。

```c
inline void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}
```

**前置声明**

## array

**define**: type name[size]

**init**: `int a[10] = {0}`, all elements assigned to 0

```c
#include <stdio.h>

int main()
{
    double arr[10] = {0};

    for(int i=0; i<sizeof(arr)/sizeof(double); i++)
        printf("%d ", arr[i]);
    printf("\n");

    // two dimension array[i][j], i row j column, all ele init to 0
    int a[3][4] = {0};
    for(int i=0; i<3; i++)
        {
        for(int j=0; j<4; j++)
                printf("%d ", a[i][j]);
        printf("\n");
        }
    return 0;
}
```

### 二维数组

在逻辑上是方阵，由行和列组成。

但是二维数组在物理上是线性的，按行来依次进行存放，内存是连续的。

二维数组名的步长是一行的长度，比如一下例子中：

```c
age + 1 address is 00EFFC04
age + 2 address is 00EFFC14
```

因为每一行有四个元素，每个int类型的元素占四个字节，一行有16个字节，所以数组名age加1后地址增加了16个字节说明数组名的步长位一行的长度。

具体到每一个元素加1的时候，地址增加的是一个元素所占字节的大小，因此元素的步长即为元素本身的大小，例如：

```c
age[2][0] + 0 address is 00EFFC14
age[2][0] + 1 address is 00EFFC18
```

示例及运行结果：

```c
#include <stdio.h>

int main()
{
    int age[6][4];
    for (int i = 0; i < sizeof(age)/sizeof(age[0]) ; i++)
        printf("age + %d address is %p\n",i, age + i);

    for (int i = 0; i < sizeof(age) / sizeof(age[0]); i++)
        for (int j = 0; j < sizeof(age[0]) / sizeof(int); j++)
            printf("age[%d][0] + %d address is %p\n",i,j,&age[i][0]+j);
}
```

more see `c-array.md`

## enum

```c
enum DAY
{
      MON=1, TUE, WED, THU, FRI, SAT, SUN
};
```

这样看起来是不是更简洁了。

**注意** **第一个枚举成员的默认值为整型的 0**，后续枚举成员的值在前一个成员上加 1。我们在这个实例中把第一个枚举成员的值定义为 1，第二个就为 2，以此类推。

```c
enum DAY
{
MON=1, TUE, WED, THU, FRI, SAT, SUN
};
int main()
{
enum DAY day;
day = WED;
printf("%d",day);	// 3
return 0;
}
```

**NOTE** 在C 语言中，枚举类型是被当做 int 或者 unsigned int 类型来处理的

## pointer

like int and double, it's a data type, memory size is a "计算机字长", **what stored is another var's memory address**.

```c
#include <stdio.h>

int main ()
{
   int  var = 20;   /* 实际变量的声明 */
   int  *ip = &var;        /* 指针变量的声明 */
 
   printf("Address of var variable: %p\n", &var  );
   /* 在指针变量中存储的地址 */
   printf("Address stored in ip variable: %p\n", ip );
   /* 使用指针访问值 */
   printf("Value of *ip variable: %d\n", *ip );
 
   return 0;
}
```

more see `c-pointer.md`

## typedef

```c
typedef struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} Book;
```