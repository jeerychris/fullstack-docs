# C Memory

## C memory model

全局变量保存在内存的全局存储区中，占用静态的存储单元；局部变量保存在栈中，只有在所在函数被调用时才动态地为变量分配存储单元。

C语言经过编译之后将内存分为以下几个区域：

- **栈（stack）**：由编译器进行管理，自动分配和释放，存放函数调用过程中的各种参数、局部变量、返回值以及函数返回地址。操作方式类似数据结构中的栈。
- **堆（heap**）：用于程序动态申请分配和释放空间。C语言中的malloc和free，C++中的new和delete均是在堆中进行的。正常情况下，程序员申请的空间在使用结束后应该释放，若程序员没有释放空间，则程序结束时系统自动回收。注意：这里的“堆”并不是数据结构中的“堆”。
- **全局（静态）存储区**：分为**DATA段**和**BSS段**。DATA段（全局初始化区）存放初始化的全局变量和静态变量；BSS段（全局未初始化区）存放未初始化的全局变量和静态变量。程序运行结束时**自动释放**。其中**BBS段在程序执行之前会被系统自动清0**，所以未初始化的全局变量和静态变量在程序执行之前已经为0。
- `文字常量区`：存放常量字符串。程序结束后由**系统释放**。
- `程序代码区`：存放程序的二进制代码。

显然，C语言中的全局变量和局部变量在内存中是有区别的。C语言中的全局变量包括外部变量和静态变量，均是保存在全局存储区中，占用永久性的存储单元；局部变量，即自动变量，保存在栈中，只有在所在函数被调用时才由系统动态在栈中分配临时性的存储单元。

```c
#include <stdio.h>
#include <stdlib.h>

int k1 = 1;
int k2;
static int k3 = 2;
static int k4;
int main( )
{   
    static int m1=2, m2;
    int i=1;
    char*p;
    char str[10] = "hello";
    char*q = "hello";
    p= (char *)malloc( 100 );
    free(p);
    printf("栈区-变量地址  i：%p\n", &i);       // 1
    printf("                p：%p\n", &p);     //
    printf("              str：%p\n", str);
    printf("                q：%p\n", &q);
    printf("堆区地址-动态申请：%p\n", p);
    printf("全局外部有初值 k1：%p\n", &k1);
    printf("    外部无初值 k2：%p\n", &k2);
    printf("静态外部有初值 k3：%p\n", &k3);
    printf("    外静无初值 k4：%p\n", &k4);
    printf("  内静态有初值 m1：%p\n", &m1);
    printf("  内静态无初值 m2：%p\n", &m2);
    printf("文字常量地址    ：%p, %s\n",q, q);
    printf("程序区地址      ：%p\n",&main);
    return 0;
}
/*
栈区-变量地址  i：000000000024FE4C
                p：000000000024FE40
              str：000000000024FE36
                q：000000000024FE28
堆区地址-动态申请：0000000000345DE0
全局外部有初值 k1：0000000000403010
    外部无初值 k2：0000000000407970
静态外部有初值 k3：0000000000403014
    外静无初值 k4：0000000000407030
  内静态有初值 m1：0000000000403018
  内静态无初值 m2：0000000000407034
文字常量地址    ：0000000000404000, hello
程序区地址      ：0000000000401550
*/
```

## C storage keywords

存储类定义 C 程序中变量/函数的范围（可见性）和生命周期。这些说明符放置在它们所修饰的类型之前。

- `auto`
- `register`
- `static`
- `extern`

**auto**: default to local variable, only used inside function

**register**: register 存储类用于定义存储在寄存器中而不是 RAM 中的**局部变量**, 寄存器只用于需要快速访问的变量，比如计数器。还应注意的是，定义 'register' 并不意味着变量将被存储在寄存器中，它**意味着变量可能存储在寄存器**中，这取决于硬件和实现的限制。

```c
void func()
{
    int a = 0;  // default is auto,
    register int cnt = 10;  // for quick speed
}
```

### static

variable decorated with **static has file scope**

when **used to global variable**, scope is the **same file**, even use extern keyword. you can't use it in **diff file**,

