# JAVA 8

[Java8 函数式编程探秘](http://www.importnew.com/27901.html)
[scala函数编程]()

"D:\developer\Git\bin\bash.exe" --login -i

# functional programming

lambda && Function && Stream && Collector

```java
// lambda
List<Integer> v = Arrays.asList(1, 3, 2, 4);
v.sort(Integer::compareTo);
v.forEach(x -> System.out.print(x + "-"));

// stream
int sumOfWeights = widgets.parallelStream()
                               .filter(b -> b.getColor() == RED)
                               .mapToInt(b -> b.getWeight())
                               .sum();

System.out.println(v.stream().filter(x -> x > 2).collect(Collectors.toList()));
v.stream().max(Integer::compareTo).ifPresent(System.out::println);

Optional<Integer> sum = v.stream().reduce(Integer::sum);
sum.ifPresent(System.out::println);

System.out.println(v.stream().sorted().collect(Collectors.averagingInt(x -> x)));
System.out.println(v.stream().map(x -> x * x).collect(Collectors.toList()));
System.out.println(v.stream().collect(Collectors.toMap(x -> "" + x, y -> y * 2)).keySet());
System.out.println(v.stream().collect(Collectors.groupingBy(x -> x % 2 == 0 ? "even" : "old")));
```

# Java8函数框架解读

**函数编程的最直接的表现，莫过于将函数作为数据自由传递，结合泛型推导能力，使代码表达能力获得飞一般的提升**。那么，Java8是怎么支持函数编程的呢？主要有三个核心概念：

- 函数接口(Function)
- 流(Stream)
- 聚合器(Collector)

## 函数接口

关于函数接口，需要记住的就是两件事：

- 函数接口是**行为的抽象**；
- 函数接口是**数据转换器**。

最直接的支持就是 `java.util.Function` 包。定义了四个最基础的函数接口：

- `Supplier<T>`: 数据提供器，可以提供 T 类型对象；无参的构造器，提供了 get 方法；
- `Function<T,R>`: 数据转换器，接收一个 T 类型的对象，返回一个 R类型的对象； 单参数单返回值的行为接口；提供了 apply, compose, andThen, identity 方法；
- `Consumer<T>`: 数据消费器， 接收一个 T类型的对象，无返回值，通常用于设置T对象的值； 单参数无返回值的行为接口；提供了 accept, andThen 方法；
- `Predicate<T>`: 条件测试器，接收一个 T 类型的对象，返回布尔值，通常用于传递条件函数； 单参数布尔值的条件性接口。提供了 test (条件测试) , and-or- negate(与或非) 方法。

其中, compose, andThen, and, or, negate 用来组合函数接口而得到更强大的函数接口。

其它的函数接口都是通过这四个扩展而来。

- 在参数个数上扩展： 比如接收双参数的，有 Bi 前缀， 比如 BiConsumer<T,U>, BiFunction<T,U,R> ;
- 在类型上扩展： 比如接收原子类型参数的，有 [Int|Double|Long][Function|Consumer|Supplier|Predicate]
- 特殊常用的变形： 比如 BinaryOperator ， 是同类型的双参数 BiFunction<T,T,T> ，二元操作符 ； UnaryOperator 是 Function<T,T> 一元操作符。

那么，这些函数接口可以接收哪些值呢？

- 类/对象的静态方法引用、实例方法引用。引用符号为双冒号 ::
- 类的构造器引用，比如 Class::new
- lambda表达式

## 聚合器

先说聚合器。每一个流式计算的末尾总有一个类似 collect(Collectors.toList()) 的方法调用。collect 是 Stream 的方法，而参数则是聚合器Collector。已有的聚合器定义在Collectors 的静态方法里。 那么这个聚合器是怎么实现的呢？

**Reduce**

大部分聚合器都是基于 Reduce 操作实现的。 Reduce ，名曰推导，含有三个要素： 初始值 init, 二元操作符 BinaryOperator, 以及一个用于聚合结果的数据源S。

Reduce 的算法如下：

- STEP1: 初始化结果 R = init ；

- STEP2: 每次从 S 中取出一个值 v，通过二元操作符施加到 R 和 v ，产生一个新值赋给 R = BinaryOperator(R, v)；重复 STEP2， 直到 S 中没有值可取为止。

比如一个列表求和，Sum([1,2,3]) , 那么定义一个初始值 0 以及一个二元加法操作 BO = a + b ，通过三步完成 Reduce 操作：step1: R = 0; step2: v=1, R = 0+v = 1; step2: v=2, R = 1 + v = 3 ; step3: v = 3, R = 3 + v = 6。

### 四要素

一个聚合器的实现，通常需要提供四要素：

- 一个结果容器的初始值提供器 supplier ；
- 一个用于将每次二元操作的中间结果与结果容器的值进行操作并重新设置结果容器的累积器 accumulator ；
- 一个用于对Stream元素和中间结果进行操作的二元操作符 combiner ；
- 一个用于对结果容器进行最终聚合的转换器 finisher（可选) 。

Collectors.CollectorImpl 的实现展示了这一点：

```java
static class CollectorImpl<T, A, R> implements Collector<T, A, R> {
        private final Supplier<A> supplier;
        private final BiConsumer<A, T> accumulator;
        private final BinaryOperator<A> combiner;
        private final Function<A, R> finisher;
        private final Set<Characteristics> characteristics;
 
        CollectorImpl(Supplier<A> supplier,
                      BiConsumer<A, T> accumulator,
                      BinaryOperator<A> combiner,
                      Function<A,R> finisher,
                      Set<Characteristics> characteristics) {
            this.supplier = supplier;
            this.accumulator = accumulator;
            this.combiner = combiner;
            this.finisher = finisher;
            this.characteristics = characteristics;
        }
}
```

