#Effective STL

##与效率有关的条款
> 条款4：调用`empty`而不是检查`size()`是否为0

> 条款5：区间成员函数优先于与之对应的单元素成员函数

> 条款14：使用`reserve`来避免不必要的重新分配

> 条款15：注意`string`实现的多样性

> 条款23：考虑用排序的`vector`代替关联容器

> 条款24：当效率至关重要时，要在`map::operator[]`和`map::insert`之间谨慎选择

> 条款25：熟悉非标准的散列容器

> 条款29：对于逐个字符的输入请考虑使用`istreambuf_iterator`

> 条款31：了解各种与排序有关的选择

> 条款44：容器的成员函数优先于同名的算法

> 条款46：在调用STL算法时，考虑使用函数对象而不是函数作其参数

##容器
###条款1：慎重选择容器类型
1.C++提供了很多可供程序员使用的容器：
- 标准STL序列容器：`vector`、`string`、`deque`和`list`
- 标准STL关联容器：`set`、`multiset`、`map`和`multimap`
- 非标准序列容器`slist`和`rope`：`slist`是单链表，`rope`是重型字符串
- 非标准关联容器`hash\_set`、`hash\_multiset`、`hash\_map`和`hash\_multimap`
- `vector<char>`可以作为`string`的替代品
- `vector`作为标准关联容器的替代品
- 几种标准非STL容器：包括数组、`bitset`、`valarray`、`stack`、`queue`和`priority\_queue`

2.如何在`vector`、`deque`和`list`中作出选择：
- `vector`是默认使用的序列类型
- 当需要频繁地对序列中间做插入和删除时，应使用`list`
- 当大多数插入和删除发生在序列的头部和尾部时，考虑`deque`

3.连续内存容器：元素在一块或多块内存中。vector，string，deque和rope

4.基于节点的容器：每一个动态分配的内存中只放一个元素。

###条款2：不要视图编写独立于容器类型的代码
1.很多成员函数当且仅当容器为某一种类型时才存在。

2.鼓励使用封装技术：通过对容器类型和其迭代器类型使用`typedef`
```
class Widget{};
typedef vector<Widget> WidgetContainer;
WidgetContainer cw;
```

###条款3：确保容器中的对象拷贝操作正确而高效
1.容器中保存了对象，但并不是你提供给容器的那些对象，当向容器插入对象是，存入容器的是你所指定对象的拷贝。

2.一个对象被保存在容器中，它进程被进一步拷贝，比如对序列容器的插入删除操作，或者调用排序算法等。

3.拷贝对象是STL的工作方式

4.使拷贝更高效、正确的方式并防止剥离问题发生的一个简单办法使容器包含指针而不是对象。

###条款4：调用empty而不是检查size()是否为0
1.empty对所有的标准容器都是常数时间操作，而对于一些list操作，size耗费时间线性。

###条款5：
1.给定两个vector，v1和v2，使v1的内容和v2的后半部分相同，最好的做法：
```
v1.assign(v2.begin() + v2.size()/2, v2.end());
```

其他方案
- 使用单元素操作：

```
vector<Widget> v1, v2;
v1.clear();

for(vector<Widget>::const_iterator ci = v2.begin() + v2.size()/2;
	ci != v2.end();
	++ci)
{
	v1.push_back(*ci);
}
```
- 使用copy区间函数

```
v1.clear();
copy(v2.begin() + v2.size()/2, v2.end(), back_inserter(v1));
```
- 使用insert区间函数

```
v1.insert(v1.end(), v2.begin() + v2.size()/2, v2.end());
```

2.上述最优的方案是assign方案，使用区间函数的好处是：
- 通过使用区间成员函数，可以少写一些代码。
- 使用区间成员函通常会得到意图清晰和更加直接的代码。

3.copy区间函数存在的问题是：
- copy没有表现出循环，但是在copy中的确存在一个循环，这会降低性能

