#Effective C++

##导读

1.**explicit**：构造函数声明为explicit，避免隐式类型转换，依然可以显示类型转换。

禁止编译器执行非预期的类型换转。

2.Pass-by-Value: 会调用拷贝构造函数，因此对于自定义的类型，最好Pass-by-Reference

##01 视C++为一个语言联邦

C++主要4个次语言：

- C ：Pass-by-Value高效
- Object-Oriented C++ ：Pass-by-Reference-to-const
- Template C++ ：Pass-by-Reference-to-const
- STL ：Pass-by-Value

##02 以const，enum，inline替换#define

宏定义#define只是进行简单的替换，提倡使用const，enum和inline代替#define

- 定义常量指针：

```cpp
const char* const Name = "Xiaolong"
const std::string Name = "Xiaolong"  //这个好一点
```

- class 专属常量：常量的作用域在类内，为了保证常量至多只有一个实体，定义为static

	无法用#define来定义一个类内的专属常量
	
```cpp
****.h
class GamePlayer
{
private:
	static const int Number = 5; //声明
	enum ｛Number = 5｝;   //这也是一种方法
	int   scores[Number];
}

****.cpp
const int GamePlayer::Number; //已经有初始值，可以不赋值
```

- \#define的另一个功能是实现宏

```cpp
#define CALL_WITH_MAX(a, b)  f(  (a)>(b) ? (a) : (b) )

CALL_WITH_MAX(++a, b)  //这种用法会导致++a的次数不确定

//Template inline 函数来替换
template <typename T>
inline void call_with_max(const T &a, const T &b)
{
	f ( a>b ? a : b );
}
```
##03 尽可能的使用const

**const**：出现在\*左边，表示被指事物是常量，出现在\*右边，表示指针自身是常量；出现在两边表示指针和被指之物都是常量。

STL的迭代器的作用类似与`T *`  指针

```cpp
std::vector<int> vec;
const std::vector<int>::iterator iter = vec.begin(); // iter相当于 T * const
++iter;  //这个是错误的
std::vector<int>::const_iterator citer = vec.begin(); // iter相当于const  T * 
*citer= 10; //赋值操作是错误的
```

**const 成员变量**：当const和非const函数有相同的实现时，可以利用非const调用const函数
	
```cpp
class Textbook
{
public:
	const char & operator [] (std::size_t position) const
	{
		return Text[position];
	}

	char & operator [] (std::size_t position) 
	{
		return const_cast<char &>( 
				static_cast<const Textbook&>(*this)[position]
				);
		//将op[]返回值的const 转除为*this 加上const, 调用const op[]
	}
}
```
		
##04  确定对象被使用前已被初始化

在C++程序设计中，应该对所有对象初始化，以避免不必要的错误。

对象成员变量的初始化发生在进入构造函数本体之前，构造函数内不是初始化，而是赋值。

基类早于派生类被初始化，类的成员变量按其声明顺序被初始化。

C++ 对”定义于不同编译单元内的non-local static 对象”的初始化次序并无明确定义。为免除”跨编译单元之初始化次序”问题，请以local static 对象替换non-local static 对象。

```cpp
class FileSystem { ... };
FileSystem& tfs() 		//代替tfs对象
{
  static FileSystem fs; // 以local static的方式定义和初始化object
  return fs; // 返回一个引用
}
 
class Directory { ... };
Directory::Directory( params )
{
  ...
  std::size_t disks = tfs().numDisks();
  ...
}
 
Directory& tempDir() // 代替tempDir对象，
{
  static Directory td;
  return td;
}
```

##05 了解C++默认编写并调用哪些函数

编译器会生成，默认构造函数，拷贝构造函数，析构函数，拷贝复制操作符。

##06 若不想使用编译器自动生成的函数，就明确拒绝

实现对象不被复制，可以将拷贝构造函数，析构函数声明为private，而不去实现。

```cpp
class HomeForSale
{
public:
	.....
private:
	HomeForSale (cosnt HomeForSale &);
	HomeForSale  &operator = (cosnt HomeForSale &);
｝;
```

（1）更好的办法，在编译期发现错误，用下面的类

```cpp
class UnCopyable
{
public:
	UnCopyable();   //允许派生类构造和析构
	~UnCopyable();

private:
	UnCopyable( const UnCopyable &);   //阻止复制
	UnCopyable & operator=  (const UnCopyable &);
};

class HomeForSale : public UnCopyable{
	.......
};
```

这种方法带来的问题是，可能造成多重继承，这会导致很多麻烦。

（2）创建一个宏，并将之放到每一个独一无二对象的private中，该宏为：

	// 禁止使用拷贝构造函数和 operator= 赋值操作的宏
	// 应该类的 private: 中使用

```cpp
#define DISALLOW_COPY_AND_ASSIGN(TypeName) \
TypeName(const TypeName&); \
void operator=(const TypeName&)
```

```cpp
boost::noncopyable
```

google C++编程规范中提倡使用该方法。

