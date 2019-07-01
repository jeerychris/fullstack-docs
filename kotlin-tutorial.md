# Syntax

# Baisc

## default imported packaages

有多个包会默认导入到每个 Kotlin 文件中：

```java
kotlin.*
kotlin.annotation.*
kotlin.collections.*
kotlin.comparisons.*
kotlin.io.*
kotlin.ranges.*
kotlin.sequences.*
kotlin.text.*           //Functions for working with text and regular expressions.
```

Additional packages are imported depending on the target platform:

- JVM:
    - `java.lang.*`
    - `kotlin.jvm.*`
- JS:
    - `kotlin.js.*`

## defining function

`fun` keyword

no semicolon `;` is required for statement

```kotlin
// primitive type Int, 
// only return type `Unit` can be ommited
fun sum(a: Int, b: Int): Int {
    return a + b
}

// expression body and referred return type, with last statement
fun sum1(a: Int, b: Int) = a + b

// Unit, like `void` in java
fun printSum(a: Int, b: Int): Unit {
    println("sum of $a and $b is ${a + b}")
}

// inferred return type
fun printSum1(a: Int, b: Int) {
    println("sum of $a and $b is ${a + b}")
}
```

# defining variable

use keyword `var`, pseudo **dynamic language**, that after assignment, can't change type

```kotlin
var a:Int = 1	// immediate assignment
var b = 2		// Int type is referred

var c: Int		// type is required when no initializer is provided
c = 3
c = "ccc"		// wrong, can't change type
```

## Comment

like java, `//` for line comment, `/**/` for block comment

the only difference is that block comment can nested in Kotlin

## Using String Template

```kotlin
var a = 1
var s1 = "a is $a"

a = 2
println("${s1.replace("is", "was")}, but now is $a")
```

## Using conditional expressions

```kotlin
fun max(a: Int, b: Int): Int{
    if (a > b)
        return a
    else
        return b
}

fun max_1(a: Int, b: Int) = if (a > b) a else b
```

# class

## property, getter and setter

```kotlin
class Runoob {
    var name: String = ""	// default has getter and setter
    val url: String = ""	// default has getter
}

class Person {

    var lastName: String = "zhang"
        get() = field.toUpperCase()   // 将变量赋值后转换为大写
        set		// redundant setter

    var no: Int = 100
        get() = field                // 后端变量, redundant
        set(value) {
            if (value < 10) {       // 如果传入的值小于 10 返回该值
                field = value
            } else {
                field = -1         // 如果传入的值大于等于 10 返回 -1
            }
        }

    var heiht: Float = 145.4f
}
```

**field 关键字**

最关键的一句：**Remember in kotlin whenever you write foo.bar = value it will be translated into a setter call instead of a PUTFIELD.**

也就是说，在 Kotlin 中，任何时候当你写出“一个变量后边加等于号”这种形式的时候，比如我们定义 var no: Int 变量，当你写出 no = ... 这种形式的时候，这个等于号都会被编译器翻译成调用 **setter** 方法；而同样，在任何位置引用变量时，只要出现 **no** 变量的地方都会被编译器翻译成 **getter** 方法。那么问题就来了，当你在 **setter** 方法内部写出 no = ... 时，相当于在 **setter** 方法中调用 **setter** 方法，形成递归，进而形成死循环，例如文中的例子：

```kotlin
var no: Int = 100
    get() = field                // 后端变量
    set(value) {
        if (value < 10) {       // 如果传入的值小于 10 返回该值
            field = value
        } else {
            field = -1         // 如果传入的值大于等于 10 返回 -1
        }
    }
```

这段代码按以上这种写法是正确的，因为使用了 **field** 关键字，但是如果不用 **field** 关键字会怎么样呢？例如：

```kotlin
var no: Int = 100
    get() = no
    set(value) {
        if (value < 10) {       // 如果传入的值小于 10 返回该值
            no = value
        } else {
            no = -1         // 如果传入的值大于等于 10 返回 -1
        }
    }
```

注意这里我们使用的 Java 的思维写了 **getter** 和 **setter** 方法，那么这时，如果将这段代码翻译成 Java 代码会是怎么样呢？如下：

