# Python 函数式编程指南

这大概算是Python最难啃的一块骨头吧。在我Python生涯的这一年里，我遇到了一些Pythoner，他们毫无例外地完全不会使用函数式编程（有些人喜欢称为Pythonic），比如，从来不会传递函数，不知道lambda是什么意思，知道列表展开但从来不知道用在哪里，对Python不提供经典for循环感到无所适从，言谈之中表现出对函数式风格的一种抗拒甚至厌恶。

我尝试剖析这个问题，最终总结了这么两个原因：1、不想改变，认为现有的知识可以完成任务；2、对小众语言的歧视，Python目前在国内市场份额仍然很小很小，熟悉Python风格用处不大。

然而我认为，学习使用一种截然不同的风格可以颠覆整个编程的思想。我会慢慢总结一个系列共4篇文字，篇幅都不大，轻松就能看完，希望对喜欢Python的人们有所帮助，因为我个人确实从中受益匪浅。

## 一 概述

### 什么是函数式编程？

函数式编程使用一系列的函数解决问题。函数仅接受输入并产生输出，不包含任何能影响产生输出的内部状态。任何情况下，使用相同的参数调用函数始终能产生同样的结果。

在一个函数式的程序中，输入的数据"流过"一系列的函数，每一个函数根据它的输入产生输出。函数式风格避免编写有"边界效应"(side effects)的函数：修改内部状态，或者是其他无法反应在输出上的变化。完全没有边界效应的函数被称为"纯函数式的"(purely functional)。避免边界效应意味着不使用在程序运行时可变的数据结构，输出只依赖于输入。

可以认为函数式编程刚好站在了面向对象编程的对立面。对象通常包含内部状态（字段），和许多能修改这些状态的函数，程序则由不断修改状态构成；函数式编程则极力避免状态改动，并通过在函数间传递数据流进行工作。但这并不是说无法同时使用函数式编程和面向对象编程，事实上，复杂的系统一般会采用面向对象技术建模，但混合使用函数式风格还能让你额外享受函数式风格的优点。

### 为什么使用函数式编程？

函数式的风格通常被认为有如下优点：
- 逻辑可证
  - 这是一个学术上的优点：没有边界效应使得更容易从逻辑上证明程序是正确的（而不是通过测试）。

- 模块化
  - 函数式编程推崇简单原则，一个函数只做一件事情，将大的功能拆分成尽可能小的模块。小的函数更易于阅读和检查错误。

- 组件化
  - 小的函数更容易加以组合形成新的功能。

- 易于调试
  - 细化的、定义清晰的函数使得调试更加简单。当程序不正常运行时，每一个函数都是检查数据是否正确的接口，能更快速地排除没有问题的代码，定位到出现问题的地方。

- 易于测试
  - 不依赖于系统状态的函数无须在测试前构造测试桩，使得编写单元测试更加容易。

- 更高的生产率
  - 函数式编程产生的代码比其他技术更少（往往是其他技术的一半左右），并且更容易阅读和维护。

### 如何辨认函数式风格？

支持函数式编程的语言通常具有如下特征，大量使用这些特征的代码即可被认为是函数式的：

**函数是一等公民**

函数能作为参数传递，或者是作为返回值返回。这个特性使得模板方法模式非常易于编写，这也促使了这个模式被更频繁地使用。

以一个简单的集合排序为例，假设lst是一个数集，并拥有一个排序方法sort需要将如何确定顺序作为参数。

如果函数不能作为参数，那么lst的sort方法只能接受普通对象作为参数。这样一来我们需要首先定义一个接口，然后定义一个实现该接口的类，最后将该类的一个实例传给sort方法，由sort调用这个实例的compare方法，就像这样：

```python
#伪代码
interface Comparator {
    compare(o1, o2)
}
lst = list(range(5))
lst.sort(Comparator() {
    compare(o1, o2) {
        return o2 - o1 //逆序
})
```

可见，我们定义了一个新的接口、新的类型（这里是一个匿名类），并new了一个新的对象只为了调用一个方法。如果这个方法可以直接作为参数传递会怎样呢？看起来应该像这样：

```python
def compare(o1, o2):
    return o2 - o1 #逆序
lst = list(range(5))
lst.sort(compare)
```

请注意，前一段代码已经使用了匿名类技巧从而省下了不少代码，但仍然不如直接传递函数简单、自然。

**匿名函数(lambda)**

lambda提供了快速编写简单函数的能力。对于偶尔为之的行为，lambda让你不再需要在编码时跳转到其他位置去编写函数。

lambda表达式定义一个匿名的函数，如果这个函数仅在编码的位置使用到，你可以现场定义、直接使用：

```python
lst.sort(lambda o1, o2: o1.compareTo(o2))
```

相信从这个小小的例子你也能感受到强大的生产效率：）

**封装控制结构的内置模板函数**

为了避开边界效应，函数式风格尽量避免使用变量，而仅仅为了控制流程而定义的循环变量和流程中产生的临时变量无疑是最需要避免的。

