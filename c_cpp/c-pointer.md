# 指针数组 & array pointer

```c
#include <stdio.h>
 
const int MAX = 3;

int main ()
{
   // var is array pointer, point to the first ele of the array, and is const
   int  var[] = {10, 100, 200}; 
   int i;
 
   for (i = 0; i < MAX; i++)
   {
      printf("Value of var[%d] = %d\n", i, var[i] );
   }
   return 0;
}

/* pointer array  */
void pointer_array_demo()
{
   char *names[2] = {
      "chris J",
      "chalice"
   };

   for (int i = 0; i < 2; i++)
      printf("%s\n", names[i]);
}
```

# pointer to pointer

`*p, **p, ***p` all is pointer, stored is a memery addr, size is a `computer word`

```c
#include <stdio.h>
 
int main ()
{
   int  var;
   int  *ptr;
   int  **pptr;

   var = 3000;

   /* 获取 var 的地址 */
   ptr = &var;

   /* 使用运算符 & 获取 ptr 的地址 */
   pptr = &ptr;

   /* 使用 pptr 获取值 */
   printf("Value of var = %d\n", var );
   printf("Value available at *ptr = %d\n", *ptr );
   printf("Value available at **pptr = %d\n", **pptr);

   return 0;
}
```

# 传递指针给函数

```c
void getSeconds(unsigned long *par)
{
   /* 获取当前的秒数 */
   *par = time( NULL );
   return;
}

int main()
{
    int secs = 0;
    getSeconds(&secs);

    printf("%d\n", secs)
}
```

# 从函数返回指针

调用函数时返回局部变量的地址，must 定义局部变量为 static 变量

因为**局部变量是存储在内存的栈区内，当函数调用结束后，局部变量所占的内存地址便被释放了**，因此当其函数执行完毕后，函数内的变量便不再拥有那个内存地址，所以不能返回其指针。

除非将其变量定义为 static 变量，static 变量的值存放在内存中的静态数据区，不会随着函数执行的结束而被清除，故能返回其地址。

```c
#include <stdio.h>
#include <time.h>
#include <stdlib.h> 
 
/* 要生成和返回随机数的函数 */
int * getRandom( )
{
   static int  r[10];
   int i;
 
   /* 设置种子 */
   srand( (unsigned)time( NULL ) );
   for ( i = 0; i < 10; ++i)
   {
      r[i] = rand();
      printf("%d\n", r[i] );
   }
 
   return r;
}
 
/* 要调用上面定义函数的主函数 */
int main ()
{
   /* 一个指向整数的指针 */
   int *p;
   int i;
 
   p = getRandom();
   for ( i = 0; i < 10; i++ )
       printf("*(p + [%d]) : %d\n", i, *(p + i) );
 
   return 0;
}
```

