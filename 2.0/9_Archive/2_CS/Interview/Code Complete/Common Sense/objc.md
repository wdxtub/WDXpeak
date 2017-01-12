# Objective-C

## 类与对象

### 类方法

OC中类的方法只有实例方法和静态方法两种：

```
@interface Controller : NSObject { NSString *something; }

+ (void)thisIsAStaticMethod; // 静态方法

– (void)thisIsAnInstanceMethod; // 实例方法

@end
```

OC中的方法只要声明在@interface里，就可以认为都是公有的。实际上，OC没有像Java，C++中的那种绝对的私有及保护成员方法，仅仅可以对调用者隐藏某些方法。

声明和实现都写在@implementation里的方法，类的外部是看不到的。

可以使用 Category 来实现私有方法：

```
// AClass.h
@interface AClass : NSObject

-(void)sayHello;

@end

// AClass.m
@interface AClass(private)

-(void)privateSayHello;

@end

@implementation AClass

-(void)sayHello {
    [self privateSayHello];
}

-(void)privateSayHello {
    NSLog(@"Private Hello");
}
```

使用这种方法时，试图调用privateSayHello会引起编译错误。

也可以使用 Extension 来实现私有方法：

```
// AClass.h 与上面相同

// AClass.m
@interface AClass()

-(void)privateSayHello;

@end

@implementation AClass

-(void)sayHello {
    [self privateSayHello];
}

-(void)privateSayHello {
    NSLog(@"Private Hello");
}

@end
```

与使用 Category 类似，由于声明隐藏在 .m 中，调用者无法看到其声明，也就无法调用privateSayHello这个方法，在ARC下会引发编译错误。

和使用 Category 相比，使用 Extension 有以下两个好处：

1. Extension 声明的方法必须在类的主 @implementation 区间内实现，可以避免使用有名 Category 带来的多个不必要的 implementation 段。
2. 如果 Extension 中声明的方法没有实现，编译器会给出 Warning，使用 Category 则不会。

### 类变量

苹果推荐在OC中使用 @property 来实现成员变量：

```
@interface AClass : NSObject

@property (nonatomic, copy) NSString *name;

@end
```

使用@property声明的变量可以使用实例名.变量名来获取和修改。

@property可以看做是一种语法糖，在 MRC 下，使用 @property 可以看成实现了下面的代码：

```
// AClass.h
@interface AClass : NSObject{
@public
    NSString *_name;
}

-(NSString*) name;
-(void) setName:(NSString*)newName;
@end

// AClass.m
@implementation AClass

-(NSString*) name{
    return _name;
}

-(void) setName:(NSString *)name{
    if (_name != name) {
        [_name release];
        _name = [name copy];
    }
}
@end
```

也就是说，@property 会自动生成 getter 和 setter， 同时进行自动内存管理。

@property 的说明可以有以下几种：

+ readwrite 是可读可写特性；需要生成getter方法和setter方法时
+ readonly 是只读特性，只会生成getter方法 不会生成setter方法，不希望属性在类外改变时使用
+ assign 是赋值特性，setter方法将传入参数赋值给实例变量；仅设置变量时；
+ retain 表示持有特性，setter方法将传入参数先保留，再赋值，传入参数的retaincount会+1;
+ copy 表示拷贝特性，setter方法将传入对象复制一份；需要完全一份新的变量时。
+ nonatomic 和 atomic ，决定编译器生成的setter getter是否是原子操作。 atomic 表示使用原子操作，可以在一定程度上保证线程安全，一般使用nonatomic，nonatomic编译出的代码更快

默认的 @property 是 readwrite，assign，atomic

### 类的扩展

#### Protocol

OC是单继承的，OC中的类可以实现多个 protocol 来实现类似 C++ 中多重继承的效果。

Protocol 类似 Java 中的 interface，定义了一个方法列表，这个方法列表中的方法可以使用@required @optional 标注，以表示该方法是否是客户类必须要实现的方法。 一个 protocol 可以继承其他的 protocol 。

```
@protocol TestProtocol // NSObject也是一个 Protocol，这里即继承 NSObject 里的方法
-(void)Print;
@end

@interface B : NSObject
-(void)Print; // 默认方法是@required的，即必须实现
@end
```

Delegate（委托）是 Cocoa 中常见的一种设计模式，其实现依赖于 protocol 这个语言特性。

#### Category

