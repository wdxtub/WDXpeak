# iOS 面试相关

<!-- MarkdownTOC -->

- 业务能力
- 1. 风格纠错题
    - 优化部分
    - 硬伤部分
- 2. 什么情况使用 weak 关键字，相比 assign 有什么不同？
- 3. 怎么用 copy 关键字？
- 4. 这个写法会出什么问题： `@property (copy) NSMutableArray *array;`
- 5. 如何让自己的类用 copy 修饰符？如何重写带 copy 关键字的 setter？
- 6. @property 的本质是什么？ivar、getter、setter 是如何生成并添加到这个类中的
- 7. @protocol 和 category 中如何使用 @property
- 8. runtime 如何实现 weak 属性
- 9. @property中有哪些属性关键字？/ @property 后面可以有哪些修饰符？
- 10. weak属性需要在dealloc中置nil么？
- 11. @synthesize和@dynamic分别有什么作用？
- 12. ARC下，不显式指定任何属性关键字时，默认的关键字都有哪些？
- 13. 用@property声明的NSString（或NSArray，NSDictionary）经常使用copy关键字，为什么？如果改用strong关键字，可能造成什么问题？
    - 1. 对非集合类对象的copy操作：
    - 2、集合类对象的copy与mutableCopy
- 14. @synthesize合成实例变量的规则是什么？假如property名为foo，存在一个名为`_foo`的实例变量，那么还会自动合成新变量么？
- 15. 在有了自动合成属性实例变量之后，@synthesize还有哪些使用场景？
- 16. objc中向一个nil对象发送消息将会发生什么？
- 17. objc中向一个对象发送消息和函数之间有什么关系？
- 18. 什么时候会报 unrecognized selector 的异常？
- 19. 一个objc对象如何进行内存布局？（考虑有父类的情况）
- 20. 一个objc对象的isa的指针指向什么？有什么作用？
- 21. 下面的代码输出什么？
- 22. runtime如何通过selector找到对应的IMP地址？（分别考虑类方法和实例方法）
- 23. 使用runtime Associate方法关联的对象，需要在主对象dealloc的时候释放么？
- 24. objc中的类方法和实例方法有什么本质区别和联系？
- 25. `_objc_msgForward`函数是做什么的，直接调用它将会发生什么？
- 26. runtime如何实现weak变量的自动置nil？
- 27. 能否向编译后得到的类中增加实例变量？能否向运行时创建的类中添加实例变量？为什么？
- 28. runloop和线程有什么关系？
- 29. runloop的mode作用是什么？
- 30. 以+ scheduledTimerWithTimeInterval...的方式触发的timer，在滑动页面上的列表时，timer会暂定回调，为什么？如何解决？
- 31. 猜想runloop内部是如何实现的？
- 32. objc使用什么机制管理对象内存？
- 33. ARC通过什么方式帮助开发者管理内存？
- 34. 不手动指定autoreleasepool的前提下，一个autorealese对象在什么时刻释放？（比如在一个vc的viewDidLoad中创建）
- 35. BAD_ACCESS在什么情况下出现？
- 36. 苹果是如何实现autoreleasepool的？
- 37. 使用block时什么情况会发生引用循环，如何解决？
- 38. 在block内如何修改block外部变量？
- 39. 使用系统的某些block api（如UIView的block版本写动画时），是否也考虑引用循环问题？
- 40. GCD的队列（`dispatch_queue_t`）分哪两种类型？
- 41. 如何用GCD同步若干个异步调用？（如根据若干个url异步加载多张图片，然后在都下载完成后合成一张整图）
- 42. `dispatch_barrier_async`的作用是什么？
- 43. 苹果为什么要废弃`dispatch_get_current_queue`？
- 44. 以下代码运行结果如何？
- 45. addObserver:forKeyPath:options:context:各个参数的作用分别是什么，observer中需要实现哪个方法才能获得KVO回调？
- 46. 如何手动触发一个value的KVO
- 47. 若一个类有实例变量 `NSString *_foo` ，调用setValue:forKey:时，可以以foo还是 `_foo` 作为key？
- 48. KVC的keyPath中的集合运算符如何使用？
- 49. KVC和KVO的keyPath一定是属性么？
- 50. 如何关闭默认的KVO的默认实现，并进入自定义的KVO实现？
- 51. apple用什么方式实现对一个对象的KVO？
- 52. IBOutlet连出来的视图属性为什么可以被设置成weak?
- 53. IB中User Defined Runtime Attributes如何使用？
- 54. 如何调试BAD_ACCESS错误
- 55. lldb（gdb）常用的调试命令？

<!-- /MarkdownTOC -->


## 业务能力

毕竟平常的工作内容不是 runtime、runloop，不怎么会用到底层的黑魔法，80% 的时间都是和搭建页面、写业务逻辑、网络请求打交道。

要求面试者能够熟练构建 UI，我会找一个面试者做过的页面让他分析下页面结构、约束或者 frame 布局的连法和计算方法；有时也会让面试者说说 UITableView 常用的几个 delegate 和 data source 代理方法，动态 Cell 高度计算什么的；接下来，在手机里随便找一个 App 的页面，让面试者当场说说如果是他写应该用哪些 UI 组件和布局方式等。问几个问题后就能大概了解业务能力了，我们这边重度使用 IB 和 AutoLayout，假如面试者依然使用代码码 UI 也到没关系，有“从良”意愿就很好~

程序架构和一些设计模式如果面试者自己觉得还不错的话也会聊聊，但跪求别说 Singleton 了，用的越多对水平就越表示怀疑。对设计模式自信的我一般问一个问题，抽象工厂模式在 Cocoa SDK 中哪些类中体现？
架构上 MVC 还是 MVVM 还是 MVP 神马的到是可以聊聊各自的见解，反正也没有正确答案，只要别搞的太离谱就行，比如有的人说网络请求和数据库的操作最好放到 UIView 的子类里面干。

网络请求、数据库等各家都有成熟的封装，基本知道咋用就行。除此之外，我们还会顺带的问下除了 iOS 开发外，还会什么其他编程语言、或者熟悉哪种脚本语言和 Terminal 操作等，甚至还问问是如何翻墙- -，相信这些技能都是很重要的。


## 1. 风格纠错题

