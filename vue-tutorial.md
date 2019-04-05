# Vue

<https://vuejs.org/v2/guide/>

Vue.js（读音 /vjuː/, 类似于 view） 是一套构建用户界面的渐进式框架。
Vue 只关注视图层， 采用自底向上增量开发的设计。
Vue 的目标是通过尽可能简单的 API 实现响应的数据绑定和组合的视图组件。

# MVVM框架VUE实现原理

<http://baijiahao.baidu.com/s?id=1596277899370862119&wfr=spider&for=pc>

## MVVM定义

MVVM是Model-View-ViewModel的简写。即模型-视图-视图模型。
【模型】指的是后端传递的数据。【视图】指的是所看到的页面。【视图模型】mvvm模式的核心，它是连接view和model的桥梁。它有两个方向：

- 一是将【模型】转化成【视图】，即将后端传递的数据转化成所看到的页面。实现的方式是：**数据绑定**。
- 二是将【视图】转化成【模型】，即将所看到的页面转化成后端的数据。实现的方式是：DOM 事件监听。

这两个方向都实现的，我们称之为数据的双向绑定。

> 总结：在MVVM的框架下视图和模型是不能直接通信的。它们通过ViewModel来通信，ViewModel通常要实现一个**observer**观察者，当**数据发生变化**，ViewModel能够监听到数据的这种变化，然后通知到对应的视图做自动更新，而当用户操作视图，ViewModel也能监听到**视图的变化**，然后通知数据做改动，这实际上就实现了数据的双向绑定。

## 主流框架实现双向绑定（响应式）的做法

1. 脏值检查
`angular.js`
通过脏值检测的方式比对数据是否有变更，来决定是否更新视图，**最简单的方式**就是通过 setInterval() 定时轮询检测数据变动.
当然Google不会这么low，angular只有在**指定的事件触发时进入脏值检测**，大致如下： DOM事件，譬如用户输入文本，点击按钮等。( ng-click ) XHR响应事件 ( $http ) 浏览器Location变更事件 ( $location ) Timer事件( $timeout , $interval ) 执行 $digest() 或 $apply()在 Angular 中组件是以树的形式组织起来的，相应地，检测器也是一棵树的形状。当一个异步事件发生时，脏检查会从根组件开始，自上而下对树上的所有子组件进行检查，这种检查方式的性能存在很大问题。

2. 观察者-订阅者（数据劫持）
`vue.js` 
**Observer 数据监听器**，把一个普通的 JavaScript 对象传给 Vue 实例的 data 选项，Vue 将遍历此对象所有的属性，并使用Object.defineProperty()方法把这些属性全部转成setter、getter方法。当data中的某个属性被访问时，则会调用getter方法，当data中的属性被改变时，则会调用setter方法。
**Compile指令解析器**，它的作用对每个元素节点的指令进行解析，替换模板数据，并绑定对应的更新函数，初始化相应的订阅。
**Watcher 订阅者**，作为连接 Observer 和 Compile 的桥梁，能够订阅并收到每个属性变动的通知，执行指令绑定的相应回调函数。Dep 消息订阅器，内部维护了一个数组，用来收集订阅者（Watcher），数据变动触发notify 函数，再调用订阅者的 update 方法。执行流程如下：

![vue-mvvm-flow-chart](images/vue-mvvm.png)

从图中可以看出，当执行 new Vue() 时，Vue 就进入了**初始化阶段**

- 遍历 data 选项中的属性，并用 Object.defineProperty 将它们转为 getter/setter，实现数据变化监听功能
- 指令编译器Compile 对元素节点的指令进行解析，初始化视图，并**订阅Watcher** 来更新视图， 此时Wather 会将自己添加到消息订阅器中(Dep),初始化完毕。
- 当数据发生变化时，Observer 中的 setter 方法被触发，setter 会立即调用Dep.notify()，Dep 开始遍历所有的订阅者，并调用订阅者的 update 方法，订阅者收到通知后对视图进行相应的更新。
 