Category 是一种很灵活的扩展原有类的机制，使用 Category 不需要访问原有类的代码，也无需继承。Category提供了一种简单的方式，来实现类的相关方法的模块化，把不同的类方法分配到不同的类文件中。

Category 常见的使用方法如下：

```
// SomeClass.h
@interface SomeClass : NSObject{
}
-(void) print;
@end

// SomeClass+Hello.h
#import "SomeClass.h"

@interface SomeClass (Hello)
-(void)hello;
@end

// 实现
#import "SomeClass+Hello.h"
@implementationSomeClass (Hello)
-(void)hello{
    NSLog (@"name：%@ ", @"Jacky");
}
@end
```

#### Extension

Extension 可以认为是一种匿名的 Category， Extension 与 Category 有如下几点显著的区别：

1. 使用 Extension 必须有原有类的源码
2. Extension 可以在类中添加新的属性和实例变量，Category 不可以（注：在 Category 中实际上可以通过运行时添加新的属性，参考这里）
3. Extension 里添加的方法必须要有实现

下面是一个 Extension 的例子：

```
@interface MyClass : NSObject
- (float)value;
@end

@interface MyClass () { // 注意此处扩展的写法
    float value;
}
- (void)setValue:(float)newValue;
@end

@implementation MyClass

- (float)value {
    return value;
}

- (void)setValue:(float)newValue {
    value = newValue;
}
@end
```

### 类的导入

导入类可以使用 #include , #import 和 @class 三种方法，其区别如下：

+ #import是Objective-C导入头文件的关键字，#include是C/C++导入头文件的关键字
+ 使用#import头文件会自动只导入一次，不会重复导入，相当于#include和#pragma once；
+ @class告诉编译器需要知道某个类的声明，可以解决头文件的相互包含问题；

@class是放在interface中的，只是在引用一个类，将这个被引用类作为一个类型使用。在实现文件中，如果需要引用到被引用类的实体变量或者方法时，还需要使用#import方式引入被引用类。

### 类的初始化

Objective-C 是建立在 Runtime 基础上的语言，类也不例外。OC 中类是初始化也是动态的。在 OC 中绝大部分类都继承自 NSObject，它有两个非常特殊的类方法 load 和 initilize，用于类的初始化

`+load`

+load 方法是当类或分类被添加到 Objective-C runtime 时被调用的，实现这个方法可以让我们在类加载的时候执行一些类相关的行为。子类的 +load 方法会在它的所有父类的 +load 方法之后执行，而分类的 +load 方法会在它的主类的 +load 方法之后执行。但是不同的类之间的 +load 方法的调用顺序是不确定的。

load 方法不会被类自动继承, 每一个类中的 load 方法都不需要像 viewDidLoad 方法一样调用父类的方法。子类、父类和分类中的 +load 方法的实现是被区别对待的。也就是说如果子类没有实现 +load 方法，那么当它被加载时 runtime 是不会去调用父类的 +load 方法的。同理，当一个类和它的分类都实现了 +load 方法时，两个方法都会被调用。因此，我们常常可以利用这个特性做一些“邪恶”的事情，比如说方法混淆（Method Swizzling）。

`+initialize`

+initialize 方法是在类或它的子类收到第一条消息之前被调用的，这里所指的消息包括实例方法和类方法的调用。也就是说 +initialize 方法是以懒加载的方式被调用的，如果程序一直没有给某个类或它的子类发送消息，那么这个类的 +initialize 方法是永远不会被调用的。

+initialize 方法的调用与普通方法的调用是一样的，走的都是发送消息的流程。换言之，如果子类没有实现 +initialize 方法，那么继承自父类的实现会被调用；如果一个类的分类实现了 +initialize 方法，那么就会对这个类中的实现造成覆盖。

## Block 编程

### Block 语法

Block 可以认为是一种匿名函数，使用如下语法声明一个 Block 类型：

    return_type (^block_name)(parameters)

例如：

    double (^multiplyTwoValues)(double, double);

Block 字面值的写法如下：


    ^ (double firstValue, double secondValue) {
        return firstValue * secondValue;
    }

上面的写法省略了返回值的类型，也可以显式地指出返回值类型。

声明并且定义完一个Block之后，便可以像使用函数一样使用它：

    double (^multiplyTwoValues)(double, double) =
                              ^(double firstValue, double secondValue) {
                                  return firstValue * secondValue;
                              };
    double result = multiplyTwoValues(2,4);
    NSLog(@"The result is %f", result);

