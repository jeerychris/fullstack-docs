[TOC]

# javascript datatypes

**Dynamic feature**

> This means that the same variable can be used to hold different data types

```javascript
var x;           // Now x is undefined
x = 5;           // Now x is a Number
x = "John";      // Now x is a String
```

## Primitive Data

A primitive data value is a single simple data value with no additional properties and methods.

The `typeof` operator can return one of these primitive types:

- `string`

- `number`

- `boolean`

- `undefined`

    ```javascript
    typeof "John"              // Returns "string" 
    typeof 3.14                // Returns "number"
    typeof true                // Returns "boolean"
    typeof false               // Returns "boolean"
    typeof x                   // Returns "undefined" (if x has no value)
    ```

### string

==both single quotes and double quotes are supported, and all support especial character escape==. 

[@see also: Never Declare Number, String, or Boolean Objects](#Never Declare Number, String, or Boolean Objects)

```js
var answer2 = "He is called 'Johnny'";
var answer3 = 'He is called "Johnny"';

var x = "We are the so-called \"Vikings\" from the north.";
var x = 'It\'s alright.';
```

### number

==all number are stored in double precision inside javascript==

#### Definition

- **NaN**
- **Infinity**

[@see also: Beware of Automatic Type Conversions](#Beware of Automatic Type Conversions)

```js
var x = 10 / 0;		// no error
```

#### Common methods

```js
32.toString(10)		// incorrect, get a error

var x = 32;			// correct
x.toString(8);
```

`toFixed()` returns a string, with the number written with a specified number of decimals

```js
var x = 9.656;
x.toFixed(0);           // returns 10
x.toFixed(2);           // returns 9.66
x.toFixed(4);           // returns 9.6560
x.toFixed(6);           // returns 9.656000
```

**Converting Variables to Numbers**

There are 3 JavaScript methods that can be used to convert variables to numbers:

- The `Number()` method
- The `parseInt()` method
- The `parseFloat()` method

### boolean

==Everything With a "Value" is True, Everything Without a "Value" is False==

[@see also: 明智地使用真假判断](#明智地使用真假判断)

下列表达式统统返回 false：`false`, `0`, `undefined`, `null`, `NaN`, `''`

#### JS Comparisons

**Conditional (Ternary) Operator**

```js
var voteable = (age < 18) ? "Too young":"Old enough";
```

**Compare different type**

Comparing data of different types may give unexpected results.

> When ==comparing a string with a number==, JavaScript will ==convert the string to a number== when doing the comparison. An empty string converts to 0. A non-numeric string converts to `NaN` which is always `false`.

| Case       | Value |
| ---------- | ----- |
| 2 < 12     | true  |
| 2 < "12"   | true  |
| 2 < "John" | false |
| 2 > "John" | false |
| "2" < "12" | false |
| "2" > "12" | true  |

When comparing two strings, "2" will be greater than "12", because (alphabetically) 1 is less than 2.

### undefined

In JavaScript, a variable ==without a value==, has the value `undefined`. The type is also `undefined`.

```javascript
var car;    // Value is undefined, type is undefined
var dog = undefined;
```

#### Empty value & undefined & null

An empty value has nothing to do with `undefined`.

```javascript
var car = "";    // The value is "", the typeof is "string"
```

In JavaScript `null` is "nothing". It is supposed to be something that doesn't exist.

Unfortunately, in JavaScript, the data type of `null` is an object.

```javascript
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
person = null;    // Now value is null, but type is still an object
```

`undefined` and `null` are equal in value but different in type:

```javascript
typeof undefined           // undefined
typeof null                // object
typeof ""				   // string

null === undefined         // false
null == undefined          // true
null == ""          	   // false
```

# 

## Complex Data

The `typeof` operator can return one of two complex types:

- `function`
- `object`

The `typeof` operator returns object for both objects, arrays, and null.

The `typeof` operator does not return object for functions.

```javascript
typeof {name:'John', age:34} // Returns "object"
typeof [1,2,3,4]             // Returns "object" (not "array", see note below)
typeof null                  // Returns "object"
typeof function myFunc(){}   // Returns "function"
```

> **Note:**The `typeof` operator returns "`object`" for arrays because in JavaScript arrays are objects.

### function

[@more: 全局命名空间污染与 IIFE](#全局命名空间污染与 IIFE)

#### Function Invocation

The code inside the function will execute when "something" **invokes** (calls) the function:

- When an event occurs (when a user clicks a button)
- When it is invoked (called) from JavaScript code
- ==Automatically (self invoked)==

#### The () Operator

Using the example above, **`toCelsius`** refers to the ==function object==, and **`toCelsius()`** refers to the ==function result==.

Accessing a function without () will return the function definition instead of the function result

```js
function toCelsius() {
    return (5 / 9) * (Math.floor(Math.random() * 200) - 32);
}
/*
@return:
function toCelsius() {
    return (5 / 9) * (Math.floor(Math.random() * 200) - 32);
}
 */
console.log(toCelsius);

/**
 * @return
 * 31.111111111111114, <b>note</b> this is random
 */
console.log(toCelsius());

```

#### Function Definitions

**Function Declarations**

```js
function myFunction(a, b) {
  return a * b;
}
```

==Semicolons are used to separate executable JavaScript statements.==
==Since a function **declaration** is not an executable statement, it is not common to end it with a semicolon.==

**function expression**

```js
var x = function (a, b) {return a * b};
```

The function above is actually an **anonymous function** (a function without a name).

**The Function() Constructor**

```js
var myFunction = new Function("a", "b", "return a * b");

var x = myFunction(4, 3);
```

**Function Hoisting**

```js
myFunction(5);

function myFunction(y) {
  return y * y;
}
```

**Self-Invoking Functions**

==only run once==

```js
(function () {
  var x = "Hello!!";  // I will invoke myself
})();
```

**Functions are Objects**

The `typeof` operator in JavaScript returns "function" for functions.

But, JavaScript functions can best be described as objects.

JavaScript functions have both **properties** and **methods**.

The `arguments.length` property returns the number of arguments received when the function was invoked:

```js
function myFunction(a, b) {
  return arguments.length;
}
console.log(myFunction.toString());
```

**Arrow functions**

```js
// ES5
var x = function(x, y) {
  return x * y;
}

// ES6
const x = (x, y) => x * y;
```

Arrow functions **do not have their own `this`**. They are not well suited for defining **object methods**.

Arrow functions are **not hoisted**. They must be defined **before** they are used.

Using `const` is safer than using `var`, because a function expression is always constant value.

You can only omit the `return` keyword and the curly brackets if the ==function is a single statement==. Because of this, it might be a good habit to always keep them:

```js
const x = (x, y) => { return x * y };
```

#### Function Parameters

Function **parameters** are the **names** listed in the function definition.

Function **arguments** are the real **values** passed to (and received by) the function.

**Parameter rules**

JavaScript function definitions do not specify data types for parameters.

JavaScript functions ==do not perform type checking== on the passed arguments.

JavaScript functions ==do not check the number of arguments received==.

**Default parameters**

[ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp) allows default parameters in the function call:

```js
function (a=1, b=1) { // function code }
```

##### Arguments are Passed by Value

The parameters, in a function call, are the function's arguments.

JavaScript arguments are passed by **value**: The function only gets to know the values, not the argument's locations.

If a function changes an argument's value, it does not change the parameter's original value.

**Changes to arguments are not visible (reflected) outside the function.**

------

##### Objects are Passed by Reference

In JavaScript, ==object references are values==.

Because of this, objects will ==behave like they are passed by **reference==:**

If a function changes an object property, it changes the original value.

**Changes to object properties are visible (reflected) outside the function.**

#### Function `call` and `apply`

**All Functions are Methods**

In JavaScript all functions are object methods.

If a function is not a method of a JavaScript object, it is a function of the global object (see previous chapter).

##### The Difference Between call() and apply()

The `call()` method takes arguments **separately**.

The `apply()` method takes arguments as an **array**.

```js
var person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}
var person1 = {
  firstName:"John",
  lastName: "Doe",
}
person.fullName.apply(person1, ["Oslo", "Norway"]);

person.fullName.call(person1, "Oslo", "Norway");
```

#### Function ==closures==

**Variable Lifetime**

Global variables live as long as your application (your window / your web page) lives.

Local variables have short lives. They are created when the function is invoked, and deleted when the function is finished.

==Variables created **without** the keyword **var**, are always global, even if they are created inside a function.==

##### A Counter Dilemma

```js
// Initiate counter
var counter = 0;

// Function to increment counter
function add() {
  counter += 1;
}

// Call add() 3 times
add();
add();
add();

// The counter should now be 3
```

There is a problem with the solution above: Any code on the page can change the counter, without calling add().

The counter should be local to the `add()` function, to prevent other code from changing it:

##### JavaScript Nested Functions

All functions have access to the global scope.  

In fact, in JavaScript, all functions have access to the scope "above" them.

JavaScript supports nested functions. ==Nested functions have access to the scope "above" them==.

In this example, the inner function `plus()` has access to the `counter` variable in the parent function:

```js
function add() {
  var counter = 0;
  function plus() {counter += 1;}
  plus();    
  return counter; 
}
```

This could have solved the counter dilemma, if we could **reach the `plus()` function from the outside**.

We also need to find a way to **execute `counter = 0` only once**.

**We need a closure.**

##### JavaScript Closures

self-invoking functions

```js
var add = (function () {
  var counter = 0;
  return function () {counter += 1; return counter}
})();

add();
add();
add();

// the counter is now 3
```

**Explain**

The variable `add` is assigned the return value of a ==self-invoking function==.

==The self-invoking function only runs once==. It sets the counter to zero (0), and returns a function expression.

This way add becomes a function. The "wonderful" part is that it can access the counter in the parent scope.

This is called a JavaScript **closure.** It makes it possible for a function to have "**private**" variables.

The counter is protected by the scope of the anonymous function, and can only be changed using the add function.

==A closure is a function having access to the parent scope, even after the parent function has closed.==

### object

In JavaScript, almost "everything" is an object.

- Booleans can be objects (if defined with the `new` keyword)
- Numbers can be objects (if defined with the `new` keyword)
- Strings can be objects (if defined with the `new` keyword)
- Dates are always objects
- Maths are always objects
- Regular expressions are always objects
- Arrays are always objects
- Functions are always objects
- Objects are always objects

All JavaScript values, except primitives (string, number, boolean, undefined), are objects.

#### Object Definition

```js
var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
```

**Accessing Object Properties**

```js
person.lastName;
person["lastName"];

person.fullName();		// return "John Doe"
person.fullName;		// return function definition
```

**JavaScript Objects are Mutable**

Objects are mutable: They are ==addressed by reference, not by value==.

If person is an object, the following statement will not create a copy of person:

```js
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"}

var x = person;
x.age = 10;           // This will change both x.age and person.age
```

The object x is **not a copy** of person. It **is** person. Both x and person are the same object.

#### Object Properties

```js
objectName.property         // person.age
or

objectName["property"]      // person["age"]
or

objectName[expression]      // x = "age"; person[x]
```

##### for ... in loop

The JavaScript `for...in` statement loops through the properties of an object.

```js
var person = {fname:"John", lname:"Doe", age:25}; 

for (x in person) {
  txt += person[x];
}
```

##### Adding New Properties

You can add new properties to an existing object by simply giving it a value.

Assume that the person object already exists - you can then give it new properties.

```js
person.sex = 'male';
```

##### ==Delete== Properties

```js
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
delete person.age;   // or delete person["age"]; 
```

The `delete` keyword deletes both the value of the property and the property itself.

After deletion, the property cannot be used before it is added back again.

The `delete` operator is ==designed to be used on object properties. It has no effect on variables or functions.==

The `delete` operator should not be used on predefined JavaScript object properties. It can crash your application.

##### Property Attributes

All properties have a name. In addition they also have a value.

The ==value== is one of the property's attributes.

Other attributes are: ==enumerable==, ==configurable==, and ==writable==.

These attributes define how the property can be accessed (is it readable?, is it writable?)

In JavaScript, all attributes can be read, but only the value attribute can be changed (and only if the property is writable).

( ECMAScript 5 has methods for both getting and setting all property attributes)

##### Prototype Properties

JavaScript objects inherit the properties of their prototype.

The `delete` keyword does not delete ==inherited properties==, but if you delete a prototype property, it will affect all objects inherited from the prototype.

#### Object Methods

##### Adding a Method to an Object

```js
person.name = function () {
  return this.firstName + " " + this.lastName;
};
```

#### Object Accessors

**JavaScript Accessors (Getters and Setters)**

ECMAScript 5 (2009) introduced Getter and Setters.

Getters and setters allow you to define Object Accessors (Computed Properties).

##### Getter and Setters, key word get and set

```js
// Create an object:
var person = {
  firstName: "John",
  lastName : "Doe",
  language : "en",
  get lang() {
    return this.language;
  }
  set lang(lang) {
    this.language = lang;
  }
};

// Set an object property using a setter:
person.lang = "en";
// Display data from the object using a getter:
document.getElementById("demo").innerHTML = person.lang;
```

**JavaScript Function or Getter?**

What is the differences between these two examples?

- access fullName ==as a function==: person.fullName().

```js
var person = {
  firstName: "John",
  lastName : "Doe",
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};

// Display data from the object using a method:
document.getElementById("demo").innerHTML = person.fullName();
```

- access fullName ==as a property==: person.fullName

```js
var person = {
  firstName: "John",
  lastName : "Doe",
  get fullName() {
    return this.firstName + " " + this.lastName;
  }
};

// Display data from the object using a getter:
document.getElementById("demo").innerHTML = person.fullName;
```

**Why Using Getters and Setters?**

- It gives simpler syntax
- It allows equal syntax for properties and methods

**A Counter example**

```js
var obj = {
  counter : 0,
  get reset() {
    this.counter = 0;
  },
  get increment() {
    this.counter++;
  },
  get decrement() {
    this.counter--;
  },
  set add(value) {
    this.counter += value;
  },
  set subtract(value) {
    this.counter -= value;
  }
};

// Play with the counter:
obj.reset;
obj.add = 5;
obj.subtract = 1;
obj.increment;
obj.decrement;
```

The `Object.defineProperty()`

```js
// Define object
var obj = {counter : 0};

// Define setters
Object.defineProperty(obj, "reset", {
  get : function () {this.counter = 0;}
});
Object.defineProperty(obj, "increment", {
  get : function () {this.counter++;}
});
Object.defineProperty(obj, "decrement", {
  get : function () {this.counter--;}
});
Object.defineProperty(obj, "add", {
  set : function (value) {this.counter += value;}
});
Object.defineProperty(obj, "subtract", {
  set : function (value) {this.counter -= value;}
});

// Play with the counter:
obj.reset;
obj.add = 5;
obj.subtract = 1;
obj.increment;
obj.decrement;
```

#### Object Constructor

```js
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
var john = new Person("John", "Doe", 50, "blue");
var sally = new Person("Sally", "Rally", 48, "green");
```

**Adding a Property to a Constructor**

**Incorrect**

```js
Person.nationality = "English";
var john = new Person("John", "Doe", 50, "blue");
console.log(john.nationaliy);		// return undefined
```

**correct**

To add a new property to a constructor, you must add it to the constructor function:

```js
function Person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
  this.nationality = "English";
}
```



#### Object Prototypes

==All JavaScript objects inherit properties and methods from a prototype.==

**Prototype Inheritance**

All JavaScript objects inherit properties and methods from a prototype:

- `Date` objects inherit from `Date.prototype`
- `Array` objects inherit from `Array.prototype`
- `Person` objects inherit from `Person.prototype`

The `Object.prototype` is on the top of the prototype inheritance chain:

`Date` objects, `Array` objects, and `Person` objects inherit from `Object.prototype`.

##### Adding Properties and Methods to Objects

Sometimes you want to add new properties (or methods) to all existing objects of a given type.

Sometimes you want to add new properties (or methods) to an object constructor.

```js
function Person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
}

Person.prototype.nationality = "English";
Person.prototype.name = function() {
  return this.firstName + " " + this.lastName;
};
```

<span style="color: red">Only modify your **own** prototypes. Never modify the prototypes of standard JavaScript objects.</span>

##### JavaScript ES5 Object Methods

```js
// Adding or changing an object property
Object.defineProperty(object, property, descriptor)

// Adding or changing many object properties
Object.defineProperties(object, descriptors)

// Accessing Properties
Object.getOwnPropertyDescriptor(object, property)

// Returns all properties as an array
Object.getOwnPropertyNames(object)

// Returns enumerable properties as an array
Object.keys(object)

// Accessing the prototype
Object.getPrototypeOf(object)

// Prevents adding properties to an object
Object.preventExtensions(object)
// Returns true if properties can be added to an object
Object.isExtensible(object)

// Prevents changes of object properties (not values)
Object.seal(object)
// Returns true if object is sealed
Object.isSealed(object)

// Prevents any changes to an object
Object.freeze(object)
// Returns true if object is frozen
Object.isFrozen(object)
```

```js
var person = {
  firstName: "John",
  lastName : "Doe",
  language : "EN"
};

// Add a property
Object.defineProperty(person, "year", {value:"2008"});
```



#### Array objects

==Arrays are a special kind of objects, with numbered indexes. objects use named indexes.==

##### basic

**basic manipulations**

```js
var fruits = ["Banana", "Orange", "Apple", "Mango"];

fruits.forEach(function (value) {
    console.log(value);
});

for (let i = 0; i <fruits.length ; i++) {
    console.log(fruits[i])
}

while(fruits.length > 0){
    console.log(fruits.pop());
}

// add and del
fruits.push("Pineapple");
fruits.pop();
```

**never use `new`**

```js
var points = new Array(40, 100, 1, 5, 25, 10); // Bad
var points = [40, 100, 1, 5, 25, 10];          // Good
```

**Recognize**

```js
Array.isArray(fruits);
// or
fruits.constructor.toString().indexOf('Array') > -1;
// or
fruits instanceof Array;
```

**more operations**

`push()`,`pop()`,`shift()`,`unshift()`,`delete`, `splice()`, `concat()`,`slice()`

```js
var fruits = ["Banana", "Orange", "Apple", "Mango"];
```



==slice() create new array objects==

**undefined holes**

```js
fruits[fruits.length + 1];		// leave fruits[fruits.length] undefined
delete fruits[0];				// leave fruits[0] undefined
```

##### sort

**for string array** 

```js
fruits.sort()		// alphabaticaly
fruits.reverse()	//
```

**for number array** ==Compare function==

```js
var points = [40, 100, 1, 5, 25, 10];
points.sort();		// return alpha order, [1, 10, 100, 25, 40, 5]

points.sort(function(a, b){return a-b;});	// numberic, [1, 5, 10, 25, 40, 100]
```

**for object array**

```js
var cars = [
  {type:"Volvo", year:2016},
  {type:"Saab", year:2001},
  {type:"BMW", year:2010}
];
// compare the car's year
cars.sort(function(a, b){return a.year - b.year});

// compare the car's type
cars.sort(function(a, b){
  var x = a.type.toLowerCase();
  var y = b.type.toLowerCase();
  if (x < y) {return -1;}
  if (x > y) {return 1;}
  return 0;
});
```

**Using Math.max() on an Array**

`Math.max.apply(null, [1, 2, 3])` is equivalent to `Math.max(1, 2, 3)`.

##### Iteration

**`Array.forEach()`**

The `forEach()` method calls a function (a ==callback function==) once for each array element.

```js
var txt = "";
var numbers = [45, 4, 9, 16, 25];
numbers.forEach(myFunction);

// When a callback function uses only the value parameter, the index and array parameters can be omitted
function myFunction(value, index, array) {
  txt = txt + value + "<br>"; 
}
```

**`Array.map()`**

The `map()` method ==creates a new array== by performing a function on each array element.
The `map()` method does not execute the function for array elements ==without values==.

```js
var numbers1 = [45, 4, 9, 16, 25];
var numbers2 = numbers1.map(function (value) { 
    return value * 2;
});
```

#### Date

**JavaScript stores dates as number of milliseconds since January 01, 1970, 00:00:00 UTC (Universal Time Coordinated).**





#### RegExp



## datatype & Wrapper

### JS Types

In JavaScript there are 5 different data types that can contain values:

- `string`
- `number`
- `boolean`
- `object`
- `function`

There are 3 types of objects:

- `Object`
- `Date`
- `Array`
- `RegExp`

And 2 data types that cannot contain values:

- `null`
- `undefined`

```js
typeof "John"                 // Returns "string" 
typeof 3.14                   // Returns "number"
typeof NaN                    // Returns "number"
typeof false                  // Returns "boolean"
typeof [1,2,3,4]              // Returns "object"
typeof {name:'John', age:34}  // Returns "object"
typeof new Date()             // Returns "object"
typeof function () {}         // Returns "function"
typeof myCar                  // Returns "undefined" *
typeof null                   // Returns "object"
typeof /()/                   // Returns "object"
```

**The constructor Property**

The `constructor` property returns the constructor function for all JavaScript variables.

```js
"John".constructor                // Returns function String()  {[native code]}
(3.14).constructor                // Returns function Number()  {[native code]}
false.constructor                 // Returns function Boolean() {[native code]}
[1,2,3,4].constructor             // Returns function Array()   {[native code]}
{name:'John',age:34}.constructor  // Returns function Object()  {[native code]}
new Date().constructor            // Returns function Date()    {[native code]}
function () {}.constructor        // Returns function Function(){[native code]}
/()/.constructor        		  // Returns function RegExp()  {[native code]}
```

[@see also: Beware of Automatic Type Conversions](#Beware of Automatic Type Conversions)

# JS Events

```html
<button onclick="document.getElementById('demo').innerHTML = Date()">The time is?</button>
```

**Common html events**

| Event       |                    Description                     |
| :---------- | :------------------------------------------------: |
| onchange    |          An HTML element has been changed          |
| onclick     |          The user clicks an HTML element           |
| onmouseover |   The user moves the mouse over an HTML element    |
| onmouseout  | The user moves the mouse away from an HTML element |
| onkeydown   |           The user pushes a keyboard key           |
| onload      |     The browser has finished loading the page      |

# Keyword ==this==

## What is **this**?

The JavaScript `this` keyword refers to ==the object it belongs to==.

It has different values depending on where it is used:

- In a method, `this` refers to the **owner object**.
- Alone, `this` refers to the **global object**.
- In a function, `this` refers to the **global object**.
- In a function, in strict mode, `this` is `undefined`.
- In an event, `this` refers to the **element** that received the event.
- Methods like `call()`, and `apply()` can refer `this` to **any object**.
- In HTML event handlers, `this` refers to the HTML element that received the event

# JS RegExp

**definition**: /*pattern*/*modifiers*;

```js
var reg = /(\w+)/ig
```



```js
var obj = /e/ig.exec("The best things in life are free!");

// ["e", index: 2, input: "The best things in life are free!", groups: undefined]
obj.valueof();
```



# JS Scope

> ES2015 introduced two important new JavaScript keywords: ***`let`*** and ***`const`***.
>
> These two keywords provide **Block Scope** variables (and constants) in JavaScript.
>
> Before ES2015, JavaScript had only two types of scope: **Global Scope** and **Function Scope**. 

## Global Scope

> Variables declared **Globally** (==outside any function==) have **Global Scope**.

```js
var carName = "Volvo";

// code here can use carName

function myFunction() {
  // code here can also use carName 
}
```

## Function Scope

> Variables declared **Locally** (==inside a function==) have **Function Scope**.

```js
// code here can NOT use carName

function myFunction() {
  var carName = "Volvo";
  // code here CAN use carName
}

// code here can NOT use carName
```

## Block Scope

> Variables declared with the `var` keyword can not have **Block Scope**.
>
> Variables declared inside a block **{}** can be accessed from outside the block.

```js
{ 
  var x = 2; 
}
// x CAN be used here
```

> Before ES2015 JavaScript did not have **Block Scope**.
>
> Variables declared with the `let` keyword can have Block Scope.
>
> Variables declared inside a block **{}** can not be accessed from outside the block:

```js
{ 
  let x = 2;
}
// x can NOT be used here
```

### Redeclaring Variables

***Problem***

```js
var x = 10;
// Here x is 10
{ 
  var x = 2;
  // Here x is 2
}
// Here x is 2
```

Redeclaring a variable using the `let` keyword can solve this problem.

Redeclaring a variable inside a block will not redeclare the variable outside the block:

```js
var x = 10;
// Here x is 10
{ 
  let x = 2;
  // Here x is 2
}
// Here x is 10
```

### For Loop

***Problem***

```js
var i = 5;
for (var i = 0; i < 10; i++) {
  // some statements
}
// Here i is 10
```

***Solution***

```js
let i = 5;
for (let i = 0; i < 10; i++) {
  // some statements
}
// Here i is 5
```

### keyword *`const`*

1. `const` is similar to `let` when it comes to **Block Scope**

    ```js
    var x = 10;
    // Here x is 10
    { 
      const x = 2;
      // Here x is 2
    }
    // Here x is 10
    ```

2. `const` is similar to java's `final` when it comes to constant, but `const` object can't be reassigned.

```js
// incorrect, get a error
const PI;
PI = 3.14159265359;

// correct
const PI = 3.14159265359;
```

**Not real constants**

-  **Primitive Values**

> If we assign a primitive value to a constant, we cannot change the primitive value: 

```js
const PI = 3.141592653589793;
PI = 3.14;      // This will give an error
PI = PI + 10;   // This will also give an error
```

-  **Constant Objects can Change**

> You can change the properties of a constant object

```js
// You can create a const object:
const car = {type:"Fiat", model:"500", color:"white"};

// You can change a property:
car.color = "red";

// You can add a property:
car.owner = "Johnson";
```

> **But you can NOT reassign a constant object**

```js
const car = {type:"Fiat", model:"500", color:"white"};
car = {type:"Volvo", model:"EX60", color:"red"};    // ERROR
```

# JavaScript Hoisting

Hoisting is JavaScript's default behavior of moving ==declarations== to the top.

JavaScript ==Declarations are Hoisted==, JavaScript ==Initializations are Not Hoisted==

> Variables and constants declared with `let` or `const` are not hoisted!

```js
var x = 5;  // Initialize x
console.log("x is " + x + " and y is " + y);  // Display x and y
var y = 7;  // Initialize y
```

equal to

```js
var x, y;
x = 5;
console.log("x is " + x + " and y is " + y);  // Display x and y
y = 7;
```

[@more: 理解 JavaScript 的定义域和定义域提升](#理解 JavaScript 的定义域和定义域提升)

# Strict mode

## The "use strict" Directive

The `"use strict"` directive was new in ECMAScript version 5.

It is not a statement, but a literal expression, ignored by earlier versions of JavaScript.

The purpose of `"use strict"` is to indicate that the code should be executed in "strict mode".

With strict mode, you can not, for example, use undeclared variables.

## Declaring Strict Mode

Declared at the ==beginning of a script==, it has global scope (all code in the script will execute in strict mode)

```js
"use strict";
x = 3.14;       // This will cause an error because x is not declared
```

Declared ==inside a function==, it has local scope (only the code inside the function is in strict mode)

```js
x = 3.14;       // This will not cause an error. 
myFunction();

function myFunction() {
  "use strict";
  y = 3.14;   // This will cause an error
}
```



# JS Style Guide

## Code Indentation

Always use 2 spaces for indentation of code blocks:

```js
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
```

<span style="color: red">Do not use tabs (tabulators) for indentation. Different editors interpret tabs differently.</span>

## Statement Rules

General rules for ==simple statements==:

- Always end a simple statement with a semicolon.

```js
var values = ["Volvo", "Saab", "Fiat"];

var person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};
```

General rules for ==complex (compound) statements==: function, loop, conditional

- Put the opening bracket at the end of the first line.
- Use one space before the opening bracket.
- Put the closing bracket on a new line, without leading spaces.
- ==Do not end a complex statement with a semicolon==.

**function**

```js
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
```

**loops**

```js
for (i = 0; i < 5; i++) {
  x += i;
}
```

**conditionals**

```js
if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}
```

[@more: 分号](#分号)

## Naming Conventions

Always use the same naming convention for all your code. For example:

- Variable and function names written as **camelCase**
- Global variables written in **UPPERCASE** (We don't, but it's quite common)
- Constants (like PI) written in **UPPERCASE**

Should you use **hyp-hens**, **camelCase**, or **under_scores** in variable names?

This is a question programmers often discuss. The answer depends on who you ask:

**Hyphens in HTML and CSS:**

HTML5 attributes can start with data- (data-quantity, data-price).

CSS uses hyphens in property-names (font-size).

==Hyphens can be mistaken as subtraction attempts. Hyphens are not allowed in JavaScript names.==

**Underscores:**

Many programmers prefer to use underscores (date_of_birth), especially in SQL databases.

Underscores are often used in PHP documentation.

**PascalCase:** the first word is Uppercase, like `GetSize()`

PascalCase is often preferred by C programmers.

**camelCase:**

camelCase is used by JavaScript itself, by jQuery, and other JavaScript libraries.

Do not start names with a $ sign. It will put you in conflict with many JavaScript library names.

# JavaScript Best Practices

Avoid global variables, avoid `new`, avoid `==`, avoid `eval()`

## Avoid Global Variables

Minimize the use of global variables.

This includes all data types, objects, and functions.

==Global variables and functions can be overwritten by other scripts.==

Use local variables instead, and learn how to use [closures](https://www.w3schools.com/js/js_function_closures.asp).

## Declarations on Top

It is a good coding practice to put all declarations at the top of each script or function.

This will:

- Give cleaner code
- Provide a single place to look for local variables
- Make it easier to avoid unwanted (implied) global variables
- Reduce the possibility of unwanted re-declarations

## Initialize Variables

It is a good coding practice to initialize variables when you declare them.

This will:

- Give cleaner code
- Provide a single place to initialize variables
- Avoid undefined values

```js
// Declare and initiate at the beginning
var firstName = "",
lastName = "",
price = 0,
discount = 0,
fullPrice = 0,
myArray = [],
myObject = {};
```

## Never Declare Number, String, or Boolean Objects

==Always treat numbers, strings, or booleans as primitive values==. Not as objects.

Declaring these types as objects, slows down execution speed, and produces nasty side effects:

```javascript
var x = "John";             
var y = new String("John");
(x === y) // is false because x is a string and y is an object.
x == y	// true, y auto convert to string
```

**worse**

```javascript
var x = new String("John");             
var y = new String("John");
(x == y) // is false because you cannot compare objects.
```

## Don't Use new Object()

- Use `{}` instead of `new Object()`
- Use `""` instead of `new String()`
- Use `0` instead of `new Number()`
- Use `false` instead of `new Boolean()`
- Use `[]` instead of `new Array()`
- Use `/()/` instead of `new RegExp()`
- Use `function (){}` instead of `new Function()`

```javascript
var x1 = {};           // new object
var x2 = "";           // new primitive string
var x3 = 0;            // new primitive number
var x4 = false;        // new primitive boolean
var x5 = [];           // new array object
var x6 = /()/;         // new regexp object
var x7 = function(){}; // new function object
```

------

## Beware of Automatic Type Conversions

Beware that numbers can accidentally be converted to strings or `NaN` (Not a Number).

```js
var x = 5 + 7;       // x.valueOf() is 12,  typeof x is a number
var x = 5 + "7";     // x.valueOf() is 57,  typeof x is a string
var x = "5" + 7;     // x.valueOf() is 57,  typeof x is a string
var x = 5 - 7;       // x.valueOf() is -2,  typeof x is a number
var x = 5 - "7";     // x.valueOf() is -2,  typeof x is a number
var x = "5" - 7;     // x.valueOf() is -2,  typeof x is a number
var x = "5" + "7";	 // x.valueOf() is 57,  typeof x is a string
var x = '5' - '7';	 // x.valueOf() is -2,  typeof x is a number

var x = 10 / 0;		 // x.valueOf() is Infinity,  typeof x is a number, no error
var x = 5 - "x";     // x.valueOf() is NaN, typeof x is a number
```

==Subtracting a string from a string==, does not generate an error but returns `NaN` (Not a Number)

```js
"Hello" - "Dolly"    // returns NaN
```

## Use === Comparison

The `==` comparison operator ==always converts (to matching types) before comparison==.

The `===` operator forces comparison of values and type:

如果你想了解更多关于强制类型转换的信息，你可以读一读 [Dmitry Soshnikov 的这篇文章](http://dmitrysoshnikov.com/notes/note-2-ecmascript-equality-operators/)。

在只使用 `==` 的情况下，JavaScript 所带来的强制类型转换使得判断结果跟踪变得复杂，下面的例子可以看出这样的结果有多怪了：

```js
0 == "";        // true
1 == "1";       // true
1 == true;      // true

0 === "";       // false
1 === "1";      // false
1 === true;     // false
```



## Use Parameter Defaults

If a function is called with a missing argument, ==the value of the missing argument is set to undefined==.

Undefined values can break your code. It is a good habit to assign default values to arguments.

```js
function myFunction(x, y) {
  if (y === undefined) {
    y = 0;
  }
}
// or
function myFunction(x, y) {
  var y = y || 0;
}
```

[ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp) allows default parameters in the function call

```js
function (a=1, b=1) { // function code }
```

[@see also: 变量赋值时的逻辑操作](#变量赋值时的逻辑操作)

## Avoid Using eval()

The `eval()` function is used to run text as code. In almost all cases, it should not be necessary to use it.

Because it allows arbitrary code to be run, it also represents a security problem.

# JS Mistakes

## `switch`

It is a common mistake to forget that `switch` statements use strict comparison:

This `case switch` will display an alert:

```js
var x = 10;
switch(x) {
  case 10: alert("Hello");
}
```

This `case switch` will not display an alert:

```js
var x = 10;
switch(x) {
  case "10": alert("Hello");
}
```

## Misunderstanding Floats

==All numbers in JavaScript are stored as 64-bits **Floating point numbers** (Floats)==.

All programming languages, including JavaScript, have difficulties with precise floating point values:

```js
var x = 0.1;
var y = 0.2;
var z = x + y            // the result in z will not be 0.3
```

To solve the problem above, it helps to multiply and divide

```js
var z = (x * 10 + y * 10) / 10;       // z will be 0.3

// or
z.toFixed(1);
```

## Breaking lines

**breaking string**

```js
var str = "Hello \
	World";
```

A safer way to break up a string literal, is to use string addition:

```js
var str = "Hello" +
    "World";
```



<span style="background-color: red">never break return statement</span>

```js
return
a + b;		//return undefined
```

```js
return a + b;	// correct
```

==use semicolon==

# ECMAScipte 5

ECMAScript 5 is also known as ES5 and ECMAScript 2009

This chapter introduces some of the most important features of ES5.

**ECMAScript 5 Features**

- The `"use strict"` Directive
- `String.trim()`
- `Array.isArray()`
- `Array.forEach()`
- `Array.map()`
- `Array.filter()`
- `Array.reduce()`
- `Array.reduceRight()`
- `Array.every()`
- `Array.some()`
- `Array.indexOf()`
- `Array.lastIndexOf()`
- `JSON.parse()`
- `JSON.stringify()`
- `Date.now()`
- Property Getters and Setters
- New Object Property Methods

# ECMAScript 6

ECMAScript 6 is also known as ES6 and ECMAScript 2015.

Some people calls it JavaScript 6.

This chapter will introduce some of the new features in ES6.

- JavaScript `let`
- JavaScript `const`
- Exponentiation (`**`)
- Default parameter values
- `Array.find()`
- `Array.findIndex()`

# Front Programming Guild line

come from <https://www.w3cschool.cn/bdl2e3/arcv12j4.html>,

date: Wed Jan 16 2019 10:42:42

## Common

## html

## JavaScript 

### 全局命名空间污染与 IIFE

总是将代码包裹成一个 IIFE(Immediately-Invoked Function Expression)，用以创建独立隔绝的定义域。这一举措可防止全局命名空间被污染。

IIFE 还可确保你的代码不会轻易被其它全局命名空间里的代码所修改（i.e. 第三方库，window 引用，被覆盖的未定义的关键字等等）。

**不推荐**

```js
var x = 10,
    y = 100;
 
// Declaring variables in the global scope is resulting in global scope pollution. All variables declared like this
// will be stored in the window object. This is very unclean and needs to be avoided.
console.log(window.x + ' ' + window.y);
```

**推荐**

```js
// We declare a IIFE and pass parameters into the function that we will use from the global space
(function(log, w){
  'use strict';
 
  var x = 10,
      y = 100;
 
  // Will output 'true true'
  log((w.x === undefined) + ' ' + (w.y === undefined));
 
}(window.console.log, window));
```

### IIFE（立即执行的函数表达式）

无论何时，想要创建一个新的封闭的定义域，那就用 IIFE。它不仅避免了干扰，也使得内存在执行完后立即释放。

所有脚本文件建议都从 IIFE 开始。

立即执行的函数表达式的执行括号应该写在外包括号内。虽然写在内还是写在外都是有效的，但写在内使得整个表达式看起来更像一个整体，因此推荐这么做。

**不推荐**

```js
(function(){})();
```

**推荐**

```js
(function(){}());
```

so，用下列写法来格式化你的 IIFE 代码：

```js
(function(){
  'use strict';
 
  // Code goes here
 
}());
```

如果你想引用全局变量或者是外层 IIFE 的变量，可以通过下列方式传参：

```js
(function($, w, d){
  'use strict';
 
  $(function() {
    w.alert(d.querySelectorAll('div').length);
  });
}(jQuery, window, document));
```

### 严格模式

ECMAScript 5 严格模式可在==整个脚本==或==独个方法内==被激活。它对应不同的 javascript 语境会做更加严格的错误检查。严格模式也确保了 javascript 代码更加的健壮，运行的也更加快速。

严格模式会阻止使用在未来很可能被引入的预留关键字。

你应该在你的脚本中启用严格模式，最好是在独立的 IIFE 中应用它。避免在你的脚本第一行使用它而导致你的所有脚本都启动了严格模式，这有可能会引发一些第三方类库的问题。

**不推荐**

```js
// Script starts here
'use strict';
 
(function(){
 
  // Your code starts here
 
}());
```

**推荐**

```js
(function(){
  'use strict';
 
  // Your code starts here
 
}());
```

### 理解 JavaScript 的定义域和定义域提升

在 JavaScript 中==变量和方法定义==会自动提升到执行之前。JavaScript 只有 function 级的定义域，而无其他很多编程语言中的块定义域，所以使得你在某一 function 内的某语句和循环体中定义了一个变量，此变量可作用于整个 function 内，而不仅仅是在此语句或循环体中，因为它们的声明被 JavaScript 自动提升了。

我们通过例子来看清楚这到底是怎么一回事：

**原 function**

```js
(function(log){
  'use strict';
 
  var a = 10;
 
  for(var i = 0; i < a; i++) {
    var b = i * i;
    log(b);
  }
 
  if(a === 10) {
    var f = function() {
      log(a);
    };
    f();
  }
 
  function x() {
    log('Mr. X!');
  }
  x();
 
}(window.console.log));
```

**被 JS 提升过后**

```js
(function(log){
  'use strict';
  // All variables used in the closure will be hoisted to the top of the function
  var a,
      i,
      b,
      f;
  // All functions in the closure will be hoisted to the top
  function x() {
    log('Mr. X!');
  }
 
  a = 10;
 
  for(i = 0; i < a; i++) {
    b = i * i;
    log(b);
  }
 
  if(a === 10) {
    // Function assignments will only result in hoisted variables but the function body will not be hoisted
    // Only by using a real function declaration the whole function will be hoisted with its body
    f = function() {
      log(a);
    };
    f();
  }
 
  x();
 
}(window.console.log));
```

根据以上提升过程，你是否可理解以下代码？

**有效代码**

```js
(function(log){
  'use strict';
 
  var a = 10;
 
  i = 5;
 
  x();
 
  for(var i; i < a; i++) {
    log(b);
    var b = i * i;
  }
 
  if(a === 10) {
    f = function() {
      log(a);
    };
    f();
 
    var f;
  }
 
  function x() {
    log('Mr. X!');
  }
 
}(window.console.log));
```

正如你所看到的这段令人充满困惑与误解的代码导致了出人意料的结果。只有良好的声明习惯，也就是下一章节我们要提到的声明规则，才能尽可能的避免这类错误风险。

------

**提升声明**

为避免上一章节所述的变量和方法定义被自动提升造成误解，把风险降到最低，我们应该手动地显示地去声明变量与方法。也就是说，所有的变量以及方法，应当定义在 function 内的首行。

只用一个 `var` 关键字声明，多个变量用逗号隔开。

**不推荐**

```js
(function(log){
  'use strict';
 
  var a = 10;
  var b = 10;
 
  for(var i = 0; i < 10; i++) {
    var c = a * b * i;
  }
 
  function f() {
 
  }
 
  var d = 100;
  var x = function() {
    return d * d;
  };
  log(x());
 
}(window.console.log));
```

**推荐**

```js
(function(log){
  'use strict';
 
  var a = 10,
      b = 10,
      i,
      c,
      d,
      x;
 
  function f() {
 
  }
 
  for(i = 0; i < 10; i++) {
    c = a * b * i;
  }
 
  d = 100;
  x = function() {
    return d * d;
  };
  log(x());
 
}(window.console.log));
```



### ==明智地使用真假判断==

当我们在一个 if 条件语句中使用变量或表达式时，会做真假判断。`if(a == true)` 是不同于 `if(a)` 的。后者的判断比较特殊，我们称其为真假判断。这种判断会通过特殊的操作将其转换为 true 或 false，下列表达式统统返回 false：`false`, `0`, `undefined`, `null`, `NaN`, `''`（空字符串）.

这种真假判断在我们只求结果而不关心过程的情况下，非常的有帮助。

以下示例展示了真假判断是如何工作的：

```js
(function(log){
  'use strict';
 
  function logTruthyFalsy(expr) {
    if(expr) {
      log('truthy');
    } else {
      log('falsy');
    }
  }
 
  logTruthyFalsy(true); // truthy
  logTruthyFalsy(1); // truthy
  logTruthyFalsy({}); // truthy
  logTruthyFalsy([]); // truthy
  logTruthyFalsy('0'); // truthy
 
  logTruthyFalsy(false); // falsy
  logTruthyFalsy(0); // falsy
  logTruthyFalsy(undefined); // falsy
  logTruthyFalsy(null); // falsy
  logTruthyFalsy(NaN); // falsy
  logTruthyFalsy(''); // falsy
 
}(window.console.log));
```

### 变量赋值时的逻辑操作

逻辑操作符 `||` 和 `&&` 也可被用来返回布尔值。如果==操作对象为**非布尔对象**，那每个表达式将会被自左向右地做真假判断==。基于此操作，最终总有一个表达式被返回回来。这在变量赋值时，是可以用来简化你的代码的。

**不推荐**

```js
if(!x) {
  if(!y) {
    x = 1;
  } else {
    x = y;
  }
}
```

**推荐**

```js
x = x || y || 1;
```

这一小技巧经常用来==给方法设定默认的参数==。

```js
(function(log){
  'use strict';
 
  function multiply(a, b) {
    a = a || 1;
    b = b || 1;
 
    log('Result ' + a * b);
  }
 
  multiply(); // Result 1
  multiply(10); // Result 10
  multiply(3, NaN); // Result 3
  multiply(9, 5); // Result 45
 
}(window.console.log));
```

### 分号

总是使用分号，因为隐式的代码嵌套会引发难以察觉的问题。当然我们更要从根本上来杜绝这些问题[^1]。以下几个示例展示了缺少分号的危害：

```js
// 1.
MyClass.prototype.myMethod = function() {
  return 42;
}  // No semicolon here.
 
(function() {
  // Some initialization code wrapped in a function to create a scope for locals.
})();
 
 
var x = {
  'i': 1,
  'j': 2
}  // No semicolon here.
 
// 2.  Trying to do one thing on Internet Explorer and another on Firefox.
// I know you'd never write code like this, but throw me a bone.
[ffVersion, ieVersion][isIE]();
 
 
var THINGS_TO_EAT = [apples, oysters, sprayOnCheese]  // No semicolon here.
 
// 3. conditional execution a la bash
-1 == resultOfOperation() || die();
```

**So what happens?**

1. JavaScript 错误 —— 首先返回 42 的那个 function 被第二个 function 当中参数传入调用，接着数字 42 也被“调用”而导致出错。
2. 八成你会得到 ‘no such property in undefined’ 的错误提示，因为在真实环境中的调用是这个样子：`x[ffVersion, ieVersion][isIE]()`.
3. `die` 总是被调用。因为数组减 1 的结果是 `NaN`，它不等于任何东西（无论 `resultOfOperation` 是否返回 `NaN`）。所以最终的结果是 `die()`执行完所获得值将赋给 `THINGS_TO_EAT`.

**Why?**

JavaScript 中语句要以分号结束，否则它将会继续执行下去，不管换不换行。以上的每一个示例中，函数声明或对象或数组，都变成了在一句语句体内。要知道闭合圆括号并不代表语句结束，JavaScript 不会终结语句，除非它的下一个 token 是一个中缀符[^2] 或者是圆括号操作符。

这真是让人大吃一惊，所以乖乖地给语句末加上分号吧。

==**澄清：分号与函数**==

分号需要用在表达式的结尾，而并非函数声明的结尾。区分它们最好的例子是：

```js
var foo = function() {
  return true;
};  // semicolon here.
 
function foo() {
  return true;
}  // no semicolon here.
```

### 嵌套函数

嵌套函数是非常有用的，比如用在持续创建和隐藏辅助函数的任务中。你可以非常自由随意地使用它们。

### 语句块内的函数声明

切勿在语句块内声明函数，在 ECMAScript 5 的严格模式下，这是不合法的。函数声明应该在定义域的顶层。但在语句块内可将函数申明转化为函数表达式赋值给变量。

**不推荐**

```js
if (x) {
  function foo() {}
}
```

**推荐**

```js
if (x) {
  var foo = function() {};
}
```

### 异常

基本上你无法避免出现异常，特别是在做大型开发时（使用应用开发框架等等）。

在没有自定义异常的情况下，从有返回值的函数中返回错误信息一定非常的棘手，更别提多不优雅了。不好的解决方案包括了传第一个引用类型来接纳错误信息，或总是返回一个对象列表，其中包含着可能的错误对象。以上方式基本上是比较简陋的异常处理方式。适时可做自定义异常处理。

在复杂的环境中，你可以考虑抛出对象而不仅仅是字符串（默认的抛出值）。

```js
if(name === undefined) {
  throw {
    name: 'System Error',
    message: 'A name should always be specified!'
  }
}
```

### 简易的原型继承

如果你想在 JavaScript 中继承你的对象，请遵循一个简易的模式来创建此继承。如果你预计你会遇上复杂对象的继承，那可以考虑采用一个继承库，比如 [Proto.js by Axel Rauschmayer](https://github.com/rauschma/proto-js).

简易继承请用以下方式：

```js
(function(log){
  'use strict';
 
  // Constructor function
  function Apple(name) {
    this.name = name;
  }
  // Defining a method of apple
  Apple.prototype.eat = function() {
    log('Eating ' + this.name);
  };
 
  // Constructor function
  function GrannySmithApple() {
    // Invoking parent constructor
    Apple.prototype.constructor.call(this, 'Granny Smith');
  }
  // Set parent prototype while creating a copy with Object.create
  GrannySmithApple.prototype = Object.create(Apple.prototype);
  // Set constructor to the sub type, otherwise points to Apple
  GrannySmithApple.prototype.constructor = GrannySmithApple;
 
  // Calling a super method
  GrannySmithApple.prototype.eat = function() {
    // Be sure to apply it onto our current object with call(this)
    Apple.prototype.eat.call(this);
 
    log('Poor Grany Smith');
  };
 
  // Instantiation
  var apple = new Apple('Test Apple');
  var grannyApple = new GrannySmithApple();
 
  log(apple.name); // Test Apple
  log(grannyApple.name); // Granny Smith
 
  // Instance checks
  log(apple instanceof Apple); // true
  log(apple instanceof GrannySmithApple); // false
 
  log(grannyApple instanceof Apple); // true
  log(grannyApple instanceof GrannySmithApple); // true
 
  // Calling method that calls super method
  grannyApple.eat(); // Eating Granny Smith\nPoor Grany Smith
 
}(window.console.log));
```



## CSS and Sass(SCSS)



[^1]: 作者指的是采用严格规范的语句写法，从根本上杜绝由分号缺失而引起的代码歧义。
[^2]: 中缀符，指的是像 `x + y` 中的 `+`。