假如我们需要对刚才的数集进行过滤得到所有的正数，使用指令式风格的代码应该像是这样：

```python
lst2 = list()
for i in range(len(lst)): #模拟经典for循环
    if lst[i] > 0:
        lst2.append(lst[i])
```

这段代码把从创建新列表、循环、取出元素、判断、添加至新列表的整个流程完整的展示了出来，俨然把解释器当成了需要手把手指导的傻瓜。然而，"过滤"这个动作是很常见的，为什么解释器不能掌握过滤的流程，而我们只需要告诉它过滤规则呢？

在Python里，过滤由一个名为filter的内置函数实现。有了这个函数，解释器就学会了如何"过滤"，而我们只需要把规则告诉它：

```python
lst2 = filter(lambda n: n > 0, lst)
```

这个函数带来的好处不仅仅是少写了几行代码这么简单。

封装控制结构后，代码中就只需要描述功能而不是做法，这样的代码更清晰，更可读。因为避开了控制结构的干扰，第二段代码显然能让你更容易了解它的意图。

另外，因为避开了索引，使得代码中不太可能触发下标越界这种异常，除非你手动制造一个。

函数式编程语言通常封装了数个类似"过滤"这样的常见动作作为模板函数。唯一的缺点是这些函数需要少量的学习成本，但这绝对不能掩盖使用它们带来的好处。

**闭包(closure)**

闭包是绑定了外部作用域的变量（但不是全局变量）的函数。大部分情况下外部作用域指的是外部函数。

闭包包含了自身函数体和所需外部函数中的"变量名的引用"。引用变量名意味着绑定的是变量名，而不是变量实际指向的对象；如果给变量重新赋值，闭包中能访问到的将是新的值。

闭包使函数更加灵活和强大。即使程序运行至离开外部函数，如果闭包仍然可见，则被绑定的变量仍然有效；每次运行至外部函数，都会重新创建闭包，绑定的变量是不同的，不需要担心在旧的闭包中绑定的变量会被新的值覆盖。

回到刚才过滤数集的例子。假设过滤条件中的 0 这个边界值不再是固定的，而是由用户控制。如果没有闭包，那么代码必须修改为：

```python
class greater_than_helper:
    def __init__(self, minval):
        self.minval = minval
    def is_greater_than(self, val):
        return val > self.minval

def my_filter(lst, minval):
    helper = greater_than_helper(minval)
    return filter(helper.is_greater_than, lst)
```

请注意我们现在已经为过滤功能编写了一个函数my_filter。如你所见，我们需要在别的地方（此例中是类greater_than_helper）持有另一个操作数minval。

如果支持闭包，因为闭包可以直接使用外部作用域的变量，我们就不再需要greater_than_helper了：

```python
def my_filter(lst, minval):
    return filter(lambda n: n > minval, lst)
```

可见，闭包在不影响可读性的同时也省下了不少代码量。

函数式编程语言都提供了对闭包的不同程度的支持。在Python 2.x中，闭包无法修改绑定变量的值，所有修改绑定变量的行为都被看成新建了一个同名的局部变量并将绑定变量隐藏。Python 3.x中新加入了一个关键字 nonlocal 以支持修改绑定变量。但不管支持程度如何，你始终可以访问（读取）绑定变量。

**内置的不可变数据结构**

为了避开边界效应，不可变的数据结构是函数式编程中不可或缺的部分。不可变的数据结构保证数据的一致性，极大地降低了排查问题的难度。

例如，Python中的元组(tuple)就是不可变的，所有对元组的操作都不能改变元组的内容，所有试图修改元组内容的操作都会产生一个异常。

函数式编程语言一般会提供数据结构的两种版本（可变和不可变），并推荐使用不可变的版本。

**递归**

递归是另一种取代循环的方法。递归其实是函数式编程很常见的形式，经常可以在一些算法中见到。但之所以放到最后，是因为实际上我们一般很少用到递归。如果一个递归无法被编译器或解释器优化，很容易就会产生栈溢出；另一方面复杂的递归往往让人感觉迷惑，不如循环清晰，所以众多最佳实践均指出使用循环而非递归。

这一系列短文中都不会关注递归的使用。

## 二 函数

### 定义一个函数

如下定义了一个求和函数：

```python
def add(x, y):
    return x + y
```

关于参数和返回值的语法细节可以参考其他文档，这里就略过了。

使用lambda可以定义简单的单行匿名函数。lambda的语法是：

```
lambda args: expression
```

参数(args)的语法与普通函数一样，同时表达式(expression)的值就是匿名函数调用的返回值；而lambda表达式返回这个匿名函数。如果我们给匿名函数取个名字，就像这样：

```
lambda_add = lambda x, y: x + y
```

这与使用def定义的求和函数完全一样，可以使用lambda_add作为函数名进行调用。然而，提供lambda的目的是为了编写偶尔为之的、简单的、可预见不会被修改的匿名函数。这种风格虽然看起来很酷，但并不是一个好主意，特别是当某一天需要对它进行扩充，再也无法用一个表达式写完时。如果一开始就需要给函数命名，应该始终使用def关键字。