##07  为多态基类声明virtual析构函数

（1）带多态性质的base class应该声明一个virtual 析构函数。

如果class 带有任何virtual 函数，它就应该拥有一个virtual 析构函数。这样，当用户delete基类指针时，会自动调用派生类的析构函数（而不是只调用基类的析构函数）。

（2）class的设计目的如果不是作为base class 使用，或不是为了具备多态性(polymorphically) ，就不该声明virtual 析构函数。

这是因为，当一个函数声明为virtual时，C++编译器会创建虚函数表以完成动态绑定功能，这将带来时间和空间上的花销。

不能

class my：public std::vector  //严格禁止


public is
private have
##08 别让异常逃离析构函数

如果析构函数抛出异常，可能导致其他程序无法正常析构，造成资源泄漏。

（1）析构函数绝对不要吐出异常。如果一个被析构函数调用的函数可能抛出异常，析构函数应该捕获任何异常，然后吞下它们(不传播)或结束程序。

（2）如果客户需要对某个操作函数运行期间抛出的异常做出反应，那么class 应该提供一个普通函数(而非在析构函数中)执行该操作。

##09 绝不在构造和析构过程中调用virtual函数

在构造过程中，基类的虚函数还是指向其自己，可以说还不是虚函数。

在派生类的基类构造过程中，对象的类型是基类，而不是派生类。

##10 令operator = 返回一个reference to *this

为了实现“连锁赋值“，应令operator= 返回一个reference to *this。

```cpp
Widget & operator =  (const Widget &)
{
	......
	return *this;
}
```

The Design and Evolution of C++ 里面说要返回const T&， 为了防止 (a=b)=c;

Exceptional C++ 说要返回 T&，为了与STL的容器兼容。

所以两种返回方式都可以，看具体需求。

##11 在operator = 处理自我赋值

确保当对象自我赋值时operator= 有良好的行为。其中包括比较”来源对象”和”目标对象”的地址、语句顺序、以及 copy-and-swap。

```cpp
class Bitmap{...};
class Widget
{
	...
private:
	Bitmap *pb;
};

Widget& Widget::operator=(const Widget& rhs)
{
	delete pb;       //如果自我赋值，则不安全，pb已经被删除
	pb = new Bitmap(*rhs.pb);
	return *this;
}
```

（1）验证源对象和目标对象是不是同一个

```cpp
Widget& Widget::operator=(const Widget& rhs)
{
	if(this == &rhs) return *this;  //目标对象和源对象是同一个，则不需要赋值操作
	delete pb;      
	pb = new Bitmap(*rhs.pb);
	return *this;
}
```
不具备异常安全性，如果new失败，则会异常，pb指向一块被删除的内存。

（2）如果new出现异常，pb还可以保持原始值。

```cpp
widget& Widget::operator=(const Widget& rhs)
{
	Bitmap* pOrig = pb;
	pb = new Bitmap(*rhs.pb);
	delete pOrig;
	return *this;
}
```

（3）Copy-and-Swap 技术

```cpp
class Widget 
{
	void swap(Widget& rhs); //交换*this 和rhs 的数据:详见条款29
	...
};
 
Widget& Widget::operator=(Widget rhs) //rhs是被传对象的一份复件(副本),Pass by value.
{
  swap(rhs); //将*this 的数据和复件/副本的数据互换
  return *this;
}
```

##12复制对象时勿忘其每一个成分

copy操作应该确保复制对象中的每一个成员变量以及其基类的成员变量。

（1）复制所有的成员变量  （2）调用基类的copy函数

```cpp
class Customer{};
class PriorityCustomer : public Customer
{
public:
	...
	PriorityCustomer(const PriorityCustomer& rhs);
	PriorityCustomer & operator = (const PriorityCustomer & rhs);

private:
	int priority;
};

PriorityCustomer::PriorityCustomer(const PriorityCustomer &rhs)
	:Customer(rhs)   //调用基类的构造函数
	,priority(rhs.priority)
{
}

PriorityCustomer&
PriorityCustomer::operator = (const PriorityCustomer & rhs)
{
	Customer::operator=(rhs);   //对基类部分进行复制
	priority = rhs.priority;
	return *this;
}
```

##13 以对象管理资源

把资源放入对象中，依赖C++的析构函数自动调用机制保证资源被释放。

为防止资源泄漏，可以使用RAII对象(“资源取得时机便是初始化时机“；Resource Acquisition Is Initialization； RAII))，它们在构造函数中获得资源并在析构函数中释放资源。

可以利用智能指针。

注：`auto_ptr`通过拷贝构造函数或者拷贝赋值，会使其变为NULL

STL不可以使用`auto_ptr`

可以使用`boost::shared_ptr`
	
##14  在资源管理类中小心coping行为

（1）禁止复制

（2）引用计数

##15 在资源管理器类中提供对原始资源的访问

(1)	APIs往往要求访问原始资源( raw resources) ，所以每一个RAII class 应该提供一个”取得其所管理之资源”的办法。

