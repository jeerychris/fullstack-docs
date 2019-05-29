# array

## array as function parameter

is converted to `*`, pointer

```c
#include <stdio.h>
 
/* 函数声明 */
double getAverage(int arr[], int size);
 
int main ()
{
   /* 带有 5 个元素的整型数组 */
   int balance[5] = {1000, 2, 3, 17, 50};
   double avg;
 
   /* 传递一个指向数组的指针作为参数 */
   avg = getAverage( balance, 5 ) ;
 
   /* 输出返回值 */
   printf( "平均值是： %f ", avg );
    
   return 0;
}
 
// equal to `double getAverage(int *, int size)`
double getAverage(int arr[], int size)
{
  int    i;
  double avg;
  double sum=0;
 
  for (i = 0; i < size; ++i)
    sum += arr[i];
 
  avg = sum / size;
 
  return avg;
}
```

## 二维数组传递给函数

如果我们想将二维数组作为实参传递给某个函数，如下代码是有问题的:

```c
double * MatrixMultiple(double a[][], double b[][]);
```

原因可以简单理解为：编译器并没有那么高级，在二维以上的数组一定要规定一个最高维数:

```c
double * MatrixMultiple(double a[][2], double b[][3]);  /* 这才是正确的 */
```

**二维数组传递给函数**

列举 C 语言传递二维数组的方法。

方法1: 第一维的长度可以不指定，但必须指定第二维的长度：

```c
void print_a(int a[][5], int n, int m)
```

方法2: 指向一个有5个元素一维数组的指针：

```c
void print_b(int (*a)[5], int n, int m)
```

方法3: 利用数组是顺序存储的特性,通过降维来访问原数组!

```c
void print_c(int *a, int n, int m)
```

如果知道二维数组的长度，当然选择第一或者第二种方式，但是长度不确定时，只能传入数组大小来遍历元素啦。

```c
#include <stdio.h>
/*********************************
* 方法1: 第一维的长度可以不指定
*        但必须指定第二维的长度
*********************************/ 
void print_a(int a[][5], int n, int m){ 
    int i, j;
    for(i = 0; i < n; i++) {
        for(j = 0; j < m; j++) 
            printf("%d ", a[i][j]); 
        printf("\n"); 
    } 
} 

/***************************************** 
* 方法2: 指向一个有5个元素一维数组的指针
*****************************************/ 
void print_b(int (*a)[5], int n, int m) { 
    int i, j;
    for(i = 0; i < n; i++) { 
        for(j = 0; j < m; j++) 
            printf("%d ", a[i][j]);
        printf("\n"); 
    } 
}

/*********************************** 
* 方法3: 利用数组是顺序存储的特性, 
*       通过降维来访问原数组!
***********************************/ 
void print_c(int *a, int n, int m) { 
    int i, j; 
    for(i = 0; i < n; i++) { 
        for(j = 0; j < m; j++) 
            printf("%d ", *(a + i*m + j));
        printf("\n"); 
    } 
}
int main(void) 
{ 
    int a[5][5] = {{1, 2}, {3, 4, 5}, {6}, {7}, {0, 8}}; 

    printf("\n方法1:\n");   
    print_a(a, 5, 5); 

    printf("\n方法2:\n");   
    print_b(a, 5, 5);   

    printf("\n方法3:\n");   
    print_c(&a[0][0], 5, 5); 

//    getch(); 
    return 0; 
} 
```

## 指向数组的指针

数组名是一个**指向数组中第一个元素**的**常量指针**。因此，在下面的声明中：

```c
double balance[50];
```

**balance** 是一个指向 &balance[0] 的指针，即数组 balance 的第一个元素的地址。因此，下面的程序片段把 **p** 赋值为 **balance** 的第一个元素的地址：

```c
double *p;
double a[10];

p = a;
p++; // ok
a++	// wrong, it's a const pointer
```

使用数组名作为常量指针是合法的，反之亦然。因此，*(balance + 4) 是一种访问 balance[4] 数据的合法方式。

一旦您把第一个元素的地址存储在 p 中，您就可以使用 *p、*(p+1)、*(p+2) 等来访问数组元素。

**diff**

- a is **const**, can't be lvalue
- a's step is the **size of one row**, p's is **size of one ele**