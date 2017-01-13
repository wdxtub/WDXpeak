# 课堂笔记

<!-- MarkdownTOC -->

- Grade
- 31 Aug. Mon
- 2 Sep. Wed

<!-- /MarkdownTOC -->

## Grade

+ Assignment1 18.5/20
	+ No class descrition on the top of class
	+ No package structure. Give meaningful names to package

## 31 Aug. Mon

> What is Java?

Two parts: Java programming Language & Java Virtual Machine

+ SDK - J2SE
+ J2EE - Application Server
	+ A runtime environment that takes care of system elements allowing developer to focus on coding
	+ High Concurrency
	+ DB connectivity
+ J2ME - Mobile development(Android instead)
+ Secure
	+ Low level security mechanism, Class signing, more difficult to forge access to data structures
+ Robust
	+ Strong typing eg Procedure declarations
	+ Dynamic Checking, Late Binding(solving fragile base class problem)

> Dynamic?

+ JIT loading of classes in runtime
+ Dynamic Bingding

> Distributed?

+ Creating Distributed systems
+ Web Services
+ JVM to JVM interaction or runtime environments

> Java Performance Puzzle

+ Speed of executing Java bytecode
+ Java library implementation
+ Runtime system
+ Opereating system and hardware

> Late binding?

+ Offsets are not calculated until load time (not compile time)
+ Field and method references represented symbolically in the bytecode
+ Less efficient but JIT compilers optimize
+ Leads to robust component model and hence popularity of Beans etc.

> Java Runtime Environment

+ javac - .java file to create .class file
+ java - JRE - .class file and loads
+ Class Loader(Bytecode Verifier, BV)
	+ Local Classes from CLASSPATH
	+ Classes over Internet
	+ BV - checks the integrity of class file is intact
	+ BV - rules of the language are followed
	+ send to `JIT compiler` and `Bytecode Interpreter`
+ JIT compiler
	+ reduce the number of bytecodes
+ Bytecode Interpreter
	+ take each bytecode and convert it to native
	+ native - local machine architecure
+ memory allocation - done with methods
+ deallocation - garbage collection

> Is Java a compiled language or interpreted language?

+ JRE is intergreted.
+ Java Platform (language and JRE) is both compiled and interpreted

> Java Development Environment

+ Java Programs, Ada Programs, Java bytecode assembly Programs -\> Bytecode Compliler(eg javac, jikes, jasmine etc) -\> Class Files
+ Class Files -\> Obfuscator, Bytecode Optimizer(creama, DashO)
+ Class Files -\> Decompiler, Bytecode disassembler(eg javap, mocha) -\> Java Programs

> Java Programming Language

+ Object has
	+ properties - unique for each object(instance variables)
	+ methods - act on properties to enable object behavior (changing values of property)
+ Class - blueprint of an object
+ new - allocates memory for an object based on its class definition

> OOD

+ Object Relationships
	+ How object interact with each other?
+ Object is self-contained independent entity
+ 1.Encapsulation (Information hiding)
+ 2.Containment (An object is contained in another)
+ 3.Association - dependency of one object on another for a singular transaction. (temp) - (perm)
+ 4.Inheritence - properites from parent are passed to child
+ 5.Polymorphism - one word -\> many things

> Basic data types

+ Byte, short, int, long
+ Float, Double (32, 64 bits)
+ char (16 bit Unicode)
+ boolean

string 不可变，改用 stringbuffer - stringbuilder

> Reference Types

+ Class, Interface (For OO programming)
+ Arrays (First class; not pointer to memory like in C/C++)
+ Strings (First class; not null-terminated array of chars)
+ Default values(0 for basic types, null for others)

> Control Structures

+ If-else, switch-case
+ for, while, do-while
+ try-catch-finally, throw
+ break, continue, return

> Classes and Objects

+ Class has fields(data), Methods(code)
+ Objects are instances of class
+ Data
	+ per class data (static fields)
	+ per object data (instance fields)
+ Methods
	+ per class methods (static methods)
	+ per object methods (instance methods)

> Java Virtual Machine

JVM is an execution environment for class files containing methods expressed in the Java bytecode ISA.

+ Bytecode ISA
+ Binary platform-independent classfile
+ Class File Verification

Compiling to Java VM

+ JVM abstract computing machine
+ JVM knows nothing of the Java language
	+ knows just about class file
+ JVM expects type-checking at compile time
+ JVM stack oriented
	+ ops operate on opnds of stack
	+ results push back new opnds to stack

## 2 Sep. Wed

+ Object is created from a class
+ Self contained independent entity
+ Behavior - Properties (that will help manage the behavior)
+ Behavior - Methods that can modify properites for specific behavior outcomes