**NOTE**:
初始化指针，没有被初始化的指针被称为失控指针(野指针）

# Conclusion

## complex pointer

原则: 从变量名处起, 根据运算符优先级结合, 一步一步分析。

-  `int p`; -- 这是一个普通的整型变量
-  `int *p`; -- 首先从 p 处开始,先与*结合,所以说明 p 是一个指针, 然后再与 int 结合, 说明指针所指向的内容的类型为 int 型。所以 p 是一个返回整型数据的指针。
-  `int p[3]` -- 首先从 p 处开始,先与[] 结合,说明 p 是一个数组, 然后与 int 结合, 说明数组里的元素是整型的, 所以 p 是一个由整型数据组成的数组。
-  `int *p[3]`; -- 首先从 p 处开始, **先与 [] 结合, 因为其优先级比 * 高**,所以 p 是一个数组, 然后再与 * 结合, 说明数组里的元素是指针类型, 然后再与 int 结合, 说明指针所指向的内容的类型是整型的, 所以 p 是一个由返回整型数据的指针所组成的数组。
-  `int (*p)[3]`; -- 首先从 p 处开始, 先与 * 结合,说明 p 是一个指针然后再与 [] 结合(与"()"这步可以忽略,只是为了改变优先级), 说明指针所指向的内容是一个数组, 然后再与int 结合, 说明数组里的元素是整型的。所以 p 是一个**指向由整型数据组成的数组的指针**。
-  `int **p`; -- 首先从 p 开始, 先与 * 结合, 说是 p 是一个指针, 然后再与 * 结合, 说明指针所指向的元素是指针, 然后再与 int 结合, 说明该指针所指向的元素是整型数据。由于二级指针以及更高级的指针极少用在复杂的类型中, 所以后面更复杂的类型我们就不考虑多级指针了, 最多只考虑一级指针。
-  `int p(int);` -- 从 p 处起,先与 () 结合, 说明 p 是一个函数, 然后进入 () 里分析, 说明该函数有一个整型变量的参数, 然后再与外面的 int 结合, 说明函数的返回值是一个整型数据。
-  `int (*p)(int)`; -- 从 p 处开始, 先与指针结合, 说明 p 是一个指针, 然后与()结合, 说明指针指向的是一个函数, 然后再与()里的 int 结合, 说明函数有一个int 型的参数, 再与最外层的 int 结合, 说明函数的返回类型是整型, 所以 **p 是一个指向有一个整型参数且返回类型为整型的函数的指针**。
-  `int *(*p(int))[3]`; -- 可以先跳过, 不看这个类型, 过于复杂从 p 开始,先与 () 结合, 说明 p 是一个函数, 然后进入 () 里面, 与 int 结合, 说明函数有一个整型变量参数, 然后再与外面的 * 结合, 说明函数返回的是一个指针, 然后到最外面一层, 先与[]结合, 说明返回的指针指向的是一个数组, 然后再与 * 结合, 说明数组里的元素是指针, 然后再与 int 结合, 说明指针指向的内容是整型数据。所以 p 是一个参数为一个整数据且返回一个指向由整型指针变量组成的数组的指针变量的函数。

## 指针实例：

```c
int board[8][8];    /* int 数组的数组 */ 
int ** ptr;         /* 指向 int 指针的指针 */
int * risks[10];    /* 具有 10 个元素的数组, 每个元素是一个指向 int 的指针 */
int (* rusks) [10];  /* 一个指针, 指向具有 10 个元素的 int 数组 */
int * oof[3][4];    /* 一个 3 x 4 的数组, 每个元素是一个指向 int 的指针 */ 
int (* uuf) [3][4]; /* 一个指针, 指向 3 X 4 的 int 数组 */
int (* uof[3]) [4]; /* 一个具有 3 个元素的数组, 每个元素是一个指向具有 4 个元素的int 数组的指针 */ 
```

## 指向函数的指针

代码和数据是一样的，都需要占据一定内存，那当然也会有一个基地址，所以我们可以定义一个指针来指向这个基地址，这就是所谓的函数指针。

假设有函数：

```c
double func(int a,char c);
double (*p)(int a,char c);
p=&func;
```

即可以定义一个函数指针。

**调用函数**

```c
double s1=func(100,'x');
double s2=(*p)(100,'x');
```

上面两个语句是等价的。

## typedef and callback

**typedef 还有一个作用，就是为复杂的声明定义一个新的简单的别名。用在回调函数中特别好用：**

1. 原声明：`int *(*a[5])(int, char*);`

在这里，变量名为`a`, 直接用一个新别名 `pFun` 替换 **a** 就可以了：

```c
typedef int *(*pFun)(int, char*);
```

于是，原声明的最简化版：

```c
pFun a[5];
```

2. 原声明：`void (*b[10]) (void (*)());`

这里，变量名为 b，先替换右边部分括号里的，pFunParam 为别名一：

```c
typedef void (*pFunParam)();
```

再替换左边的变量 **b**，**pFunx** 为别名二：

```c
typedef void (*pFunx)(pFunParam);
```

于是，原声明的最简化版：

```c
pFunx b[10];
```

其实，可以这样理解:

```c
typedef int *(*pFun)(int, char*); 
```

由 **typedef** 定义的函数 **pFun**，为一个新的类型，所以这个新的类型可以像 **int** 一样定义变量，于是，pFun a[5]; 就定义了 `int *(*a[5])(int, char*)`;

所以我们可以用来定义回调函数，特别好用。

另外，也要注意，typedef 在语法上是一个存储类的关键字（如 auto、extern、mutable、static、register 等一样），虽然它并不真正影响对象的存储特性，如：

```c
typedef static int INT2; // 不可行
```

编译将失败，会提示“指定了一个以上的存储类”。