### 使用函数赋值

事实上你已经见过了，上一节中我们将lambda表达式赋值给了add。同样，使用def定义的函数也可以赋值，相当于为函数取了一个别名，并且可以使用这个别名调用函数：

```python
add_a_number_to_another_one_by_using_plus_operator = add
print add_a_number_to_another_one_by_using_plus_operator(1, 2)
```

既然函数可以被变量引用，那么将函数作为参数和返回值就是很寻常的做法了。

### 闭包

闭包是一类特殊的函数。如果一个函数定义在另一个函数的作用域中，并且函数中引用了外部函数的局部变量，那么这个函数就是一个闭包。下面的代码定义了一个闭包：

```python
def f():
    n = 1
    def inner():
        print n
    inner()
    n = 'x'
    inner()
```

函数inner定义在f的作用域中，并且在inner中使用了f中的局部变量n，这就构成了一个闭包。闭包绑定了外部的变量，所以调用函数f的结果是打印1和'x'。这类似于普通的模块函数和模块中定义的全局变量的关系：修改外部变量能影响内部作用域中的值，而在内部作用域中定义同名变量则将遮蔽（隐藏）外部变量。

如果需要在函数中修改全局变量，可以使用关键字global修饰变量名。Python 2.x中没有关键字为在闭包中修改外部变量提供支持，在3.x中，关键字nonlocal可以做到这一点：

```python
#Python 3.x supports `nonlocal'
def f():
    n = 1
    def inner():
        nonlocal n
        n = 'x'
    print(n)
    inner()
    print(n)
```

调用这个函数的结果是打印1和'x'，如果你有一个Python 3.x的解释器，可以试着运行一下。

由于使用了函数体外定义的变量，看起来闭包似乎违反了函数式风格的规则即不依赖外部状态。但是由于闭包绑定的是外部函数的局部变量，而一旦离开外部函数作用域，这些局部变量将无法再从外部访问；另外闭包还有一个重要的特性，每次执行至闭包定义处时都会构造一个新的闭包，这个特性使得旧的闭包绑定的变量不会随第二次调用外部函数而更改。所以闭包实际上不会被外部状态影响，完全符合函数式风格的要求。（这里有一个特例，Python 3.x中，如果同一个作用域中定义了两个闭包，由于可以修改外部变量，他们可以相互影响。）

虽然闭包只有在作为参数和返回值时才能发挥它的真正威力，但闭包的支持仍然大大提升了生产率。

### 作为参数

如果你对OOP的模板方法模式很熟悉，相信你能很快速地学会将函数当作参数传递。两者大体是一致的，只是在这里，我们传递的是函数本身而不再是实现了某个接口的对象。

我们先来给前面定义的求和函数add热热身：

```python
print add('三角形的树', '北极')
```

与加法运算符不同，你一定很惊讶于答案是'三角函数'。这是一个内置的彩蛋...bazinga!

言归正传。我们的客户有一个从0到4的列表：

```python
lst = range(5) #[0, 1, 2, 3, 4]
```

虽然我们在上一小节里给了他一个加法器，但现在他仍然在为如何计算这个列表所有元素的和而苦恼。当然，对我们而言这个任务轻松极了：

```python
amount = 0
for num in lst:
    amount = add(amount, num)
```

这是一段典型的指令式风格的代码，一点问题都没有，肯定可以得到正确的结果。现在，让我们试着用函数式的风格重构一下。

首先可以预见的是求和这个动作是非常常见的，如果我们把这个动作抽象成一个单独的函数，以后需要对另一个列表求和时，就不必再写一遍这个套路了：

```python
def sum_(lst):
    amount = 0
    for num in lst:
        amount = add(amount, num)
    return amount

print sum_(lst)
```

还能继续。sum_函数定义了这样一种流程：
1. 使用初始值与列表的第一个元素相加；
2. 使用上一次相加的结果与列表的下一个元素相加；
3. 重复第二步，直到列表中没有更多元素；
4. 将最后一次相加的结果返回。

如果现在需要求乘积，我们可以写出类似的流程----只需要把相加换成相乘就可以了：

```python
def multiply(lst):
    product = 1
    for num in lst:
        product = product * num
    return product
```

除了初始值换成了1以及函数add换成了乘法运算符，其他的代码全部都是冗余的。我们为什么不把这个流程抽象出来，而将加法、乘法或者其他的函数作为参数传入呢？

```python
def reduce_(function, lst, initial):
    result = initial
    for num in lst:
        result = function(result, num)
    return result