(2)	对原始资源的访问可能经由显式转换或隐式转换。一般而言显式转换(如调用get()函数)比较安全，但隐式转换对客户比较方便。

##16 成对使用new和delete要使用相同的形式

如果`new`中使用了`[]`，则`delete`中也要使用`[]`

##17 以独立语句将newed 对象置入智能指针

对于如下的调用

```cpp
processWidget(std::trl::shared_ptr<Widget> pw(new Widget), priority());
```

在调用processWidget之前，编译器必须创建代码，做以下三件事：

(1)	调用priority

(2)	执行”new Widget”

(3)	调用trl: : shared_ptr 构造函数

这三件事的执行顺序是不能保证的，如果顺序为（2）（1）（3），如果调用priority出现异常，则new的资源不能被正常释放，出现内存泄漏。

正确的方法如下：

```cpp
std::trl::shared_ptr<Widget> pw(new Widget); //在独立语句内以智能指针存储Widget对象
processWidget(pw, priority()); //这个调用肯定不存在内存泄漏
```

##18 让接口容易被正确使用，不易被误用

理想情况下，使用某个接口没有获得预期的行为，应该在编译期阻止。

通过导入新类型来防止接口被误用

限制类型内什么可以做，什么不可以做，常见的限制方法是加上const

shared_ptr支持定制型删除器，可以解决跨Dll问题

##19 设计class 犹如设计type

class的设计就是type的设计，需要考虑各种因素。

##20 提倡以pass-by -reference-to-const 替换pass-by-value

pass-by-value需要调用拷贝构造函数，会造成资源的浪费。

pass-by -reference-to-const 没有任何构造函数和析构函数被调用，没有任何新的对象被创建。

pass-by-value会导致切割问题(slicing problem)（所谓切割问题，是指派生类的对象传给基类类型的参数时，派生对象中的一些属性会被截断）

对于内置类型，STL迭代器和函数对象，pass-by-value更合适

##21 必须返回对象时，别妄想返回其reference

绝不要返回pointer 或reference指向一个local stack 对象，或返回reference 指向一个heap-allocated对象，或返回pointer 或reference指向一个local static 对象而有可能同时需要多个这样的对象。

正确的方法：

```cpp
const Rational& operator* (const Rational& lhs,const Rational& rhs) 
{
  return Rational(lhs.n * rhs.n, lhs.d * rhs.d); 
}
```

(1)	如果返回pointer 或reference指向一个local stack 对象:

```cpp
const Rational& operator* (const Rational& lhs,const Rational& rhs) {
	Rational result(lhs.n * rhs.n, lhs.d * rhs.d);   //result被析构，返回值无定义
	return result;
}
```
解释：result是local对象，而local 对象在函数退出前被销毁，这导致返回值坠入”无定义行为”。

(2)	返回reference 指向一个heap-allocated对象

```cpp
const Rational& operator* (const Rational& lhs,const Rational& rhs) 
{
  Rational* result = new Rational(lhs.n * rhs.n, lhs.d * rhs.d);
  return *result;
}
```
这种方式很容易造成内存泄露，如：

```cpp
Rational w, x, y , z;
w = x * y * z;   //与operator*(operator*(x， y) , z) 相同，内存泄露
```

(3)	返回pointer 或reference指向一个local static

```cpp
const Rational& operator* (const Rational& lhs, const Rational& rhs) 
{
  static Rational result;
  result = ... ;
  return result;
}
 
if((a * b) == (c * d)) {
  //当乘积相等时，做适当的相应动作;
} else {
  //当乘积不等时，做适当的相应动作;
}
```
	这样做的问题是，(a * b) == (c * d)永远为true。

##22 将成员变量声明为private

将成员变量声明为private，具有更好的封装性，所有对数据的访问通过接口实现，同时可以提供给class作者充分的实现自由。

protect并不比public更具有封装性。

##23 宁以non-member 、non-friend 替换member 函数

##24 若所有参数都需要类型转换，请为此采用non-member函数

##25 考虑写出一个不抛异常的swap函数

```cpp
	namespace std
	{
		template<typename T>
		void swap(T &a, T&b)
		{
			T temp(a);
			a = b;
			b = temp;
		}
	}
```

特化版本

```cpp
	class WidgetImpl;
	class Widget
	{
	public:
		void swap(Widget &other)
		{
			using std::swap;
			swap(pImpl, other.pImpl);
		}
	private:
		WidgetImpl * pImpl;
	};

	namespace std
	{
		template<>
		void swap<Widget>(Widget &a, Widget &b)
		{
			a.swap(b);
		}
	}
```

##26 尽可能延后变量定义式的出现时间

##34 区分接口继承和实现继承

成员函数的接口总会被继承。

声明一个pure virtual函数的目的就是为了让子类只继承函数接口。

声明一个impure virtual函数的目的是为了让子类继承该函数的接口和缺省实现。

声明非virtual函数的目的是为了让子类继承该函数的接口及一份强制实现。这类函数不应该在子类中被重新定义

