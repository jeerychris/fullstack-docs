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
<!-- remove/insert the <p> element based on the truthiness of the value of the expression seen -->
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
## event modifiers

> It is a very common need to call `event.preventDefault()` or `event.stopPropagation()` inside event handlers. Although we can do this easily inside methods, it would be better if the methods can be purely about data logic rather than having to deal with DOM event details.

```html
<!-- the click event's propagation will be stopped -->
<a v-on:click.stop="doThis"></a>

<!-- the submit event will no longer reload the page -->
<form v-on:submit.prevent="onSubmit"></form>

<!-- modifiers can be chained -->
<a v-on:click.stop.prevent="doThat"></a>

<!-- just the modifier -->
<form v-on:submit.prevent></form>

<!-- use capture mode when adding the event listener -->
<!-- i.e. an event targeting an inner element is handled here before being handled by that element -->
<div v-on:click.capture="doThis">...</div>

<!-- only trigger handler if event.target is the element itself -->
<!-- i.e. not from a child element -->
<div v-on:click.self="doThat">...</div>
```

## key modifiers

```html
<div id="vue-app">
    <h1>Keyboard Events</h1>
    <label>Name:</label>
    <input type="text" v-on:keyup.enter="logName" />
    <label>Age:</label>
    <input type="text" v-on:keyup.alt.enter="logAge" />

    <!-- this will fire even if Alt or Shift is also pressed -->
    <button @click.ctrl="onClick">A</button>
    <!-- this will only fire when Ctrl and no other keys are pressed -->
    <button @click.ctrl.exact="onCtrlClick">A</button>
</div>
```

# Form Input Bindings (双向绑定)

> You can use the `v-model` directive to create two-way data bindings on form input, textarea, and select elements.

**NOTE**: `v-model` will ignore the initial `value`, `checked` or `selected` attributes found on any form elements. It will always treat the Vue instance data as the source of truth. You should declare the initial value on the JavaScript side, inside the `data` option of your component.

```html
<div id="vue-app">
    <h1>Keyboard Events</h1>
    <label>Name:</label>
    <input type="text" v-on:keyup.enter="logName" />
    <span>{{ name }}</span>
    <label>Age:</label>
    <input type="text" v-on:keyup.alt.enter="logAge" v-model="age" />
    <span>{{ age }}</span>
</div>
```
## basic

### Text
### textarea
### checkbox
### radio
### select

<https://vuejs.org/v2/guide/forms.html>

```html
<!-- Text -->
<input v-model="message" placeholder="edit me">
<p>Message is: {{ message }}</p>
<!-- textarea -->
<span>Multiline message is:</span>
<p style="white-space: pre-line;">{{ message }}</p>
<br>
<textarea v-model="message" placeholder="add multiple lines"></textarea>
<!-- checkbox -->
<input type="checkbox" id="checkbox" v-model="checked">
<label for="checkbox">{{ checked }}</label>
<!-- radio -->
<!-- select -->
```

**NOTE**: Interpolation on textareas (`<textarea>{{text}}</textarea>`) won't work. Use `v-model` instead.

## value binding

```html
<input
  type="checkbox"
  v-model="toggle"
  true-value="yes"
  false-value="no"
>
```

```js
// when checked:
vm.toggle === 'yes'
// when unchecked:
vm.toggle === 'no'
```

## modifiers

```html
<!-- synced after "change" instead of "input" -->
<input v-model.lazy="msg" >
<input v-model.number="age" type="number">
<input v-model.trim="msg">
```

# Computed Properties and Watchers

## Computed Properties

> In-template expressions are very **convenient**, but they are meant **for simple operations**. Putting too much logic in your templates can make them bloated and hard to maintain. For example:

```html
<div id="example">
  {{ message.split('').reverse().join('') }}
</div>
```

At this point, the template is no longer **simple and declarative**. You have to look at it for a second before realizing that it displays `message` in reverse. The problem is made worse when you want to include the reversed message in your template more than once.

That’s **why** for any complex logic, you should use a computed property.

### basic example

```html
<div id="example">
  <p>Original message: "{{ message }}"</p>
  <p>Computed reversed message: "{{ reversedMessage }}"</p>
</div>
```

```js
var vm = new Vue({
  el: '#example',
  data: {
    message: 'Hello'
  },
  computed: {
    // a computed getter
    reversedMessage: function () {
      // `this` points to the vm instance
      return this.message.split('').reverse().join('')
    }
  }
})
```

### Computed Caching vs Methods

You may have noticed we can achieve the same result by invoking a method in the expression:

```html
<p>Reversed message: "{{ reverseMessage() }}"</p>
```
```js
// in component
methods: {
  reverseMessage: function () {
    return this.message.split('').reverse().join('')
  }
}
```

the difference is that **computed properties are cached based on their reactive dependencies.** A computed property will **only re-evaluate** when some of its **reactive dependencies** have changed. <span style="background-color:yellow">This means as long as `message` has not changed, multiple access to the `reversedMessage` computed property will immediately return the previously computed result without having to run the function again.</span>