print reduce_(add, lst, 0)
```

现在，想要算出乘积，可以这样做：

```python
print reduce_(lambda x, y: x * y, lst, 1)
```

那么，如果想要利用reduce_找出列表中的最大值，应该怎么做呢？请自行思考：）

虽然有模板方法这样的设计模式，但那样的复杂度往往使人们更情愿到处编写循环。将函数作为参数完全避开了模板方法的复杂度。

Python有一个内建函数reduce，完整实现并扩展了reduce_的功能。本文稍后的部分包含了有用的内建函数的介绍。请注意我们的目的是没有循环，使用函数替代循环是函数式风格区别于指令式风格的最显而易见的特征。

*像Python这样构建于类C语言之上的函数式语言，由于语言本身提供了编写循环代码的能力，内置函数虽然提供函数式编程的接口，但一般在内部还是使用循环实现的。同样的，如果发现内建函数无法满足你的循环需求，不妨也封装它，并提供一个接口。

### 作为返回值

将函数返回通常需要与闭包一起使用（即返回一个闭包）才能发挥威力。我们先看一个函数的定义：

```python
def map_(function, lst):
    result = []
    for item in lst:
        result.append(function(item))
    return result
```

函数`map_`封装了最常见的一种迭代：对列表中的每个元素调用一个函数。`map_`需要一个函数参数，并将每次调用的结果保存在一个列表中返回。这是指令式的做法，当你知道了列表解析(list comprehension)后，会有更好的实现。

这里我们先略过`map_`的蹩脚实现而只关注它的功能。对于上一节中的lst，你可能发现最后求乘积结果始终是0，因为lst中包含了0。为了让结果看起来足够大，我们来使用map_为lst中的每个元素加1：

```python
lst = map_(lambda x: add(1, x), lst) 
print reduce_(lambda x, y: x * y, lst, 1) 
```

答案是120，这还远远不够大。再来：

```python
lst = map_(lambda x: add(10, x), lst) 
print reduce_(lambda x, y: x * y, lst, 1) 
```

囧，事实上我真的没有想到答案会是360360，我发誓没有收周鸿祎任何好处。

现在回头看看我们写的两个lambda表达式：相似度超过90%，绝对可以使用抄袭来形容。而问题不在于抄袭，在于多写了很多字符有木有？如果有一个函数，根据你指定的左操作数，能生成一个加法函数，用起来就像这样：

```python
lst = map_(add_to(10), lst) 
#add_to(10)返回一个函数，这个函数接受一个参数并加上10后返回 
```

写起来应该会舒服不少。下面是函数add_to的实现：

```python
def add_to(n):     
	return lambda x: add(n, x) 
```
	
通过为已经存在的某个函数指定数个参数，生成一个新的函数，这个函数只需要传入剩余未指定的参数就能实现原函数的全部功能，这被称为偏函数。Python内置的functools模块提供了一个函数partial，可以为任意函数生成偏函数：

	functools.partial(func[, _args][, *_keywords]) 
	
你需要指定要生成偏函数的函数、并且指定数个参数或者命名参数，然后partial将返回这个偏函数；不过严格的说partial返回的不是函数，而是一个像函数一样可直接调用的对象，当然，这不会影响它的功能。

另外一个特殊的例子是装饰器，装饰器用于增强甚至干脆改变原函数的功能。

*题外话，单就例子中的这个功能而言，在一些其他的函数式语言中（例如Scala）可以使用名为柯里化(Currying)的技术实现得更优雅。柯里化是把接受多个参数的函数变换成接受一个单一参数（最初函数的第一个参数）的函数，并且返回接受余下的参数而且返回结果的新函数的技术。如下的伪代码所示：

```scala
#不是真实的代码 
def add(x)(y): #柯里化     
	return x + y