```kotlin
int no = 100;
public int getNo() {
    return getNo();// Kotlin中的get() = no语句中出来了变量no，直接被编译器理解成“调用getter方法”
}

public void setNo(int value) {
    if (value < 10) {
        setNo(value);// Kotlin中出现“no =”这样的字样，直接被编译器理解成“这里要调用setter方法”
    } else {
        setNo(-1);// 在setter方法中调用setter方法，这是不正确的
    }
}
```

翻译成 Java 代码之后就很直观了，在 **getter** 方法和 **setter** 方法中都形成了递归调用，显然是不正确的，最终程序会出现内存溢出而异常终止。

## primary and second constructor

### primary constructor

```kotlin
class Person(val name: String, val age: Int)
```

主构造器中不能包含任何代码，初始化代码可以放在初始化代码段中，初始化代码段使用 init 关键字作为前缀。

```kotlin
// here firstName is not a property, but can use inside init block
class Person constructor(firstName: String) {
    init {
        println("FirstName is $firstName")
    }
}
```

注意：主构造器的参数可以在初始化代码段中使用，也可以在类主体n定义的属性初始化代码中使用。 一种简洁语法，可以通过主构造器来定义属性并初始化属性值（可以是var或val）：

```kotlin
// use var, val means the parameter is also a property.
// val, defautt getter
// var, default getter and setter
class People(var firstName: String, val lastName: String) {
    //...
}
```

如果构造器有注解，或者有可见度修饰符，这时constructor关键字是必须的，注解和修饰符要放在它之前。

### second constructor

二级构造函数，需要加前缀 constructor

如果类有主构造函数，每个次构造函数都要，或直接或间接通过另一个次构造函数代理主构造函数。在同一个类中代理另一个构造函数使用 `this` 关键字：

```kotlin
class Person(val name: String) {
    constructor (name: String, age:Int) : this(name) {
        // 初始化...
    }
}
```

if no primary and secondary construtor, like java,  JVM supply a no arg constructor

## 抽象类

抽象是面向对象编程的特征之一，类本身，或类中的部分成员，都可以声明为abstract的。抽象成员在类中不存在具体的实现。

注意：无需对抽象类或抽象成员标注open注解。

```kotlin
open class Base {	// default is final, can't be inherited
    open fun f() {}
}

abstract class Derived : Base() {
    override abstract fun f()
}
```

## 嵌套类

我们可以把类嵌套在其他类中，看以下实例：

use `Outer.Nested()`

```kotlin
class Outer {                  // 外部类
    private val bar: Int = 1
    class Nested {             // 嵌套类
        fun foo() = 2
    }
}
```

## 内部类

内部类使用 `inner` 关键字来表示。

内部类会带有一个对外部类的对象的引用，所以内部类可以访问外部类成员属性和成员函数。

use `Outer().Inner()`

```kotlin
class Outer {
    private val bar: Int = 1
    var v = "成员属性"
    /**嵌套内部类**/
    inner class Inner {
        fun foo() = bar  // 访问外部类成员
        fun innerTest() {
            var o = this@Outer //获取外部类的成员变量
            println("内部类可以引用外部类的成员，例如：" + o.v)
        }
    }
}
```

为了消除歧义，要访问来自外部作用域的 this，我们使用`this@label`，其中 @label 是一个 代指 this 来源的标签。

------

## 匿名内部类(object expression)

使用对象表达式来创建匿名内部类：

```kotlin
class Test {
    var v = "成员属性"

    fun setInterFace(test: TestInterFace) {
        test.test()
    }
}

/**
 * 定义接口
 */
interface TestInterFace {
    fun test()
}

fun main(args: Array<String>) {
    var test = Test()

    /**
     * 采用对象表达式来创建接口对象，即匿名内部类的实例。
     */
    test.setInterFace(object : TestInterFace {
        override fun test() {
            println("对象表达式创建匿名内部类的实例")
        }
    })
}
```

## 类的修饰符

类的修饰符包括 classModifier 和_accessModifier_:

- classModifier: 类属性修饰符，标示类本身特性。

    ```kotlin
    abstract    // 抽象类  
    final       // 类不可继承，默认属性
    enum        // 枚举类
    open        // 类可继承，类默认是final的
    annotation  // 注解类
    ```

- accessModifier: 访问权限修饰符

    ```kotlin
    private    // 仅在同一个文件中可见
    protected  // 同一个文件中或子类可见
    public     // 所有调用的地方都可见
    internal   // 同一个模块中可见
    ```

# class inheritence

- single inheritence, but can implement mulitipel interface

Kotlin 中所有类都继承该 `Any` 类，它是所有类的超类，对于没有超类型声明的类是默认超类：

```kotlin
class Example // 从 Any 隐式继承
```

Any 默认提供了三个函数：

```kotlin
equals()
hashCode()
toString()
```

注意：**Any 不是 java.lang.Object**。

如果一个类要被继承，可以使用 open 关键字进行修饰。default class and method without `open` is final

```kotlin
open class Base(p: Int)           // 定义基类
class Derived(p: Int) : Base(p)
```

## constructor

如果**子类有主构造函数**， 则基类必须在主构造函数中立即初始化。

**no primary constructor**, use `super` keyword in secondary construtor

```kotlin
// derived class has primary constructor
open class Person(var name : String, var age : Int)
class Student(name : String, age : Int, var no : String, var score : Int) : Person(name, age)

// no primary constructor
class Student : Person {
    constructor(ctx: Context) : super(ctx) {} 
    constructor(ctx: Context, attrs: AttributeSet) : super(ctx,attrs) {}
}
```

## overloading

**在基类中，使用fun声明函数时，此函数默认为`final`修饰，不能被子类重写**。如果允许子类重写该函数，那么就要手动添加`open`修饰它, 子类重写方法使用`override`关键词：

```kotlin
/**用户基类**/
open class Person{
    open fun study(){       // 允许子类重写
        println("我毕业了")
    }
}

/**子类继承 Person 类**/
class Student : Person() {
    override fun study(){    // 重写方法
        println("我在读大学")
    }
}
```

如果有多个相同的方法（继承或者实现自其他类，如A、B类），则必须要重写该方法，使用super范型去选择性地调用父类的实现。

```kotlin
open class A {
    open fun f () { print("A") }
}

interface B {
    fun f() { print("B") } //接口的成员变量默认是 open 的
}

class C() : A() , B{
    override fun f() {
        super<A>.f()//调用 A.f(), optional
        super<B>.f()//调用 B.f(), optional
    }
}
```

> C 继承自 a() 或 b(), C 不仅可以从 A 或则 B 中继承函数，而且 C 可以继承 A()、B() 中共有的函数。此时该函数在中只有一个实现，为了消除歧义，must 提供自己的实现。

## property overloading

属性重写使用 override 关键字，属性必须具有**兼容类型**，每一个声明的属性都可以通过**初始化程序或者getter**方法被重写

你可以用一个**var属性重写一个val属性**，但是反过来不行。因为val属性本身定义了getter方法，重写为var属性会在衍生类中额外声明一个setter方法

你可以在主构造函数中使用 override 关键字作为属性声明的一部分:

```kotlin
interface Foo {
    val count: Int
}

class Bar1(override val count: Int) : Foo

class Bar2 : Foo {
    override var count: Int = 0
}
```

## operator overloading

# Interface

Kotlin 接口与 Java 8 类似，使用 interface 关键字定义接口，**允许方法有默认实现**：

**接口中的属性**

接口中的属性只能是抽象的，不允许初始化值，接口不会保存属性值，实现接口时，必须重写属性

```kotlin
interface MyInterface {
    var name:String //name 属性, 抽象的
    fun bar()
    fun foo() {
        // 可选的方法体
        println("foo")
    }
}
class Child : MyInterface {
    override var name: String = "runoob" //重写属性
    override fun bar() {
        // 方法体
        println("bar")
    }
}
fun main(args: Array<String>) {
    val c =  Child()
    c.foo();
    c.bar();
    println(c.name)
 
}
```

---

# extension

## function extension

扩展函数可以在已有类中添加新的方法，不会对原类做修改