### Computed vs Watched Property

### computed setter

# Class and Style Bindings

> A common need for data binding is manipulating an element’s class list and its inline styles. Since they are both attributes, we can use `v-bind` to handle them: we only need to calculate a final string with our expressions. However, **meddling with string concatenation is annoying and error-prone**. For this reason, Vue provides special enhancements when `v-bind` is used with `class` and `style`. In addition to strings, the expressions can also evaluate to objects or arrays.

## Binding HTML classes

### Object Syntax

```html
<div v-bind:class="{ active: isActive }"></div>
```

The above syntax means the presence of the `active` class will be determined by the truthiness of the data property `isActive`.

You can have multiple classes toggled by having more fields in the object. In addition, the `v-bind:class` directive can also **co-exist with the plain `class` attribute**. So given the following template:

```html
<div
  class="static"
  v-bind:class="{ active: isActive, 'text-danger': hasError }"
></div>
```

And the following data:

```js
data: {
  isActive: true,
  hasError: false
}
```

It will render:

```html
<div class="static active"></div>
```

When `isActive` or `hasError` changes, the class list will be updated accordingly. For example, if `hasError` becomes `true`, the class list will become `"static active text-danger"`.

The bound object doesn’t have to be inline, We can also bind to a computed property that returns an object. This is a common and powerful pattern:

```html
<div v-bind:class="classObject"></div>
```
```js
data: {
  isActive: true,
  error: null
},
computed: {
  classObject: function () {
    return {
      active: this.isActive && !this.error,
      'text-danger': this.error && this.error.type === 'fatal'
    }
  }
}
```

### Array Syntax

We can pass an array to `v-bind:class` to apply a list of classes:

```html
<div v-bind:class="[activeClass, errorClass]"></div>
```
```js
data: {
  activeClass: 'active',
  errorClass: 'text-danger'
}
```

Which will render:

```html
<div class="active text-danger"></div>
```

If you would like to also toggle a class in the list conditionally, you can do it with a ternary expression:

```html
<div v-bind:class="[isActive ? activeClass : '', errorClass]"></div>
```

This will always apply `errorClass`, but will only apply `activeClass` when `isActive`is truthy.

However, this can be a bit verbose if you have multiple conditional classes. That’s why it’s also possible to use the object syntax inside array syntax:

```html
<div v-bind:class="[{ active: isActive }, errorClass]"></div>
```

### With Components

// TODO

## Binding Inline Styles

### Object Syntax

The object syntax for `v-bind:style` is pretty straightforward - it looks almost like CSS, except it’s a JavaScript object. You can use either camelCase or kebab-case (use quotes with kebab-case) for the CSS property names:

```html
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```
```js
data: {
  activeColor: 'red',
  fontSize: 30
}
```

It is often a good idea to bind to a style object directly so that the template is cleaner:

```html
<div v-bind:style="styleObject"></div>
```
```js
data: {
  styleObject: {
    color: 'red',
    fontSize: '13px'
  }
}
```

**NOTE**: <span style="background-color:yellow">Again, the object syntax is often used in conjunction with computed properties that return objects.</span>

# Conditional Rendering

<https://vuejs.org/v2/guide/conditional.html#v-if>

## `v-if`

The directive `v-if` is used to conditionally render a block. **The block will only be rendered if the directive’s expression returns a truthy value**.

```html
<h1 v-if="awesome">Vue is awesome!</h1>
```

It is also possible to add an “else block” with `v-else`:

```html
<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```

### Conditional Groups with `v-if` on `<template>`

Because `v-if` is a directive, it has to be attached to a single element. But what if we want to toggle more than one element? In this case we can use `v-if` on a `<template>` element, which serves as an invisible wrapper. The final rendered result will not include the `<template>` element.

```
<template v-if="ok">
  <h1>Title</h1>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</template>
```

### `v-else`

You can use the `v-else` directive to indicate an “else block” for `v-if`:

```html
<div v-if="Math.random() > 0.5">
  Now you see me
</div>
<div v-else>
  Now you don't
</div>
```

A `v-else` element must immediately follow a `v-if` or a `v-else-if` element - otherwise it will not be recognized.

### `v-else-if`

> New in 2.1.0+

The `v-else-if`, as the name suggests, serves as an “else if block” for `v-if`. It can also be chained multiple times:

```html
<div v-if="type === 'A'">
  A
</div>
<div v-else-if="type === 'B'">
  B
</div>
<div v-else-if="type === 'C'">
  C
</div>
<div v-else>
  Not A/B/C
</div>
```

Similar to `v-else`, a `v-else-if` element must immediately follow a `v-if` or a `v-else-if` element.

### Controlling Reusable Elements with `key`

## `v-show`

Another option for conditionally displaying an element is the `v-show` directive. The usage is largely the same:

```html
<h1 v-show="ok">Hello!</h1>
```

