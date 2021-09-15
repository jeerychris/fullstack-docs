**References:**

1. [详细讲解redis数据结构（内存模型）以及常用命令](https://www.cnblogs.com/hjwublog/p/5639990.html)
2. [为什么说Redis是单线程的以及Redis为什么这么快](https://blog.csdn.net/chenyao1994/article/details/79491337)

# Redis到底有多快

> Redis采用的是基于内存的采用的是**单进程单线程模型的 KV 数据库**，由C语言编写，官方提供的数据是可以达到100000+的QPS（每秒内查询次数）。

![redis-QPS.png](images/redis-QPS.png)

# Redis为什么这么快

- **完全基于内存**，绝大部分请求是纯粹的内存操作，非常快速。数据存在内存中，**类似于HashMap**，HashMap的优势就是**查找和操作的时间复杂度都是O(1)**；
- **数据结构简单**，对数据操作也简单，Redis中的数据结构是专门进行设计的；
- 采用**单线程**，避免了不必要的**上下文切换和竞争条件**，也不存在多进程或者多线程导致的切换而消耗 CPU，不用去考虑各种**锁**的问题，不存在加锁释放锁操作，没有因为可能出现死锁而导致的性能消耗；
- 使用**多路I/O复用模型**，**非阻塞IO**；
- 使用底层模型不同，它们之间底层实现方式以及与客户端之间通信的应用协议不一样，Redis直接自己构建了VM 机制 ，因为一般的系统调用系统函数的话，会浪费一定的时间去移动和请求；

**Note**: ==多路I/O复用模型==

> 利用 **select、poll、epoll 可以同时监察多个流的 I/O 事件的能力**，在空闲的时候，会把当前线程阻塞掉，当有一个或多个流有 I/O 事件时，就从阻塞态中唤醒，于是程序就会轮询一遍所有的流（epoll 是只轮询那些真正发出了事件的流），并且只依次顺序的处理就绪的流，这种做法就避免了大量的无用操作。
>
> 这里“多路”指的是**多个网络连接**，“复用”指的是复用**同一个线程**。采用多路 I/O 复用技术可以让单个线程高效的处理多个连接请求（尽量减少网络 IO 的时间消耗），且 Redis 在内存中操作数据的速度非常快，也就是说内存内的操作不会成为影响Redis性能的瓶颈，主要由以上几点造就了 Redis 具有很高的吞吐量。

# Redis数据类型

与Memcached仅支持简单的key-value结构的数据记录不同，Redis支持的数据类型要丰富得多，常用的数据类型主要有五种：`String、List、Hash、Set和Sorted Set`。

## **Redis数据类型内存结构分析**

Redis内部使用一个**redisObject对象来表示所有的key和value**。redisObject主要的信息包括数据类型（type）、编码方式(encoding)、数据指针（ptr）、虚拟内存（vm）等。type代表一个value对象具体是何种数据类型，encoding是不同数据类型在redis内部式。

![redis-Object.png](images/redis-Object.png)

## **String类型**

字符串是Redis值的最基础的类型。Redis中使用的字符串是通过包装的，基于c语言字符数组实现的简单动态字符串(simple dynamic string, SDS)一个抽象数据结构。其源码定义如下：

```c
struct sdshdr {
    int len; //len表示buf中存储的字符串的长度。
    int free; //free表示buf中空闲空间的长度。
    char buf[]; //buf用于存储字符串内容。
};
```

![c-style-helloworld.jpg](images/c-style-helloworld.jpg)