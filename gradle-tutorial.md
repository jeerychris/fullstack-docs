# Gradle vs Maven

**References:**

1. <https://dzone.com/articles/gradle-vs-maven>
2. <https://gradle.org/maven-vs-gradle/>

> The following is a summary of the major differences between Gradle and Apache
> Maven: **flexibility**, **performance**, user **experience**, and **dependency management**.
> It is not meant to be exhaustive, but you can check the Gradle feature list
> and Gradle vs Maven performance comparison to learn more.

**side by side Maven vs Gradle `clean install`**

![gradle-vs-maven.gif](images/gradle-vs-maven.gif)

----

## Flexibility

Both Gradle and Maven provide convention over configuration. However, Maven
provides a very rigid model that makes customization tedious and sometimes
impossible.

## Performance

Improving build time is one of the most direct ways to *ship faster*. Both
Gradle and Maven employ some form of parallel project building and parallel
dependency resolution. The biggest differences are Gradle's mechanisms for
work avoidance and incrementality. The top 3 features that make Gradle much
faster than Maven are:

- [Incrementality](https://blog.gradle.org/introducing-incremental-build-support) 
> Gradle avoids work by tracking input and output of tasks and only running
> what is necessary, and only processing [files that changed](https://blog.gradle.org/incremental-compiler-avoidance) when possible.

- [Build Cache](https://blog.gradle.org/introducing-gradle-build-cache) 
> Reuses the build outputs of any other Gradle build with the same inputs, including between machines.

- [Gradle Daemon](https://docs.gradle.org/current/userguide/gradle_daemon.html) 
> A long-lived process that keeps build information "hot" in memory.

These and more [performance features](https://gradle.org/features/#performance) make Gradle at least twice as fast for nearly every scenario (100x faster for large builds using the build cache) in this [Gradle vs Maven performance comparison](https://gradle.org/gradle-vs-maven-performance/).

![gradle-vs-maven-performance.png](images/gradle-vs-maven-performance.png)

### Incremental Compilation

<https://blog.gradle.org/incremental-compiler-avoidance>

For those who work on a single project with lots of sources:

- changing a single file, in a big monolithic project and recompiling
- changing a single file, in a medium-sized monolithic project and recompiling

For multi-project builds:

- making a change in an **ABI-compatible** way (change the body of a method, for example, but not method signatures) in a subproject, and recompiling
- making a change in an ABI-incompatible way (change a public method signature, for example) in a subproject, and recompiling

***Note:*** Application Binary Interface

#### Compile avoidance

Compile avoidance is different from incremental compilation, which we will cover later. So what does it mean? It’s actually very simple. Imagine that your project `app` depends on project `core`, which itself depends on project `utils`:

In `app`:

```java
public class Main {
   public static void main(String... args) {
        WordCount wc = new WordCount();
        wc.collect(new File(args[0]);
        System.out.println("Word count: " + wc.wordCount());
   }
}
```

In `core`:

```java
public class WordCount {  // WordCount lives in project `core`
   // ...
   void collect(File source) {
       IOUtils.eachLine(source, WordCount::collectLine);
   }
}
```

In `utils`:

```java
public class IOUtils { // IOUtils lives in project `utils`
    void eachLine(File file, Callable<String> action) {
        try {
            try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
                // ...
            }
        } catch (IOException e) {
            // ...
        }
    }
}
```

Then, change the implementation of `IOUtils`. For example, change the body of `eachLine` to introduce the expected charset:

```java
public class IOUtils { // IOUtils lives in project `utils`
    void eachLine(File file, Callable<String> action) {
        try {
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(file), "utf-8") )) {
                // ...
            }
        } catch (IOException e) {
            // ...
        }
    }
}
```

Now rebuild `app`. What happens? Until now, `utils` had to be recompiled, but then it also triggered the recompilation of `core` and eventually `app`, because of the dependency chain. It sounds reasonable at first glance, but is it really?

> What changed in `IOUtils` is purely an internal detail. The implementation of `eachLine` changed, but its public API didn’t. Any class file previously compiled against `IOUtils` is still valid. Gradle is now smart enough to realize that. This means that if you make such a change, Gradle will only recompile `utils`, and nothing else! This is what we call **compilation avoidance**.

And while this example may sound simple, it’s actually a very common pattern: typically, a `core` project is shared by many subprojects, and each subproject has dependencies on different subprojects. A change to `core` would trigger a recompilation of all **projects**. With Gradle 3.4 this will no longer be the case, meaning that it recognizes ABI (*Application Binary Interface*) breaking changes, and will trigger recompilation only in that case.

## Improved incremental compilation

For years, Gradle has supported an experimental incremental compiler for Java. In Gradle 3.4, not only is this compiler stable, but we also have significantly improved both its robustness and performance! Use it now: we’re going to make it the default soon! To enable Java incremental compilation, all you need to do is to set it on the compile options:

```groovy
tasks.withType(JavaCompile) {
   options.incremental = true // one flag, and things will get MUCH faster
}
```

If we add the following class in project `core`:

```java
public class NGrams {  // NGrams lives in project `core`
   // ...
   void collect(String source, int ngramLength) {
       collectInternal(StringUtils.sanitize(source), ngramLength);
   }
   // ...
}
```

and this class in project `utils`:

```java
public class StringUtils {
   static String sanitize(String dirtyString) { ... }
}
```

Imagine that we change the class `StringUtils` and recompile our project. can easily see that we only need to recompile `StringUtils` and `NGrams` but not `WordCount`. `NGrams` is a dependent class of `StringUtils`. `WordCount` doesn’t use `StringUtils`, so why would it need to be recompiled?
> This is what the incremental compiler does: it analyzes the dependencies between **classes**, and only recompiles a class when it has changed, or one of the classes it depends on has changed.

Those of you who have already tried the incremental Java compiler before may have seen that it wasn’t very smart when a changed **class contained a constant**. For example, this class contains a constant:

```java
public class SomeClass {
    public static int MAGIC_NUMBER = 123;
}
```

If this class was changed, then Gradle gave up and recompiled not just all the classes of that project but also all the classes in projects that depend on that project. If you wonder why, you have to understand that the **Java compiler inlines constants** like this. So when **we analyze the result of compilation, and that the bytecode of a class contains the *literal* 123, we have no idea where the literal was defined.** It could be in the class itself, or a constant of any dependency found anywhere on its classpath. In Gradle 3.4, we made that behavior much smarter, and only recompile classes which could *potentially* be affected by the change. In other words, if the class is changed, but the constant is not, we don’t need to recompile. Similarly, if the constant is changed, but that the dependents didn’t have a literal in their bytecode of the old value, we don’t need to recompile them: we would only recompile the classes that have *candidate literals*. This also means that not all constants are born equal: a constant value of `0` is much more likely to trigger a full recompilation when changed, than a constant value `188847774`…

Our incremental compiler is also now backed with in-memory caches that live in the Gradle daemon across builds, and thus make it significantly faster than it used to be: extracting the ABI of a Java class is an expensive operation that used to be cached, but on disk only.

If you combine all those incremental compilation improvements with the *compile avoidance* that we described earlier in this post, Gradle is now really fast when recompiling Java code. Even better, it also works for external dependencies. Imagine that you upgrade from `foo-1.0.0` to `foo-1.0.1`. If the only difference between the two versions of the library is, for example, a bugfix, and that the API hasn’t changed, compile avoidance will kick in and this change in an external dependency will not trigger a recompile of your code. If the new version of the external dependency has a modified public API, Gradle’s incremental compiler will analyze the dependencies of your project on *individual* classes of the external dependency, and only recompile where <kbd>necessary</kbd>.