```kotlin
class User(var name:String)

/**扩展函数**/
fun User.Print(){
    print("用户名 $name")
}

// 扩展函数 swap,调换不同位置的值
fun MutableList<Int>.swap(index1: Int, index2: Int) {
    val tmp = this[index1]     //  this 对应该列表
    this[index1] = this[index2]
    this[index2] = tmp
}

fun main(arg:Array<String>){
    var user = User("Runoob")
    user.Print()
    
    val l = mutableListOf(1, 2, 3)
    // 位置 0 和 2 的值做了互换
    l.swap(0, 2) // 'swap()' 函数内的 'this' 将指向 'l' 的值
}
```

## 扩展函数是静态解析的

扩展函数是静态解析的，并不是接收者类型的虚拟成员，在调用扩展函数时，具体被调用的的是哪一个函数，由调用函数的的对象表达式来决定的，而不是动态的类型决定的:

```kotlin
open class C

class D: C()

fun C.foo() = "c"   // 扩展函数 foo

fun D.foo() = "d"   // 扩展函数 foo

fun printFoo(c: C) {
    println(c.foo())  // 类型是 C 类
}

fun main(arg:Array<String>){
    printFoo(D())	// output is c
}
```

若扩展函数和成员函数一致，则使用该函数时，会**优先使用成员函数**。

# 数据类与密封类

## 数据类

Kotlin 可以创建一个只包含数据的类，关键字为 `data`：

```kotlin
data class User(val name: String, val age: Int)
```

编译器会自动的从主构造函数中根据所有声明的属性提取以下函数：

- `equals()` / `hashCode()`
- `toString()` 格式如 `"User(name=John, age=42)"`
- `componentN() functions` 对应于属性，按声明顺序排列
- `copy()` 函数

如果这些函数在类中已经被明确定义了，或者从超类中继承而来，就不再会生成。

为了保证生成代码的一致性以及有意义，数据类需要满足以下条件：

- 主构造函数至少包含一个参数。
- 所有的主构造函数的参数必须标识为`val` 或者 `var` ;
- 数据类不可以声明为 `abstract`, `open`, `sealed` 或者 `inner`;
- 数据类不能继承其他类 (但是可以实现接口)。

**复制**

复制使用 copy() 函数，我们可以使用该函数复制对象并修改部分属性, 对于上文的 User 类，其实现会类似下面这样：

```kotlin
fun copy(name: String = this.name, age: Int = this.age) = User(name, age)
```

### 解构声明

like python `cli_sock, raddr = serv_sock.accept()`

组件函数允许数据类在解构声明中使用：

```kotlin
val jane = User("Jane", 35)
val (name, age) = jane
println("$name, $age years of age") // prints "Jane, 35 years of age"
```

# diff from java

## val && var

`val`, immutable
`var`, mutable

```kotlin
    var a =3
    a = 4
    
    val b = 3
    b = 4   // error, can't be reassigned
```

## null safty

default is not nullable, like `var str: String = ""`

nullabel, `var str: String? = null`

useful in chained calls

```kotlin
//类型后面加?表示可为空
var age: String? = "23" 
//抛出空指针异常
val ages = age!!.toInt()
//不做处理返回 null
val ages1 = age?.toInt()
//age为空返回-1
val ages2 = age?.toInt() ?: -1

fun sendMessageToClient(
        client: Client?, message: String?, mailer: Mailer
) {
    val email/*: String?*/ = client?.personalInfo?.email
    // mailer.sendMessage(email, message)   // error, expected String, but inferred String?
    if (email != null && message != null)
    // type auto converted in this scope
        mailer.sendMessage(email, message)
    // mailer.sendMessage(email, message)   // error, type recovered to String?

    /*
    mailer.sendMessage(client?.personalInfo?.email?:"", message?:"")
    */
}

class Client(val personalInfo: PersonalInfo?)
class PersonalInfo(val email: String?)
interface Mailer {
    fun sendMessage(email: String, message: String)
}
```

## no `new`

```kotlin
class A{}
a = A()
```

## class and method

1. class and method default is `final`, except `abstract class` and `interface`,  can't be inherite, use `open` to inherit