lst = map_(add(10), lst) 
```
通过将add函数柯里化，使得add接受第一个参数x，并返回一个接受第二个参数y的函数，调用该函数与前文中的`add_to`完全相同（返回x + y），且不再需要定义`add_to`。看上去是不是更加清爽呢？遗憾的是Python并不支持柯里化。

### 部分内建函数介绍

	reduce(function, iterable[, initializer]) 

这个函数的主要功能与我们定义的reduce_相同。需要补充两点： 

+ 它的第二个参数可以是任何可迭代的对象（实现了__iter__()方法的对象）； 
+ 如果不指定第三个参数，则第一次调用function将使用iterable的前两个元素作为参数。 

由reduce和一些常见的function组合成了下面列出来的内置函数：

```python
all(iterable) == reduce(lambda x, y: bool(x and y), iterable)
any(iterable) == reduce(lambda x, y: bool(x or y), iterable)
max(iterable[, args...][, key]) == reduce(lambda x, y: x if key(x) > key(y) else y, iterable_and_args)
min(iterable[, args...][, key]) == reduce(lambda x, y: x if key(x) < key(y) else y, iterable_and_args)
sum(iterable[, start]) == reduce(lambda x, y: x + y, iterable, start)
```

	map(function, iterable, ...) 

这个函数的主要功能与我们定义的`map_`相同。需要补充一点： 

map还可以接受多个iterable作为参数，在第n次调用function时，将使用iterable1[n], iterable2[n], ...作为参数。

	filter(function, iterable) 

这个函数的功能是过滤出iterable中所有以元素自身作为参数调用function时返回True或bool(返回值)为True的元素并以列表返回，与系列第一篇中的`my_filter`函数相同。

	zip(iterable1, iterable2, ...) 

这个函数返回一个列表，每个元素都是一个元组，包含`(iterable1[n], iterable2[n], ...)`。 

例如：`zip([1, 2], [3, 4]) --> [(1, 3), (2, 4)] `

如果参数的长度不一致，将在最短的序列结束时结束；如果不提供参数，将返回空列表。

## 三 迭代器

### 迭代器(Iterator)概述

迭代器是访问集合内元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素都被访问一遍后结束。

迭代器不能回退，只能往前进行迭代。这并不是什么很大的缺点，因为人们几乎不需要在迭代途中进行回退操作。

迭代器也不是线程安全的，在多线程环境中对可变集合使用迭代器是一个危险的操作。但如果小心谨慎，或者干脆贯彻函数式思想坚持使用不可变的集合，那这也不是什么大问题。

对于原生支持随机访问的数据结构（如tuple、list），迭代器和经典for循环的索引访问相比并无优势，反而丢失了索引值（可以使用内建函数enumerate()找回这个索引值，这是后话）。但对于无法随机访问的数据结构（比如set）而言，迭代器是唯一的访问元素的方式。

迭代器的另一个优点就是它不要求你事先准备好整个迭代过程中所有的元素。迭代器仅仅在迭代至某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。这个特点使得它特别适合用于遍历一些巨大的或是无限的集合，比如几个G的文件，或是斐波那契数列等等。这个特点被称为延迟计算或惰性求值(Lazy evaluation)。

迭代器更大的功劳是提供了一个统一的访问集合的接口。只要是实现了__iter__()方法的对象，就可以使用迭代器进行访问。

### 使用迭代器

使用内建的工厂函数iter(iterable)可以获取迭代器对象：

```python
>>> lst = range(2)
>>> it = iter(lst)
>>> it
<listiterator object at 0x00BB62F0>
```

使用迭代器的next()方法可以访问下一个元素：

```python
>>> it.next()
0
```

如果是Python 2.6+，还有内建函数next(iterator)可以完成这一功能：

```python
>>> next(it) 
1
```

如何判断迭代器还有更多的元素可以访问呢？Python里的迭代器并没有提供类似has_next()这样的方法。 

那么在这个例子中，我们已经访问到了最后一个元素1，再使用next()方法会怎样呢？

```python
>>> it.next() 
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module> 
StopIteration
```

Python遇到这样的情况时将会抛出StopIteration异常。事实上，Python正是根据是否检查到这个异常来决定是否停止迭代的。 

这种做法与迭代前手动检查是否越界相比各有优点。但Python的做法总有一些利用异常进行流程控制的嫌疑。

了解了这些情况以后，我们就能使用迭代器进行遍历了。

```python
it = iter(lst)
try:
    while True:
        val = it.next()
        print val
except StopIteration:
    pass
```

实际上，因为迭代操作如此普遍，Python专门将关键字for用作了迭代器的语法糖。在for循环中，Python将自动调用工厂函数iter()获得迭代器，自动调用next()获取元素，还完成了检查StopIteration异常的工作。上述代码可以写成如下的形式，你一定非常熟悉：

```python
for val in lst:
    print val
```

首先Python将对关键字in后的对象调用iter函数获取迭代器，然后调用迭代器的next方法获取元素，直到抛出StopIteration异常。对迭代器调用iter函数时将返回迭代器自身，所以迭代器也可以用于for语句中，不需要特殊处理。

常用的几个内建数据结构tuple、list、set、dict都支持迭代器，字符串也可以使用迭代操作。你也可以自己实现一个迭代器，如上所述，只需要在类的__iter__方法中返回一个对象，这个对象拥有一个next()方法，这个方法能在恰当的时候抛出StopIteration异常即可。但是需要自己实现迭代器的时候不多，即使需要，使用生成器会更轻松。下一篇我们将讨论生成器的部分。

*异常并不是非抛出不可的，不抛出该异常的迭代器将进行无限迭代，某些情况下这样的迭代器很有用。这种情况下，你需要自己判断元素并中止，否则就死循环了！

使用迭代器的循环可以避开索引，但有时候我们还是需要索引来进行一些操作的。这时候内建函数enumerate就派上用场咯，它能在iter函数的结果前加上索引，以元组返回，用起来就像这样：

```python
for idx, ele in enumerate(lst):
    print idx, ele