when used **to local variable**:

```c
int count=10;

int main()
{
  while (count--) {
      func1();
  }
  return 0;
}
 
void func1(void)
{
/* 'thingy' 是 'func1' 的局部变量 - 只初始化一次
 * 每次调用函数 'func1' 'thingy' 值不会被重置。
 */                
  static int thingy=5;
  thingy++;
  printf(" thingy 为 %d ， count 为 %d\n", thingy, count);
}
```

when used **to function**:
> the function can only be used in the same file. even you use `extern type func();` to declare in others.

### extern

default to function, so you are declare and use it in other files.

another usage is to declare global var that defined in other files

## C 语言中全局变量、局部变量、静态全局变量、静态局部变量的区别

- **生命周期(存储方式)**
    - 程序运行到结束，global, 
    - 函数执行到结束，local,
- **作用域(使用范围)**
    - 整个源程序
    - file, `static`
    - 函数

**从作用域看：**

1、全局变量具有全局作用域。全局变量只需在一个源文件中定义，就可以作用于所有的源文件。当然，其他不包含全局变量定义的源文件需要用extern 关键字再次声明这个全局变量。

2、静态局部变量具有局部作用域，它只被初始化一次，自从第一次被初始化直到程序运行结束都一直存在，它和全局变量的区别在于全局变量对所有的函数都是可见的，而**静态局部变量只对定义自己的函数体始终可见**。

3、局部变量也只有局部作用域，它是自动对象（auto），它在程序运行期间不是一直存在，而是只在函数执行期间存在，函数的一次调用执行结束后，变量被撤销，其所占用的内存也被收回。

4、静态全局变量也具有全局作用域，它与全局变量的区别在于如果程序包含多个文件的话，它作用于定义它的文件里，不能作用到其它文件里，即被**static关键字修饰过的变量具有文件作用域**。这样即使两个不同的源文件都定义了相同名字的静态全局变量，它们也是不同的变量。

**从分配内存空间看：**

1、全局变量，静态局部变量，静态全局变量都在静态存储区分配空间，而局部变量在栈里分配空间

2、全局变量本身就是静态存储方式， 静态全局变量当然也是静态存储方式。这两者在存储方式上并无不同。这两者的区别虽在于非静态全局变量的作用域是整个源程序，当一个源程序由多个源文件组成时，非静态的全局变量在各个源文件中都是有效的。而**静态全局变量则限制了其作用域**，即只在定义该变量的源文件内有效，在同一源程序的其它源文件中不能使用它。由于静态全局变量的作用域局限于一个源文件内，只能为该源文件内的函数公用，因此可以避免在其它源文件中引起错误。

-  1)静态变量会被放在程序的静态数据存储区(全局可见)中，这样可以在下一次调用的时候还可以保持原来的赋值。这一点是它与堆栈变量和堆变量的区别。
-  2)变量用static告知编译器，自己仅仅在变量的作用范围内可见。这一点是它与全局变量的区别。

从以上分析可以看出， 把**局部变量改变为静态变量**后是**改变了它的存储方式即改变了它的生存期**。**把全局变量改变为静态变量后是改变了它的作用域**，限制了它的使用范围。因此static 这个说明符在不同的地方所起的作用是不同的。应予以注意。

**Tips:**

-  A.若全局变量仅在单个C文件中访问，则可以将这个变量修改为静态全局变量，以降低模块间的耦合度；
-  B.若全局变量仅由单个函数访问，则可以将这个变量改为该函数的静态局部变量，以降低模块间的耦合度；
-  C.设计和使用访问动态全局变量、静态全局变量、静态局部变量的函数时，需要考虑重入问题，因为他们都放在静态数据存储区，全局可见；
-  D.如果我们需要一个可重入的函数，那么，我们一定要避免函数中使用static变量(这样的函数被称为：带"内部存储器"功能的的函数)
-  E.函数中必须要使用static变量情况:比如当某函数的返回值为指针类型时，则必须是static的局部变量的地址作为返回值，若为auto类型，则返回为错指针。