![enter image description here](http://i.imgur.com/O7Zev94.png)
修改完的代码：

修改方法有很多种，现给出一种做示例：


```objc
// .h文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 修改完的代码，这是第一种修改方法，后面会给出第二种修改方法

typedef NS_ENUM(NSInteger, CYLSex) {
    CYLSexMan,
    CYLSexWoman
};

@interface CYLUser : NSObject<NSCopying>

@property (nonatomic, readonly, copy) NSString *name;
@property (nonatomic, readonly, assign) NSUInteger age;
@property (nonatomic, readonly, assign) CYLSex sex;

- (instancetype)initWithName:(NSString *)name age:(NSUInteger)age sex:(CYLSex)sex;
+ (instancetype)userWithName:(NSString *)name age:(NSUInteger)age sex:(CYLSex)sex;

@end
```

### 优化部分

 1. enum 建议使用 `NS_ENUM` 和 `NS_OPTIONS` 宏来定义枚举类型，参见官方的 [Adopting Modern Objective-C](https://developer.apple.com/library/ios/releasenotes/ObjectiveC/ModernizationObjC/AdoptingModernObjective-C/AdoptingModernObjective-C.html) 一文：

```objc
//定义一个枚举
typedef NS_ENUM(NSInteger, CYLSex) {
    CYLSexMan,
    CYLSexWoman
};
```
 （仅仅让性别包含男和女可能并不严谨，最严谨的做法可以参考 [这里](https://github.com/ChenYilong/iOSInterviewQuestions/issues/9) 。）

 2.age 属性的类型：应避免使用基本类型，建议使用 Foundation 数据类型，对应关系如下：

```objc
int -> NSInteger
unsigned -> NSUInteger
float -> CGFloat
动画时间 -> NSTimeInterval
```
同时考虑到 age 的特点，应使用 NSUInteger ，而非 int 。
这样做的是基于64-bit 适配考虑，详情可参考出题者的博文[《64-bit Tips》](http://blog.sunnyxx.com/2014/12/20/64-bit-tips/)。

3.如果工程项目非常庞大，需要拆分成不同的模块，可以在类、typedef宏命名的时候使用前缀。

4.doLogIn方法不应写在该类中

登录操作属于业务逻辑，观察类名 UserModel ，以及属性的命名方式，该类应该是一个 Model 而不是一个“ MVVM 模式下的 ViewModel ”：

> 无论是 MVC 模式还是 MVVM 模式，业务逻辑都不应当写在 Model 里：MVC 应在 C，MVVM 应在 VM。

（如果抛开命名规范，假设该类真的是 MVVM 模式里的 ViewModel ，那么 UserModel 这个类可能对应的是用户注册页面，如果有特殊的业务需求，比如： `-logIn` 对应的应当是注册并登录的一个 Button ，出现 `-logIn` 方法也可能是合理的。）

5.doLogIn 方法命名不规范：添加了多余的动词前缀。

请牢记：

> 如果方法表示让对象执行一个动作，使用动词打头来命名，注意不要使用 `do`，`does` 这种多余的关键字，动词本身的暗示就足够了。

因为 `-logIn` （注意： `Login` 是名词， `LogIn`  是动词，都表示登陆。  见[ ***Log in vs. login*** ](http://grammarist.com/spelling/log-in-login/)）

6.`-(id)initUserModelWithUserName: (NSString*)name withAge:(int)age;`方法中不要用 `with` 来连接两个参数: `withAge:` 应当换为`age:`，`age:` 已经足以清晰说明参数的作用，也不建议用 `andAge:` ：通常情况下，即使有类似 `withA:withB:` 的命名需求，也通常是使用`withA:andB:` 这种命名，用来表示方法执行了两个相对独立的操作（*从设计上来说，这时候也可以拆分成两个独立的方法*），它不应该用作阐明有多个参数，比如下面的：

```objc
//错误，不要使用"and"来连接参数
- (int)runModalForDirectory:(NSString *)path andFile:(NSString *)name andTypes:(NSArray *)fileTypes;
//错误，不要使用"and"来阐明有多个参数
- (instancetype)initWithName:(CGFloat)width andAge:(CGFloat)height;
//正确，使用"and"来表示两个相对独立的操作
- (BOOL)openFile:(NSString *)fullPath withApplication:(NSString *)appName andDeactivate:(BOOL)flag;
```

7.由于字符串值可能会改变，所以要把相关属性的“内存管理语义”声明为 copy 。(原因在下文有详细论述：***用@property声明的NSString（或NSArray，NSDictionary）经常使用copy关键字，为什么？***)

8.“性别”(sex）属性的：该类中只给出了一种“初始化方法” (initializer)用于设置“姓名”(Name)和“年龄”(Age)的初始值，那如何对“性别”(Sex）初始化？

Objective-C 有 designated 和 secondary 初始化方法的观念。 designated 初始化方法是提供所有的参数，secondary 初始化方法是一个或多个，并且提供一个或者更多的默认参数来调用 designated 初始化方法的初始化方法。举例说明：

```objc
// .m文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
//

@implementation CYLUser

- (instancetype)initWithName:(NSString *)name
                        age:(NSUInteger)age
                        sex:(CYLSex)sex {
   if(self = [super init]) {
       _name = [name copy];
       _age = age;
       _sex = sex;
   }
   return self;
}

- (instancetype)initWithName:(NSString *)name
                        age:(NSUInteger)age {
   return [self initWithName:name age:age sex:nil];
}

@end
```

上面的代码中initWithName:age:sex: 就是 designated 初始化方法，另外的是 secondary 初始化方法。因为仅仅是调用类实现的 designated 初始化方法。

因为出题者没有给出 `.m` 文件，所以有两种猜测：1：本来打算只设计一个 designated 初始化方法，但漏掉了“性别”(sex）属性。那么最终的修改代码就是上文给出的第一种修改方法。2：不打算初始时初始化“性别”(sex）属性，打算后期再修改，如果是这种情况，那么应该把“性别”(sex）属性设为 readwrite 属性，最终给出的修改代码应该是：

```objc
// .h文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 第二种修改方法（基于第一种修改方法的基础上）

typedef NS_ENUM(NSInteger, CYLSex) {
    CYLSexMan,
    CYLSexWoman
};

@interface CYLUser : NSObject<NSCopying>

@property (nonatomic, readonly, copy) NSString *name;
@property (nonatomic, readonly, assign) NSUInteger age;
@property (nonatomic, readwrite, assign) CYLSex sex;

- (instancetype)initWithName:(NSString *)name age:(NSUInteger)age sex:(CYLSex)sex;
- (instancetype)initWithName:(NSString *)name age:(NSUInteger)age;
+ (instancetype)userWithName:(NSString *)name age:(NSUInteger)age sex:(CYLSex)sex;

@end
```

`.h` 中暴露 designated 初始化方法，是为了方便子类化 （想了解更多，请戳--》 [***《禅与 Objective-C 编程艺术 （Zen and the Art of the Objective-C Craftsmanship 中文翻译）》***](http://is.gd/OQ49zk)。）

9.按照接口设计的惯例，如果设计了“初始化方法” (initializer)，也应当搭配一个快捷构造方法。而快捷构造方法的返回值，建议为 instancetype，为保持一致性，init 方法和快捷构造方法的返回类型最好都用 instancetype。

10.如果基于第一种修改方法：既然该类中已经有一个“初始化方法” (initializer)，用于设置“姓名”(Name)、“年龄”(Age)和“性别”(Sex）的初始值:

那么在设计对应 `@property` 时就应该尽量使用不可变的对象：其三个属性都应该设为“只读”。用初始化方法设置好属性值之后，就不能再改变了。在本例中，仍需声明属性的“内存管理语义”。于是可以把属性的定义改成这样

```objc
@property (nonatomic, readonly, copy) NSString *name;
@property (nonatomic, readonly, assign) NSUInteger age;
@property (nonatomic, readonly, assign) CYLSex sex;
```

由于是只读属性，所以编译器不会为其创建对应的“设置方法”，即便如此，我们还是要写上这些属性的语义，以此表明初始化方法在设置这些属性值时所用的方式。要是不写明语义的话，该类的调用者就不知道初始化方法里会拷贝这些属性，他们有可能会在调用初始化方法之前自行拷贝属性值。这种操作多余而且低效。

11.`initUserModelWithUserName` 如果改为 `initWithName` 会更加简洁，而且足够清晰。

12.`UserModel` 如果改为 `User` 会更加简洁，而且足够清晰。

13.`UserSex`如果改为`Sex` 会更加简洁，而且足够清晰。

14.第二个 `@property` 中 assign 和 nonatomic 调换位置。

推荐按照下面的格式来定义属性

```objc
@property (nonatomic, readwrite, copy) NSString *name;
```
 属性的参数应该按照下面的顺序排列： 原子性，读写 和 内存管理。 这样做你的属性更容易修改正确，并且更好阅读。这在[《禅与Objective-C编程艺术 >》](https://github.com/oa414/objc-zen-book-cn#属性定义)里有介绍。而且习惯上修改某个属性的修饰符时，一般从属性名从右向左搜索需要修动的修饰符。最可能从最右边开始修改这些属性的修饰符，根据经验这些修饰符被修改的可能性从高到底应为：内存管理 > 读写权限 >原子操作。

### 硬伤部分

1. 在`-`和`(void)`之间应该有一个空格
2. enum 中驼峰命名法和下划线命名法混用错误：枚举类型的命名规则和函数的命名规则相同：命名时使用驼峰命名法，勿使用下划线命名法。
3. enum 左括号前加一个空格，或者将左括号换到下一行
4. enum 右括号后加一个空格
5. `UserModel :NSObject` 应为`UserModel : NSObject`，也就是`:`右侧少了一个空格。
6. `@interface` 与 `@property` 属性声明中间应当间隔一行。
7. 两个方法定义之间不需要换行，有时为了区分方法的功能也可间隔一行，但示例代码中间隔了两行。
8. `-(id)initUserModelWithUserName: (NSString*)name withAge:(int)age;`方法中方法名与参数之间多了空格。而且 `-` 与 `(id)` 之间少了空格。
9. `-(id)initUserModelWithUserName: (NSString*)name withAge:(int)age;`方法中方法名与参数之间多了空格：`(NSString*)name` 前多了空格。
10. `-(id)initUserModelWithUserName: (NSString*)name withAge:(int)age;` 方法中 `(NSString*)name`,应为 `(NSString *)name`，少了空格。

## 2. 什么情况使用 weak 关键字，相比 assign 有什么不同？

什么情况使用 weak 关键字？

1. 在 ARC 中,在有可能出现循环引用的时候,往往要通过让其中一端使用 weak 来解决,比如: delegate 代理属性

2. 自身已经对它进行一次强引用,没有必要再强引用一次,此时也会使用 weak,自定义 IBOutlet 控件属性一般也使用 weak；当然，也可以使用strong。在下文也有论述：***《IBOutlet连出来的视图属性为什么可以被设置成weak?》***

不同点：

1. `weak` 此特质表明该属性定义了一种“非拥有关系” (nonowning relationship)。为这种属性设置新值时，设置方法既不保留新值，也不释放旧值。此特质同assign类似，然而在属性所指的对象遭到摧毁时，属性值也会清空(nil out)。而 `assign` 的“设置方法”只会执行针对“纯量类型” (scalar type，例如 CGFloat 或 NSlnteger 等)的简单赋值操作。
2. assigin 可以用非 OC 对象,而 weak 必须用于 OC 对象

## 3. 怎么用 copy 关键字？

用途：

1. NSString、NSArray、NSDictionary 等等经常使用copy关键字，是因为他们有对应的可变类型：NSMutableString、NSMutableArray、NSMutableDictionary；
2. block 也经常使用 copy 关键字，具体原因见[官方文档：***Objects Use Properties to Keep Track of Blocks***](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithBlocks/WorkingwithBlocks.html#//apple_ref/doc/uid/TP40011210-CH8-SW12)：

block 使用 copy 是从 MRC 遗留下来的“传统”,在 MRC 中,方法内部的 block 是在栈区的,使用 copy 可以把它放到堆区.在 ARC 中写不写都行：对于 block 使用 copy 还是 strong 效果是一样的，但写上 copy 也无伤大雅，还能时刻提醒我们：编译器自动对 block 进行了 copy 操作。如果不写 copy ，该类的调用者有可能会忘记或者根本不知道“编译器会自动对 block 进行了 copy 操作”，他们有可能会在调用之前自行拷贝属性值。这种操作多余而低效。

![enter image description here](http://i.imgur.com/VlVKl8L.png)

下面做下解释：

copy 此特质所表达的所属关系与 strong 类似。然而设置方法并不保留新值，而是将其“拷贝” (copy)。

当属性类型为 NSString 时，经常用此特质来保护其封装性，因为传递给设置方法的新值有可能指向一个 NSMutableString 类的实例。这个类是 NSString 的子类，表示一种可修改其值的字符串，此时若是不拷贝字符串，那么设置完属性之后，字符串的值就可能会在对象不知情的情况下遭人更改。所以，这时就要拷贝一份“不可变” (immutable)的字符串，确保对象中的字符串值不会无意间变动。只要实现属性所用的对象是“可变的” (mutable)，就应该在设置新属性值时拷贝一份。

> 用 `@property` 声明 NSString、NSArray、NSDictionary 经常使用 copy 关键字，是因为他们有对应的可变类型：NSMutableString、NSMutableArray、NSMutableDictionary，他们之间可能进行赋值操作，为确保对象中的字符串值不会无意间变动，应该在设置新属性值时拷贝一份。

该问题在下文中也有论述：***用@property声明的NSString（或NSArray，NSDictionary）经常使用copy关键字，为什么？如果改用strong关键字，可能造成什么问题？***

## 4. 这个写法会出什么问题： `@property (copy) NSMutableArray *array;`

两个问题：1、添加,删除,修改数组内的元素的时候,程序会因为找不到对应的方法而崩溃.因为 copy 就是复制一个不可变 NSArray 的对象；2、使用了 atomic 属性会严重影响性能 ；

第1条的相关原因在下文中有论述***《用@property声明的NSString（或NSArray，NSDictionary）经常使用 copy 关键字，为什么？如果改用strong关键字，可能造成什么问题？》*** 以及上文***《怎么用 copy 关键字？》***也有论述。

比如下面的代码就会发生崩溃

```objc
// .h文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 下面的代码就会发生崩溃

@property (nonatomic, copy) NSMutableArray *mutableArray;
```

```objc
// .m文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 下面的代码就会发生崩溃

NSMutableArray *array = [NSMutableArray arrayWithObjects:@1,@2,nil];
self.mutableArray = array;
[self.mutableArray removeObjectAtIndex:0];
```

接下来就会奔溃：

```objc
 -[__NSArrayI removeObjectAtIndex:]: unrecognized selector sent to instance 0x7fcd1bc30460
```

第2条原因，如下：

> 该属性使用了同步锁，会在创建时生成一些额外的代码用于帮助编写多线程程序，这会带来性能问题，通过声明 nonatomic 可以节省这些虽然很小但是不必要额外开销。

在默认情况下，由编译器所合成的方法会通过锁定机制确保其原子性(atomicity)。如果属性具备 nonatomic 特质，则不使用同步锁。请注意，尽管没有名为“atomic”的特质(如果某属性不具备 nonatomic 特质，那它就是“原子的”(atomic))。

在iOS开发中，你会发现，几乎所有属性都声明为 nonatomic。

一般情况下并不要求属性必须是“原子的”，因为这并不能保证“线程安全” ( thread safety)，若要实现“线程安全”的操作，还需采用更为深层的锁定机制才行。例如，一个线程在连续多次读取某属性值的过程中有别的线程在同时改写该值，那么即便将属性声明为 atomic，也还是会读到不同的属性值。

因此，开发iOS程序时一般都会使用 nonatomic 属性。但是在开发 Mac OS X 程序时，使用
 atomic 属性通常都不会有性能瓶颈。

## 5. 如何让自己的类用 copy 修饰符？如何重写带 copy 关键字的 setter？


> 若想令自己所写的对象具有拷贝功能，则需实现 NSCopying 协议。如果自定义的对象分为可变版本与不可变版本，那么就要同时实现 `NSCopying` 与 `NSMutableCopying` 协议。

具体步骤：

1. 需声明该类遵从 NSCopying 协议
2. 实现 NSCopying 协议。该协议只有一个方法:

```objc
- (id)copyWithZone:(NSZone *)zone;
```

注意：一提到让自己的类用 copy 修饰符，我们总是想覆写copy方法，其实真正需要实现的却是 “copyWithZone” 方法。

以第一题的代码为例：

```objc
// .h文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 修改完的代码

typedef NS_ENUM(NSInteger, CYLSex) {
    CYLSexMan,
    CYLSexWoman
};

@interface CYLUser : NSObject<NSCopying>

@property (nonatomic, readonly, copy) NSString *name;
@property (nonatomic, readonly, assign) NSUInteger age;
@property (nonatomic, readonly, assign) CYLSex sex;

- (instancetype)initWithName:(NSString *)name age:(NSUInteger)age sex:(CYLSex)sex;
+ (instancetype)userWithName:(NSString *)name age:(NSUInteger)age sex:(CYLSex)sex;

@end
```

然后实现协议中规定的方法：

```objc
- (id)copyWithZone:(NSZone *)zone {
	CYLUser *copy = [[[self class] allocWithZone:zone]
		             initWithName:_name
 							      age:_age
						          sex:_sex];
	return copy;
}
```

但在实际的项目中，不可能这么简单，遇到更复杂一点，比如类对象中的数据结构可能并未在初始化方法中设置好，需要另行设置。举个例子，假如 CYLUser 中含有一个数组，与其他 CYLUser 对象建立或解除朋友关系的那些方法都需要操作这个数组。那么在这种情况下，你得把这个包含朋友对象的数组也一并拷贝过来。下面列出了实现此功能所需的全部代码:

```objc
// .h文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 以第一题《风格纠错题》里的代码为例

typedef NS_ENUM(NSInteger, CYLSex) {
    CYLSexMan,
    CYLSexWoman
};

@interface CYLUser : NSObject<NSCopying>

@property (nonatomic, readonly, copy) NSString *name;
@property (nonatomic, readonly, assign) NSUInteger age;
@property (nonatomic, readonly, assign) CYLSex sex;

- (instancetype)initWithName:(NSString *)name age:(NSUInteger)age sex:(CYLSex)sex;
+ (instancetype)userWithName:(NSString *)name age:(NSUInteger)age sex:(CYLSex)sex;
- (void)addFriend:(CYLUser *)user;
- (void)removeFriend:(CYLUser *)user;

@end
```

// .m文件

```objc
// .m文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
//

@implementation CYLUser {
    NSMutableSet *_friends;
}

- (void)setName:(NSString *)name {
    _name = [name copy];
}

- (instancetype)initWithName:(NSString *)name
                         age:(NSUInteger)age
                         sex:(CYLSex)sex {
    if(self = [super init]) {
        _name = [name copy];
        _age = age;
        _sex = sex;
        _friends = [[NSMutableSet alloc] init];
    }
    return self;
}

- (void)addFriend:(CYLUser *)user {
    [_friends addObject:user];
}

- (void)removeFriend:(CYLUser *)user {
    [_friends removeObject:person];
}

- (id)copyWithZone:(NSZone *)zone {
    CYLUser *copy = [[[self class] allocWithZone:zone]
                     initWithName:_name
                     age:_age
                     sex:_sex];
    copy->_friends = [_friends mutableCopy];
    return copy;
}

- (id)deepCopy {
    CYLUser *copy = [[[self class] allocWithZone:zone]
                     initWithName:_name
                     age:_age
                     sex:_sex];
    copy->_friends = [[NSMutableSet alloc] initWithSet:_friends
                                             copyItems:YES];
    return copy;
}

@end
```

以上做法能满足基本的需求，但是也有缺陷：

> 如果你所写的对象需要深拷贝，那么可考虑新增一个专门执行深拷贝的方法。

在例子中，存放朋友对象的 set 是用 “copyWithZone:” 方法来拷贝的，这种浅拷贝方式不会逐个复制 set 中的元素。若需要深拷贝的话，则可像下面这样，编写一个专供深拷贝所用的方法:

```objc
- (id)deepCopy {
    CYLUser *copy = [[[self class] allocWithZone:zone]
                     initWithName:_name
                     age:_age
                     sex:_sex];
    copy->_friends = [[NSMutableSet alloc] initWithSet:_friends
                                             copyItems:YES];
    return copy;
}
```

至于***如何重写带 copy 关键字的 setter***这个问题，

如果抛开本例来回答的话，如下：

```objc
- (void)setName:(NSString *)name {
    //[_name release];
    _name = [name copy];
}
```

不过也有争议，有人说“苹果如果像下面这样干，是不是效率会高一些？”

```objc
- (void)setName:(NSString *)name {
    if (_name != name) {
        //[_name release];//MRC
        _name = [name copy];
    }
}
```

> 不要在 setter 里进行像 `if(_obj != newObj)` 这样的判断。（该观点参考链接：[ ***How To Write Cocoa Object Setters： Principle 3: Only Optimize After You Measure*** ](http://vgable.com/blog/tag/autorelease/)
）

什么情况会在 copy setter 里做 if 判断？

例如，车速可能就有最高速的限制，车速也不可能出现负值，如果车子的最高速为300，则 setter 的方法就要改写成这样：

```objc
-(void)setSpeed:(int)_speed{
    if(_speed < 0) speed = 0;
    if(_speed > 300) speed = 300;
    _speed = speed;
}
```

回到这个题目，如果单单就上文的代码而言，我们不需要也不能重写 name 的 setter ：由于是 name 是只读属性，所以编译器不会为其创建对应的“设置方法”，用初始化方法设置好属性值之后，就不能再改变了。（ 在本例中，之所以还要声明属性的“内存管理语义”--copy，是因为：如果不写 copy，该类的调用者就不知道初始化方法里会拷贝这些属性，他们有可能会在调用初始化方法之前自行拷贝属性值。这种操作多余而低效）。

那如何确保 name 被 copy？在初始化方法(initializer)中做：

```objc
- (instancetype)initWithName:(NSString *)name
							 age:(NSUInteger)age
							 sex:(CYLSex)sex {
     if(self = [super init]) {
     	_name = [name copy];
     	_age = age;
     	_sex = sex;
     	_friends = [[NSMutableSet alloc] init];
     }
     return self;
}
```

## 6. @property 的本质是什么？ivar、getter、setter 是如何生成并添加到这个类中的

**@property 的本质是什么？**

> @property = ivar + getter + setter;

下面解释下：

> “属性” (property)有两大概念：ivar（实例变量）、存取方法（access method ＝ getter + setter）。

“属性” (property)作为 Objective-C 的一项特性，主要的作用就在于封装对象中的数据。 Objective-C 对象通常会把其所需要的数据保存为各种实例变量。实例变量一般通过“存取方法”(access method)来访问。其中，“获取方法” (getter)用于读取变量值，而“设置方法” (setter)用于写入变量值。这个概念已经定型，并且经由“属性”这一特性而成为 `Objective-C 2.0` 的一部分。

而在正规的 Objective-C 编码风格中，存取方法有着严格的命名规范。

正因为有了这种严格的命名规范，所以 Objective-C 这门语言才能根据名称自动创建出存取方法。其实也可以把属性当做一种关键字，其表示:

> 编译器会自动写出一套存取方法，用以访问给定类型中具有给定名称的变量。
> 所以你也可以这么说：@property = getter + setter;

例如下面这个类：

```objc
@interface Person : NSObject
@property NSString *firstName;
@property NSString *lastName;
@end
```

上述代码写出来的类与下面这种写法等效：

```objc
@interface Person : NSObject
- (NSString *)firstName;
- (void)setFirstName:(NSString *)firstName;
- (NSString *)lastName;
- (void)setLastName:(NSString *)lastName;
@end
```

**ivar、getter、setter 是如何生成并添加到这个类中的?**

> “自动合成”( autosynthesis)

完成属性定义后，编译器会自动编写访问这些属性所需的方法，此过程叫做“自动合成”(autosynthesis)。需要强调的是，这个过程由编译器在编译期执行，所以编辑器里看不到这些“合成方法”(synthesized method)的源代码。除了生成方法代码 getter、setter 之外，编译器还要自动向类中添加适当类型的实例变量，并且在属性名前面加下划线，以此作为实例变量的名字。在前例中，会生成两个实例变量，其名称分别为 `_firstName` 与 `_lastName`。也可以在类的实现代码里通过 `@synthesize` 语法来指定实例变量的名字.

```objc
@implementation Person
@synthesize firstName = _myFirstName;
@synthesize lastName = _myLastName;
@end
```

我为了搞清属性是怎么实现的,曾经反编译过相关的代码,他大致生成了五个东西

1. `OBJC_IVAR_$类名$属性名称` ：该属性的“偏移量” (offset)，这个偏移量是“硬编码” (hardcode)，表示该变量距离存放对象的内存区域的起始地址有多远。
2. setter 与 getter 方法对应的实现函数
3. `ivar_list` ：成员变量列表
4. `method_list` ：方法列表
5. `prop_list` ：属性列表


也就是说我们每次在增加一个属性,系统都会在 `ivar_list` 中添加一个成员变量的描述,在 `method_list` 中增加 setter 与 getter 方法的描述,在属性列表中增加一个属性的描述,然后计算该属性在对象中的偏移量,然后给出 setter 与 getter 方法对应的实现,在 setter 方法中从偏移量的位置开始赋值,在 getter 方法中从偏移量开始取值,为了能够读取正确字节数,系统对象偏移量的指针类型进行了类型强转.

## 7. @protocol 和 category 中如何使用 @property

1. 在 protocol 中使用 property 只会生成 setter 和 getter 方法声明,我们使用属性的目的,是希望遵守我协议的对象能实现该属性
2. category 使用 @property 也是只会生成 setter 和 getter 方法的声明,如果我们真的需要给 category 增加属性的实现,需要借助于运行时的两个函数：
	1. `objc_setAssociatedObject`
	2. `objc_getAssociatedObject`

## 8. runtime 如何实现 weak 属性

要实现 weak 属性，首先要搞清楚 weak 属性的特点：

> weak 此特质表明该属性定义了一种“非拥有关系” (nonowning relationship)。为这种属性设置新值时，设置方法既不保留新值，也不释放旧值。此特质同 assign 类似， 然而在属性所指的对象遭到摧毁时，属性值也会清空(nil out)。

那么 runtime 如何实现 weak 变量的自动置nil？

> runtime 对注册的类， 会进行布局，对于 weak 对象会放入一个 hash 表中。 用 weak 指向的对象内存地址作为 key，当此对象的引用计数为0的时候会 dealloc，假如 weak 指向的对象内存地址是a，那么就会以a为键， 在这个 weak 表中搜索，找到所有以a为键的 weak 对象，从而设置为 nil。

（注：在下文的《使用runtime Associate方法关联的对象，需要在主对象dealloc的时候释放么？》里给出的“对象的内存销毁时间表”也提到`__weak`引用的解除时间。）

我们可以设计一个函数（伪代码）来表示上述机制：

`objc_storeWeak(&a, b)`函数：

`objc_storeWeak`函数把第二个参数--赋值对象（b）的内存地址作为键值key，将第一个参数--weak修饰的属性变量（a）的内存地址（&a）作为value，注册到 weak 表中。如果第二个参数（b）为0（nil），那么把变量（a）的内存地址（&a）从weak表中删除，

你可以把`objc_storeWeak(&a, b)`理解为：`objc_storeWeak(value, key)`，并且当key变nil，将value置nil。

在b非nil时，a和b指向同一个内存地址，在b变nil时，a变nil。此时向a发送消息不会崩溃：在Objective-C中向nil发送消息是安全的。

而如果a是由 assign 修饰的，则：
在 b 非 nil 时，a 和 b 指向同一个内存地址，在 b 变 nil 时，a 还是指向该内存地址，变野指针。此时向 a 发送消息极易崩溃。

下面我们将基于`objc_storeWeak(&a, b)`函数，使用伪代码模拟“runtime如何实现weak属性”：

```objc
// 使用伪代码模拟：runtime如何实现weak属性
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong

id obj1;
objc_initWeak(&obj1, obj);
/*obj引用计数变为0，变量作用域结束*/
objc_destroyWeak(&obj1);
```

下面对用到的两个方法`objc_initWeak`和`objc_destroyWeak`做下解释：

总体说来，作用是：
通过`objc_initWeak`函数初始化“附有weak修饰符的变量（obj1）”，在变量作用域结束时通过`objc_destoryWeak`函数释放该变量（obj1）。

下面分别介绍下方法的内部实现：

`objc_initWeak`函数的实现是这样的：在将“附有weak修饰符的变量（obj1）”初始化为0（nil）后，会将“赋值对象”（obj）作为参数，调用`objc_storeWeak`函数。

```objc
obj1 = 0；
obj_storeWeak(&obj1, obj);
```

也就是说：

>  weak 修饰的指针默认值是 nil （在Objective-C中向nil发送消息是安全的）

然后`obj_destroyWeak`函数将0（nil）作为参数，调用`objc_storeWeak`函数。

`objc_storeWeak(&obj1, 0);`

前面的源代码与下列源代码相同。

```objc
// 使用伪代码模拟：runtime如何实现weak属性
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong

id obj1;
obj1 = 0;
objc_storeWeak(&obj1, obj);
/* ... obj的引用计数变为0，被置nil ... */
objc_storeWeak(&obj1, 0);
```

`objc_storeWeak` 函数把第二个参数--赋值对象（obj）的内存地址作为键值，将第一个参数--weak修饰的属性变量（obj1）的内存地址注册到 weak 表中。如果第二个参数（obj）为0（nil），那么把变量（obj1）的地址从 weak 表中删除，在后面的相关一题会详解。

使用伪代码是为了方便理解，下面我们“真枪实弹”地实现下：

> 如何让不使用weak修饰的@property，拥有weak的效果。

我们从setter方法入手：

```objc
- (void)setObject:(NSObject *)object
{
    objc_setAssociatedObject(self, "object", object, OBJC_ASSOCIATION_ASSIGN);
    [object cyl_runAtDealloc:^{
        _object = nil;
    }];
}
```

也就是有两个步骤：

1.在setter方法中做如下设置：

```objc
        objc_setAssociatedObject(self, "object", object, OBJC_ASSOCIATION_ASSIGN);
```

2.在属性所指的对象遭到摧毁时，属性值也会清空(nil out)。做到这点，同样要借助 runtime：

```objc
//要销毁的目标对象
id objectToBeDeallocated;
//可以理解为一个“事件”：当上面的目标对象销毁时，同时要发生的“事件”。
id objectWeWantToBeReleasedWhenThatHappens;
objc_setAssociatedObject(objectToBeDeallocted,
                         someUniqueKey,
                         objectWeWantToBeReleasedWhenThatHappens,
                         OBJC_ASSOCIATION_RETAIN);
```

知道了思路，我们就开始实现 `cyl_runAtDealloc` 方法，实现过程分两部分：

第一部分：创建一个类，可以理解为一个“事件”：当目标对象销毁时，同时要发生的“事件”。借助 block 执行“事件”。

// .h文件

```objc
// .h文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 这个类，可以理解为一个“事件”：当目标对象销毁时，同时要发生的“事件”。借助block执行“事件”。

typedef void (^voidBlock)(void);

@interface CYLBlockExecutor : NSObject

- (id)initWithBlock:(voidBlock)block;

@end
```

// .m文件

```objc
// .m文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 这个类，可以理解为一个“事件”：当目标对象销毁时，同时要发生的“事件”。借助block执行“事件”。

#import "CYLBlockExecutor.h"

@interface CYLBlockExecutor() {
    voidBlock _block;
}
@implementation CYLBlockExecutor

- (id)initWithBlock:(voidBlock)aBlock
{
    self = [super init];

    if (self) {
        _block = [aBlock copy];
    }

    return self;
}

- (void)dealloc
{
    _block ? _block() : nil;
}

@end
```

第二部分：核心代码：利用runtime实现`cyl_runAtDealloc`方法

```objc
// CYLNSObject+RunAtDealloc.h文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 利用runtime实现cyl_runAtDealloc方法

#import "CYLBlockExecutor.h"

const void *runAtDeallocBlockKey = &runAtDeallocBlockKey;

@interface NSObject (CYLRunAtDealloc)

- (void)cyl_runAtDealloc:(voidBlock)block;

@end


// CYLNSObject+RunAtDealloc.m文件
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong
// 利用runtime实现cyl_runAtDealloc方法

#import "CYLNSObject+RunAtDealloc.h"
#import "CYLBlockExecutor.h"

@implementation NSObject (CYLRunAtDealloc)

- (void)cyl_runAtDealloc:(voidBlock)block
{
    if (block) {
        CYLBlockExecutor *executor = [[CYLBlockExecutor alloc] initWithBlock:block];

        objc_setAssociatedObject(self,
                                 runAtDeallocBlockKey,
                                 executor,
                                 OBJC_ASSOCIATION_RETAIN);
    }
}

@end
```

使用方法：

导入

```objc
#import "CYLNSObject+RunAtDealloc.h"
```

然后就可以使用了：

```objc
NSObject *foo = [[NSObject alloc] init];

[foo cyl_runAtDealloc:^{
    NSLog(@"正在释放foo!");
}];
```

如果对 `cyl_runAtDealloc` 的实现原理有兴趣，可以看下这篇博文 [***Fun With the Objective-C Runtime: Run Code at Deallocation of Any Object***](http://stackoverflow.com/a/31560217/3395008)


## 9. @property中有哪些属性关键字？/ @property 后面可以有哪些修饰符？

属性可以拥有的特质分为四类:

1. 原子性 - `nonatomic` 特质
	+ 在默认情况下，由编译器合成的方法会通过锁定机制确保其原子性(atomicity)。如果属性具备 nonatomic 特质，则不使用同步锁。请注意，尽管没有名为“atomic”的特质(如果某属性不具备 nonatomic 特质，那它就是“原子的” ( atomic) )，但是仍然可以在属性特质中写明这一点，编译器不会报错。若是自己定义存取方法，那么就应该遵从与属性特质相符的原子性。
2. 读/写权限 - `readwrite(读写)`、`readonly (只读)`
3. 内存管理语义 - `assign`、`strong`、 `weak`、`unsafe_unretained`、`copy`
4. 方法名 - `getter=<name>` 、`setter=<name>`

`getter=<name>`的样式：

```objc
@property (nonatomic, getter=isOn) BOOL on;
```

`setter=<name>`一般用在特殊的情境下，比如：

在数据反序列化、转模型的过程中，服务器返回的字段如果以 `init` 开头，所以你需要定义一个 `init` 开头的属性，但默认生成的 `setter` 与 `getter` 方法也会以 `init` 开头，而编译器会把所有以 `init` 开头的方法当成初始化方法，而初始化方法只能返回 self 类型，因此编译器会报错。

这时你就可以使用下面的方式来避免编译器报错：

```objc
@property(nonatomic, strong, getter=p_initBy, setter=setP_initBy:)NSString *initBy;
```

另外也可以用关键字进行特殊说明，来避免编译器报错：

```objc
@property(nonatomic, readwrite, copy, null_resettable) NSString *initBy;
- (NSString *)initBy __attribute__((objc_method_family(none)));
```

> 不常用的：`nonnull`,`null_resettable`,`nullable`

## 10. weak属性需要在dealloc中置nil么？

不需要。

> 在ARC环境无论是强指针还是弱指针都无需在 dealloc 设置为 nil ， ARC 会自动帮我们处理

即便是编译器不帮我们做这些，weak也不需要在 dealloc 中置nil：

正如上文的：***runtime 如何实现 weak 属性*** 中提到的：

我们模拟下 weak 的 setter 方法，应该如下：

```objc
- (void)setObject:(NSObject *)object
{
    objc_setAssociatedObject(self, "object", object, OBJC_ASSOCIATION_ASSIGN);
    [object cyl_runAtDealloc:^{
        _object = nil;
    }];
}
```

也即:

> 在属性所指的对象遭到摧毁时，属性值也会清空(nil out)。


## 11. @synthesize和@dynamic分别有什么作用？

1. @property有两个对应的词，一个是 @synthesize，一个是 @dynamic。如果 @synthesize和 @dynamic都没写，那么默认的就是`@syntheszie var = _var;`
2. @synthesize 的语义是如果你没有手动实现 setter 方法和 getter 方法，那么编译器会自动为你加上这两个方法。
3. @dynamic 告诉编译器：属性的 setter 与 getter 方法由用户自己实现，不自动生成。（当然对于 readonly 的属性只需提供 getter 即可）。假如一个属性被声明为 @dynamic var，然后你没有提供 @setter方法和 @getter 方法，编译的时候没问题，但是当程序运行到 `instance.var = someVar`，由于缺 setter 方法会导致程序崩溃；或者当运行到 `someVar = var` 时，由于缺 getter 方法同样会导致崩溃。编译时没问题，运行时才执行相应的方法，这就是所谓的动态绑定。

## 12. ARC下，不显式指定任何属性关键字时，默认的关键字都有哪些？

1. 对应基本数据类型默认关键字是
	+ atomic,readwrite,assign
2. 对于普通的 Objective-C 对象
	+ atomic,readwrite,strong

参考链接：

1. [ ***Objective-C ARC: strong vs retain and weak vs assign*** ](http://stackoverflow.com/a/15541801/3395008)
2. [ ***Variable property attributes or Modifiers in iOS*** ](http://rdcworld-iphone.blogspot.in/2012/12/variable-property-attributes-or.html)

## 13. 用@property声明的NSString（或NSArray，NSDictionary）经常使用copy关键字，为什么？如果改用strong关键字，可能造成什么问题？

1. 因为父类指针可以指向子类对象,使用 copy 的目的是为了让本对象的属性不受外界影响,使用 copy 无论给我传入是一个可变对象还是不可对象,我本身持有的就是一个不可变的副本.
2. 如果我们使用是 strong ,那么这个属性就有可能指向一个可变对象,如果这个可变对象在外部被修改了,那么会影响该属性.

copy 此特质所表达的所属关系与 strong 类似。然而设置方法并不保留新值，而是将其“拷贝” (copy)。

当属性类型为 NSString 时，经常用此特质来保护其封装性，因为传递给设置方法的新值有可能指向一个 NSMutableString 类的实例。这个类是 NSString 的子类，表示一种可修改其值的字符串，此时若是不拷贝字符串，那么设置完属性之后，字符串的值就可能会在对象不知情的情况下遭人更改。所以，这时就要拷贝一份“不可变” (immutable)的字符串，确保对象中的字符串值不会无意间变动。只要实现属性所用的对象是“可变的” (mutable)，就应该在设置新属性值时拷贝一份。

举例说明：

定义一个以 strong 修饰的 array：

```objc
@property (nonatomic ,readwrite, strong) NSArray *array;
```

然后进行下面的操作：

```objc
NSMutableArray *mutableArray = [[NSMutableArray alloc] init];
NSArray *array = @[ @1, @2, @3, @4 ];
self.array = mutableArray;
[mutableArray removeAllObjects];;
NSLog(@"%@",self.array);

[mutableArray addObjectsFromArray:array];
self.array = [mutableArray copy];
[mutableArray removeAllObjects];;
NSLog(@"%@",self.array);
```

打印结果如下所示：

```objc
2015-09-27 19:10:32.523 CYLArrayCopyDmo[10681:713670] (
)
2015-09-27 19:10:32.524 CYLArrayCopyDmo[10681:713670] (
    1,
    2,
    3,
    4
)
```

为了理解这种做法，首先要知道，两种情况：

1. 对非集合类对象的 copy 与 mutableCopy 操作；
2. 对集合类对象的 copy 与 mutableCopy 操作。

### 1. 对非集合类对象的copy操作：

在非集合类对象中：对 immutable 对象进行 copy 操作，是指针复制，mutableCopy 操作时内容复制；对 mutable 对象进行 copy 和 mutableCopy 都是内容复制。用代码简单表示如下：


- [immutableObject copy] // 浅复制
- [immutableObject mutableCopy] //深复制
- [mutableObject copy] //深复制
- [mutableObject mutableCopy] //深复制


比如以下代码：

```objc
NSMutableString *string = [NSMutableString stringWithString:@"origin"];//copy
NSString *stringCopy = [string copy];
```

查看内存，会发现 string、stringCopy 内存地址都不一样，说明此时都是做内容拷贝、深拷贝。即使你进行如下操作：

```objc
[string appendString:@"origion!"]
```

stringCopy 的值也不会因此改变，但是如果不使用 copy，stringCopy 的值就会被改变。集合类对象以此类推。

所以，

> 用 @property 声明 NSString、NSArray、NSDictionary 经常使用 copy 关键字，是因为他们有对应的可变类型：NSMutableString、NSMutableArray、NSMutableDictionary，他们之间可能进行赋值操作，为确保对象中的字符串值不会无意间变动，应该在设置新属性值时拷贝一份。

### 2、集合类对象的copy与mutableCopy

集合类对象是指 NSArray、NSDictionary、NSSet ... 之类的对象。下面先看集合类immutable对象使用 copy 和 mutableCopy 的一个例子：

```objc
NSArray *array = @[@[@"a", @"b"], @[@"c", @"d"]];
NSArray *copyArray = [array copy];
NSMutableArray *mCopyArray = [array mutableCopy];
```

查看内容，可以看到 copyArray 和 array 的地址是一样的，而 mCopyArray 和 array 的地址是不同的。说明 copy 操作进行了指针拷贝，mutableCopy 进行了内容拷贝。但需要强调的是：此处的内容拷贝，仅仅是拷贝 array 这个对象，array 集合内部的元素仍然是指针拷贝。这和上面的非集合 immutable 对象的拷贝还是挺相似的，那么mutable对象的拷贝会不会类似呢？我们继续往下，看 mutable 对象拷贝的例子：

```objc
NSMutableArray *array = [NSMutableArray arrayWithObjects:[NSMutableString stringWithString:@"a"],@"b",@"c",nil];
NSArray *copyArray = [array copy];
NSMutableArray *mCopyArray = [array mutableCopy];
```

查看内存，如我们所料，copyArray、mCopyArray和 array 的内存地址都不一样，说明 copyArray、mCopyArray 都对 array 进行了内容拷贝。同样，我们可以得出结论：

在集合类对象中，对 immutable 对象进行 copy，是指针复制， mutableCopy 是内容复制；对 mutable 对象进行 copy 和 mutableCopy 都是内容复制。但是：集合对象的内容复制仅限于对象本身，对象元素仍然是指针复制。用代码简单表示如下：


```objc
[immutableObject copy] // 浅复制
[immutableObject mutableCopy] //单层深复制
[mutableObject copy] //单层深复制
[mutableObject mutableCopy] //单层深复制
```

这个代码结论和非集合类的非常相似。

参考链接：[iOS 集合的深复制与浅复制](https://www.zybuluo.com/MicroCai/note/50592)

## 14. @synthesize合成实例变量的规则是什么？假如property名为foo，存在一个名为`_foo`的实例变量，那么还会自动合成新变量么？

在回答之前先说明下一个概念：

> 实例变量 = 成员变量 ＝ ivar

这些说法，笔者下文中，可能都会用到，指的是一个东西。

正如
[Apple官方文档 ***You Can Customize Synthesized Instance Variable Names***](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/EncapsulatingData/EncapsulatingData.html#//apple_ref/doc/uid/TP40011210-CH5-SW6) 所说：
![enter image description here](http://i.imgur.com/D6d0zGJ.png)

如果使用了属性的话，那么编译器就会自动编写访问属性所需的方法，此过程叫做“自动合成”( auto synthesis)。需要强调的是，这个过程由编译器在编译期执行，所以编辑器里看不到这些“合成方法” (synthesized method)的源代码。除了生成方法代码之外，编译器还要自动向类中添加适当类型的实例变量，并且在属性名前面加下划线，以此作为实例变量的名字。

```objc
@interface CYLPerson : NSObject
@property NSString *firstName;
@property NSString *lastName;
@end
```

在上例中，会生成两个实例变量，其名称分别为
 `_firstName` 与 `_lastName`。也可以在类的实现代码里通过 `@synthesize` 语法来指定实例变量的名字:

```objc
@implementation CYLPerson
@synthesize firstName = _myFirstName;
@synthesize lastName = _myLastName;
@end
```

上述语法会将生成的实例变量命名为 `_myFirstName` 与 `_myLastName` ，而不再使用默认的名字。一般情况下无须修改默认的实例变量名，但是如果你不喜欢以下划线来命名实例变量，那么可以用这个办法将其改为自己想要的名字。笔者还是推荐使用默认的命名方案，因为如果所有人都坚持这套方案，那么写出来的代码大家都能看得懂。

总结下 @synthesize 合成实例变量的规则，有以下几点：

1. 如果指定了成员变量的名称,会生成一个指定的名称的成员变量,
2. 如果这个成员已经存在了就不再生成了.
3. 如果是 `@synthesize foo;` 还会生成一个名称为foo的成员变量，也就是说：如果没有指定成员变量的名称会自动生成一个属性同名的成员变量,
4. 如果是 `@synthesize foo = _foo;` 就不会生成成员变量了.

假如 property 名为 foo，存在一个名为 `_foo` 的实例变量，那么还会自动合成新变量么？
不会。如下图：

![enter image description here](http://i.imgur.com/t28ge4W.png)


## 15. 在有了自动合成属性实例变量之后，@synthesize还有哪些使用场景？

回答这个问题前，我们要搞清楚一个问题，什么情况下不会autosynthesis（自动合成）？

1. 同时重写了 setter 和 getter 时
2. 重写了只读属性的 getter 时
3. 使用了 @dynamic 时
4. 在 @protocol 中定义的所有属性
5. 在 category 中定义的所有属性
6. 重载的属性

你在子类中重载了父类中的属性，你必须 使用 `@synthesize` 来手动合成ivar。

除了后三条，对其他几个我们可以总结出一个规律：当你想手动管理 @property 的所有内容时，你就会尝试通过实现 @property 的所有“存取方法”（the accessor methods）或者使用 `@dynamic` 来达到这个目的，这时编译器就会认为你打算手动管理 @property，于是编译器就禁用了 autosynthesis（自动合成）。

因为有了 autosynthesis（自动合成），大部分开发者已经习惯不去手动定义ivar，而是依赖于 autosynthesis（自动合成），但是一旦你需要使用ivar，而 autosynthesis（自动合成）又失效了，如果不去手动定义ivar，那么你就得借助 `@synthesize` 来手动合成 ivar。

其实，`@synthesize` 语法还有一个应用场景，但是不太建议大家使用：

可以在类的实现代码里通过 `@synthesize` 语法来指定实例变量的名字:

```objc
@implementation CYLPerson
@synthesize firstName = _myFirstName;
@synthesize lastName = _myLastName;
@end
```

上述语法会将生成的实例变量命名为 `_myFirstName` 与 `_myLastName`，而不再使用默认的名字。一般情况下无须修改默认的实例变量名，但是如果你不喜欢以下划线来命名实例变量，那么可以用这个办法将其改为自己想要的名字。笔者还是推荐使用默认的命名方案，因为如果所有人都坚持这套方案，那么写出来的代码大家都能看得懂。

举例说明：应用场景：


```objc
//
// .m文件
// http://weibo.com/luohanchenyilong/ (微博@iOS程序犭袁)
// https://github.com/ChenYilong
// 打开第14行和第17行中任意一行，就可编译成功

@import Foundation;

@interface CYLObject : NSObject
@property (nonatomic, copy) NSString *title;
@end

@implementation CYLObject {
    //    NSString *_title;
}

//@synthesize title = _title;

- (instancetype)init
{
    self = [super init];
    if (self) {
        _title = @"微博@iOS程序犭袁";
    }
    return self;
}

- (NSString *)title {
    return _title;
}

- (void)setTitle:(NSString *)title {
    _title = [title copy];
}

@end
```

结果编译器报错：

![enter image description here](http://i.imgur.com/fAEGHIo.png)

当你同时重写了 setter 和 getter 时，系统就不会生成 ivar（实例变量/成员变量）。这时候有两种选择：

1. 要么如第14行：手动创建 ivar
2. 要么如第17行：使用`@synthesize foo = _foo;` ，关联 @property 与 ivar。

更多信息，请戳- 》[ ***When should I use @synthesize explicitly?*** ](http://stackoverflow.com/a/19821816/3395008)

## 16. objc中向一个nil对象发送消息将会发生什么？

在 Objective-C 中向 nil 发送消息是完全有效的——只是在运行时不会有任何作用:

1.如果一个方法返回值是一个对象，那么发送给nil的消息将返回0(nil)。例如：

```objc
Person * motherInlaw = [[aPerson spouse] mother];
```

如果 spouse 对象为 nil，那么发送给 nil 的消息 mother 也将返回 nil。

2.如果方法返回值为指针类型，其指针大小为小于或者等于sizeof(void*)，float，double，long double 或者 long long 的整型标量，发送给 nil 的消息将返回0。

3.如果方法返回值为结构体,发送给 nil 的消息将返回0。结构体中各个字段的值将都是0。

4.如果方法的返回值不是上述提到的几种情况，那么发送给 nil 的消息的返回值将是未定义的。

具体原因如下：

> objc是动态语言，每个方法在运行时会被动态转为消息发送，即：objc_msgSend(receiver, selector)。

那么，为了方便理解这个内容，还是贴一个objc的源代码：

```objc
// runtime.h（类在runtime中的定义）
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong

struct objc_class {
  Class isa OBJC_ISA_AVAILABILITY; //isa指针指向Meta Class，因为Objc的类的本身也是一个Object，为了处理这个关系，runtime就创造了Meta Class，当给类发送[NSObject alloc]这样消息时，实际上是把这个消息发给了Class Object
  #if !__OBJC2__
  Class super_class OBJC2_UNAVAILABLE; // 父类
  const char *name OBJC2_UNAVAILABLE; // 类名
  long version OBJC2_UNAVAILABLE; // 类的版本信息，默认为0
  long info OBJC2_UNAVAILABLE; // 类信息，供运行期使用的一些位标识
  long instance_size OBJC2_UNAVAILABLE; // 该类的实例变量大小
  struct objc_ivar_list *ivars OBJC2_UNAVAILABLE; // 该类的成员变量链表
  struct objc_method_list **methodLists OBJC2_UNAVAILABLE; // 方法定义的链表
  struct objc_cache *cache OBJC2_UNAVAILABLE; // 方法缓存，对象接到一个消息会根据isa指针查找消息对象，这时会在method Lists中遍历，如果cache了，常用的方法调用时就能够提高调用的效率。
  struct objc_protocol_list *protocols OBJC2_UNAVAILABLE; // 协议链表
  #endif
  } OBJC2_UNAVAILABLE;
```
objc在向一个对象发送消息时，runtime库会根据对象的isa指针找到该对象实际所属的类，然后在该类中的方法列表以及其父类方法列表中寻找方法运行，然后在发送消息的时候，objc_msgSend方法不会返回值，所谓的返回内容都是具体调用时执行的。

那么，回到本题，如果向一个nil对象发送消息，首先在寻找对象的isa指针时就是0地址返回了，所以不会出现任何错误。

## 17. objc中向一个对象发送消息和函数之间有什么关系？

即 `[obj foo]`和`objc_msgSend()`

具体原因同上题：该方法编译之后就是`objc_msgSend()`函数调用.

我们用 clang 分析下，clang 提供一个命令，可以将Objective-C的源码改写成C++语言，借此可以研究下`[obj foo]`和`objc_msgSend()`函数之间有什么关系。

以下面的代码为例，由于 clang 后的代码达到了10万多行，为了便于区分，添加了一个叫 iOSinit 方法，

```objc
//
//  main.m
//  http://weibo.com/luohanchenyilong/
//  https://github.com/ChenYilong
//

#import "CYLTest.h"

int main(int argc, char * argv[]) {
    @autoreleasepool {
        CYLTest *test = [[CYLTest alloc] init];
        [test performSelector:(@selector(iOSinit))];
        return 0;
    }
}
```

在终端中输入

```objc
clang -rewrite-objc main.m
```
就可以生成一个`main.cpp`的文件，在最低端（10万4千行左右）

![enter image description here](http://i.imgur.com/eAH5YWn.png)

我们可以看到大概是这样的：

```objc
((void ()(id, SEL))(void )objc_msgSend)((id)obj, sel_registerName("foo"));
```

也就是说：

> [obj foo];在objc动态编译时，会被转意为：`objc_msgSend(obj, @selector(foo));`。

## 18. 什么时候会报 unrecognized selector 的异常？

简单来说：

> 当调用该对象上某个方法,而该对象上没有实现这个方法的时候，
可以通过“消息转发”进行解决。

简单的流程如下，在上一题中也提到过：

> objc是动态语言，每个方法在运行时会被动态转为消息发送，即：objc_msgSend(receiver, selector)。

objc在向一个对象发送消息时，runtime库会根据对象的isa指针找到该对象实际所属的类，然后在该类中的方法列表以及其父类方法列表中寻找方法运行，如果，在最顶层的父类中依然找不到相应的方法时，程序在运行时会挂掉并抛出异常unrecognized selector sent to XXX 。但是在这之前，objc的运行时会给出三次拯救程序崩溃的机会：

1. Method resolution
	+ objc运行时会调用`+resolveInstanceMethod:`或者 `+resolveClassMethod:`，让你有机会提供一个函数实现。如果你添加了函数，那运行时系统就会重新启动一次消息发送的过程，否则 ，运行时就会移到下一步，消息转发（Message Forwarding）。
2. Fast forwarding
	+ 如果目标对象实现了`-forwardingTargetForSelector:`，Runtime 这时就会调用这个方法，给你把这个消息转发给其他对象的机会。
	+ 只要这个方法返回的不是nil和self，整个消息发送的过程就会被重启，当然发送的对象会变成你返回的那个对象。否则，就会继续Normal Fowarding。
	+ 这里叫Fast，只是为了区别下一步的转发机制。因为这一步不会创建任何新的对象，但下一步转发会创建一个NSInvocation对象，所以相对更快点。
3. Normal forwarding
	+ 这一步是Runtime最后一次给你挽救的机会。首先它会发送`-methodSignatureForSelector:`消息获得函数的参数和返回值类型。如果`-methodSignatureForSelector:`返回nil，Runtime则会发出`-doesNotRecognizeSelector:`消息，程序这时也就挂掉了。如果返回了一个函数签名，Runtime就会创建一个NSInvocation对象并发送`-forwardInvocation:`消息给目标对象。

## 19. 一个objc对象如何进行内存布局？（考虑有父类的情况）

- 所有父类的成员变量和自己的成员变量都会存放在该对象所对应的存储空间中.
- 每一个对象内部都有一个isa指针,指向他的类对象,类对象中存放着本对象的
	1. 对象方法列表（对象能够接收的消息列表，保存在它所对应的类对象中）
	2. 成员变量的列表,
	3. 属性列表,

它内部也有一个isa指针指向元对象(meta class),元对象内部存放的是类方法列表,类对象内部还有一个superclass的指针,指向他的父类对象。

每个 Objective-C 对象都有相同的结构，如下图所示：

![enter image description here](http://i.imgur.com/7mJlUj1.png)

翻译过来就是

|  Objective-C 对象的结构图 |
 ------------- |
 ISA指针 |
 根类的实例变量 |
 倒数第二层父类的实例变量 |
 ... |
 父类的实例变量 |
 类的实例变量 |

- 根对象就是NSobject，它的superclass指针指向nil
- 类对象既然称为对象，那它也是一个实例。类对象中也有一个isa指针指向它的元类(meta class)，即类对象是元类的实例。元类内部存放的是类方法列表，根元类的isa指针指向自己，superclass指针指向NSObject类。

如图:
![enter image description here](http://i.imgur.com/w6tzFxz.png)

## 20. 一个objc对象的isa的指针指向什么？有什么作用？

指向他的类对象,从而可以找到对象上的方法

## 21. 下面的代码输出什么？

```objc
@implementation Son : Father
- (id)init
{
    self = [super init];
    if (self) {
        NSLog(@"%@", NSStringFromClass([self class]));
        NSLog(@"%@", NSStringFromClass([super class]));
    }
    return self;
}
@end
```


**答案：**

都输出 Son

```objc
NSStringFromClass([self class]) = Son
NSStringFromClass([super class]) = Son
```

这个题目主要是考察关于 Objective-C 中对 self 和 super 的理解。

我们都知道：self 是类的隐藏参数，指向当前调用方法的这个类的实例。那 super 呢？

很多人会想当然的认为“ super 和 self 类似，应该是指向父类的指针吧！”。这是很普遍的一个误区。其实 super 是一个 Magic Keyword， 它本质是一个编译器标示符，和 self 是指向的同一个消息接受者！他们两个的不同点在于：super 会告诉编译器，调用 class 这个方法时，要去父类的方法，而不是本类里的。

上面的例子不管调用`[self class]`还是`[super class]`，接受消息的对象都是当前 `Son ＊xxx` 这个对象。

当使用 self 调用方法时，会从当前类的方法列表中开始找，如果没有，就从父类中再找；而当使用 super 时，则从父类的方法列表中开始找。然后调用父类的这个方法。

这也就是为什么说“不推荐在 init 方法中使用点语法”，如果想访问实例变量 iVar 应该使用下划线（ `_iVar` ），而非点语法（ `self.iVar` ）。

点语法（ `self.iVar` ）的坏处就是子类有可能覆写 setter 。假设 Person 有一个子类叫 ChenPerson，这个子类专门表示那些姓“陈”的人。该子类可能会覆写 lastName 属性所对应的设置方法：

```objc
//
//  ChenPerson.m
//
//
//  Created by https://github.com/ChenYilong on 15/8/30.
//  Copyright (c) 2015年 http://weibo.com/luohanchenyilong/ 微博@iOS程序犭袁. All rights reserved.
//

#import "ChenPerson.h"

@implementation ChenPerson

@synthesize lastName = _lastName;

- (instancetype)init
{
    self = [super init];
    if (self) {
        NSLog(@"🔴类名与方法名：%s（在第%d行），描述：%@", __PRETTY_FUNCTION__, __LINE__, NSStringFromClass([self class]));
        NSLog(@"🔴类名与方法名：%s（在第%d行），描述：%@", __PRETTY_FUNCTION__, __LINE__, NSStringFromClass([super class]));
    }
    return self;
}

- (void)setLastName:(NSString*)lastName
{
    //设置方法一：如果setter采用是这种方式，就可能引起崩溃
//    if (![lastName isEqualToString:@"陈"])
//    {
//        [NSException raise:NSInvalidArgumentException format:@"姓不是陈"];
//    }
//    _lastName = lastName;

    //设置方法二：如果setter采用是这种方式，就可能引起崩溃
    _lastName = @"陈";
    NSLog(@"🔴类名与方法名：%s（在第%d行），描述：%@", __PRETTY_FUNCTION__, __LINE__, @"会调用这个方法,想一下为什么？");

}

@end
```

在基类 Person 的默认初始化方法中，可能会将姓氏设为空字符串。此时若使用点语法（ `self.lastName` ）也即 setter 设置方法，那么调用将会是子类的设置方法，如果在刚刚的 setter 代码中采用设置方法一，那么就会抛出异常


为了方便采用打印的方式展示，究竟发生了什么，我们使用设置方法二。

如果基类的代码是这样的：


```objc
//
//  Person.m
//  nil对象调用点语法
//
//  Created by https://github.com/ChenYilong on 15/8/29.
//  Copyright (c) 2015年 http://weibo.com/luohanchenyilong/ 微博@iOS程序犭袁. All rights reserved.
//

#import "Person.h"

@implementation Person

- (instancetype)init
{
    self = [super init];
    if (self) {
        self.lastName = @"";
        //NSLog(@"🔴类名与方法名：%s（在第%d行），描述：%@", __PRETTY_FUNCTION__, __LINE__, NSStringFromClass([self class]));
        //NSLog(@"🔴类名与方法名：%s（在第%d行），描述：%@", __PRETTY_FUNCTION__, __LINE__, self.lastName);
    }
    return self;
}

- (void)setLastName:(NSString*)lastName
{
    NSLog(@"🔴类名与方法名：%s（在第%d行），描述：%@", __PRETTY_FUNCTION__, __LINE__, @"根本不会调用这个方法");
    _lastName = @"炎黄";
}

@end
```

那么打印结果将会是这样的：

```objc
🔴类名与方法名：-[ChenPerson setLastName:]（在第36行），描述：会调用这个方法,想一下为什么？
🔴类名与方法名：-[ChenPerson init]（在第19行），描述：ChenPerson
🔴类名与方法名：-[ChenPerson init]（在第20行），描述：ChenPerson
```

我在仓库里也给出了一个相应的 Demo（名字叫：Demo_21题_下面的代码输出什么）。有兴趣可以跑起来看一下，主要看下他是怎么打印的，思考下为什么这么打印。

接下来让我们利用 runtime 的相关知识来验证一下 super 关键字的本质，使用clang重写命令:

```objc
$ clang -rewrite-objc test.m
```

将这道题目中给出的代码被转化为:

```objc
NSLog((NSString *)&__NSConstantStringImpl__var_folders_gm_0jk35cwn1d3326x0061qym280000gn_T_main_a5cecc_mi_0, NSStringFromClass(((Class (*)(id, SEL))(void *)objc_msgSend)((id)self, sel_registerName("class"))));

NSLog((NSString *)&__NSConstantStringImpl__var_folders_gm_0jk35cwn1d3326x0061qym280000gn_T_main_a5cecc_mi_1, NSStringFromClass(((Class (*)(__rw_objc_super *, SEL))(void *)objc_msgSendSuper)((__rw_objc_super){ (id)self, (id)class_getSuperclass(objc_getClass("Son")) }, sel_registerName("class"))));
```

从上面的代码中，我们可以发现在调用 [self class] 时，会转化成 `objc_msgSend`函数。看下函数定义：

```objc
id objc_msgSend(id self, SEL op, ...)
```

我们把 self 做为第一个参数传递进去。

而在调用 [super class]时，会转化成 `objc_msgSendSuper`函数。看下函数定义:

```objc
id objc_msgSendSuper(struct objc_super *super, SEL op, ...)
```

第一个参数是 `objc_super` 这样一个结构体，其定义如下:

```objc
struct objc_super {
	   __unsafe_unretained id receiver;
	   __unsafe_unretained Class super_class;
};
```

结构体有两个成员，第一个成员是 receiver, 类似于上面的 `objc_msgSend`函数第一个参数self 。第二个成员是记录当前类的父类是什么。

所以，当调用 ［self class] 时，实际先调用的是 `objc_msgSend`函数，第一个参数是 Son当前的这个实例，然后在 Son 这个类里面去找 - (Class)class这个方法，没有，去父类 Father里找，也没有，最后在 NSObject类中发现这个方法。而 - (Class)class的实现就是返回self的类别，故上述输出结果为 Son。

objc Runtime开源代码对- (Class)class方法的实现:

```objc
- (Class)class {
    return object_getClass(self);
}
```

而当调用 `[super class]`时，会转换成`objc_msgSendSuper函数`。第一步先构造 `objc_super` 结构体，结构体第一个成员就是 `self` 。

第二个成员是 `(id)class_getSuperclass(objc_getClass(“Son”))` , 实际该函数输出结果为 Father。

第二步是去 Father这个类里去找 `- (Class)class`，没有，然后去NSObject类去找，找到了。最后内部是使用 `objc_msgSend(objc_super->receiver, @selector(class))`去调用，

此时已经和`[self class]`调用相同了，故上述输出结果仍然返回 Son。

参考链接：[微博@Chun_iOS](http://weibo.com/junbbcom)的博文[刨根问底Objective－C Runtime（1）－ Self & Super](http://chun.tips/blog/2014/11/05/bao-gen-wen-di-objective%5Bnil%5Dc-runtime(1)%5Bnil%5D-self-and-super/)


## 22. runtime如何通过selector找到对应的IMP地址？（分别考虑类方法和实例方法）

每一个类对象中都一个方法列表,方法列表中记录着方法的名称,方法实现,以及参数类型,其实selector本质就是方法名称,通过这个方法名称就可以在方法列表中找到对应的方法实现.

## 23. 使用runtime Associate方法关联的对象，需要在主对象dealloc的时候释放么？

> 无论在MRC下还是ARC下均不需要。


[ ***2011年版本的Apple API 官方文档 - Associative References***  ](https://web.archive.org/web/20120818164935/http://developer.apple.com/library/ios/#/web/20120820002100/http://developer.apple.com/library/ios/documentation/cocoa/conceptual/objectivec/Chapters/ocAssociativeReferences.html) 一节中有一个MRC环境下的例子：

```objc
// 在MRC下，使用runtime Associate方法关联的对象，不需要在主对象dealloc的时候释放
// http://weibo.com/luohanchenyilong/ (微博@iOS程序犭袁)
// https://github.com/ChenYilong
// 摘自2011年版本的Apple API 官方文档 - Associative References

static char overviewKey;

NSArray *array =
    [[NSArray alloc] initWithObjects:@"One", @"Two", @"Three", nil];
// For the purposes of illustration, use initWithFormat: to ensure
// the string can be deallocated
NSString *overview =
    [[NSString alloc] initWithFormat:@"%@", @"First three numbers"];

objc_setAssociatedObject (
    array,
    &overviewKey,
    overview,
    OBJC_ASSOCIATION_RETAIN
);

[overview release];
// (1) overview valid
[array release];
// (2) overview invalid
```

文档指出

> At point 1, the string `overview` is still valid because the `OBJC_ASSOCIATION_RETAIN` policy specifies that the array retains the associated object. When the array is deallocated, however (at point 2), `overview` is released and so in this case also deallocated.

我们可以看到，在`[array release];`之后，overview就会被release释放掉了。

既然会被销毁，那么具体在什么时间点？

> 根据[ ***WWDC 2011, Session 322 (第36分22秒)*** ](https://developer.apple.com/videos/wwdc/2011/#322-video)中发布的内存销毁时间表，被关联的对象在生命周期内要比对象本身释放的晚很多。它们会在被 NSObject -dealloc 调用的 object_dispose() 方法中释放。

对象的内存销毁时间表，分四个步骤：

	// 对象的内存销毁时间表
	// http://weibo.com/luohanchenyilong/ (微博@iOS程序犭袁)
	// https://github.com/ChenYilong
    // 根据 WWDC 2011, Session 322 (36分22秒)中发布的内存销毁时间表

     1. 调用 -release ：引用计数变为零
         * 对象正在被销毁，生命周期即将结束.
         * 不能再有新的 __weak 弱引用， 否则将指向 nil.
         * 调用 [self dealloc]
     2. 父类 调用 -dealloc
         * 继承关系中最底层的父类 在调用 -dealloc
         * 如果是 MRC 代码 则会手动释放实例变量们（iVars）
         * 继承关系中每一层的父类 都在调用 -dealloc
     3. NSObject 调 -dealloc
         * 只做一件事：调用 Objective-C runtime 中的 object_dispose() 方法
     4. 调用 object_dispose()
         * 为 C++ 的实例变量们（iVars）调用 destructors
         * 为 ARC 状态下的 实例变量们（iVars） 调用 -release
         * 解除所有使用 runtime Associate方法关联的对象
         * 解除所有 __weak 引用
         * 调用 free()

对象的内存销毁时间表：[参考链接](http://stackoverflow.com/a/10843510/3395008)。

## 24. objc中的类方法和实例方法有什么本质区别和联系？

类方法：

1. 类方法是属于类对象的
2. 类方法只能通过类对象调用
2. 类方法中的self是类对象
2. 类方法可以调用其他的类方法
2. 类方法中不能访问成员变量
2. 类方法中不定直接调用对象方法

实例方法：

1. 实例方法是属于实例对象的
2. 实例方法只能通过实例对象调用
2. 实例方法中的self是实例对象
2. 实例方法中可以访问成员变量
2. 实例方法中直接调用实例方法
2. 实例方法中也可以调用类方法(通过类名)


@property部分主要参考
[Apple官方文档：Properties Encapsulate an Object’s Values](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/EncapsulatingData/EncapsulatingData.html#//apple_ref/doc/uid/TP40011210-CH5-SW2)

runtime部分主要参考[Apple官方文档：Declared Properties](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtPropertyIntrospection.html)

## 25. `_objc_msgForward`函数是做什么的，直接调用它将会发生什么？

> `_objc_msgForward`是 IMP 类型，用于消息转发的：当向一个对象发送一条消息，但它并没有实现的时候，`_objc_msgForward`会尝试做消息转发。

我们可以这样创建一个`_objc_msgForward`对象：

    IMP msgForwardIMP = _objc_msgForward;

在“消息传递”过程中，`objc_msgSend`的动作比较清晰：首先在 Class 中的缓存查找 IMP （没缓存则初始化缓存），如果没找到，则向父类的 Class 查找。如果一直查找到根类仍旧没有实现，则用`_objc_msgForward`函数指针代替 IMP 。最后，执行这个 IMP 。

Objective-C运行时是开源的，所以我们可以看到它的实现。打开[ ***Apple Open Source 里Mac代码里的obj包*** ](http://www.opensource.apple.com/tarballs/objc4/)下载一个最新版本，找到 `objc-runtime-new.mm`，进入之后搜索`_objc_msgForward`。

![enter image description here](http://i.imgur.com/rGBfaoL.png)

里面有对`_objc_msgForward`的功能解释：

![enter image description here](http://i.imgur.com/vcThcdA.png)

```objc
/***********************************************************************
* lookUpImpOrForward.
* The standard IMP lookup.
* initialize==NO tries to avoid +initialize (but sometimes fails)
* cache==NO skips optimistic unlocked lookup (but uses cache elsewhere)
* Most callers should use initialize==YES and cache==YES.
* inst is an instance of cls or a subclass thereof, or nil if none is known.
*   If cls is an un-initialized metaclass then a non-nil inst is faster.
* May return _objc_msgForward_impcache. IMPs destined for external use
*   must be converted to _objc_msgForward or _objc_msgForward_stret.
*   If you don't want forwarding at all, use lookUpImpOrNil() instead.
**********************************************************************/
```

对 `objc-runtime-new.mm`文件里与`_objc_msgForward`有关的三个函数使用伪代码展示下：

```objc
//  objc-runtime-new.mm 文件里与 _objc_msgForward 有关的三个函数使用伪代码展示
//  Created by https://github.com/ChenYilong
//  Copyright (c)  微博@iOS程序犭袁(http://weibo.com/luohanchenyilong/). All rights reserved.
//  同时，这也是 obj_msgSend 的实现过程

id objc_msgSend(id self, SEL op, ...) {
    if (!self) return nil;
	IMP imp = class_getMethodImplementation(self->isa, SEL op);
	imp(self, op, ...); //调用这个函数，伪代码...
}

//查找IMP
IMP class_getMethodImplementation(Class cls, SEL sel) {
    if (!cls || !sel) return nil;
    IMP imp = lookUpImpOrNil(cls, sel);
    if (!imp) return _objc_msgForward; //_objc_msgForward 用于消息转发
    return imp;
}

IMP lookUpImpOrNil(Class cls, SEL sel) {
    if (!cls->initialize()) {
        _class_initialize(cls);
    }

    Class curClass = cls;
    IMP imp = nil;
    do { //先查缓存,缓存没有时重建,仍旧没有则向父类查询
        if (!curClass) break;
        if (!curClass->cache) fill_cache(cls, curClass);
        imp = cache_getImp(curClass, sel);
        if (imp) break;
    } while (curClass = curClass->superclass);

    return imp;
}
```

虽然Apple没有公开`_objc_msgForward`的实现源码，但是我们还是能得出结论：

> `_objc_msgForward`是一个函数指针（和 IMP 的类型一样），是用于消息转发的：当向一个对象发送一条消息，但它并没有实现的时候，`_objc_msgForward`会尝试做消息转发。

> 在“消息传递”过程中，`objc_msgSend`的动作比较清晰：首先在 Class 中的缓存查找 IMP （没缓存则初始化缓存），如果没找到，则向父类的 Class 查找。如果一直查找到根类仍旧没有实现，则用`_objc_msgForward`函数指针代替 IMP 。最后，执行这个 IMP 。

为了展示消息转发的具体动作，这里尝试向一个对象发送一条错误的消息，并查看一下`_objc_msgForward`是如何进行转发的。

首先开启调试模式、打印出所有运行时发送的消息：

可以在代码里执行下面的方法：

```objc
(void)instrumentObjcMessageSends(YES);
```

或者断点暂停程序运行，并在 gdb 中输入下面的命令：

```objc
call (void)instrumentObjcMessageSends(YES)
```

以第二种为例，操作如下所示：

![enter image description here](http://i.imgur.com/uEwTCC4.png)

之后，运行时发送的所有消息都会打印到`/tmp/msgSend-xxxx`文件里了。

终端中输入命令前往：

```objc
open /private/tmp
```

![enter image description here](http://i.imgur.com/Fh5hhCw.png)

可能看到有多条，找到最新生成的，双击打开

在模拟器上执行执行以下语句（这一套调试方案仅适用于模拟器，真机不可用，关于该调试方案的拓展链接：[ ***Can the messages sent to an object in Objective-C be monitored or printed out?*** ](http://stackoverflow.com/a/10750398/3395008)），向一个对象发送一条错误的消息：


```objc
//
//  main.m
//  CYLObjcMsgForwardTest
//
//  Created by http://weibo.com/luohanchenyilong/.
//  Copyright (c) 2015年 微博@iOS程序犭袁. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "AppDelegate.h"
#import "CYLTest.h"

int main(int argc, char * argv[]) {
    @autoreleasepool {
        CYLTest *test = [[CYLTest alloc] init];
        [test performSelector:(@selector(iOS程序犭袁))];
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
    }
}
```

![enter image description here](http://i.imgur.com/UjbmVvB.png)

你可以在`/tmp/msgSend-xxxx`（我这一次是`/tmp/msgSend-9805`）文件里，看到打印出来：

![enter image description here](http://i.imgur.com/AAERz1T.png)

```objc
+ CYLTest NSObject initialize
+ CYLTest NSObject alloc
- CYLTest NSObject init
- CYLTest NSObject performSelector:
+ CYLTest NSObject resolveInstanceMethod:
+ CYLTest NSObject resolveInstanceMethod:
- CYLTest NSObject forwardingTargetForSelector:
- CYLTest NSObject forwardingTargetForSelector:
- CYLTest NSObject methodSignatureForSelector:
- CYLTest NSObject methodSignatureForSelector:
- CYLTest NSObject class
- CYLTest NSObject doesNotRecognizeSelector:
- CYLTest NSObject doesNotRecognizeSelector:
- CYLTest NSObject class
```

结合[《NSObject官方文档》](https://developer.apple.com/library/prerelease/watchos/documentation/Cocoa/Reference/Foundation/Classes/NSObject_Class/#//apple_ref/doc/uid/20000050-SW11)，排除掉 NSObject 做的事，剩下的就是`_objc_msgForward`消息转发做的几件事：

1. 调用`resolveInstanceMethod:`方法 (或 `resolveClassMethod:`)。允许用户在此时为该 Class 动态添加实现。如果有实现了，则调用并返回YES，那么重新开始`objc_msgSend`流程。这一次对象会响应这个选择器，一般是因为它已经调用过`class_addMethod`。如果仍没实现，继续下面的动作。
2. 调用`forwardingTargetForSelector:`方法，尝试找到一个能响应该消息的对象。如果获取到，则直接把消息转发给它，返回非 nil 对象。否则返回 nil ，继续下面的动作。注意，这里不要返回 self ，否则会形成死循环。
3. 调用`methodSignatureForSelector:`方法，尝试获得一个方法签名。如果获取不到，则直接调用`doesNotRecognizeSelector`抛出异常。如果能获取，则返回非nil：创建一个 NSlnvocation 并传给`forwardInvocation:`。
4. 调用`forwardInvocation:`方法，将第3步获取到的方法签名包装成 Invocation 传入，如何处理就在这里面了，并返回非ni。
5. 调用`doesNotRecognizeSelector:` ，默认的实现是抛出异常。如果第3步没能获得一个方法签名，执行该步骤。

上面前4个方法均是模板方法，开发者可以override，由 runtime 来调用。最常见的实现消息转发：就是重写方法3和4，吞掉一个消息或者代理给其他对象都是没问题的

也就是说`_objc_msgForward`在进行消息转发的过程中会涉及以下这几个方法：

1. `resolveInstanceMethod:`方法 (或 `resolveClassMethod:`)。
2. `forwardingTargetForSelector:`方法
3. `methodSignatureForSelector:`方法
4. `forwardInvocation:`方法
5. `doesNotRecognizeSelector:` 方法

下面回答下第二个问题“直接`_objc_msgForward`调用它将会发生什么？”

直接调用`_objc_msgForward`是非常危险的事，如果用不好会直接导致程序Crash，但是如果用得好，能做很多非常酷的事。

就好像跑酷，干得好，叫“耍酷”，干不好就叫“作死”。

正如前文所说：

> `_objc_msgForward`是 IMP 类型，用于消息转发的：当向一个对象发送一条消息，但它并没有实现的时候，`_objc_msgForward`会尝试做消息转发。

如何调用`_objc_msgForward`？
`_objc_msgForward`隶属 C 语言，有三个参数 ：

|--| `_objc_msgForward`参数| 类型 |
-------------|-------------|-------------
 1. | 所属对象 | id类型
 2. |方法名 | SEL类型
 3. |可变参数 |可变参数类型

首先了解下如何调用 IMP 类型的方法，IMP类型是如下格式：

为了直观，我们可以通过如下方式定义一个 IMP类型 ：

```objc
typedef void (*voidIMP)(id, SEL, ...)
```

一旦调用`_objc_msgForward`，将跳过查找 IMP 的过程，直接触发“消息转发”，

如果调用了`_objc_msgForward`，即使这个对象确实已经实现了这个方法，你也会告诉`objc_msgSend`：

> “我没有在这个对象里找到这个方法的实现”

想象下`objc_msgSend`会怎么做？通常情况下，下面这张图就是你正常走`objc_msgSend`过程，和直接调用`_objc_msgForward`的前后差别：

有哪些场景需要直接调用`_objc_msgForward`？最常见的场景是：你想获取某方法所对应的`NSInvocation`对象。举例说明：

[JSPatch （Github 链接）](https://github.com/bang590/JSPatch)就是直接调用`_objc_msgForward`来实现其核心功能的：

>  JSPatch 以小巧的体积做到了让JS调用/替换任意OC方法，让iOS APP具备热更新的能力。

作者的博文[《JSPatch实现原理详解》](http://blog.cnbang.net/tech/2808/)详细记录了实现原理，有兴趣可以看下。

## 26. runtime如何实现weak变量的自动置nil？

> runtime 对注册的类， 会进行布局，对于 weak 对象会放入一个 hash 表中。 用 weak 指向的对象内存地址作为 key，当此对象的引用计数为0的时候会 dealloc，假如 weak 指向的对象内存地址是a，那么就会以a为键， 在这个 weak 表中搜索，找到所有以a为键的 weak 对象，从而设置为 nil。

我们可以设计一个函数（伪代码）来表示上述机制：

`objc_storeWeak(&a, b)`函数：

`objc_storeWeak`函数把第二个参数--赋值对象（b）的内存地址作为键值key，将第一个参数--weak修饰的属性变量（a）的内存地址（&a）作为value，注册到 weak 表中。如果第二个参数（b）为0（nil），那么把变量（a）的内存地址（&a）从weak表中删除，

你可以把`objc_storeWeak(&a, b)`理解为：`objc_storeWeak(value, key)`，并且当key变nil，将value置nil。

在b非nil时，a和b指向同一个内存地址，在b变nil时，a变nil。此时向a发送消息不会崩溃：在Objective-C中向nil发送消息是安全的。

而如果a是由assign修饰的，则：
在b非nil时，a和b指向同一个内存地址，在b变nil时，a还是指向该内存地址，变野指针。此时向a发送消息极易崩溃。

下面我们将基于`objc_storeWeak(&a, b)`函数，使用伪代码模拟“runtime如何实现weak属性”：


```objc
// 使用伪代码模拟：runtime如何实现weak属性
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong

id obj1;
objc_initWeak(&obj1, obj);
/*obj引用计数变为0，变量作用域结束*/
objc_destroyWeak(&obj1);
```

下面对用到的两个方法`objc_initWeak`和`objc_destroyWeak`做下解释：

总体说来，作用是：

通过`objc_initWeak`函数初始化“附有weak修饰符的变量（obj1）”，在变量作用域结束时通过`objc_destoryWeak`函数释放该变量（obj1）。

下面分别介绍下方法的内部实现：

`objc_initWeak`函数的实现是这样的：在将“附有weak修饰符的变量（obj1）”初始化为0（nil）后，会将“赋值对象”（obj）作为参数，调用`objc_storeWeak`函数。


```objc
obj1 = 0；
obj_storeWeak(&obj1, obj);
```

也就是说：

>  weak 修饰的指针默认值是 nil （在Objective-C中向nil发送消息是安全的）

然后`obj_destroyWeak`函数将0（nil）作为参数，调用`objc_storeWeak`函数。

`objc_storeWeak(&obj1, 0);`

前面的源代码与下列源代码相同。

```objc
// 使用伪代码模拟：runtime如何实现weak属性
// http://weibo.com/luohanchenyilong/
// https://github.com/ChenYilong

id obj1;
obj1 = 0;
objc_storeWeak(&obj1, obj);
/* ... obj的引用计数变为0，被置nil ... */
objc_storeWeak(&obj1, 0);
```

`objc_storeWeak`函数把第二个参数--赋值对象（obj）的内存地址作为键值，将第一个参数--weak修饰的属性变量（obj1）的内存地址注册到 weak 表中。如果第二个参数（obj）为0（nil），那么把变量（obj1）的地址从weak表中删除。

## 27. 能否向编译后得到的类中增加实例变量？能否向运行时创建的类中添加实例变量？为什么？

- 不能向编译后得到的类中增加实例变量；
- 能向运行时创建的类中添加实例变量；

解释下：

- 因为编译后的类已经注册在 runtime 中，类结构体中的 `objc_ivar_list` 实例变量的链表 和 `instance_size` 实例变量的内存大小已经确定，同时runtime 会调用 `class_setIvarLayout` 或 `class_setWeakIvarLayout` 来处理 strong weak 引用。所以不能向存在的类中添加实例变量；
- 运行时创建的类是可以添加实例变量，调用 `class_addIvar` 函数。但是得在调用 `objc_allocateClassPair` 之后，`objc_registerClassPair` 之前，原因同上。

## 28. runloop和线程有什么关系？

总的说来，Run loop，正如其名，loop表示某种循环，和run放在一起就表示一直在运行着的循环。实际上，run loop和线程是紧密相连的，可以这样说run loop是为了线程而生，没有线程，它就没有存在的必要。Run loops是线程的基础架构部分， Cocoa 和 CoreFundation 都提供了 run loop 对象方便配置和管理线程的 run loop （以下都以 Cocoa 为例）。每个线程，包括程序的主线程（ main thread ）都有与之相应的 run loop 对象。

runloop 和线程的关系：

1.主线程的run loop默认是启动的。

iOS的应用程序里面，程序启动后会有一个如下的main()函数

```objc
int main(int argc, char * argv[]) {
    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
    }
}
```

重点是UIApplicationMain()函数，这个方法会为main thread设置一个NSRunLoop对象，这就解释了：为什么我们的应用可以在无人操作的时候休息，需要让它干活的时候又能立马响应。

2.对其它线程来说，run loop默认是没有启动的，如果你需要更多的线程交互则可以手动配置和启动，如果线程只是去执行一个长时间的已确定的任务则不需要。

3.在任何一个 Cocoa 程序的线程中，都可以通过以下代码来获取到当前线程的 run loop 。

```objc
NSRunLoop *runloop = [NSRunLoop currentRunLoop];
```

参考链接：[《Objective-C之run loop详解》](http://blog.csdn.net/wzzvictory/article/details/9237973)。

## 29. runloop的mode作用是什么？

model 主要是用来指定事件在运行循环中的优先级的，分为：

* NSDefaultRunLoopMode（kCFRunLoopDefaultMode）：默认，空闲状态
* UITrackingRunLoopMode：ScrollView滑动时
* UIInitializationRunLoopMode：启动时
* NSRunLoopCommonModes（kCFRunLoopCommonModes）：Mode集合

苹果公开提供的 Mode 有两个：

1. NSDefaultRunLoopMode（kCFRunLoopDefaultMode）
2. NSRunLoopCommonModes（kCFRunLoopCommonModes）

## 30. 以+ scheduledTimerWithTimeInterval...的方式触发的timer，在滑动页面上的列表时，timer会暂定回调，为什么？如何解决？

RunLoop只能运行在一种mode下，如果要换mode，当前的loop也需要停下重启成新的。利用这个机制，ScrollView滚动过程中NSDefaultRunLoopMode（kCFRunLoopDefaultMode）的mode会切换到UITrackingRunLoopMode来保证ScrollView的流畅滑动：只能在NSDefaultRunLoopMode模式下处理的事件会影响scrllView的滑动。

如果我们把一个NSTimer对象以NSDefaultRunLoopMode（kCFRunLoopDefaultMode）添加到主运行循环中的时候,ScrollView滚动过程中会因为mode的切换，而导致NSTimer将不再被调度。

同时因为mode还是可定制的，所以：

Timer计时会被scrollView的滑动影响的问题可以通过将timer添加到NSRunLoopCommonModes（kCFRunLoopCommonModes）来解决。代码如下：

```objc
//
// http://weibo.com/luohanchenyilong/ (微博@iOS程序犭袁)
// https://github.com/ChenYilong

//将timer添加到NSDefaultRunLoopMode中
[NSTimer scheduledTimerWithTimeInterval:1.0
     target:self
     selector:@selector(timerTick:)
     userInfo:nil
     repeats:YES];
//然后再添加到NSRunLoopCommonModes里
NSTimer *timer = [NSTimer timerWithTimeInterval:1.0
     target:self
     selector:@selector(timerTick:)
     userInfo:nil
     repeats:YES];
[[NSRunLoop currentRunLoop] addTimer:timer forMode:NSRunLoopCommonModes];
```

## 31. 猜想runloop内部是如何实现的？

> 一般来讲，一个线程一次只能执行一个任务，执行完成后线程就会退出。如果我们需要一个机制，让线程能随时处理事件但并不退出，通常的代码逻辑
是这样的：

	function loop() {
	    initialize();
	    do {
	        var message = get_next_message();
	        process_message(message);
	    } while (message != quit);
	}


或使用伪代码来展示下:

	//
	// http://weibo.com/luohanchenyilong/ (微博@iOS程序犭袁)
	// https://github.com/ChenYilong
	int main(int argc, char * argv[]) {
     //程序一直运行状态
     while (AppIsRunning) {
          //睡眠状态，等待唤醒事件
          id whoWakesMe = SleepForWakingUp();
          //得到唤醒事件
          id event = GetEvent(whoWakesMe);
          //开始处理事件
          HandleEvent(event);
     }
     return 0;
	}

参考链接：

1. [《深入理解RunLoop》](http://blog.ibireme.com/2015/05/18/runloop/#base)
2. 摘自博文[***CFRunLoop***](https://github.com/ming1016/study/wiki/CFRunLoop)，原作者是[微博@我就叫Sunny怎么了](http://weibo.com/u/1364395395)

## 32. objc使用什么机制管理对象内存？

通过 retainCount 的机制来决定对象是否需要释放。

每次 runloop 的时候，都会检查对象的 retainCount，如果retainCount 为 0，说明该对象没有地方需要继续使用了，可以释放掉了。

## 33. ARC通过什么方式帮助开发者管理内存？

ARC相对于MRC，不是在编译时添加retain/release/autorelease这么简单。应该是编译期和运行期两部分共同帮助开发者管理内存。

在编译期，ARC用的是更底层的C接口实现的retain/release/autorelease，这样做性能更好，也是为什么不能在ARC环境下手动retain/release/autorelease，同时对同一上下文的同一对象的成对retain/release操作进行优化（即忽略掉不必要的操作）；ARC也包含运行期组件，这个地方做的优化比较复杂，但也不能被忽略。

## 34. 不手动指定autoreleasepool的前提下，一个autorealese对象在什么时刻释放？（比如在一个vc的viewDidLoad中创建）

分两种情况：手动干预释放时机、系统自动去释放。

1. 手动干预释放时机 - 指定autoreleasepool
 就是所谓的：当前作用域大括号结束时释放。
2. 系统自动去释放 - 不手动指定autoreleasepool

Autorelease对象出了作用域之后，会被添加到最近一次创建的自动释放池中，并会在当前的 runloop 迭代结束时释放。

释放的时机总结起来，可以用下图来表示：

![autoreleasepool与 runloop 的关系图](http://i61.tinypic.com/28kodwp.jpg)

下面对这张图进行详细的解释：

从程序启动到加载完成是一个完整的运行循环，然后会停下来，等待用户交互，用户的每一次交互都会启动一次运行循环，来处理用户所有的点击事件、触摸事件。

我们都是知道：
**所有 autorelease 的对象，在出了作用域之后，会被自动添加到最近创建的自动释放池中。**

但是如果每次都放进应用程序的 `main.m` 中的 autoreleasepool 中，迟早有被撑满的一刻。这个过程中必定有一个释放的动作。何时？

在一次完整的运行循环结束之前，会被销毁。

那什么时间会创建自动释放池？运行循环检测到事件并启动后，就会创建自动释放池。

子线程的 runloop 默认是不工作，无法主动创建，必须手动创建。

自定义的 NSOperation 和 NSThread 需要手动创建自动释放池。比如： 自定义的 NSOperation 类中的 main 方法里就必须添加自动释放池。否则出了作用域后，自动释放对象会因为没有自动释放池去处理它，而造成内存泄露。

但对于 blockOperation 和 invocationOperation 这种默认的Operation ，系统已经帮我们封装好了，不需要手动创建自动释放池。

@autoreleasepool 当自动释放池被销毁或者耗尽时，会向自动释放池中的所有对象发送 release 消息，释放自动释放池中的所有对象。

如果在一个vc的viewDidLoad中创建一个 Autorelease对象，那么该对象会在 viewDidAppear 方法执行前就被销毁了。

参考链接：[《黑幕背后的Autorelease》](http://blog.sunnyxx.com/2014/10/15/behind-autorelease/)

## 35. BAD_ACCESS在什么情况下出现？

访问了野指针，比如对一个已经释放的对象执行了release、访问已经释放对象的成员变量或者发消息。

死循环

## 36. 苹果是如何实现autoreleasepool的？

autoreleasepool 以一个队列数组的形式实现,主要通过下列三个函数完成.

1. `objc_autoreleasepoolPush`
2. `objc_autoreleasepoolPop`
3. `objc_autorelease`

看函数名就可以知道，对 autorelease 分别执行 push，和 pop 操作。销毁对象时执行release操作。

举例说明：我们都知道用类方法创建的对象都是 Autorelease 的，那么一旦 Person 出了作用域，当在 Person 的 dealloc 方法中打上断点，我们就可以看到这样的调用堆栈信息：

![enter image description here](http://i60.tinypic.com/15mfj11.jpg)

## 37. 使用block时什么情况会发生引用循环，如何解决？

一个对象中强引用了block，在block中又使用了该对象，就会发射循环引用。
解决方法是将该对象使用__weak或者__block修饰符修饰之后再在block中使用。

1. `id weak weakSelf = self;`
	+ 或者` weak __typeof(&*self)weakSelf = self`该方法可以设置宏
2. `id __block weakSelf = self;`

## 38. 在block内如何修改block外部变量？

默认情况下，在block中访问的外部变量是复制过去的，即：**写操作不对原变量生效**。但是你可以加上`__block`来让其写操作生效，示例代码如下:

	__block int a = 0;
	void  (^foo)(void) = ^{
	    a = 1;
	}
	f00();
	//这里，a的值被修改为1

参考链接：[微博@唐巧_boy](http://weibo.com/tangqiaoboy)的著作《iOS开发进阶》中的第11.2.3章节

## 39. 使用系统的某些block api（如UIView的block版本写动画时），是否也考虑引用循环问题？

系统的某些block api中，UIView的block版本写动画时不需要考虑，但也有一些api 需要考虑：

所谓“引用循环”是指双向的强引用，所以那些“单向的强引用”（block 强引用 self ）没有问题，比如这些：

```objc
[UIView animateWithDuration:duration animations:^{ [self.superview layoutIfNeeded]; }];
```

```objc
[[NSOperationQueue mainQueue] addOperationWithBlock:^{ self.someProperty = xyz; }];
```

```objc
[[NSNotificationCenter defaultCenter] addObserverForName:@"someNotification"
                                                  object:nil
                           queue:[NSOperationQueue mainQueue]
                                              usingBlock:^(NSNotification * notification) {
                                                    self.someProperty = xyz; }];
```

这些情况不需要考虑“引用循环”。

但如果你使用一些参数中可能含有 ivar 的系统 api ，如 GCD 、NSNotificationCenter就要小心一点：比如GCD 内部如果引用了 self，而且 GCD 的其他参数是 ivar，则要考虑到循环引用：

```objc
__weak __typeof__(self) weakSelf = self;
dispatch_group_async(_operationsGroup, _operationsQueue, ^
{
__typeof__(self) strongSelf = weakSelf;
[strongSelf doSomething];
[strongSelf doSomethingElse];
} );
```

类似的：

```objc
__weak __typeof__(self) weakSelf = self;
_observer = [[NSNotificationCenter defaultCenter] addObserverForName:@"testKey"
                                                                object:nil
                                                                 queue:nil
                                                            usingBlock:^(NSNotification *note) {
      __typeof__(self) strongSelf = weakSelf;
      [strongSelf dismissModalViewControllerAnimated:YES];
  }];
```

`self --> _observer --> block --> self` 显然这也是一个循环引用。

## 40. GCD的队列（`dispatch_queue_t`）分哪两种类型？

1. 串行队列 Serial Dispatch Queue
2. 并行队列 Concurrent Dispatch Queue

## 41. 如何用GCD同步若干个异步调用？（如根据若干个url异步加载多张图片，然后在都下载完成后合成一张整图）

使用Dispatch Group追加block到Global Group Queue,这些block如果全部执行完毕，就会执行Main Dispatch Queue中的结束处理的block。

```objc
dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
dispatch_group_t group = dispatch_group_create();
dispatch_group_async(group, queue, ^{ /*加载图片1 */ });
dispatch_group_async(group, queue, ^{ /*加载图片2 */ });
dispatch_group_async(group, queue, ^{ /*加载图片3 */ });
dispatch_group_notify(group, dispatch_get_main_queue(), ^{
        // 合并图片
});
```

## 42. `dispatch_barrier_async`的作用是什么？

在并行队列中，为了保持某些任务的顺序，需要等待一些任务完成后才能继续进行，使用 barrier 来等待之前任务完成，避免数据竞争等问题。

`dispatch_barrier_async` 函数会等待追加到Concurrent Dispatch Queue并行队列中的操作全部执行完之后，然后再执行 `dispatch_barrier_async` 函数追加的处理，等 `dispatch_barrier_async` 追加的处理执行结束之后，Concurrent Dispatch Queue才恢复之前的动作继续执行。

打个比方：比如你们公司周末跟团旅游，高速休息站上，司机说：大家都去上厕所，速战速决，上完厕所就上高速。超大的公共厕所，大家同时去，程序猿很快就结束了，但程序媛就可能会慢一些，即使你第一个回来，司机也不会出发，司机要等待所有人都回来后，才能出发。 `dispatch_barrier_async` 函数追加的内容就如同 “上完厕所就上高速”这个动作。

（注意：使用 `dispatch_barrier_async` ，该函数只能搭配自定义并行队列 `dispatch_queue_t` 使用。不能使用： `dispatch_get_global_queue` ，否则 `dispatch_barrier_async` 的作用会和 `dispatch_async` 的作用一模一样。 ）


## 43. 苹果为什么要废弃`dispatch_get_current_queue`？

`dispatch_get_current_queue`容易造成死锁

## 44. 以下代码运行结果如何？


	- (void)viewDidLoad
	{
	    [super viewDidLoad];
	    NSLog(@"1");
	    dispatch_sync(dispatch_get_main_queue(), ^{
	        NSLog(@"2");
	    });
	    NSLog(@"3");
	}

只输出：1 。发生主线程锁死。

## 45. addObserver:forKeyPath:options:context:各个参数的作用分别是什么，observer中需要实现哪个方法才能获得KVO回调？

```objc
// 添加键值观察
/*
1 观察者，负责处理监听事件的对象
2 观察的属性
3 观察的选项
4 上下文
*/
[self.person addObserver:self forKeyPath:@"name" options:NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld context:@"Person Name"];
```

observer中需要实现一下方法：

```objc
// 所有的 kvo 监听到事件，都会调用此方法
/*
 1. 观察的属性
 2. 观察的对象
 3. change 属性变化字典（新／旧）
 4. 上下文，与监听的时候传递的一致
 */
- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context;
```

## 46. 如何手动触发一个value的KVO

所谓的“手动触发”是区别于“自动触发”：

自动触发是指类似这种场景：在注册 KVO 之前设置一个初始值，注册之后，设置一个不一样的值，就可以触发了。

想知道如何手动触发，必须知道自动触发 KVO 的原理：

键值观察通知依赖于 NSObject 的两个方法:  `willChangeValueForKey:` 和 `didChangevlueForKey:` 。在一个被观察属性发生改变之前，  `willChangeValueForKey:` 一定会被调用，这就
会记录旧的值。而当改变发生后，  `didChangeValueForKey:` 会被调用，继而 `observeValueForKey:ofObject:change:context:` 也会被调用。如果可以手动实现这些调用，就可以实现“手动触发”了。

那么“手动触发”的使用场景是什么？一般我们只在希望能控制“回调的调用时机”时才会这么做。

具体做法如下：

如果这个  `value` 是  表示时间的 `self.now` ，那么代码如下：最后两行代码缺一不可。

```objc
//  .m文件
//  Created by https://github.com/ChenYilong
//  微博@iOS程序犭袁(http://weibo.com/luohanchenyilong/).
//  手动触发 value 的KVO，最后两行代码缺一不可。

//@property (nonatomic, strong) NSDate *now;
- (void)viewDidLoad
{
    [super viewDidLoad];
    [self willChangeValueForKey:@"now"]; // “手动触发self.now的KVO”，必写。
    [self didChangeValueForKey:@"now"]; // “手动触发self.now的KVO”，必写。
}
```

但是平时我们一般不会这么干，我们都是等系统去“自动触发”。“自动触发”的实现原理：

> 比如调用 `setNow:` 时，系统还会以某种方式在中间插入 `wilChangeValueForKey:` 、 `didChangeValueForKey:`  和 `observeValueForKeyPath:ofObject:change:context:` 的调用。

大家可能以为这是因为 `setNow:` 是合成方法，有时候我们也能看到人们这么写代码:

```objc
- (void)setNow:(NSDate *)aDate {
    [self willChangeValueForKey:@"now"]; // 没有必要
    _now = aDate;
    [self didChangeValueForKey:@"now"];// 没有必要
}
```

这是完全没有必要的代码，不要这么做，这样的话，KVO代码会被调用两次。KVO在调用存取方法之前总是调用 `willChangeValueForKey:`  ，之后总是调用 `didChangeValueForkey:` 。怎么做到的呢?答案是通过 isa 混写（isa-swizzling）。下文《apple用什么方式实现对一个对象的KVO？》会有详述。

参考链接： [Manual Change Notification---Apple 官方文档](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOCompliance.html#//apple_ref/doc/uid/20002178-SW3)

## 47. 若一个类有实例变量 `NSString *_foo` ，调用setValue:forKey:时，可以以foo还是 `_foo` 作为key？

都可以。

## 48. KVC的keyPath中的集合运算符如何使用？

1. 必须用在集合对象上或普通对象的集合属性上
2. 简单集合运算符有@avg， @count ， @max ， @min ，@sum，
3. 格式 @"@sum.age"或 @"集合属性.@max.age"

## 49. KVC和KVO的keyPath一定是属性么？

KVO支持实例变量

## 50. 如何关闭默认的KVO的默认实现，并进入自定义的KVO实现？

请参考：[《如何自己动手实现 KVO》](http://tech.glowing.com/cn/implement-kvo/)

## 51. apple用什么方式实现对一个对象的KVO？

[Apple 的文档](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOImplementation.html)对 KVO 实现的描述：

> Automatic key-value observing is implemented using a technique called isa-swizzling... When an observer is registered for an attribute of an object the isa pointer of the observed object is modified, pointing to an intermediate class rather than at the true class ...

从[Apple 的文档](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOImplementation.html)可以看出：Apple 并不希望过多暴露 KVO 的实现细节。不过，要是借助 runtime 提供的方法去深入挖掘，所有被掩盖的细节都会原形毕露：

> 当你观察一个对象时，一个新的类会被动态创建。这个类继承自该对象的原本的类，并重写了被观察属性的 setter 方法。重写的 setter 方法会负责在调用原 setter 方法之前和之后，通知所有观察对象：值的更改。最后通过 ` isa 混写（isa-swizzling）` 把这个对象的 isa 指针 ( isa 指针告诉 Runtime 系统这个对象的类是什么 ) 指向这个新创建的子类，对象就神奇的变成了新创建的子类的实例。我画了一张示意图，如下所示：

![enter image description here](http://i62.tinypic.com/sy57ur.jpg)

KVO 确实有点黑魔法：

> Apple 使用了 ` isa 混写（isa-swizzling）`来实现 KVO 。

下面做下详细解释：

键值观察通知依赖于 NSObject 的两个方法:  `willChangeValueForKey:` 和 `didChangevlueForKey:` 。在一个被观察属性发生改变之前，  `willChangeValueForKey:` 一定会被调用，这就会记录旧的值。而当改变发生后，  `didChangeValueForKey:` 会被调用，继而 `observeValueForKey:ofObject:change:context:` 也会被调用。可以手动实现这些调用，但很少有人这么做。一般我们只在希望能控制回调的调用时机时才会这么做。大部分情况下，改变通知会自动调用。

比如调用 `setNow:` 时，系统还会以某种方式在中间插入 `wilChangeValueForKey:` 、 `didChangeValueForKey:`  和 `observeValueForKeyPath:ofObject:change:context:` 的调用。大家可能以为这是因为 `setNow:` 是合成方法，有时候我们也能看到人们这么写代码:

```objc
- (void)setNow:(NSDate *)aDate {
    [self willChangeValueForKey:@"now"]; // 没有必要
    _now = aDate;
    [self didChangeValueForKey:@"now"];// 没有必要
}
```

这是完全没有必要的代码，不要这么做，这样的话，KVO代码会被调用两次。KVO在调用存取方法之前总是调用 `willChangeValueForKey:`  ，之后总是调用 `didChangeValueForkey:` 。怎么做到的呢?答案是通过 isa 混写（isa-swizzling）。第一次对一个对象调用 `addObserver:forKeyPath:options:context:` 时，框架会创建这个类的新的 KVO 子类，并将被观察对象转换为新子类的对象。在这个 KVO 特殊子类中， Cocoa 创建观察属性的 setter ，大致工作原理如下:

```objc
- (void)setNow:(NSDate *)aDate {
    [self willChangeValueForKey:@"now"];
    [super setValue:aDate forKey:@"now"];
    [self didChangeValueForKey:@"now"];
}
```

这种继承和方法注入是在运行时而不是编译时实现的。这就是正确命名如此重要的原因。只有在使用KVC命名约定时，KVO才能做到这一点。

KVO 在实现中通过 `isa 混写（isa-swizzling）` 把这个对象的 isa 指针 ( isa 指针告诉 Runtime 系统这个对象的类是什么 ) 指向这个新创建的子类，对象就神奇的变成了新创建的子类的实例。这在[Apple 的文档](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOImplementation.html)可以得到印证：

> Automatic key-value observing is implemented using a technique called isa-swizzling... When an observer is registered for an attribute of an object the isa pointer of the observed object is modified, pointing to an intermediate class rather than at the true class ...

然而 KVO 在实现中使用了 `isa 混写（ isa-swizzling）` ，这个的确不是很容易发现：Apple 还重写、覆盖了 `-class` 方法并返回原来的类。 企图欺骗我们：这个类没有变，就是原本那个类。。。

但是，假设“被监听的对象”的类对象是 `MYClass` ，有时候我们能看到对 `NSKVONotifying_MYClass` 的引用而不是对  `MYClass`  的引用。借此我们得以知道 Apple 使用了 `isa 混写（isa-swizzling）`。具体探究过程可参考[ 这篇博文 ](https://www.mikeash.com/pyblog/friday-qa-2009-01-23.html)。

## 52. IBOutlet连出来的视图属性为什么可以被设置成weak?

参考链接：[ ***Should IBOutlets be strong or weak under ARC?*** ](http://stackoverflow.com/questions/7678469/should-iboutlets-be-strong-or-weak-under-arc)

文章告诉我们：

> 因为既然有外链那么视图在xib或者storyboard中肯定存在，视图已经对它有一个强引用了。

不过这个回答漏了个重要知识，使用storyboard（xib不行）创建的vc，会有一个叫_topLevelObjectsToKeepAliveFromStoryboard的私有数组强引用所有top level的对象，所以这时即便outlet声明成weak也没关系

## 53. IB中User Defined Runtime Attributes如何使用？

它能够通过KVC的方式配置一些你在interface builder 中不能配置的属性。当你希望在IB中作尽可能多得事情，这个特性能够帮助你编写更加轻量级的viewcontroller

## 54. 如何调试BAD_ACCESS错误

1. 重写object的respondsToSelector方法，现实出现EXEC_BAD_ACCESS前访问的最后一个object
2. 通过 Zombie ![enter image description here](http://i.stack.imgur.com/ZAdi0.png)
3. 设置全局断点快速定位问题代码所在行
4. Xcode 7 已经集成了BAD_ACCESS捕获功能：**Address Sanitizer**。

用法如下：在配置中勾选✅Enable Address Sanitizer

![enter image description here](https://developer.apple.com/library/prerelease/ios/documentation/DeveloperTools/Conceptual/WhatsNewXcode/Art/xc7-asan_2x.png)

## 55. lldb（gdb）常用的调试命令？

- breakpoint 设置断点定位到某一个函数
- n 断点指针下一步
- po打印对象

更多 lldb（gdb） 调试命令可查看

1. [ ***The LLDB Debugger*** ](http://lldb.llvm.org/lldb-gdb.html)；
2. 苹果官方文档：[ ***iOS Debugging Magic*** ](https://developer.apple.com/library/ios/technotes/tn2239/_index.html)。