同时，Block 也是一种 Objective-C 对象，可以用于赋值，当做参数传递，也可以放入 NSArray 和 NSDictionary 中。

注意：当用于函数参数时，Block 应该放在参数列表的最后一个。

### Block 可以捕获外部变量

Block 可以来自外部作用域的变量，这是Block一个很强大的特性。

    - (void)testMethod {
        int anInteger = 42;
        void (^testBlock)(void) = ^{
            NSLog(@"Integer is: %i", anInteger);
        };
        testBlock();
    }

默认情况下，Block 中捕获的到变量是不能修改的，如果想修改，需要使用__block来声明：

    __block int anInteger = 42;

### 使用 Block 时的注意事项

在非 ARC 的情况下，对于 block 类型的属性应该使用 copy ，因为 block 需要维持其作用域中捕获的变量。在 ARC 中编译器会自动对 block 进行 copy 操作，因此使用 strong 或者 copy 都可以，没有什么区别，但是苹果仍然建议使用 copy 来指明编译器的行为。

block 在捕获外部变量的时候，会保持一个强引用，当在 block 中捕获 self 时，由于对象会对 block 进行 copy，于是便形成了强引用循环：

```
@interface XYZBlockKeeper : NSObject
@property (copy) void (^block)(void);
@end
@implementation XYZBlockKeeper
- (void)configureBlock {
    self.block = ^{
        [self doSomething];    // capturing a strong reference to self
                               // creates a strong reference cycle
    };
}
...
@end
```

为了避免强引用循环，最好捕获一个 self 的弱引用：

```
- (void)configureBlock {
    XYZBlockKeeper * __weak weakSelf = self;
    self.block = ^{
        [weakSelf doSomething];   // capture the weak reference
                                  // to avoid the reference cycle
    }
}
```

使用弱引用会带来另一个问题，weakSelf 有可能会为 nil，如果多次调用 weakSelf 的方法，有可能在 block 执行过程中 weakSelf 变为 nil。因此需要在 block 中将 weakSelf “强化“

```
__weak __typeof__(self) weakSelf = self;
NSBlockOperation *op = [[[NSBlockOperation alloc] init] autorelease];
[ op addExecutionBlock:^ {
    __strong __typeof__(self) strongSelf = weakSelf;
    [strongSelf doSomething];
    [strongSelf doMoreThing];
} ];
[someOperationQueue addOperation:op];
这样上面的 doSomething 和 doMoreThing 要么全执行成功，要么全失败，不会出现一个成功一个失败，即执行到中间 self 变成 nil 的情况。
```

## Objective-C Runtime

http://yulingtianxia.com/blog/2014/11/05/objective-c-runtime/

## Objective-C 内存管理

### 堆与栈

**栈**

栈是用于存放本地变量，内部临时变量以及有关上下文的内存区域。程序在调用函数时，操作系统会自动通过压栈和弹栈完成保存函数现场等操作，不需要程序员手动干预。

栈是一块连续的内存区域，栈顶的地址和栈的最大容量是系统预先规定好的。能从栈获得的空间较小。如果申请的空间超过栈的剩余空间时，例如递归深度过深，将提示stackoverflow。

栈是机器系统提供的数据结构，计算机会在底层对栈提供支持：分配专门的寄存器存放栈的地址，压栈出栈都有专门的指令执行，这就决定了栈的效率比较高。

**堆**

堆是用于存放除了栈里的东西之外所有其他东西的内存区域，当使用malloc和free时就是在操作堆中的内存。对于堆来说，释放工作由程序员控制，容易产生memory leak。

堆是向高地址扩展的数据结构，是不连续的内存区域。这是由于系统是用链表来存储的空闲内存地址的，自然是不连续的，而链表的遍历方向是由低地址向高地址。堆的大小受限于计算机系统中有效的虚拟内存。由此可见，堆获得的空间比较灵活，也比较大。

对于堆来讲，频繁的new/delete势必会造成内存空间的不连续，从而造成大量的碎片，使程序效率降低。对于栈来讲，则不会存在这个问题，因为栈是先进后出的队列，永远都不可能有一个内存块从栈中间弹出。

堆都是动态分配的，没有静态分配的堆。栈有2种分配方式：静态分配和动态分配。静态分配是编译器完成的，比如局部变量的分配。动态分配由alloca函数进行分配，但是栈的动态分配和堆是不同的，他的动态分配是由编译器进行释放，无需我们手工实现。