4.insert单元素版本的存在性能问题：
- 不必要的函数调用；
- 把v中的已有的元素频繁移动到插入后的所处的位置；
- 重复使用单元素插入而不是一个区间插入可能导致的多次内存分配。

5.区间创建，所有标准容器都提供如下形式的构造函数：
```
container::container(InputIterator begin, // 区间开始
						InputIterator end); // 区间结束
```
6.区间插入，所有标准序列容器都提供如下形式的insert：
```
void container::insert(iterator position, // 在何处插入区间
						InputIterator begin, // 区间开始
						InputIterator end); // 区间结束
```
关联容器使用它们的比较函数来决定元素要放在哪里，所以它们了省略position参数。
```
void container::insert(lnputIterator begin, InputIterator end);
```
7.区间删除，所有的标准容器都提供了一个区间形式的erase，但是序列和关联容器的返回类型不同。

序列容器提供了这个：
```
iterator container::erase(iterator begin, iterator end);
```
关联容器提供这个：
```
void container::erase(iterator begin, iterator end);
```
8.区间赋值，所有标准列容器都提供了区间形式的assign：
```
void container::assign(InputIterator begin, InputIterator end);
```

###条款6：当心C++编译器最烦人的分析机制
假设你有一个int的文件，你想要把那些int拷贝到一个list中。这看起来像是一个合理的方式：
```
ifstream dataFile("ints.dat");
list<int> data(istream_iterator<int>(dataFile), istream_iterator<int>());
```
这里的想法是传一对istream_iterator给list的区间构造函数，因此把int从文件拷贝到list中。

你这段代码实际上是声明了一个data函数，它的返回值是list<int>，两个参数均为istream_iterator<int>类型。

解决办法
```
ifstream dataFile("ints.dat");
istream_iterator<int> dataBegin(dataFile);
istream_iterator<int> dataEnd;
list<int> data(dataBegin, dataEnd);
```

> C++中的一条普遍规律，即尽可能的解释为函数声明。

###条款7：如果容器中包含了通过new操作创建的指针，切记在容器对象析构前将指针delete掉
1.最简单的方式，采用智能指针容器来替换指针容器：`boost::share_ptr`

###条款8：切勿创建包含auto_ptr的容器对象
1.当你复制一个auto_ptr时，它所指向的对象的所有权被移交到复制的auto_ptr上，而它自身被设置为NULL。

###条款9：慎重选择删除元素的方法
1.删除元素可能导致迭代器失效，因此删除元素的时候，需要注意。

2.要删除元素中有特定值的所有对象：
- 如果是vector，string或deque，使用erase-remove习惯用法
```
c.erase(c.remove(c.begin(), c.end(), 123), c.end());  // remove会将元素移到末位，并但会迭代器
```
- 如果是list，则使用list::reomve
```
c.remove(123);
```
- 如果是标准关联容器，则使用它的erase成员函数
```
c.earse(123);
```

3.要删除容器中满足特定判别式的所有对象：
-  如果是vector，string或deque，使用erase-remove_if习惯用法
```
bool BadValue();
c.erase(c.remove_if(c.begin(), c.end(), BadValue), c.end());  // remove会将元素移到末位，并但会迭代器
```
- 如果是list，则使用list::reomve_if
```
c.remove_if(BadValue);
```
- 如果是标准关联容器，高效办法，遍历容器中的元素，把迭代器传给earse时，对它进行后缀自增
```
AssocContainer<int> c;
for(AssocContainer<int>::iterator i=c.begin(); i!=c.end();)
{
	if(BadValue(*i))
    {
    	c.earse(i++);
    }
    else
    {
    	++i;
    }
}
```

4.要在循环内部做某些(除了删除对象之外的)操作

- 如果是标准序列容器，循环遍历容器中元素，记住每次调用erase之后用其返回值更新迭代器

    ```
    SeqContainer<int> c;
    for(SeqContainer<int>::iterator i=c.begin(); i!=c.end();)
    {
        if(BadValue(*i))
        {
            //do_somethiing
            i = c.earse(i);  //更新迭代器
        }
        else
        {
            ++i;
        }
    }
    ```

