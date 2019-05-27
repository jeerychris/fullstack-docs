# for difficulties in python

# yield

**什么情况下需要使用 yield？**

一个函数 f，f 返回一个 list，这个 list 是动态计算出来的（不管是数学上的计算还是逻辑上的读取格式化），并且这个 list 会很大（无论是固定很大还是随着输入参数的增大而增大），这个时候，我们希望每次调用这个函数并使用迭代器进行循环的时候一个一个的得到每个 list 元素而不是直接得到一个完整的 list 来节省内存，这个时候 yield 就很有用。

具体怎么使用 yield 参考：[Python yield 使用浅析](https://www.runoob.com/w3cnote/python-yield-used-analysis.html)

以斐波那契函数为例，我们一般希望从 n 返回一个 n 个数的 list：

```python
def fab(max): 
   n, a, b = 0, 0, 1 
   L = [] 
   while n < max: 
       L.append(b) 
       a, b = b, a + b 
       n = n + 1 
   return L
```

上面那个 fab 函数从参数 max 返回一个有 max 个元素的 list，当这个 **max 很大**的时候，会非常的占用内存。

一般我们使用的时候都是这个样子的，比如：

```python
f = iter(fab(1000))
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
```

这样我们实际上是先生成了一个 1000 个元素的 list:f，然后我们再去使用这个 f。

现在，我们换一个方法：

因为我们实际使用的是 list 的遍历，也就是 list 的迭代器。那么我们可以让这个函数 fab 每次只返回一个迭代器——一个计算结果，而不是一个完整的 list：

```python
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 
```

这样，我们每次调用fab函数，比如这样：

```python
for x in fab(1000):
    print(x)
```

或者 next 函数之类的，实际上的运行方式是每次的调用都在 yield 处中断并返回一个结果，然后再次调用的时候再恢复中断继续运行。