计算机底层并没有对堆的支持，堆则是C/C++函数库提供的，同时由于上面提到的碎片问题，都会导致堆的效率比栈要低。

**Objective-C中的内存分配**

在 Objective-C 中，对象通常是使用 alloc 方法在堆上创建的。 [NSObject alloc] 方法会在对堆上分配一块内存，按照NSObject的内部结构填充这块儿内存区域。

一旦对象创建完成，就不可能再移动它了。因为很可能有很多指针都指向这个对象，这些指针并没有被追踪。因此没有办法在移动对象的位置之后更新全部的这些指针。

### MRC 与 ARC

Objective-C中提供了两种内存管理机制：MRC（MannulReference Counting）和ARC(Automatic Reference Counting)，分别提供对内存的手动和自动管理，来满足不同的需求。现在苹果推荐是用 ARC 来进行内存管理。

**MRC**

在MRC的内存管理模式下，与对变量的管理相关的方法有：retain,release和autorelease。retain和release方法操作的是引用记数，当引用记数为零时，便自动释放内存。并且可以用NSAutoreleasePool对象，对加入自动释放池（autorelease调用）的变量进行管理，当drain时回收内存。

1. retain，该方法的作用是将内存数据的所有权附给另一指针变量，引用数加1，即retainCount+= 1;
2. release，该方法是释放指针变量对内存数据的所有权，引用数减1，即retainCount-= 1;
3. autorelease，该方法是将该对象内存的管理放到autoreleasepool中。

示例代码:

```
//假设Number为预定义的类
Number* num = [[Number alloc] init];
Number* num2 = [num retain];//此时引用记数+1，现为2

[num2 release]; //num2 释放对内存数据的所有权 引用记数-1,现为1;
[num release];//num释放对内存数据的所有权 引用记数-1,现为0;
[num add:1 and 2];//bug，此时内存已释放。

//autoreleasepool 的使用 在MRC管理模式下，我们摒弃以前的用法，NSAutoreleasePool对象的使用，新手段为@autoreleasepool

@autoreleasepool {
    Number* num = [[Number alloc] init];
    [numautorelease];//由autoreleasepool来管理其内存的释放
}
```

**ARC**

ARC 是苹果引入的一种自动内存管理机制，会自动监视对象的生存周期，并在编译时期自动在已有代码中插入合适的内存管理代码。

**变量标识符**

在ARC中与内存管理有关的变量标识符，有下面几种：

+ `__strong`
+ `__weak`
+ `__unsafe_unretained`
+ `__autoreleasing`

`__strong` 是默认使用的标识符。只有还有一个强指针指向某个对象，这个对象就会一种存活。

`__weak` 声明这个引用不会保持被引用对象的存活，如果对象没有强引用了，弱引用会被置为nil

`__unsafe_unretained` 声明这个引用不会保持被引用对象的存活，如果对象没有强引用了，它不会被置为nil。如果它引用的对象被回收掉了，该指针就变成了野指针。

`__autoreleasing` 用于标示使用引用传值的参数（id *），在函数返回时会被自动释放掉。

变量标识符的用法如下：

    __strong Number* num = [[Number alloc] init];

**属性标识符**

类中的属性也可以加上标志符：

    @property (assign/retain/strong/weak/unsafe_unretained/copy) Number* num

assign表明 setter 仅仅是一个简单的赋值操作，通常用于基本的数值类型，例如CGFloat和NSInteger。

strong表明属性定义一个拥有者关系。当给属性设定一个新值的时候，首先这个值进行 retain ，旧值进行 release ，然后进行赋值操作。

weak表明属性定义了一个非拥有者关系。当给属性设定一个新值的时候，这个值不会进行 retain，旧值也不会进行 release， 而是进行类似 assign 的操作。不过当属性指向的对象被销毁时，该属性会被置为nil。

unsafe_unretained的语义和 assign 类似，不过是用于对象类型的，表示一个非拥有(unretained)的，同时也不会在对象被销毁时置为nil的(unsafe)关系。

copy 类似于 strong，不过在赋值时进行 copy 操作而不是 retain 操作。通常在需要保留某个不可变对象（NSString最常见），并且防止它被意外改变时使用。

**引用循环**

当两个对象互相持有对方的强引用，并且这两个对象的引用计数都不是0的时候，便造成了引用循环。

要想破除引用循环，可以从以下几点入手：

+ 注意变量作用域，使用 autorelease 让编译器来处理引用
+ 使用弱引用(weak)
+ 当实例变量完成工作后，将其置为nil