```

### 生成器表达式(Generator expression)和列表解析(List Comprehension)

绝大多数情况下，遍历一个集合都是为了对元素应用某个动作或是进行筛选。如果看过本文的第二部分，你应该还记得有内建函数map和filter提供了这些功能，但Python仍然为这些操作提供了语言级的支持。

```python
(x+1 for x in lst) #生成器表达式，返回迭代器。外部的括号可在用于参数时省略。 
[x+1 for x in lst] #列表解析，返回list
```

如你所见，生成器表达式和列表解析（注：这里的翻译有很多种，比如列表展开、列表推导等等，指的是同一个意思）的区别很小，所以人们提到这个特性时，简单起见往往只描述成列表解析。然而由于返回迭代器时，并不是在一开始就计算所有的元素，这样能得到更多的灵活性并且可以避开很多不必要的计算，所以除非你明确希望返回列表，否则应该始终使用生成器表达式。接下来的文字里我就不区分这两种形式了：）

你也可以为列表解析提供if子句进行筛选：

	(x+1 for x in lst if x!=0)

或者提供多条for子句进行嵌套循环，嵌套次序就是for子句的顺序：

	((x, y) for x in range(3) for y in range(x))

列表解析就是鲜明的Pythonic。我常遇到两个使用列表解析的问题，本应归属于最佳实践，但这两个问题非常典型，所以不妨在这里提一下：

第一个问题是，因为对元素应用的动作太复杂，不能用一个表达式写出来，所以不使用列表解析。这是典型的思想没有转变的例子，如果我们将动作封装成函数，那不就是一个表达式了么？

第二个问题是，因为if子句里的条件需要计算，同时结果也需要进行同样的计算，不希望计算两遍，就像这样：

	(x.doSomething() for x in lst if x.doSomething()>0)

这样写确实很糟糕，但组合一下列表解析即可解决：

	(x for x in (y.doSomething() for y in lst) if x>0)

内部的列表解析变量其实也可以用x，但为清晰起见我们改成了y。或者更清楚的，可以写成两个表达式：

	tmp = (x.doSomething() for x in lst)
	(x for x in tmp if x > 0)

列表解析可以替代绝大多数需要用到map和filter的场合，可能正因为此，著名的静态检查工具pylint将map和filter的使用列为了警告。

### 相关的库

Python内置了一个模块itertools，包含了很多函数用于creating iterators for efficient looping（创建更有效率的循环迭代器），这说明很是霸气，这一小节就来浏览一遍这些函数并留下印象吧，需要这些功能的时候隐约记得这里面有就好。这一小节的内容翻译自itertools模块官方文档。

####  无限迭代

+ count(start, [step]) 
	+ 从start开始，以后每个元素都加上step。step默认值为1。 
+ count(10) --> 10 11 12 13 14 ...
+ cycle(p) 
	+ 迭代至序列p的最后一个元素后，从p的第一个元素重新开始。 
+ cycle('ABCD') --> A B C D A B C D ...
+ repeat(elem [,n]) 
	+ 将elem重复n次。如果不指定n，则无限重复。 
	+ repeat(10, 3) --> 10 10 10

#### 在最短的序列参数终止时停止迭代

+ chain(p, q, ...) 
	+ 迭代至序列p的最后一个元素后，从q的第一个元素开始，直到所有序列终止。 
+ chain('ABC', 'DEF') --> A B C D E F
+ compress(data, selectors) 
	+ 如果bool(selectors[n])为True，则next()返回data[n]，否则跳过data[n]。 
+ compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
+ dropwhile(pred, seq) 
	+ 当pred对seq[n]的调用返回False时才开始迭代。 
+ dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
+ takewhile(pred, seq) 
	+ dropwhile的相反版本。 
	+ takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
+ ifilter(pred, seq) 
	+ 内建函数filter的迭代器版本。 
	+ ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
+ ifilterfalse(pred, seq) 
	+ ifilter的相反版本。 
	+ ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
+ imap(func, p, q, ...) 
	+ 内建函数map的迭代器版本。 
	+ imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
+ starmap(func, seq) 
	+ 将seq的每个元素以变长参数(*args)的形式调用func。 
	+ starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
+ izip(p, q, ...) 
	+ 内建函数zip的迭代器版本。 
	+ izip('ABCD', 'xy') --> Ax By
	+ izip_longest(p, q, ..., fillvalue=None) 
	+ izip的取最长序列的版本，短序列将填入fillvalue。 
	+ `izip_longest`('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
+ tee(it, n) 
	+ 返回n个迭代器it的复制迭代器。
+ groupby(iterable[, keyfunc]) 
	+ 这个函数功能类似于SQL的分组。使用groupby前，首先需要使用相同的keyfunc对iterable进行排序，比如调用内建的sorted函数。然后，groupby返回迭代器，每次迭代的元素是元组(key值, iterable中具有相同key值的元素的集合的子迭代器)。或许看看Python的排序指南对理解这个函数有帮助。 
	+ groupby([0, 0, 0, 1, 1, 1, 2, 2, 2]) --> (0, (0 0 0)) (1, (1 1 1)) (2, (2 2 2))

#### 组合迭代器

+ product(p, q, ... [repeat=1]) 
	+ 笛卡尔积。 
	+ product('ABCD', repeat=2) --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
+ permutations(p[, r]) 
	+ 排列。 
	+ permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
+ combinations(p, r) 
	+ 组合。 
	+ combinations('ABCD', 2) --> AB AC AD BC BD CD
+ `combinations_with_replacement() `
	+ 组合 有重复 
	+ `combinations_with_replacement('ABCD', 2)` --> AA AB AC AD BB BC BD CC CD DD

## 四 生成器(generator)

### 生成器简介

首先请确信，生成器就是一种迭代器。生成器拥有next方法并且行为与迭代器完全相同，这意味着生成器也可以用于Python的for循环中。另外，对于生成器的特殊语法支持使得编写一个生成器比自定义一个常规的迭代器要简单不少，所以生成器也是最常用到的特性之一。

从Python 2.5开始，的实现为生成器加入了更多的特性，这意味着生成器还可以完成更多的工作。这部分我们会在稍后的部分介绍。

### 生成器函数

#### 使用生成器函数定义生成器

如何获取一个生成器？首先来看一小段代码：

```python
>>> def get_0_1_2():
...   yield 0
...   yield 1
...   yield 2
...
>>> get_0_1_2
<function get_0_1_2 at 0x00B2CB70>
```
我们定义了一个函数`get_0_1_2`，并且可以查看到这确实是函数类型。但与一般的函数不同的是，`get_0_1_2`的函数体内使用了关键字yield，这使得`get_0_1_2`成为了一个生成器函数。生成器函数的特性如下：

调用生成器函数将返回一个生成器；

```python
>>> generator = get_0_1_2()
>>> generator
<generator object get_0_1_2 at 0x00B1C7D8>
```

第一次调用生成器的next方法时，生成器才开始执行生成器函数（而不是构建生成器时），直到遇到yield时暂停执行（挂起），并且yield的参数将作为此次next方法的返回值；

```pyton
>>> generator.next()
0
```

之后每次调用生成器的next方法，生成器将从上次暂停执行的位置恢复执行生成器函数，直到再次遇到yield时暂停，并且同样的，yield的参数将作为next方法的返回值；

```python
>>> generator.next()
1
>>> generator.next()
2
```

如果当调用next方法时生成器函数结束（遇到空的return语句或是到达函数体末尾），则这次next方法的调用将抛出StopIteration异常（即for循环的终止条件）；

```python
>>> generator.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

