# 课件笔记

<!-- MarkdownTOC -->

- Object Relationships
- Java API
    - String
    - StringBuffer
    - File IO
    - Reflection (Program7)
- Advanced OOP
    - Package
    - Abstract Methods and Classes
    - Interfaces
    - Inner Classes
    - Generics
- Exception Handling
    - Runtime Exceptions
    - try Block
    - finally Block
- Java Native Interface
- Reflection

<!-- /MarkdownTOC -->


## Object Relationships

+ Data Encapsulation: wrapping, data hiding
+ Inheritance: objects of one class acquire the properties of objects of another class
    + idea of reusablity
+ Polymorphism
    + more than one form
+ Dynamic Binding
    + code associated with a given procedure call is not known until the time of the call at runtime. Dynamic binding is associated with polymorphism and inheritance.
+ Data Abstraction
    + representing essential features without including the background details or explanations.
+ Message Communication
    + send/receive information

## Java API

### String

+ Strings are class objects and implemented using two classes, namely String and StringBuffer.

### StringBuffer

While String class creates strings of fixed lengths, StringBuffer class creates strings of flexible length that can be modified in terms of both length and content.

+ setCharAt
+ append
+ insertAt
+ setLength

### File IO

+ Text Streams and Buffers (Program3)
+ Binary Streams and Buffers (Program4)
+ Filters (Program5)
+ Object Files (Program6)

### Reflection (Program7)

+ The reflection API reflects the classes, interfaces, and objects in the current JVM.
+ With the reflection API, you can
    + Determine the class of an object.
    + Class’s modifiers,fields,methods,constructors,and superclasses.
    + Create an instance of a class whose name is not known until runtime.
    + What constants and method declarations belong to an interface.
    + Get and set the value of an object's field, even if the field name is unknown to your program until runtime.
    + Invoke a method on an object, even if the method is not known until runtime.

## Advanced OOP

### Package

The statement, declaring the package should be the first statement in a Java source file.

### Abstract Methods and Classes

+ abstract classes cannot be instantiated
+ abstract method: methodsthatmust be redefined in a subclass, thus making overriding compulsory.
+ Whenaclasscontainsoneormoreabstract methods, it should be declared as abstract

### Interfaces

+ An interface is a class
+ It has collection of method definitions (without implementations) and constant values.

Advantages of Interfaces

+ Useful for capturing similarities between unrelated classes, without forcing a class relationship
+ Declares methods, without implementation that one or more classes are expected to implement

### Inner Classes

+ An inner class can access all the private resources methods,properties of the top-level class.
+ Inner classes can be hidden from other classes in the same package. You don’t have to worry about name conflicts between it and other classes.
+ Inner classes are convenient,when you are writing event-driven programs.
+ An inner class is a short class file, that exists only for a limited purpose.

Scope

+ Rules governing the scope of an inner class match those governing variables.
+ An inner class’s name is not visible outside its scope, except in a fully qualified name.
+ The code for an inner class can use simple names from enclosing scopes, including class and member variables of enclosing classes, as well as local variables of enclosing blocks.
+ You can also define a top-level class as a static member of another top-level class. By nesting, you can organize classes.

### Generics

+ Basic Definition – `Gen<T>` (Program10.java)
+ `Gen<T, V>` (Program11.java)
+ `Gen(T extends V)` (Program12.java)
+ `Gen<?>` in method definition (Program13.java)

## Exception Handling

### Runtime Exceptions

RuntimeException are those exceptions that occur within the Java runtime system. Includes:

+ Arithmetic exceptions (such as division by zero)
+ Pointer exceptions (such as trying to access an
object through a null reference)
+ Indexing exceptions (such as attempting to access an array element through an index that is too large or too small).

### try Block

Exception handling is done by using try - catch – finally blocks.

### finally Block

+ Java’s finally block provides a mechanism that allows method to clean up after itself, regardless of what happens within the try block.
+ The finally block can be used to close files or release other system resources.

## Java Native Interface

+ Java Native Interface (JNI) is a standard programming interface for writing Java native methods and embedding the JVM into native applications.
+ The primary goal is binary compatibility of native method libraries across all Java virtual machine implementations on a given platform.

## Reflection

The reflection API reflects the classes, interfaces, and objects in the current JVM.

    Person p=new Person();

这是什么？当然是实例化一个对象了。可是这种实例化对象的方法存在一个问题，那就是必须要知道类名才可以实例化它的对象，这样我们在应用方面就会受到限制。那么有没有这样一种方式，让我们不知道这个类的类名就可以实例化它的对象呢？Thank Goodness！幸亏我们用的是java，java就提供了这样的机制。

java程序在运行时可以获得任何一个类的字节码信息，包括类的修饰符(public、static等)、基类(超类、父类)、实现的接口、字段和方法等信息。

java程序在运行时可以根据字节码信息来创建该类的实例对象，改变对象的字段内容和调用对象方法。

这样的机制就叫反射技术。可以想象光学中的反射，就像我们照镜子，镜子中又出现一个自己(比喻可能不太恰当，但是足以表达清楚意思了)。反射技术提供了一种通用的动态连接程序组件的方法，不必要把程序所需要的目标类硬编码到源程序中，从而使得我们可以创建灵活的程序。

Java的反射机制是通过反射API来实现的，它允许程序在运行过程中取得任何一个已知名称的类的内部信息。反射API位于java.lang.reflect包中。主要包括以下几类：

+ Constructor类：用来描述一个类的构造方法。
+ Field类：用来描述一个类的成员变量。
+ Method类：用来描述一个类的方法。
+ Modifer类：用来描述类内各元素的修饰符。
+ Array：用来对数组进行操作。

Constructor,Field,Method这三个类都是JVM(虚拟机)在程序运行时创建的，用来表示加载类中相应的成员。这三个类都实现了java.lang.reflect.Member接口，Member接口定义了获取类成员或构造方法等信息的方法。要使用这些反射API，必须先得到要操作的对象或类的Class类的实例。通过调用Class类的newInstance方法(只能调用类的默认构造方法)可以创建类的实例。这样有局限性，我们可以先冲类的Class实例获取类需要的构造方法，然后在利用反射来创建类的一个实例。