- 如果是关联容器，循环遍历容器中的元素，把迭代器传给earse时，对它进行后缀自增
```
AssocContainer<int> c;
for(AssocContainer<int>::iterator i=c.begin(); i!=c.end();)
{
	if(BadValue(*i))
    {
    	//do_somethiing
    	c.earse(i++);
    }
    else
    {
    	++i;
    }
}
```

###10.了解allocator的约定和限制
1.如果要自定义allocator，参考这个页面[http://www.josuttis.com/cppcode/myalloc.hpp.html](http://www.josuttis.com/cppcode/myalloc.hpp.html)

```
#include <limits>
#include <iostream>

namespace MyLib {
   template <class T>
   class MyAlloc {
     public:
       // type definitions
       typedef T        value_type;
       typedef T*       pointer;
       typedef const T* const_pointer;
       typedef T&       reference;
       typedef const T& const_reference;
       typedef std::size_t    size_type;
       typedef std::ptrdiff_t difference_type;

       // rebind allocator to type U
       template <class U>
       struct rebind {
           typedef MyAlloc<U> other;   //标准容器依赖于该模版，如list
       };

       // return address of values
       pointer address (reference value) const {
           return &value;
       }
       const_pointer address (const_reference value) const {
           return &value;
       }

       /* constructors and destructor
        * - nothing to do because the allocator has no state
        */
       MyAlloc() throw() {
       }
       MyAlloc(const MyAlloc&) throw() {
       }
       template <class U>
         MyAlloc (const MyAlloc<U>&) throw() {
       }
       ~MyAlloc() throw() {
       }

       // return maximum number of elements that can be allocated
       size_type max_size () const throw() {
           return std::numeric_limits<std::size_t>::max() / sizeof(T);
       }

       // allocate but don't initialize num elements of type T
       pointer allocate (size_type num, const void* = 0) {
           // print message and allocate memory with global new
           std::cerr << "allocate " << num << " element(s)"
                     << " of size " << sizeof(T) << std::endl;
           pointer ret = (pointer)(::operator new(num*sizeof(T)));
           std::cerr << " allocated at: " << (void*)ret << std::endl;
           return ret;
       }

       // initialize elements of allocated storage p with value value
       void construct (pointer p, const T& value) {
           // initialize memory with placement new
           new((void*)p)T(value);
       }

       // destroy elements of initialized storage p
       void destroy (pointer p) {
           // destroy objects by calling their destructor
           p->~T();
       }

       // deallocate storage p of deleted elements
       void deallocate (pointer p, size_type num) {
           // print message and deallocate memory with global delete
           std::cerr << "deallocate " << num << " element(s)"
                     << " of size " << sizeof(T)
                     << " at: " << (void*)p << std::endl;
           ::operator delete((void*)p);
       }
   };

   // return that all specializations of this allocator are interchangeable
   template <class T1, class T2>
   bool operator== (const MyAlloc<T1>&,
                    const MyAlloc<T2>&) throw() {
       return true;
   }
   template <class T1, class T2>
   bool operator!= (const MyAlloc<T1>&,
                    const MyAlloc<T2>&) throw() {
       return false;
   }
}
```

###条款11：理解自定义allocator的合理用法
1.同一类型的allocator必须是等价的

###条款12：切勿对STL容器的线程安全有不切实际的依赖
1.STL线程不安全，需要自己做线程同步

##vector和string

###条款13：vector和string优先于动态分配的数组

###条款14：使用reserve来比main不必要的重新分配
1.对于vector和string，需要更多空间时，需要做如下操作：
- 分配一块大小为当前容量2倍的新内存
- 把容器中所有的元素从旧内存复制到新内存中
- 析构旧内存中的元素
- 释放旧内存

2.reserve成员函数能使重新分配的次数减少到最低限度，避免重新分配和指针、迭代器、引用失效带来的开销。

###条款15：注意string实现的多样性

###条款16：了解如何把vector和string数据传给旧的API
1.vector
```
void do_something(const int *,size_t);

vector<int> v;
if(!v.empty())
{
	do_something(&v[0], v.size());
}
```

2.string
- string中的数据不一定存储在连续的内存中
- string的内部表示不一定以空字符串结尾

```
void do_something(const char *);

string s;
do_something(s.c_str());
```

3.先让C API把数据写入vector中，然后把数据复制到期望最终写入的STL容器中总是可行的

###条款17：使用swap技巧除去多余的容量

```
class Contestant{};
vector<Contestant> contestants;
// 创建临时变量，和contestants交换，临时变量析构后，资源释放
vector<Contestant>(contestants).swap(contestants);
```

###条款18：避免使用`vector<bool>`
1.替代`vetcor<bool>`的方案
- `deque<bool>`
- `bitset`

##3.关联容器

###条款19：理解equality和equivalence的区别
1.find对相同的定义是相等，是以`operator==`为基础的；insert对相同的定义是等价，是以`operator<`为基础的。

2.等价的含义：如果两个值中的任何一个（按照一定的顺序）都不在另一个的前面，那么这两个值（按照这一准则）就是等价的。

3.标准关联容器总是保持顺序排列的，所以每个容器必须有一个比较函数（默认为less）来决定保持怎样的顺序。等价的定义正是通过这个比较函数来确定的。而需要判断相等时，一般惯例是直接调用`operator==`

###条款20：为包含指针的关联容器指针比较类型

1.当关联容器中保存的是对象指针时，需要自己定义比较器（不是一个函数，而是一个仿函数模板），不然关联容器会按照指针大小进行排序，而不是指针指向的内容。
```
struct StringLess:public binary_function<
		const string *, const string *, bool>
{
	bool operator()(const string *sp1, const string *sp2) cosnt
    {
    	return *sp1<*sp2;
    }
};

std::set<string*, StringLess> ssp;
```

###条款21：总是让比较函数在等值的情况下返回false
1.关联容器中，自定义比较类型时，对于两个元素相等时，应该返回false，也就是返回0。不然会破坏所有的标准关联容器。

###条款22：切勿直接修改set或mulitset中的键
1.set和mulitset按照一定的顺序来存放自己的元素，如果修改了元素的值，它们可能不在正确的位置上，会打破容器的有序性。

2.对于map和mulitmap是默认是无法修改的，因为其类型是`pair<const K, V>`

3.如果遵循C++标准所制定的规则，那就永远不要试图修改在map和mulitmap中作为键的对象。

4.安全的修改方法
- 通过搜索找到元素
- 为将要修改的元素做拷贝
- 修改拷贝之后的元素
- 删除原元素
- 将修改后的元素插入

###条款23：考虑用排序的vector来替代关联容器
1.对于查找几乎从不跟插入和删除在一起使用时，可以考虑使用排序的vector来代替关联容器

2.用vector模拟关联容器的代码如下：
```
typedef pair<string, int> Data; // 在这个例子里存储在"map"中的类型

class DataCompare { // 比较函数的类
public:
	bool operator()(const Data& lhs, const Data& rhs) const // 用于排序的比较函数
    {
    	return keyLess(lhs.first, rhs.first); // keyLes是小于
    }
    bool operator()(const Data& Ihs, const Data::first_type& k) const // 用于查找的比较函数
    {
    	return keyLess(lhs.first, k);
    }
    bool operator()(const Data::first_type& k, const Data& rhs) const // （形式2）
    {
    	return keyLess(k, rhs.first);
    }
private:
	bool keyLess(const Data::first_type& k1, const Data::first_type& k2) const // 实际比较函数
    {
    	return k1 < k2;
    }
};

vector<Data> vd; // 代替map<string, int>

... //设置阶段：大量插入，查找很少

sort(vd.begin(), vd.end(), DataCompare()); // 结束设置阶段。

string s; // 用于存放待查找的对象

... // 开始查找阶段

if (binary_search(vd.begin(), vd.end(), s,DataCompare()))... // 通过binary_search查找

vector<Data>::iterator i =lower_bound(vd.begin(), vd.end(), s, DataCompare()); // 再次通过lower_bound查找，

if (i != vd.end() && !DataCompare()(s, *i))... // 条款45解释了“!DataCompare()(s, *i)”测试

pair<vector<Data>::iterator,

vector<Data>::iterator> range = equal_range(vd.begin(), vd.end(), s,
								DataCompare()); // 通过equal_range查找

if (range.first != range.second)...

... // 结束查找阶段，开始

// 重组阶段

sort(vd.begin(), vd.end(), DataCompare()); // 开始新的查找阶段...
```

###条款24：当效率至关重要时，请在map::operator[]与map::insert之间谨慎作出选择
1.当向映射表中添加元素时，要优先使用insert，当更新已经在映射表中的元素的值时，要优先选用operator[]。

###条款25：熟悉非标准的散列容器
1.C++11里面提供了散列容器
```
unordered_set //（C++11 起）	收集的唯一键，键哈希运算
unordered_map //（C++11 起）	键 - 值对的集合，散列键，键是唯一的
unordered_multiset //（C++11 起）	集合中的密钥，通过键散列
unordered_multimap //（C++11 起）
```

##4.迭代器

###条款26：`iterator`优先于`const_iterator`、`reverse_iterator`及`const_reverse_iterator`
1.尽量使用iterator而不是const或reverse型的迭代器，可以使容器更为简单有效，并且可以避免潜在的问题。

###条款27：使用distance和advance将容器的const_iterator转换成iterator
1.如果只有一个const_iterator如何在该迭代器所指的位置插入一个新的值：
- 不存在const_iterator到iterator的隐式转换
- 强制转换也不行，iterator和const_iterator是完全不同的两个类
- 安全的方案：

```
typedef deque<int> IntDeque;
typedef IntDeque::iterator Iter;
typedef IntDeque::const_iterator ConstIter;

IntDeque d;
ConstIter ci;

... // 让ci指向d

Iter i(d.begin()); // 初始化i为d.begin()

advance(i, distance <ConstIter> (i, ci)); // 把i移到指向ci位置
```

- 所以在使用容器的时候，尽量用iterator来代替const或reverse迭代器，条款26

###条款28：正确理解由reverse_iterator的base()成员函数所产生的iterator的用法

###条款29：对于逐个字符的输入请考虑使用istreambuf_iterator

##5.算法
###条款30：确保目标区间足够大
1.如果使用的算法需要指定一个目标区间，那么必须保证目标区间足够大，或者确保它会随着算法的运行而增大。
```
vector<int> values;
vector<int> results;

results.reserve(results.size() + values.size()); // 预留空间
transform(values.begin(), values.end(), // 把transmogrify的结果
back_inserter(results), // 写入results的结尾，
transmogrify); // 处理时避免了重新分配
```

###条款31：了解各种与排序有关的选择
1.如果需要在vector、string、deque或数组上进行完全排序，你可以使用sort或stable_sort

2.如果有一个vector、string、deque或数组，并且只需要排序前n个元素，应该用partial_sort

3.如果有一个vector、string、deque或数组，并且需要找到第n个位置上的元素或你需要找到最前的n个元素又不必对这个n个元素进行排序，可以采用nth_element

4.如果需要把标准序列容器的元素是否满足某个条件分开，可以考虑partition或stable_partition

5.如果是在list中，可以使用partition和`stable_partition`算法；也可以使用list::sort来代替sort和`stable_sort`。如果需要`partial_sort`或`nth_element`提供的效果,可以间接实现，主要有三种方法：
- 把元素复制到一个支持随机访问迭代器的容器中，然后执行相应的算法。
- 建立一个list::iterator的容器，对那个容器使用算法，然后通过迭代器访问list元素。
- 使用有序的迭代器容器的信息，调用splice成员函数，把list的元素调整到期望的位置。

###条款32：如果确实需要删除元素，则需要在remove这一类算法之后调用erase

1.remove不知道操作元素所在的容器，所以remove不可能从容器中删除元素。
```
vector<int> v;
v.erase(romove(v.begin(), v.end(), 123), v.end()); // 真正删除

list.remove(123); // list::remove是真正删除
```

###条款33：对包含指针的容器使用remove这一类算法时要特别小心
1.删除包含指针的容器元素时，要注意释放指针的所指向的对象，不然会造成内存泄漏

2.可以使用智能指针

###条款34：了解哪些算法要求使用排序区间作为参数
1.STL中要求排序区间的算法有：
- binary_search：二分查找
- lower_bound：下界
- upper_bound：上街
- equal_range：所有等于某个值的元素
- set_union：集合并集
- set_intersection：集合交集
- set_difference ：集合差集
- `set_symmetric_difference`：包含在第一个集合但是不包含在第二个集合中的元素，包含在第2个集合但是不包含在第1个集合中的元素
- merge：合并两个有序表
- inplace_merge：合并两个有序表
- includes：检测一个区间的所有对象是否在另一个区间中

2.下面的算法通常情况下会与有序区间一起使用，但是并不一定要求排序区间
- unique：去重，相同的元素必须紧挨着，排序是个特例
- unique_copy：同上

###条款35：通过mismatch或lexicographical_compare实现简单的忽略大小写的字符串比较

###条款36：理解copy_if算法的正确实现
1.正确实现
```
template<typename InputInterator,
 		 typename OutputInterator,
         typename Predicate>
OutputInterator copy_if(
		InputInterator begin,
        InputInterator end,
        OutputInterator destBegin,
        Predicate p)
{
	while(begin != end)
    {
    	if(p(*begin))
        	*destBegin++ = *begin
    }
    return destBegin;
)
```

###条款37：使用accumulate或for_each进行区间统计

##6.仿函数、仿函数类、函数及其他

###条款38：遵循按值传递的原则来设计仿函数
1.函数对象往往按值传递和返回，需要保证：
- 函数对象必须尽可能的小，减少复制的开销
- 函数对象不能是多态的，不得使用虚函数

###条款39：确保判别式是“纯函数”
1.一个判别式是一个返回值为bool类型（或者可以隐式转换为bool类型）的函数

2.一个纯函数是指返回值仅依赖于其参数的函数

3.判别式类是一个仿函数类，其operator()函数是一个判别式，也就是说它的operator()返回true和false

4.为了避免语言实现细节上的陷阱，在判别式类中，将operator()的函数声明为const

###条款40：若一个类是仿函数，则应使它可适配

###条款41：理解`ptr_fun`、`mem_fun`和`mem_fun_ref`的来由

###条款42：确保`less<T>`与`operator<`具有相同的语义
1.operator<是less的默认实现方式，也是程序员期望less所做的事情

##7.在程序中使用STL

###条款43：算法调用优先于手写的循环
1.三个理由：
- 效率：算法通常比程序员自己写的循环效率更高
- 正确性：自己写循环比使用算法更容易出错
- 可维护性：使用算法的代码通常比手写循环的代码更加简洁明了

###条款44：容器的成员函数优先于同名的算法

###条款45：正确区分`count`、`find`、`binary_search`、`lower_bound`、`upper_bound`和`equal_range`


###条款46：考虑使用函数对象而不是函数作为STL算法的参数

###条款47：避免产生“直写型”代码

###条款48：总是#include正确的头文件

###条款49：学习分析与STL相关的编译器诊断信息

###条款50：熟悉有关STL的网站
1.推荐的网站
- SGI STL： [http://www.sgi.com/tech/stl/](http://www.sgi.com/tech/stl/)
- STLport： [http://www.stlport.org/](http://www.stlport.org/)
- Boost：[http://www.boost.org/](http://www.boost.org/)