生成器函数在每次暂停执行时，函数体内的所有变量都将被封存(freeze)在生成器中，并将在恢复执行时还原，并且类似于闭包，即使是同一个生成器函数返回的生成器，封存的变量也是互相独立的。 

我们的小例子中并没有用到变量，所以这里另外定义一个生成器来展示这个特点：

```python
>>> def fibonacci():
...   a = b = 1
...   yield a
...   yield b
...   while True:
...     a, b = b, a+b
...     yield b
...
>>> for num in fibonacci():
...   if num > 100: break
...   print num,
...
1 1 2 3 5 8 13 21 34 55 89
```

看到while True可别太吃惊，因为生成器可以挂起，所以是延迟计算的，无限循环并没有关系。这个例子中我们定义了一个生成器用于获取斐波那契数列。

### 生成器函数的FAQ

接下来我们来讨论一些关于生成器的有意思的话题。

你的例子里生成器函数都没有参数，那么生成器函数可以带参数吗？ 
当然可以啊亲，而且它支持函数的所有参数形式。要知道生成器函数也是函数的一种：）

```python
>>> def counter(start=0):
...   while True:
...     yield start
...     start += 1
...
```

这是一个从指定数开始的计数器。

既然生成器函数也是函数，那么它可以使用return输出返回值吗？ 

不行的亲，是这样的，生成器函数已经有默认的返回值——生成器了，你不能再另外给一个返回值；对，即使是return None也不行。但是它可以使用空的return语句结束。如果你坚持要为它指定返回值，那么Python将在定义的位置赠送一个语法错误异常，就像这样：

```python
>>> def i_wanna_return():
...   yield None
...   return None
...
  File "<stdin>", line 3
SyntaxError: 'return' with argument inside generator
```

好吧，那人家需要确保释放资源，需要在try...finally中yield，这会是神马情况？（我就是想玩你）我在finally中还yield了一次！ 

Python会在真正离开try...finally时再执行finally中的代码，而这里遗憾地告诉你，暂停不算哦！所以结局你也能猜到吧！

```python
>>> def play_u():
...   try:
...     yield 1
...     yield 2
...     yield 3
...   finally:
...     yield 0
...
>>> for val in play_u(): print val,
...
1 2 3 0
```

这与return的情况不同。return是真正的离开代码块，所以会在return时立刻执行finally子句。 

另外，“在带有finally子句的try块中yield”定义在PEP 342中，这意味着只有Python 2.5以上版本才支持这个语法，在Python 2.4以下版本中会得到语法错误异常。

如果我需要在生成器的迭代过程中接入另一个生成器的迭代怎么办？写成下面这样好傻好天真。。

```python
>>> def sub_generator():
...   yield 1
...   yield 2
...   for val in counter(10): yield val
...
```