列表类聚合器`Collectors.toList()`
列表类聚合器实现，基本是基于Reduce 操作完成的。 看如下代码：

```java
    public static <T>
    Collector<T, ?, List<T>> toList() {
        return new CollectorImpl<>((Supplier<List<T>>) ArrayList::new, List::add
                                   , (left, right) -> { left.addAll(right); return left; }, CH_ID);
    }
```

首先使用 ArrayList::new 创造一个空列表； 然后 List:add 将Stream累积操作的中间结果加入到这个列表；第三个函数则将两个列表元素进行合并成一个结果列表中。 就是这么简单。集合聚合器 toSet(), 字符串连接器 joining()，以及列表求和(summingXXX)、最大(maxBy)、最小值(minBy)等都是这个套路。

### 映射类聚合器

映射类聚合器基于Map合并来完成。看这段代码：

```java
private static <K, V, M extends Map<K,V>>
    BinaryOperator<M> mapMerger(BinaryOperator<V> mergeFunction) {
        return (m1, m2) -> {
            for (Map.Entry<K,V> e : m2.entrySet())
                m1.merge(e.getKey(), e.getValue(), mergeFunction);
            return m1;
        };
    }
```

根据指定的值合并函数 mergeFunction, 返回一个map合并器，用来合并两个map里相同key的值。mergeFunction用来对两个map中相同key的值进行运算得到新的value值，如果value值为null，会移除相应的key，否则使用value值作为对应key的值。这个方法是私有的，主要为支撑 toMap，groupingBy 而生。

toMap的实现很简短，实际上就是将指定stream的每个元素分别使用给定函数keyMapper, valueMapper进行映射得到 newKey, newValue，从而形成新的Map[newKey,newValue] (1), 再使用mapMerger(mergeFunction) 生成的 map 合并器将其合并到 mapSupplier (2)。如果只传 keyMapper, valueMapper，那么就只得到结果(1)。

```java
public static <T, K, U, M extends Map<K, U>>
    Collector<T, ?, M> toMap(Function<? super T, ? extends K> keyMapper,
                                Function<? super T, ? extends U> valueMapper,
                                BinaryOperator<U> mergeFunction,
                                Supplier<M> mapSupplier) {
        BiConsumer<M, T> accumulator
                = (map, element) -> map.merge(keyMapper.apply(element),
                                              valueMapper.apply(element), mergeFunction);
        return new CollectorImpl<>(mapSupplier, accumulator, mapMerger(mergeFunction), CH_ID);
    }
```

`Collectors.toMap()` example:

```java
List<Integer> list = Arrays.asList(1,2,3,4,5);
Supplier<Map<Integer,Integer>> mapSupplier = () -> list.stream().collect(Collectors.toMap(x->x, y-> y * y));
 
Map<Integer, Integer> mapValueAdd = list.stream().collect(Collectors.toMap(x->x, y->y, (v1,v2) -> v1+v2, mapSupplier));
System.out.println(mapValueAdd);
```

将一个 List 转成 map[1=1,2=2,3=3,4=4,5=5]，然后与另一个map[1=1,2=4,3=9,4=16,5=25]的相同key的value进行相加。注意到, toMap 的最后一个参数是 Supplier<Map> ， 是 Map 提供器，而不是 Map 对象。如果用Map对象，会报 no instances of type variables M exists so that conforms to Supplier<M>。 在函数式编程的世界里，通常是用函数来表达和组合的。

## 流

流（Stream）是Java8对函数式编程的重要支撑。大部分函数式工具都围绕Stream展开。

### Stream的接口

Stream 主要有四类接口：

- 流到流之间的转换：比如`filter`(过滤),`map`(映射转换), `mapTo[Int|Long|Double]` (到原子类型流的转换),`flatMap`(高维结构平铺)，`flatMapTo`[Int|Long|Double], `sorted`(排序)，`distinct`(不重复值)，`peek`(执行某种操作，流不变，可用于调试)，`limit`(限制到指定元素数量),`skip`(跳过若干元素) ；
- 流到终值的转换： 比如 `toArray`（转为数组），`reduce`（推导结果），`collect`（聚合结果），`min`(最小值), `max`(最大值), `count` (元素个数)， `anyMatch` (任一匹配), `allMatch`(所有都匹配)， `noneMatch`(一个都不匹配)， `findFirst`（选择首元素），`findAny`(任选一元素) ；
- 直接遍历： `forEach` (不保序遍历，比如并行流), `forEachOrdered`（保序遍历) ；
- 构造流： `empty` (构造空流)，`of` (单个元素的流及多元素顺序流)，`iterate` (无限长度的有序顺序流)，`generate` (将数据提供器转换成无限非有序的顺序流)， `concat` (流的连接)， `Builder` (用于构造流的Builder对象)

除了 Stream 本身自带的生成Stream 的方法，数组和容器及StreamSupport都有转换为流的方法。比如 Arrays.stream , [List|Set|Collection].[stream|parallelStream] , StreamSupport.[int|long|double|]stream；

流的类型主要有：Reference(对象流)， IntStream (int元素流), LongStream (long元素流)， Double (double元素流) ，定义在类 StreamShape 中，主要将操作适配于类型系统。

flatMap 的一个例子见如下所示，将一个二维数组转换为一维数组：

```java
    List<Integer> nums = Stream.of(Arrays.asList(1,2,3), Arrays.asList(1,4,9), Arrays.asList(1,8,27))
                                .flatMap(Collection::stream).collect(Collectors.toList());
    System.out.println(nums);
```