The difference is that an element with `v-show` **will always be rendered and remain in the DOM**; `v-show` only toggles the `display` CSS property of the element.

Note that `v-show` doesn’t support the `<template>` element, nor does it work with `v-else`.

## `v-if` vs `v-show`

`v-if` is “real” conditional rendering because it ensures that event listeners and child components inside the conditional block are properly destroyed and re-created during toggles.

`v-if` is also **lazy**: if the condition is false on initial render, it will not do anything - the conditional block won’t be rendered until the condition becomes true for the first time.

In comparison, `v-show` is much simpler - the element is always rendered regardless of initial condition, with **CSS-based toggling**.

Generally speaking, `v-if` has higher toggle costs while `v-show` has higher initial render costs. So prefer `v-show` if you need to toggle something very often, and prefer `v-if` if the condition is unlikely to change at runtime.

## `v-if` with `v-for`

Using `v-if` and `v-for` together is **not recommended**. See the [style guide](https://vuejs.org/v2/style-guide/#Avoid-v-if-with-v-for-essential) for further information.

When used together with `v-if`, `v-for` has a higher priority than `v-if`. See the list rendering guide for details.

# List Rendering

<https://vuejs.org/v2/guide/list.html#Mapping-an-Array-to-Elements-with-v-for>

## Mapping an Array to Elements with `v-for`

We can use the `v-for` directive to render a list of items based on an array. The `v-for`directive requires a special syntax in the form of `item in items`, where `items` is the source data array and `item` is an **alias** for the array element being iterated on:

```html
<ul id="example-1">
  <li v-for="item in items">
    {{ item.message }}
  </li>
</ul>
```
```js
var example1 = new Vue({
  el: '#example-1',
  data: {
    items: [
      { message: 'Foo' },
      { message: 'Bar' }
    ]
  }
})
```

```html
<ul id="example-1">
  <li v-for="(item, index) in items">
    {{ parentMessage }} - {{ index }} - {{ item.message }}
  </li>
</ul>
```

## `v-for` with an Object

You can also use `v-for` to iterate through the properties of an object.

```html
<ul id="v-for-object" class="demo">
  <li v-for="value in object">
    {{ value }}
  </li>
</ul>
```
```js
new Vue({
  el: '#v-for-object',
  data: {
    object: {
      firstName: 'John',
      lastName: 'Doe',
      age: 30
    }
  }
})
```

You can also provide a second argument for the key:

```html
<div v-for="(value, key) in object">
  {{ key }}: {{ value }}
</div>
```

And another for the index:

```html
<div v-for="(value, key, index) in object">
  {{ index }}. {{ key }}: {{ value }}
</div>
```

When iterating over an object, the order is based on the key enumeration order of `Object.keys()`, which is **not** guaranteed to be consistent across JavaScript engine implementations.

# Components Basics

## Base Example

<https://vuejs.org/v2/guide/components.html#Base-Example>

Here’s an example of a Vue component:

```js
// Define a new component called button-counter
Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})
```

Components are reusable Vue instances with a name: in this case, `<button-counter>`. We can use this component as a custom element inside a root Vue instance created with `new Vue`:

```html
<div id="components-demo">
  <button-counter></button-counter>
</div>
```
```js
new Vue({ el: '#components-demo' })
```

Since components are reusable Vue instances, they accept the same options as `new Vue`, such as `data`, `computed`, `watch`, `methods`, and **lifecycle hooks**. The only exceptions are a few root-specific options like `el`.

## Reusing Components

Components can be reused as many times as you want:

```html
<div id="components-demo">
  <button-counter></button-counter>
  <button-counter></button-counter>
  <button-counter></button-counter>
</div>
```

Notice that when clicking on the buttons, **each one maintains its own, separate `count`**. That’s because each time you use a component, a new **instance** of it is created.

### `data` Must Be a Function

When we defined the `<button-counter>` component, you may have noticed that `data` wasn’t directly provided an object, like this:

```js
data: {
  count: 0
}
```

Instead, **a component’s data option must be a function**, so that each instance can maintain an independent copy of the returned data object:

```js
data: function () {
  return {
    count: 0
  }
}
```

If Vue didn’t have this rule, clicking on one button would affect the data of *all other instances*, like below:

## Organizing Components

It’s common for an app to be organized into a tree of nested components:

![app-and-components](images/components.png)

For example, you might have components for a header, sidebar, and content area, each typically containing other components for navigation links, blog posts, etc.

To use these components in templates, they must be registered so that Vue knows about them. There are two types of component registration: **global** and **local**. So far, we’ve only registered components globally, using `Vue.component`:

```js
Vue.component('my-component-name', {
  // ... options ...
})
```

Globally registered components can be used in the template of any root Vue instance (`new Vue`) created afterwards – and even inside all subcomponents of that Vue instance’s component tree.

[Component Registration](https://vuejs.org/v2/guide/components-registration.html).


# Vue CLI

<https://cli.vuejs.org/guide/>