这种情况的语法改进已经被定义在[PEP 380：委托至子生成器的语法]中，据说会在Python 3.3中实现，届时也可能回馈到2.x中。实现后，就可以这么写了：

```pyrhon
>>> def sub_generator():
...   yield 1
...   yield 2
...   yield from counter(10)
  File "<stdin>", line 4
    yield from counter(10)
             ^
SyntaxError: invalid syntax
```

看到语法错误木有？现在我们还是天真一点吧~

###  协同程序(coroutine)

协同程序（协程）一般来说是指这样的函数：

+ 彼此间有不同的局部变量、指令指针，但仍共享全局变量；
+ 可以方便地挂起、恢复，并且有多个入口点和出口点；
+ 多个协同程序间表现为协作运行，如A的运行过程中需要B的结果才能继续执行。

协程的特点决定了同一时刻只能有一个协同程序正在运行（忽略多线程的情况）。得益于此，协程间可以直接传递对象而不需要考虑资源锁、或是直接唤醒其他协程而不需要主动休眠，就像是内置了锁的线程。在符合协程特点的应用场景，使用协程无疑比使用线程要更方便。

从另一方面说，协程无法并发其实也将它的应用场景限制在了一个很狭窄的范围，这个特点使得协程更多的被拿来与常规函数进行比较，而不是与线程。当然，线程比协程复杂许多，功能也更强大，所以我建议大家牢牢地掌握线程即可：Python线程指南

这一节里我也就不列举关于协程的例子了，以下介绍的方法了解即可。

Python 2.5对生成器的增强实现了协程的其他特点，在这个版本中，生成器加入了如下方法：

	send(value): 

send是除next外另一个恢复生成器的方法。Python 2.5中，yield语句变成了yield表达式，这意味着yield现在可以有一个值，而这个值就是在生成器的send方法被调用从而恢复执行时，调用

send方法的参数。 

```python
>>> def repeater():
...   n = 0
...   while True:
...     n = (yield n)
...
>>> r = repeater()
>>> r.next()
0
>>> r.send(10)
10
```

+ 调用send传入非None值前，生成器必须处于挂起状态，否则将抛出异常。不过，未启动的生成器仍可以使用None作为参数调用send。 
+ 如果使用next恢复生成器，yield表达式的值将是None。

	close(): 

这个方法用于关闭生成器。对关闭的生成器后再次调用next或send将抛出StopIteration异常。
throw(type, value=None, traceback=None): 

这个方法用于在生成器内部（生成器的当前挂起处，或未启动时在定义处）抛出一个异常。

+ 别为没见到协程的例子遗憾，协程最常见的用处其实就是生成器。

### 一个有趣的库：pipe

这一节里我要向诸位简要介绍pipe。pipe并不是Python内置的库，如果你安装了easy_install，直接可以安装它，否则你需要自己下载它：http://pypi.python.org/pypi/pipe

之所以要介绍这个库，是因为它向我们展示了一种很有新意的使用迭代器和生成器的方式：流。pipe将可迭代的数据看成是流，类似于linux，pipe使用'|'传递数据流，并且定义了一系列的“流处理”函数用于接受并处理数据流，并最终再次输出数据流或者是将数据流归纳得到一个结果。我们来看一些例子。

第一个，非常简单的，使用add求和：

```python
>>> from pipe import *
>>> range(5) | add
10
```

求偶数和需要使用到where，作用类似于内建函数filter，过滤出符合条件的元素：

```python
>>> range(5) | where(lambda x: x % 2 == 0) | add
6
```

还记得我们定义的斐波那契数列生成器吗？求出数列中所有小于10000的偶数和需要用到take_while，与itertools的同名函数有类似的功能，截取元素直到条件不成立：

```python
>>> fib = fibonacci
>>> fib() | where(lambda x: x % 2 == 0)\
...       | take_while(lambda x: x < 10000)\
...       | add
3382
```

需要对元素应用某个函数可以使用select，作用类似于内建函数map；需要得到一个列表，可以使用as_list：

```python
>>> fib() | select(lambda x: x ** 2) | take_while(lambda x: x < 100) | as_list
[1, 1, 4, 9, 25, 64]
```

pipe中还包括了更多的流处理函数。你甚至可以自己定义流处理函数，只需要定义一个生成器函数并加上修饰器Pipe。如下定义了一个获取元素直到索引不符合条件的流处理函数：

```python
>>> @Pipe
... def take_while_idx(iterable, predicate):
...   for idx, x in enumerate(iterable):
...     if predicate(idx): yield x
...     else: return
...
```

使用这个流处理函数获取fib的前10个数字：

```python
>>> fib() | take_while_idx(lambda x: x < 10) | as_list
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

更多的函数就不在这里介绍了，你可以查看pipe的源文件，总共600行不到的文件其中有300行是文档，文档中包含了大量的示例。

pipe实现起来非常简单，使用Pipe装饰器，将普通的生成器函数（或者返回迭代器的函数）代理在一个实现了`__ror__`方法的普通类实例上即可，但是这种思路真的很有趣。