> Self contained VS independent

注意区别

+ Class - Blueprint(Skeleton) for building objects
+ default constructor - provided by language.
	+ class does not have to have a constructor

具体的类书写格式，piazza 上有，注意参考设计

> Can static method modify instance variables?

Static data or method is loaded at the start of program when class is loaded.

> Can instance methods modify static data

Static data is loaded at start of class - instance method can modify it

static - shared, on copy and loaded first

> Object Relationships

+ Association - Passing an object by reference.
	+ Primitives are passed by value
	+ Objects are passed by reference
+ Containment - Creating an instance of once object inside another.
+ Inheritance - Passing functionality from parent to child class
+ Polymorphism - One method(many meanings) - In one class - Across Classes(linked directly - extends) - Across Classes (linked indirectly - implements)
+ Encapsulation - Data hiding - Preventing accesss to properites and methods

pass by value:

	Class H { // <- reference
	    int x;
	    int s1() {x = 10;}
	    public static void main(String [] args){
	        H a1 = new H();
	        a1.x = 5;
	        System.out.println(a1.x); // 5
	        a1.s1();
	        System.out.println(a1.x); // 10
	    }
	}
	
	Class H { // <- value
	    int x;
	    int s1(int y) {y = 10;}
	    public static void main(String [] args){
	        H a1 = new H();
	        int y = 5;
	        System.out.println(y); // 5
	        a1.s1(y);
	        System.out.println(y); // 10
	    }
	}

+ pass by value - copy the value of a variable form main() to function using the stack
+ pass by reference - copy of the address of vairable instead of the value

> String and Weak Association

+ Strong Association -Containment - Instance of an object is created as part of another object.
+ Assignment 1 - Policeofficer, ParkingTicket, ParkedCar and ParkingMeter

> Encapsulation (Usage of private keyword)

+ private - can be only accessed inside the class
+ protected - can be accessed inside class, package or child classes

methods can be public or protected or even private.

> Abstract class

cannot be instantiated by itself. It is dependent on other object - extended

> Inheritance and Polymorphism

+ Inheritance refers to passing properites from parent to child. (reusability - creating layers of abstract)
+ Methods written in parent class are overridden in child class
+ child class might have a better/newer implementation of the same methods.(Evolution)
+ Creating a signature for a method in parent class and reusing it in child class
	+ Signature - public int methods1(intx, int y){ }

> File IO

Text files \<- Assignment 2

What is a package and how is it created and how is scope used for packages?

+ package - is a group of classes with similar functionality.
+ import a package - all subpackages are not included
+ to import subpackage a dot notation has to be used

> Each file type

+ Stream, Buffers and Filters
+ Stream - bit sequence that connects two memory areas(storage or RAM)
+ Buffer - small memory that is used as data cache - improves performance.
+ Filter - that convert data from on type to another - Language filter

> Textfile

+ FileReader, FileWriter --\> stream objects
+ BufferedReader, BufferedWriter --\> buffered objects

Assignment 2 - Text Files

> Abstract Classes or Interfaces (Gentle Introduction)

Abstract class - parent class that has common methods that cannot instantiated. It is always dependent on child class for instantiation.

> What is the point of creating a constructor in an abstract class?

makes parent self-contained.

> Interfaces

+ It allows simplification of complex implementations.
+ Engine - Dashboard(Interface example)
+ Assignment 2- methods that will enable usage of the grading machine.

## 10 Sep. Thurs

+ File IO
+ Exception Handling (Self-Healing Software)
+ Packages
+ Scope Management

Two points:

1. Implementation
2. Design Strategy

Identify the exception or issue.

Recovery mechanisms in place - that can be enacted when exception/issue occurs.

JRE - Exception Handling system

+ Checked --\> System is aware of the exception...
+ required to use a try / catch block 
+ Unchecked
+ JVM is not aware of in runtime.

Custom exception handler.

+ Error and Exception

Conditions or Decision Making Constructs vs Exception Mgmt

try, catch, finally, throw, throws, extends Exception
checked/unchecked

abstract classes - always on something else for its existence.

interfaces - bridging object families.

Project 1 Unit 1

Lesson 101 on OOP (#FeelingHumor

OOD  +  Feelings

+ class Parent [ What does focus and seriousness have to do with each other? One comes from your heart and the other from your brain. When both are in concert - magic happens.]() 
+ class ChildInstructor extends Parent implements focus, seriousness[ When I teach  with focus and seriousness I express well]()
+ class ChildStudent extends Parent implements focus, seriousness [ When I study with focus and seriousness I learn ]()