```kotlin
open class A{
    open fun m1(){}
}

class B : A{
    override fun m1(){}		// must use override
}
```

## smart cast

我们可以使用`is`运算符检测一个表达式是否某类型的一个实例(类似于Java中的instanceof关键字)。

```kotlin
fun getStringLength(obj: Any): Int? {
  if (obj is String) {
    // 做过类型判断以后，obj会被系统自动转换为String类型
    return obj.length 
  }

  // 这里的obj仍然是Any类型的引用
  return null
}
```

```kotlin
fun getStringLength(obj: Any): Int? {
  if (obj !is String)
    return null
  // 在这个分支中, `obj` 的类型会被自动转换为 `String`
  return obj.length
}
```

```kotlin
fun getStringLength(obj: Any): Int? {
  // 在 `&&` 运算符的右侧, `obj` 的类型会被自动转换为 `String`
  if (obj is String && obj.length > 0)
    return obj.length
  return null
}
```

```kotlin
fun eval(expr: Expr): Int =
        when (expr) {
            is Num -> expr.value
            is Sum -> eval(expr.left) + eval(expr.right)
            else -> throw IllegalArgumentException("Unknown expression")
        }

interface Expr
class Num(val value: Int) : Expr
class Sum(val left: Expr, val right: Expr) : Expr

fun main() {
    println(eval(Sum(Num(1), Num(2))))
}
```

## range

区间表达式由具有操作符形式`..`的 rangeTo 函数辅以`in`和`!in`形成。

区间是为**任何可比较类型**定义的，但对于整型原生类型，它有一个优化的实现。以下是使用区间的一些示例:

```kotlin
for (i in 1..4) print(i) // 输出“1234”
for (i in 4..1) print(i) // 什么都不输出
if (i in 1..10) { // 等同于 1 <= i && i <= 10
    println(i)
}

// 使用 step 指定步长
for (i in 1..4 step 2) print(i) // 输出“13”
for (i in 4 downTo 1 step 2) print(i) // 输出“42”
// 使用 until 函数排除结束元素
for (i in 1 until 10) {   // i in [1, 10) 排除了 10
     println(i)
}
```

### self defined range

`contains`: 

In Kotlin in checks are translated to the corresponding contains calls:

```kotlin
val list = listOf("a", "b")
"a" in list  // list.contains("a")
"a" !in list // !list.contains("a")
```

`rangeTo`: 

Implement the function MyDate.rangeTo(). This allows you to create a range of dates using the following syntax:
`MyDate(2015, 5, 11)..MyDate(2015, 5, 12)`

```kotlin
data class MyDate(val year: Int, val month: Int, val dayOfMonth: Int) : Comparable<MyDate>{
    override fun compareTo(other: MyDate): Int{
        if(year != other.year) return year - other.year
        if(month != other.month) return month - other.month
        return dayOfMonth - other.dayOfMonth
    }
}

class DateRange(val start: MyDate, val endInclusive: MyDate){
    operator fun contains(date: MyDate): Boolean = date > start && date < endInclusive
}

fun checkInRange(date: MyDate, first: MyDate, last: MyDate): Boolean {
    return date in DateRange(first, last)
}

// version 2
operator fun MyDate.rangeTo(other: MyDate) = DateRange(this, other)

class DateRange(override val start: MyDate, override val endInclusive: MyDate): ClosedRange<MyDate>

fun checkInRange(date: MyDate, first: MyDate, last: MyDate): Boolean {
    return date in first..last
}
```



## lambda

if last arg is function, can place it outside the parenthesis

```kotlin
val arrayList = arrayListOf(1, 5, 2)
Collections.sort(arrayList, {x, y -> y - x})

// or
Collections.sort(arrayList){x, y -> y - x}
```

## when expression

```kotlin
when (x) {
    1 -> print("x == 1")
    2 -> print("x == 2")
    else -> { // 注意这个块
        print("x 不是 1 ，也不是 2")
    }
}

when (x) {
        in 0..10 -> println("x 在该区间范围内")
        else -> println("x 不在该区间范围内")
    }

when {
    x.isOdd() -> print("x is odd")
    x.isEven() -> print("x is even")
    else -> print("x is funny")
}
```