因为VUE使用Object.defineProperty方法来做数据绑定，而这个方法又无法通过兼容性处理，所以Vue 不支持 IE8 以及更低版本浏览器。另外，查看vue原代码，发现在vue初始化实例时， 有一个proxy代理方法，它的作用就是遍历data中的属性，把它代理到vm的实例上，这也就是我们可以这样调用属性：vm.aaa等于vm.data.aaa。

[Vue监听数据对象变化源码](https://www.jb51.net/article/107913.htm)

# simple cdn vue

`index.html`

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>VueJS Tutorials</title>
    <link href="styles.css" rel="stylesheet" />
    <script src="https://unpkg.com/vue"></script>
</head>

<body>
    <div id="vue-app">
        <h1>Hey, {{ name }}</h1>
    </div>
</body>

<script src="app.js"></script>

</html>
```

`app.js`
```js
new Vue({
    el: '#vue-app',
    data: {
        name: 'Shaun'
    }
});
/*
el: element, must be a root container
*/
```

`style.css`
```css
```

# Template syntax

## Interpolations

```html
<!-- text -->
<span>Message: {{ msg }}</span>

<!-- raw Html -->
<p>Using mustaches: {{ rawHtml }}</p>
<p>Using v-html directive: <span v-html="rawHtml"></span></p>

<!-- Attributes -->
<div v-bind:id="dynamicId"></div>

<!-- javascript expressions -->
{{ number + 1 }}
{{ ok ? 'YES' : 'NO' }}
{{ message.split('').reverse().join('') }}
<div v-bind:id="'list-' + id"></div>

<!-- can only contain one single expression, so the following will NOT work: -->

<!-- this is a statement, not an expression: -->
{{ var a = 1 }}
<!-- flow control won't work either, use ternary expressions -->
{{ if (ok) { return message } }}
```

> **Note**: Template expressions are sandboxed and only have access to a whitelist of globals such as `Math` and `Date`. You should not attempt to access user defined globals in template expressions.

## Directives

```html
<!-- emove/insert the <p> element based on the truthiness of the value of the expression seen -->
<p v-if="seen">Now you see me</p>

<!-- arguments -->
<!-- Some directives can take an “argument”, denoted by a colon after the directive name.  -->

<!--  the v-bind directive is used to reactively update an HTML attribute -->
<a v-bind:href="url"> ... </a>
<!--  listens to DOM events -->
<a v-on:click="doSomething"> ... </a>

<!-- dynamic arguments -->
<a v-bind:[attributeName]="url"> ... </a>

<!-- modifiers -->
<!-- the .prevent modifier tells the v-on directive to call event.preventDefault() on the triggered event -->
<form v-on:submit.prevent="onSubmit"> ... </form>
```

## shorthand

> Vue provides special shorthands for two of the most often used directives, `v-bind` and `v-on`:

```html
<!-- v-bind -->

<!-- full syntax -->
<a v-bind:href="url"> ... </a>
<!-- shorthand -->
<a :href="url"> ... </a>
<!-- shorthand with dynamic argument (2.6.0+) -->
<a :[key]="url"> ... </a>

<!-- v-on -->

<!-- full syntax -->
<a v-on:click="doSomething"> ... </a>
<!-- shorthand -->
<a @click="doSomething"> ... </a>
<!-- shorthand with dynamic argument (2.6.0+) -->
<a @[event]="doSomething"> ... </a>
```

# Event Handling

## Listening to Events

```html
<div id="example-1">
  <button v-on:click="counter += 1">Add 1</button>
  <p>The button above has been clicked {{ counter }} times.</p>
</div>
```

```js
var example1 = new Vue({
  el: '#example-1',
  data: {
    counter: 0
  }
})
```
## method in inline handles

> You can pass it into a method using the special `$event` variable

```html
<button v-on:click="warn('Form cannot be submitted yet.', $event)">
  Submit
</button>
```

```js
// ...
methods: {
  warn: function (message, event) {
    // now we have access to the native event
    if (event) event.preventDefault()
    alert(message)
  }
}
```

