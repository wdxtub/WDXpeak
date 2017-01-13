# Swift 2.0 学习指南

主要是参考苹果官方的教程，加上自己的一点私货，作为笔记，还是重在要点和思想，具体的细节参阅官方手册。

+ 使用 ARC(Automatic Reference Counting) 来简化管理内存
+ 采用 Objective-C 的命名参数以及动态对象模型
+ 支持代码预览

## Swift 2 概览

这一章主要是通过一些实际的代码让大家对 Swift 有一个初步的感觉，具体的语法以及技术细节会在之后的章节中详细介绍。

### 简单值

+ 使用 `let` 来声明常量
+ 使用 `var` 来声明变量
+ 大部分情况下不用明确声明类型
+ 显式声明的话，用冒号分割 `let explicitDouble: Double = 70`
+ 值永远不会被隐式转换成其他类型，需要时请显式转换
+ 一个简单的值转字符串的方法是把值写到括号中，并且在括号前加一个反斜杠，括号中可以是一个表达式
+ 使用方括号来创建数组和字典，用下标或者 key 来访问元素，最后一个元素后面允许有逗号
+ 创建空数组或者字典要用初始化语法

```swift
// variable and constant value
var myVariable = 42
myVariable = 50
let myConstant = 33

// explicit declare
let implicitInteger = 70
let implicitDouble = 70.0
let explicitDouble: Double = 70

// cast type
let label = "The width is"
let width = 94
let widthLabel = label + String(width)

// easy cast from value to string
let apples = 3
let appleSummary = "I have \(apples) apples."  

// array
var shoppingList = ["catfish", "water", "tulips"]
shoppingList[1] = "bottle of water"

// dict
var occupations = ["Da": "Captain", "Wang": "Warrior",]
occupations["WDX"] = "Hero"

// init empty array / dict
let emptyArray = [String]()
let emptyDict = [String: Float]()
```

### 控制流

+ 条件操作 `if` 和 `switch`
+ 循环操作 `for-in`, `for`, `while` 和 `repeat-while`
+ 包裹条件和循环变量的括号可以省略，但是语句体必须要大括号

```swift
// for loop with if-else statment
let Scores = [75, 43, 103, 87, 12]
var teamScore = 0
for score in Scores{
	if score > 50 {
		teamScore += 3
	} else {
		teamScore += 1
	}
}
print(teamScore)
```

可以使用 `if` 和 `let` 来处理值缺失的情况。这些值可由可选值来代表。一个可选的值是一个具体的值或者是 `nil` 以表示值缺失。在类型后面加一个问号来标记这个变量的值是可选的。在下面的例子中，如果变量的可选值是 `nil`，条件会被判断为 `false`，大括号中的代码会被跳过

```swift
var optionalString: String? = "Hello"
print(optionalString == nil)

var optionalName: String? = "Da Wang"
var greeting = "Hello!"
if let name = optionalName {
	greeting = "Hello, \(name)"
}
```

另一种方法是通过 `??` 操作符来提供一个默认值。如果可选值缺失，用默认值代替

```swift
let nickName: String? = nil
let fullName: String = "Da Wang"
let greeting = "Hi \(nickName ?? fullName)"
```

switch 支持任意类型的数据以及各种比较操作，而且不需要写 break，执行完子句会自动退出

```swift
let vegetable = "cucumber"
swtich vegetable{
	case "carrot":
		print("Oh Carrot!")
	case "cucumber":
		print("Oh Cucumber!")
	case let x where x.hasSuffix("pepper"):
		print("Oh Special One!")
	default:
		print("Nothing happened")
}
```

可以使用 `for-in` 来遍历字典

```swift
let interestingNumbers = [
	"Prime": [2, 3, 5, 7, 11, 13],
	"Fibonacci": [1, 1, 2, 3, 5, 8],
	"Square": [1, 4, 9, 16, 25],
]
var largest = 0
for (kind, numbers) in interestingNumbers{
	for number in numbers{
		if number > largest {
			largest = number
		}
	}
}
print(largest)
```

使用 `while` 来重复运行一段代码直到不满足条件，循环条件也可以在末尾，保证至少循环一次

```swift
// while loop
var n = 2
while n < 100 {
	n = n * 2
}
print(n)

// repeat while loop
var m = 2
repeat {
	m = m * 2
} while m < 100
print(m)
```

也可以在循环中使用 `..<` 来表示范围，注意 `..<` 创建的范围不包含上界，如果要包含的话，使用 `...`

```swift
var forLoop = 0
for i in 0..<4 {
	forLoop += i
}
print(forLoop)

forLoop = 0
for i in 0...4 {
	forLoop += i
}
print(forLoop)
```

### 函数和闭包

使用 `func` 来声明一个函数，使用名字和参数来调用函数。使用 `->` 来指定函数返回值的类型

```swift
func greet(name: String, day: String) -> String {
	return "Hello \(name), today is \(day)"
}

greet("Da", day: "Friday")
```

使用元组来让一个函数返回多个值。该元组的元素可以用名称或数字来表示

```swift
func calStats(scores: [Int]) -> (min: Int, max: Int, sum: Int){
	var min = scores[0]
	var max = scores[0]
	var sum = 0
	for score in scores{
		if score > max {
			max = score
		} else if score < min {
			min = score
		}
		sum += score
	}
	return (min, max, sum)
}

let stats = calStats([5, 3, 100, 2, 9])
print(stats.sum)
print(stats.2)
```

函数可以带可变个数的参数，这些参数在函数内表现为数组的形式

```swift
func sumOf(numbers: Int...) -> Int {
	var sum = 0
	for number in numbers {
		sum += number
	}
	return sum
}

sumOf()
sumOf(42, 583, 12)
```

函数可以嵌套。被嵌套的函数可以访问外侧函数的变量，可以用来重构一个太长或者太复杂的函数

```swift
func returnFifteen() -> Int {
	var y = 10
	func add() {
		y += 5
	}
	add()
	return y
}

returnFiftee()
```

函数是第一等类型，也就是说，函数可以作为另一个函数的返回值

```swift
func makeIncrementer() -> (Int -> Int){
	func addOne(number: Int) -> Int {
		return 1 + number
	}
	return addOne
}

var increment = makeIncrementer()
increment(7)
```

函数也可以当做参数传入另一个函数

```swift
func hasAnyMatches(list: [Int], condition: Int -> Bool) -> Bool {
	for item in list {
		if condition(item) {
			return true
		}
	}
	return false
}

func lessThenTen(number: Int) -> Bool {
	return number < 10
}

var numbers = [20, 19, 7, 12]
hasAnyMatches(numbers, condition: lessThanTen)
```

函数实际上是一种特殊的闭包：它是一段能之后被调取的代码。比保重的代码能访问闭包所建作用域中能得到的变量和函数，即使闭包是在一个不同的作用域被执行的

```swift
numbers.map({(number: Int) -> Int in let result = 3 * number return result})
```

如果一个闭包的类型已知，，可以忽略参数的类型和返回值。单个语句闭包会把它语句的值当作结果返回

```swift
let mappedNumbers = numbers.map({number in 3 * number })
print(mappedNumbers)
```

也可以通过参数位置而不是参数名字来引用参数。当一个闭包作为最后一个参数传给一个函数的时候，它可以直接跟在括号后面。当一个闭包是传给函数的唯一参数时，可以完全忽略括号

```swift
let sortedNumbers = numbers.sort { $0 > $1}
print(sortedNumbers)
```

### 对象和类

使用 `class` 和类名来创建一个类，其他的语法和前面说的一致。

+ 使用 `init` 来初始化一个构造器
+ 使用 `deinit` 来创建一个析构函数

```swift
class Shape {
	var numberOfSides: Int = 0
	var name: String
	
	init(name: String){
		self.name = name
	}
	
	func simpleDescription() -> String {
		return "A shape with \(numberOfSides) sides."
	}
}
```

要创建一个类的实例，在类名后面加上括号。使用点语法来访问实例的属性和方法

```swift
var shape = Shape()
shape.numberOfSides = 7
var shapeDescription = shape.simpleDescription()
```

子类的定义方法实在它们的类名后面加上父类的名字，用冒号分割。如果要重写父类的方法，需要用 override 标记，否则会报错，编译器同样会检测 override 标记的方法是否确实在父类中

```swift
class Square: Shape {
	var sideLength: Double
	
	init(sideLength: Double, name: String) {
		self.sideLength = sideLength
		super.init(name: name)
		numberOfSides = 4
	}
	
	func area() -> Double {
		return sideLength * sideLength
	}
	
	override func simpleDescription() -> String {
		return "A square with sides of length \(sideLength)."
	}
	
	let test = Square(sideLength: 5.2, name: "my test square")
	test.area()
	test.simpleDescription()
}
```

除了储存简单的属性之外，属性可以有 `getter` 和 `setter`

```swift
class EquilateralTriangle: Shape {
	var sideLength: Double = 0.0
	
	init(sideLength: Double, name: String){
		self.sideLength = sideLength
		super.init(name: name)
		numberOfSides = 3
	}
	
	var perimeter: Double {
		get {
			return 3.0 * sideLength
		}
		set {
			sideLength = newValue / 3.0
		}
	}
	
	override func simpleDescription() -> String {
		return "An equilateral triangle with sides of length \(sideLength)."
	}
}

var triangle = EquilateralTriangle(sideLength: 3.1, name: "a tragnle")
print(triangle.perimeter)
triangle.perimeter = 9.9
print(triangle.sideLength)
```

如果不需要计算属性，但是仍然需要在设置一个新值之前或者之后运行代码，使用 `willSet` 和 `didSet`

### 枚举和结构体

使用 `enum` 来创建一个枚举，枚举也可以包含方法

```swift
enum Rank: Int{
	case Ace = 1
	case Two, Three, FOur, Five, Six, Seven, Eight, Nine, Ten
	case Jack, Queen, King
	func simpleDescription() -> String {
		switch self{
			case .Ace:
				return "ace"
			case .Jack:
				return "jack"
			case .Queen:
				return "queen"
			case .King:
				return "king"
			default:
				return String(self.rawValue)
		}
	}
}

let ace = Rank.Ace
let aceRawValue = ace.rawValue
```

枚举的成员值是实际值，并不是原始值的另一种表达方法。实际上，以防原始值没有意义，我们不需要设置。

使用 `struct` 来创建一个结构体。结构体和类最大的区别是结构体是传值，类是传引用。

```swift
struct Card {
	var rank: Rank
	func simpleDescription() -> String {
		return "The \(rank.simpleDescription())"
	}
}
```

### 协议和扩展

使用 `protocol` 来声明一个协议，类、枚举和结构体都可以实现协议，在结构体中 `mutating` 关键字用来标记一个会修改结构体的方法

```swift
protocol ExampleProtocal {
	var simpleDescription: String { get }
	mutating func adjust()
}

// class
class simpleClass: ExampleProtocol {
	var simpleDescription: String = "A very simple class."
	var anotherProperty: Int = 15213
	func adjust() {
		simpleDescription += "  Now 100% adjusted"
	}
}

// struct
struct Simple Structure: ExampleProtocol {
	var simpleDescription: String = "A simple strucure"
	mutating func adjust() {
		simpleDescription += " (adjusted)"
	}
}
```

使用 extension 来为现有的类型添加功能

```swift
extension Int: ExampleProtocol {
	var simpleDescription: String {
		return "The number \(self)"
	}
	mutating func adjust() {
		self += 42
	}
}

print (7.simpleDescription)
```

### 泛型

在尖括号里写一个名字来创建一个泛型函数或者类型

```swift
func repeatItem<Item>(item: Item, numberOfTimes: Int) -> [Item]{
	var result = [Item]()
	for _ in 0..<numberOfTimes{
		result.append(item)
	}
	return result
}

repeatItem("knock", numberOfTimes: 4)
```

在类型名后面使用 `where` 来指定对类型的需求，比如，限定类型实现某一个协议，限定两个类型是相同的，或者限定某个类必须有一个特定的父类。

```swift
func anyCommonElements <T: SequenceType, U: SequenceType where T.Generator.Element: Equatable, T.Generator.Element == U.Generator.Element> (lhs: T, _ rhs: U) -> Bool){
	...
}
```

## Swift 2 基础

比较简单的部分会用要点的形式列出来，比较复杂和语言本身特性的，会单独提出来介绍

+ 常量与变量
	+ 用 `let` 声明常量
	+ 用 `var` 声明变量
	+ 一行可以声明多个，用逗号隔开：`var x = 0.0, y = 0.0, z = 0.0`
+ 类型标注(冒号和空格加上类型名称)
	+ `var welcomeMessage: String`
	+ 一行可以声明多个：`var red, green, blue: Double`
+ 输出常量和变量
	+ 函数原型：`print(_:separator:terminator:)`
	+ 通常来说 `separator` 和 `terminator` 有默认值可以忽略，如果想要自定义，可以这样：`print(someValue, terminator: "")` 这样就不会默认换行了
+ 字符串插值 string interpolation
	+ 用反斜杠加一对括号
	+ `print("The value is \(someValue)")`
+ 注释：`//` 和 `/* */`
+ 分号不强制要求，但是为了美观还是加上，或者如果一行写两个语句，就一定要分号
+ 整数：Swift 提供了 8, 16, 32, 64 的有符号和无符号整数类型
	+ 如: UInt8, Int32 等
	+ 整数范围: UInt8.min, UInt8.max，其他的类型类似
	+ 32 位平台上，Int 和 Int32 长度相同
	+ 64 位平台上，Int 和 Int64 长度相同
	+ 统一使用 Int 可以提高代码的可复用性，避免不同类型数字之间的转换，并且匹配数字的类型推断
+ 浮点数
	+ Double 64 位浮点数
	+ Float 32 位浮点数
+ Swift 是一个类型安全的语言
+ Swift 也会尽可能通过类型推断来选择合适的类型
+ 数值型字面量
	+ 十进制数：没有前缀
	+ 二进制数：`0b`
	+ 八进制数：`0o`
	+ 十六进制数：`0x`
+ 类型转换
	+ 整数和浮点数转换必须显式指定类型
+ 类型别名
	+ 用 `typealias` 关键字来定义，如 `typealias AudioSample = UInt16`
+ 布尔值：true 和 false
+ 元组
	+ 圆括号包起来的变量：`http404Error = (404, "Not Found")`
	+ 分解元素内容 `let (statusCode, Message) = http404Error`
	+ 如果只需要用一部分，忽略的部分用下划线表示 `let (justCode, _) = http404Error`
	+ 还可以通过下标来访问元组的中单个元素，下标从零开始：`http404Error.0`
	+ 可以在定义元组的时候给元素命名，这样就可以通过名字来获取对应的值：`let http200Status = (statusCode: 200, description: "OK")`
	+ 元组在临时组织值的时候很有用，但是并不适合创建复杂的数据结构
+ 运算符
	+ 基本的就不提了，和其他语言差不多，这里就记录一些要点
	+ `++` 前置的时候，先自增再返回
	+ `++` 后置的时候，先返回再自增
	+ `===` 恒等，`!==` 不恒等
	+ 三目运算符 `(condition ? statement1 : statement2)`
		+ 应该避免在一个组合语句中使用多个三目运算符
	+ 空合运算 (Nil Coalescing Operator)
		+ `(a ?? b)` 将对可选类型 a 进行空判断，如果 a 包含一个值就进行解封，否则就返回一个默认值 b。
		+ 相当于下列代码的简短表示: `a != nil ? a! : b`
	+ 区间运算符
		+ 闭区间运算符 ( a...b )，包括 a 也包括 b
		+ 半开区间运算符 ( a...<b )，包括 a 不包括 b
	+ 逻辑运算
		+ `!a`, `a&&b`, `a||b` 
+ 字符串是值类型 Strings are value types，也就是说操作的时候会创建一个新的副本
	+ 连接字符串和字符可以用 `+` 号，创建一个新的字符串
	+ 字符串插值(String Interpolation)，如 `let message = "\(multiplier) times 2.5 is \(Double(multiplier) * 2.5)"`
	+ Swift 的字符串完全兼容 Unicode
	+ 计算字符数量，用字符串 characters 属性的 count 属性
	+ `let string = "Hello World" ; print(string.characters.count)`
	+ 通过字符串索引 `startIndex`, `endIndex`, `startIndex.predecessor()`, `startIndex.succeessor()` 来访问，或者也可以通过下标访问
	+ 调用 `insert(_:atIndex:)` 方法可以在一个字符串的指定索引插入一个字符。
		+ `var welcome = "hello"; welcome.insert("!", atIndex:welcome.endIndex)`
	+ 删除字符或字符串 `removeAtIndex(_:)`, `removeRange(_:)`
	+ 比较字符串：`==`, `!=`, `hasPrefix(_:) / hasSuffix(_:)`
	+ 字符串 Unicode 表示形式
+ For 循环
	+ `for initialization; condition; increment { ... }`
	+ `for var variable in Collection { ... }`
+ While 循环
	+ `while condition { ... }`
	+ `repeat { ... } while condition`
+ if 和 switch 可以看概览中的代码例子
+ 控制转移语句 Control Transfer Statements
	+ continue
	+ break
	+ fallthrough 在分支中加上这个关键字就会落入到下一个分支中，不会检查匹配条件，类似于 C 语言 switch case 没加 break 的效果
	+ return
	+ throw
	+ 还可以利用标签来明确是 break 出哪个循环，这个在多重循环逻辑中比较有用

### 可选类型

使用可选类型(optionals)来处理值可能缺失的情况，可选类型的值有两种可能：1.有值，等于 x。2.没有值，等于nil。举个例子

```swift
let possibleNumber = "123"
let convertedNumber = Int(possibleNumber)
```

`convertedNumber` 被推测为 `Int?` 类型，表示可能包含 Int 值，也可能不包含值。

可以给可选变量赋值位 `nil` 来表示没有值，但 `nil` 不能用于非可选的常量和变量。如果声明一个可选常量或者变量但是没有赋值，会被自动设置为 `nil`。

可以使用 if 语句和 nil 比较来判断一个可选值是否包含值。使用 `==` 或 `!=` 来执行比较。当确定可选类型确实包含值之后，可以在名字后面加一个感叹号来获取值，称为可选值的强制解析(forced unwrapping)。要注意的是使用 `!` 来获取一个不存在的可选值会导致运行时错误。

```swift
if convertedNumber != nil {
	print("convertedNumber has an integer value of \(convertedNumber!).")
}
```

### 可选绑定 optional binding

判断可选类型是否包含值，如果包含就把值赋给一个临时常量或者变量。可选绑定可以用在 if 和 while 语句中，这样就可以同时完成赋值和判断两个任务，如

```swift
if let constantName = someOptional {
	statements
}
```

也可以在 if 语句中包含多个可选绑定，然后用 where 子句做布尔值判断，如

```swift
if let firstNumber = Int("4"), secondeNumber = Int("42") where firstNumber < secondNumber {
	print("\(firstNumber) < \(secondNumber)")
}
// print "4 < 42"
```

### 错误处理 error handling

一个函数可以通过在声明中添加 `throws` 关键词来抛出错误消息。当你的函数能抛出错误消息时，应该在表达式中前置 `try` 关键词

```swift
func makeASandwich() throws {
	// ...
}

do {
	try makeASandwich()
	eatASandwich()
} catch Error.OutOfCleanDishes {
	washDishes()
} catch Error.MissingIngredients(let ingredients){
	byGroceries(ingredients)
}
```

### 断言

在运行时判断一个逻辑条件是否为 `true`。全局 `assert(_:_file:line:)` 函数来写一个断言。

```swift
let age = -3
assert(age >= 0, "A person's age cannot be less than zero")
// 因为 age < 0，所以断言会触发
```

适用情景

+ 整数类型的下标索引被传入一个自定义下标脚本实现，但是下标索引值可能太小或者太大
+ 需要给函数传入一个值，但是非法的值可能导致函数不能正常运行
+ 一个可选值现在是 nil，但是后面的代码运行需要一个非 nil 值。

### 集合类型 (Collection Types)

Swift 语言提供 Arrays, Sets 和 Dictionaries 三种基本集合类型，存储的数据必须明确，不能把不正确的数据类型插入其中。

在我们不需要改变集合大小的时候创建不可变集合是很好的习惯。这样 Swift 编译器可以优化我们创建的集合

#### 数组 Arrays

会被桥接到 Foundation 中的 NSArray 类。应该遵循像 `Array<Element>` 这样的形式，其中 `Element` 是这个数组唯一允许存在的数据类型。也可以用 `[Element]` 这样的简单语法。

```swift
// 创建一个空数组
var someInts = [Int]()

// 如果代码上下文中已经提供了类型信息，可以使用一对空方括号来创建
someInts.append(3)
someInts = []

// 带有默认值的数组
var threeDoubles = [Double](count: 3, repeatedValue: 0.0)

// 两个数组相加创建一个数组
var anotherThreeDoubles = Array(count: 3, repeatedValue: 2.5)
var sixDoubles = threeDoubles + anotherThreeDoubles

// 用字面量构造数组
var shoppingList: [String] = ["Eggs", "Milk"]

// 可以使用数组中的只读属性 count 来获取数组中的数据项数量
print("The shopping list contains \(shoppingList.count) items.")

// 使用布尔值属性 isEmpty 作为检察 count 属性的值是否为 0 的捷径
if shoppingList.isEmpty {
	print("The shoppinglist is empty.")
}

// 使用 append(_:) 方法在数组后面添加数据项
shoppingList.append("Flour")

// 也可以直接用 += 来进行添加
shoppingList += ["Baking Powder"]

// 用下标来改变数据
shoppingList[0] = "Six eggs"

// 或者范围批量替换
shoppingList[4...6] = ["Bananas", "Apples"]

// 插入数据
shoppingList.insert("Maple Syrup", atIndex: 0)

// 删除数据
let mapleSyrup = shoppingList.removeAtIndex(0)
let apples = shoppingList.removeLast()

// 用 for-in 循环来遍历数组
for item in shopppingList {
	print(item)
}

// 用 `enumerate()` 方法来同时获取索引值和数据值
for (index, value) in shoppingList.enumerate(){
	print("Item \(String(index + 1)): \(Value)")
}
```

#### 集合 Sets

每个元素只出现一次，元素顺序不重要，会被桥接到 Foundation 中的 NSSet 类。存在集合中的类型必须可哈希化。集合的语法是 `Set<Element>`，但集合没有等价的简化形式

```swift
// 创建空集合
var letters = Set<Character>()

// 如果上下文提供了类型信息，创建空集合时可以简化
letters.insert("a")
letters = [] // 重新设为空，类型为 Set<Character>

// 用字面量声明集合
var favoriteGenres: Set<String> = ["Rock", "Classical", "Hip hop"]

// 因为用了字面量，其实类型的声明是可以省略的，上面的一句可以写为
var favoriteGenres: Set = ["Rock", "Classical", "Hip hop"]

// 用 count 获取元素数量
print ("I have \(favoriteGenres.count) favorite music genres.")

// 用 isEmpty 来看集合是否为空
if favoriteGenres.isEmpty {
	print("As far as music goes, I'm not picky.")
}

// insert(_:) 添加新元素
favoriteGenres.insert("Jazz")

// remove(_:) 删除元素，会返回被删除的值，如果不包含则返回 nil
if let removedGenre = favoriteGenres.remove("Rock"){
	print ("\(removedGenre)? I'm over it.")
}

// contains(_:) 检查是否包含一个特定的值
if favoriteGenres.contains("Funk") {
	print ("I get up on the good foot")
}

// 遍历集合，用 for-in，用 sort() 方法可以返回一个有序集合
for genre in favoriteGenres.sort() {
	print("\(genre)")
}
```

其他的一些集合操作

+ `intersect(_:)` 根据两个集合中都包含的值创建一个新的集合
+ `exclusiveOr(_:)` 在一个集合中但不在另一个集合中的值创建一个新的集合
+ `union(_:)` 两个集合的并集
+ `subtract(_:)` 两个集合的差集
+ `==` 判断集合相等
+ `isSubsetOf(_:)` 判断子集
+ `isSupersetOf(_:)` 判断超集
+ `isStrictSubsetOf(_:)` 判断严格子集
+ `isDisjointWith(_:)` 判断两个集合是否不含有相同的值

#### 字典 Dictionary

键值对，被桥接倒 Foundation 的 NSDictionary，语法为 `Dictionary<Key, Value>`。作为 key 的必须是 Hashable 的，可以用 `[Key: Value]` 这样的快捷形式去创建一个字典

```swift
// 创建空字典
var namesOfIntegers = [Int: String]()

// 如果上下文提供了信息，可以简化
namesOfIntegers[16] = "sixteen"
namesOfIntegers = [:] // 设置为空字典

// 用字面量创建字典
var airports: [String: String] = ["YYZ": "Toronto Pearson", "DUB": "Dublin"]

// 获取字典中元素的数量
print("The dictionary of airports contains \(airports.count) items.")

// 检查是否为空
if airports.isEmpty {
	print("The airports dictionary is empty.")
}

// 下标添加新数据，如果已有对应的 key，会覆盖更新
// 用 updateValue(_:forKey:) 方法会返回更新前的值，可选类型，如果没有 key 的话会是 nil
airports["LHR"] = "London"
if let oldValue = airports.updateValue("Dublin Airport", forKey: "DUB"){
	print("The Old value for DUB was \(oldValue)")
}

// 用下标给某个 key 赋值为 nil 可以删除这个元素
// 也可以用 removeValueForKey(_:)，方法会返回更新前的值，可选类型，如果没有 key 的话会是 nil
airports["APL"] = nil

// 用 for-in 来遍历字典，会以 (key, value) 元组形式返回
for (airportCode, airportName) in airports {
	print("\(airportCode): \(airportName)")
}

// 也可以单独用 keys 或者 values 属性来遍历，如果需要有序，可以用 sort() 方法
for airportCode in airports.keys {...}
for airportName in airports.values {...}
```

### Switch 语句高级用法

switch 语句会尝试把某个值与若干个 pattern 进行匹配。每个 case 之间不需要用 break

比较常见的用法是

```swift
switch some value to consider {
	case value 1:
		respond to value 1
	case value 2, value 3:
		respond to value 2 or 3
	default:
		otherwise
}
```

#### 区间匹配

因为是匹配一个 pattern，所以也可以利用区间，如下

```swift
let approximateCount = 62
switch approximateCount {
	case 0:
		print("no")
	case 1..<5:
		print("a few")
	case 5..<12:
		print("several")
	default:
		print("many")
}
```

#### 元组

可以使用元组来测试多个值。用下划线来匹配所有可能的值

```swift
let somePoint (1, 1)
switch somePoint {
	case (0, 0):
		print("origin")
	case (_, 0):
		print("x-axis")
	case (0, _):
		print("y-zxis")
	default:
		print("else")
}
```

#### 值绑定 Value Bindings

允许将匹配的值帮动刀一个临时的常量或变量上，就可以在 case 分支里引用

```swift
let anotherPoint = (2, 0)
switch anotherPoint {
	case (let x, 0):
		print("x-axis with value \(x)")
	case (0, let y):
		print("y-axis with value \(y)")
	case let (x, y):
		print("else x:\(x) y:\(y)")
}
```

#### where

case 分支模式可以使用 where 语句来判断额外的条件，例如

```swift
let yetAnotherPoint = (1, -1)
switch yetAnotherPoint {
	case let (x, y) where x == y:
		print("(\(x), \(y)) is on the line x = y")
	case let (x, y) where x == -y:
		print("(\(x), \(y)) is on the line -x = y")
}
```

### Guard 语句

要求条件必须为真才执行之后的代码，而且一定要带有一个 else 分句，如果条件不为真则执行 else 分句中的代码

```swift
guard let name = person["name"] else {
	print("no name")
}
```


### 检测 API 的可用性

最后一个参数 `*` 是必须的，用于处理未来的潜在平台，例如：

```swift
if #available(iOS 9, OSX 10.10, *){
	//... new api
} else {
	//... old api 
}
```

## Swift 2 进阶

### 函数

#### 定义一个函数

```swift
func sayHello(personName: String) -> String {
	let greeting = "Hello, " + personName + "!"
	return greeting
}

print(sayHello("DaWang"))
```

#### 无参数函数

```swift
func sayHelloWorld() -> String {
	return "Hello, World."
}

print(sayHelloWorld())
```

#### 多参数函数

```swift
func sayHello(personName: String, alreadyGreeted: Bool) -> String {
	if alreadyGreeted {
		// ... 
	} else {
		// ...
	}
}
```

#### 无返回值

就不需要返回箭头和返回类型

```swift
func sayGoodBye(personName: String){
	print("Goodbye, \(personName)!")
}

sayGoodbye("David")
```

#### 多重返回值函数

其实就是返回一个 tuple，名字已经由返回类型指定了，这个返回值也可以是一个可选的元组 `(min: Int, max: Int)?`

```swift
func minMax(array: [Int]) -> (min: Int, max: Int){
	var currentMin = array[0]
	var currentMax = array[0]
	for value in array[1..<array.count] {
		if value < currentMin {
			currentMin = value
		} else if value > currentMax {
			currentMax = value
		}
	}
	return (currentMin, currentMax)
}

let bounds = minMax([8, -6, 2, 109, 3, 71])
print("min is \(bounds.min) and max is \(bounds.max)")
```

如果不想为第二个及后续的参数设置外部参数名，用一个下划线来代替一个明确的参数

#### 默认参数值

```swift
func someFunction(parameterWithDefault: Int = 12) {
	// ...
}
```

#### 可变参数

可以接受零个或多个值。但是一个函数最多只能有一个可变参数，并且最好放在最后

```swift
func arithmeticMean(numbers: Double...) -> Double {
	var total: Double = 0
	for number in numbers {
		total += number
	}
	return total / Double(numbers.count)
}

arithmeticMean(1, 2, 3, 4, 5)
```

#### 变量函数参数

函数参数默认是常量，也就是说在函数体中不能更改。但是如果想要传入参数变量的值副本，可以像以下这样。但是对变量参数所进行的修改在函数调用结束后便消失了，并且对于函数体外是不可见的

```swift
func alignRight(var string: String, fotalLength: Int, pad: Character) -> String {
	// ...
}
```

#### 输入输出参数

如果需要在函数中对参数的修改仍然存在，就需要用 `inout` 关键字。只能传递变量给 inout 参数，并且需要在参数名前加 `&`，表示这个值可以被函数修改

```swift
func swapTwoInts(inout a: Int, inout _ b: Int){
	let temporaryA = a
	a = b
	b = temporaryA
}

var someInt = 3
var anotherInt = 107
swapTwoInt(&someInt, &anotherInt)
```

#### 函数类型

也就是把函数当成常量或者变量，比如

```swift
var mathFunction: (Int, Int) -> Int = addTwoInts
print("Result: \(mathFunction(2, 3))")
// 也可以让 Swift 来推断函数类型，如
let anotherMathFunction = addTwoInts
```

函数类型作为参数类型

```swift
func printMathResult(mathFunction: (Int, Int) -> Int, _ a: Int, _ b: Int) {
	print("Result: \(mathFunction(a, b))")
}

printMathResult(addTwoInts, 3, 5)
```

函数类型作为返回类型，在返回箭头后写一个完整的函数类型

```swift
func stepForward(input: Int) -> Int {
	return input + 1
}

func stepBackward(input: Int) -> Int {
	return input - 1
}

func chooseStepFunction(backwards: Bool) -> (Int) -> Int {
	return backwards ? stepBackward : stepForward
}

var currentvalue = 3
let moveNearerToZero = chooseStepFunction(currentValue > 0)
```

#### 嵌套函数 nested function

默认情况下，嵌套函数对外界不可见，但是可以被外围函数(enclosing function)调用。一个外围函数也可以返回它的某一个嵌套函数，使得这个函数可以在其他域中被使用

```swift
func chooseStepFunction(backwards: Bool) -> (Int) -> Int {
	func stepForward(input: Int) -> Int {
		return input + 1
	}
	
	func stepBackward(input: Int) -> Int {
		return input - 1
	}
	
	return backwards ? stepBackward : stepForward
}

var currentValue = -4
let moveNearerToZero = chooseStepFunction(currentValue > 0)
while currentValue != 0 {
	print("\(currentValue)...")
	currentValue = moveNearerToZero(currentValue)
}
```

### 闭包 Closure

自包含的函数代码块，可以在代码中被传递和使用。闭包采取如下三种形式之一：

+ 全局函数是一个有名字但不会捕获任何值的闭包
+ 嵌套函数是一个有名字并可以捕获其封闭函数域内值的闭包
+ 闭包表达式是一个利用轻量级语法所写的可以捕获其上下文中变量或常量值的匿名闭包

Swift 闭包表达式拥有简洁的风格，并鼓励在常见场景中进行语法优化，主要优化如下：

+ 利用上下文推断参数和返回值类型
+ 隐式返回单表达式闭包，即单表达式闭包可以省略 return 关键字
+ 参数名称所写
+ 尾随(Trailing)闭包语法

#### 闭包表达式 Closure Expressions

利用简洁语法构建內联闭包的方式。下面通过不同的方式展示了 `sort(_:)` 方法定义和语法优化的方式。

首先是最原始的方式

```swift
let names = ["Chris", "Alex&", "Ewa", "Barry", "Daniella"]

func backward(s1: String, s2: String) -> Bool {
	return s1 > s2
}
var reversed = names.sort(backwards)
```

闭包表达式语法 `{ (parameters) -> returnType in statements }`，例如，上面的 sort 可以写为：

```swift
reversed = names.sort({ (s1: String, s2: String) -> Bool in return s1 > s2 })
```

注意函数和返回值类型都写在大括号内，而不是大括号外。闭包的函数体部分由关键字 in 引入，该关键字表示闭包的参数和返回值类型定义已经完成，闭包函数体即将开始。而 Swift 可以根据调用方法的对象来推断

```swift
reversed = names.sort( { s1, s2 in return s1 > s2})
```

实际上任何情况下，通过內联闭包表达式构造的闭包作为参数传递给函数或方法时，都可以推断出闭包的参数和返回值类型，所以几乎不需要利用完整格式构造內联闭包。

**单表达式闭包隐式返回 Implicit Return From Single-Expression Closures**

其实就是省略 return 来隐式返回单行表达式的结果，如

```swift
reversed = names.sort( { s1, s2 in s1 > s2 })
```

**参数名称缩写**

可以直接通过 `$0`, `$1` 这样来顺序调用闭包的参数。如果用了缩写，就可以在闭包参数列表中省略对其的定义

```swift
reversed = names.sort( { $0 > $1 })
```

**运算符函数**

```swift
reversed = names.sort(>)
```

**尾随闭包(Trailing Closures)**

如果需要将一个很长的闭包表达式作为最后一个参数传递给函数，可以使用尾随闭包来增强函数的可读性

```swift
func someFunctionThatTakesAClosure(closure: () -> Void) {
	// 函数体部分
}

// sort 方法可以写成
reversed = names.sort() { $0 > $1 }

// 或者连圆括号都可以省略
reversed = names.sort { $0 > $1 }
```

#### 捕获值 Capturing Values

闭包可以在其被定义的上下文中捕获常量或变量。即使定义这些常量和变量的原作用域已经不存在，闭包仍然可能在闭包函数体内引用和修改这些值

+ 闭包是引用类型 Closures Are Reference Types

#### 非逃逸闭包 Nonescaping Closures

当一个闭包作为参数传到一个函数中，但是这个闭包在函数返回之后才被执行，我们称该闭包从函数中逃逸。可以在参数名之前标注 `@noescape` 能使编译器知道这个闭包的生命周期，从而进行比较激进的优化

```swift
func someFunctionWithNoescapeClosure (@noescape closure: () -> Void) {
	closure()
}
```

一种能使闭包『逃逸』处函数的方法是，将这个闭包保存在一个函数外部定义的变量中。例如，很多启动异步操作的函数接受一个闭包参数作为 completion handler。这类函数会在异步操作开始之后立刻返回，但是闭包直到异步操作结束后才会被调用，如

```swift
// 定义一个空数组，这个空数组的元素是一个闭包
var completionHandlers: [() -> Void] = []
func someFunctionWishEscapingClosure(completionHandler: () -> Void) {
	completionHandlers.append(completionHandler)
}
```

将闭包标注为 `@noescape` 使你能在闭包中隐式地引用 self

#### 自动闭包 Autoclosures

自动创建，用于包装传递给函数作为参数的表达式。这种闭包不接受任何参数，当它被调用的时候，会返回被包装在其中的表达式的值。这种便利语法让你能够用一个普通的表达式来代替显式的闭包，从而省略闭包的花括号。

自动闭包让你能够延迟求值，直到执行这个闭包时代码才会执行

```swift
var customersInLine = ["Chris", "Alex", "Ewa", "Barry", "Daniella"]
print (customersInLine.count) // output: 5

let customerProvider = {customersInLine.removeAtIndex(0)}
print (customersInLine.count) // output: 5

print ("Now serving \(customerProvider())!") // output: Chris
print (customersInLine.count) // output: 4
```

但是过度使用会使得代码非常难懂，要慎重

### 枚举 Enumerations

放到大括号里 

```swift
enum SomeEnumeration {
	// 枚举定义
}

// 例如
enum CompassPoint {
	case North
	case South
	case East
	case West
}

// 多个成员值可以放在同一行
enum Planet {
	case Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
}

// 赋值
var directionToHead = CompassPoint.West
// 因为类型已知，接下来的调用可以省略前面部分
directionToHead = .East

// 配合 switch
switch directionToHead{
	case .North:
		print("north")
	case .South:
		print("south")
	case .East:
		print("east")	
	case .West:
		print("west")	
}

// 给定原始值
enum Planet: Int {
	case Mercury = 1, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
}

let possible Planet = Planet(rawValue: 7)

// 枚举递归
用 indirect 关键字，暂略
```

### 类和结构体

相同：

+ 定义属性用于存储值
+ 定义方法用于提供功能
+ 定义附属脚本用于访问值
+ 定义构造器用于生成初始化值
+ 通过扩展以增加默认实现的功能
+ 通过协议以提供某种标准功能

与结构体相比，类还有如下的附加功能：

+ 继承允许一个类继承另一个类的特征
+ 类型转换允许在运行时检查和解释一个类实例的类型
+ 解构器允许一个类实例释放任何其所被分配的资源
+ 引用计数允许对一个类的多次引用

结构体总是通过被复制的方式在代码中传递，不使用引用计数

```swift
// 结构体定义
struct Resolution {
	var width = 0
	var height = 0
}

// 类定义
class VideoMode {
	var resolution = Resolution()
	var interlaced = false
	var frameRate = 0.0
	var name: String?
}

let someResolution = Resolution()
let someVideoMode = VideoMode()

// 属性访问
print ("The wide of someResolution is \(someResolution.width)")

// 所有结构体都有一个自动生成的成员逐一构造器
let vga = Resolution(width: 640, height: 480)
```

**结构体和枚举是值类型，并不是传引用**

**类是引用类型**，所以可能有多个变量和常量引用同一个类实例，这种时候比较是否是引用同一个实例，可以用 `===` 和 `!==`

#### 类和结构体的选择

符合一条或者多条以下条件，请考虑结构体：

+ 封装少量相关的简单数据值
+ 预计的使用方式是传值而不是引用
+ 存储的值类型也应该被拷贝
+ 不需要继承

在 Swift 中，许多基本类型，如 String, Array 和 Dictionary 类型均以结构体的形式实现。这意味着被赋值给新的常量或变量，或者被传入函数或方法中，它们的值会被拷贝。

在 Objective-C 中 NSString, NSArray 和 NSDictionary 类型均以类的形式实现，而并非结构体。它们在被赋值或者被传入函数或方法时，不会发生值拷贝，而是传递现有实例的引用

### 属性

延迟存储属性是指当第一次被调用的时候才会计算其初始值的属性。在属性声明前使用 `lazy` 来表示一个延迟存储属性。必须将延迟存储属性声明成变量，反正就是只有用到的时候才初始化，这样效率更高

```swift
class DataImporter {
	var fileName = "data.txt"
}

class DataManager {
	lazy var importer = DataImporter()
	var data = [String]()
}

let manager = DataManager()
manager.data.append("Some data")
manager.data.append("Some more data")
```

#### 便捷 setter 声明

如果计算属性的 setter 没有定义表示新值的参数名，则可以使用默认名称 `newValue`

```swift
struct AlternativeRect {
	var origin = Point()
	var size = Size()
	var center: Point {
		get {
			let centerX = origin.x + (size.width / 2)
			let centerY = origin.y + (size.height / 2)
			return Point(x: centerX, y: centerY)
		}
		set {
			origin.x = newValue.x - (size.width / 2)
			origin.y = newValue - (size.height / 2 )
		}
	}
}
```

#### 属性观察器

每次属性被设置值的时候会调用属性观察器

+ `willSet` 新值被设置前调用（默认参数 newValue）
+ `didSet` 新值被设置后调用（默认参数 oldValue）

```swift
class StepCounter {
	var totalSteps: Int = 0 {
		willSet(newTotalSteps) {
			print ("About to set totalSteps to \(newTotalSteps)")
		}
		didSet {
			if totalSteps > oldValue {
				print ("Added \(totalSteps - oldValue) steps")
			}
		}
	}
}

// 注意观察输出
let stepCounter = StepCounter()
stepCounter.totalSteps = 200
stepCounter.totalSteps = 360
```

#### 类型属性

就是属于类型本身，而不是属于类型的实例的，相当于静态变量

```swift
struct SomeStructure {
	static var storedTypeProperty = "Some value."
	static var computedTypeProperty: Int {
		return 1
	}
}

enum SomeEnumeration {
	static var storedTypeProperty = "Some value."
	static var computedTypeProperty: Int {
		return 6
	}
}

class SomeClass {
	static var storedTypeProperty = "Some value."
	static var computedTypeProperty: Int {
		return 27
	}
}

```

#### 方法 Methods

分为实例方法与类型方法，就是普通方法与 static 方法的区别，这里不赘述

### 下标脚本 Subscript

用在类、枚举、结构体等目标中，可以认为是访问集合 collection，列表 list 或序列 sequence 的快捷方式，等于是重写一个方法这样就可以用下标来访问数组的元素

```swift
struct TimesTable {
	let multiplier: Int
	subscript(index: Int) -> Int {
		return multiplier * index
	}
}

let threeTimesTable = TimesTable(multiplier: 3)
print("3 的 6 倍是 \(threeTimesTable[6])")
```

### 继承 Inheritance

基本就是面向对象的那一套，具体看代码演示

```swift
// 基类
class Vehicle {
	var currentSpeed = 0.0
	var description: String {
		return "travelling at  \(currentSpeed) miles per hour"
	}
	func makeNoise() {
		// do nothing
	}
}

let someVehicle = Vehicle()
print ("Vehicle: \(someVehicle.description)")

// 子类
class Bicycle: Vehicle {
	var hasBasket = false
}

let bycycle = Bycycle()
bycycle.hasBascket = true
bycycle.currentSpeed = 15.0
print ("Bycycle: \(bicycle.description)")

// 继续继承
class Tandem: Bicycle {
	var currentNumberOfPassengers = 0
}
let tandem = Tandem()
tandem.hasBasket = true
tandem.currentNumberOfPassengers = 2
tandem.currentSpeed = 22.0
print("Tandem: \(tandem.description)")

// 重写需要添加 override
class Train: Vehicle {
	override func makeNoise() {
		print("Choo Choo")
	}
}
let train = Train()
train.makeNoise()

// 同样也可以重写属性
class Car: Vehicle {
	var gear = 1
	override var description: String {
		return super.description + " in gear \(gear)"
	}
}

let car = Car()
car.currentSpeed  = 25.0
car.gear = 3
print("Car: \(car.description)")

// 重写属性观察器
class AutomaticCar: Car {
	override var currentSpeed: Double {
		didSet {
			gear = Int(currentSpeed / 10.0) + 1
		}
	}
}
```

防止重写的话，在前面加上 `final` 关键字即可

### 构造过程 Initialization

在构造器中设置属性时是直接设置的，不会触发任何属性观察者(property observers)

```swift
struct Fahrenheit {
	var temperature: Double
	init() {
		temperature = 32.0
	}
}

// 默认属性值
struct Fahrenheit {
	var temperature = 32.0
}

// 自定义构造过程
struct Celsius {
	var temperatureInCelsius: Double
	init (fromFahrenheit fahrenheit: Double) {
		temperatureInCelsius = (fahrenheit - 32.0) / 1.8
	}
	init (fromKelvin kelvin: Double) {
		temperatureInCelsius = kelvin - 273.15
	}
}

let boilingPointOfWater = Celsius(fromFahrenheit: 212.0)
```

#### 便利构造器

调用同一个类中的指定构造器

```swift
init(parameters){
	statements
}

covenience init(parameters){
	statements
}
```

+ 指定构造器必须调用其直接父类的指定构造器
+ 便利构造器必须调用同一类中定义的其他构造器
+ 便利构造器必须最终以吊用一个指定构造器结束

或

+ 指定构造器必须总是向上代理
+ 便利够再起必须总是横向代理

#### 两段式构造过程

阶段一中，每个存储型属性通过引入它们的类的构造器来设置初始值。当每一个存储型属性值被确定后，第二阶段开始，它给每个类一次机会在新实例准备使用之前进一步定制它们的存储型属性。

两段式构造过程的使用让构造过程更安全，同时在整个类层级结构中给予每个类完全的灵活性。两段式构造过程可以防止属性值在初始化之前被访问；也可以防止属性被另外一个构造器意外地赋予不同的值。

#### 其他一些内容

这部分等具体用到的时候再补充，这里就是有个印象

+ 可失败构造器 `init?`
+ 必要构造器 `required init()`
+ 通过闭包和函数来设置属性的默认值

### 析构过程 Deinitialization

用关键字 `deinit` 定义，每个类最多只能有一个析构器，而且不带任何参数。在实例释放发生前被自动调用。析构器是不允许被主动调用。

```swift
deinit {
	// 执行析构过程
}
```

## Swift 2 高级

这里是偏内部机制和 Swift 本身特性的部分，需要认真理解掌握。

### 自动引用计数 Automatic Reference Counting

引用计数仅仅应用于类的实例。结构体和枚举类型是值类型，不是引用类型，也不是通过引用的方式存储和传递的。

#### 工作机制

每次创建一个类的新的实例是，ARC 会分配一大块内存用来存储实例信息。内存中会包含实例的类型信息，以及这个实例所有相关属性的值。为了确保使用中的实例不会被销毁，ARC 会跟踪和计算每一个实例正在被多少属性、常量和变量所引用。哪怕实例的引用数为一，ARC 都不会销毁这个实例。

无论将实例赋值给属性、常量或变量，它们都会创建此实例的强引用。只要强引用还在，实例是不允许被销毁的。

#### 自动引用计数实践

通过一个例子来学习

```swift
class Person {
	let name: String
	init(name: String) {
		self.name = name
		print("\(name) is being initialized")
	}
	deinit {
		print("\(name) is being deinitialized")
	}
}

// 初始值自动初始化为 nil
var reference1: Person?
var reference2: Person?
var reference3: Person?

// 接下来创建一个新实例
reference1 = Person(name: "Da Wang")
// 这时从 reference1 到这个新实例间建立了一个强引用
reference2 = reference1
reference3 = reference1
// 现在这个 Person 实例已经有三个强引用了

reference2 = nil
reference3 = nil
// 这时因为还有一个强引用，所以不会被销毁

reference1 = nil
// 这时因为没有引用了，所以这个实例就被销毁了
```

但是如果有两个类，这两个类中各有一个属性是另外一个类的实例，那么就会导致循环强引用。为了解决这个问题，有两种办法：弱引用(weak reference)和无主引用(unowned reference)

弱引用和无主引用允许循环引用中的一个实例引用另外一个实例而不保持强引用。这样就避免了循环引用。对于生命周期中会变为 nil 的实例使用弱引用。相反地，对于初始化赋值后再也不会被赋值为 nil 的实例，使用无主引用。

#### 弱引用

弱引用必须被声明为变量，表明其值能在运行时被修改。因为弱引用可以没有值，必须将每一个弱引用声明为可选类型

```swift
class Person {
	let name: String
	init(name: String) {
		self.name = name
	}
	var apartment: Apartment?
	deinit {
		print("\(name) is being deinitialized")
	}
}

class Apartment {
	let unit: String
	init (unit: String){
		self.unit = unit
	}
	weak var tenant: Person?
	deinit {
		print ("Apartment \(unit) is being deinitialized")
	}
}
```

在使用垃圾回收的系统里，弱指针有时用来实现简单的缓冲机制，因为没有强引用的对象只会在内存压力触发垃圾收集时才被销毁。但是在 ARC 中，一旦值的最后一个强引用被删除，就会被立刻销毁。

#### 无主引用

无主引用是永远有值的，所以一定要被定义成非可选类型。用关键字 `unowned`。无主引用总是可以被直接访问的。不过 ARC 无法在实例被销毁后将无主引用设为 nil。

下面的例子中，因为信用卡总是关联着一个客户，因此将 customer 属性定义为无主引用，用以避免循环强引用

```swift
class Customer [
	let name: String
	var card: CreditCard?
	init (name: String){
		self.name = name
	}
	deinit {
		print("\(name) is being deinitialized")
	}
}

class CreditCard {
	let number: UInt64
	unowned let customer: Custoer
	init(number: UInt64, customer: Customer){
		self.number = number
		self.customer = customer
	}
	deinit {
		print("Card \(number) is being deinitialized")
	}
}
```

以上就是两种常用的需要打破循环强引用的场景

Person 和 Apartment 的例子展示了两个属性的值都允许为 nil，并且会潜在的产生循环强引用。适合用弱引用解决。

Customer 和 CreditCard 的例子展示了一个属性的值允许为 nil，而另一个属性的值不允许为 nil，这种情况适合用无主引用来解决。

还有第三种场景，这里两个属性都必须有值，并且初始化完成后永远不会为 nil。在这种场景中，需要一个类使用无主属性，而另外一个类使用隐式解析可选属性。

```swift
class Country {
	let name: String
	// 这里用感叹号来表示隐式解析可选属性
	var capitalCity: City!
	init(name: String, capitalName: String) {
		self.name = name
		sel.capitalCity = City(name: capitalName, country: self)
	}
}

class City {
	let name: String
	unowned let country: Country
	init(name: String, country: Country) {
		self.name = name
		self.country = country
	}
}
```

#### 闭包引起的循环强引用

可以用一个称为闭包捕获列表 closure capture list 的计数来解决这个问题。问题的产生

```swift
class HTMLElement {
	let name: String
	let text: String?
	
	lazy var asHTML: Void -> String = {
		if let text = self.text {
			return "<\(self.name)>\(text)</\(self.name)>"
		} else {
			return "<\(self.name) />"
		}
	}
	
	init(name: String, text:String? = nil){
		self.name = name
		self.text = text
	}
	
	deinit {
		print ("\(name) is being deinitialized")
	}
}

let heading = HTMLElement(name: "h1")
let defaultText = "some default text"
heading.asHTML = {
	// ...
}
```

这里实例的 `asHTML` 属性持有闭包的强引用，但是闭包在闭包体里使用了 `self`，因此闭包又持有了 HTMLElement 实例的强引用，这样就循环了。

**定义捕获列表**

每一项都由一对元素组成，一个元素是 `weak` 或 `unowned` 关键字，另一个元素是类实例的引用(如 `self`) 或初始化过的变量。如果闭包又参数列表和返回类型，把捕获列表放在它们前面

```swift
lazy var someClosure: (Int, String) -> String = {
	[unowned self, weak delegate = self.delegate!]
	(index: Int, stringToProcess: String) -> String in
		// closure body
}
```

**弱引用和无主引用**

在闭包和捕获的实例总是互相引用时并且总是同时销毁时，将闭包内捕获定义为无主引用。

相反地，在被捕获的引用可能会变为 nil 时，将闭包内的捕获定义为弱引用，所以之前的类可以改为

```swift
class HTMLElement {
	let name: String
	let text: String?
	
	lazy var asHTML: Void -> String = {
		[unowned self] in
		if let text = self.text {
			return "<\(self.name)>\(text)</\(self.name)>"
		} else {
			return "<\(self.name) />"
		}
	}
}
```

### 可空链式调用 Optional Chaining

是一种可以请求和调用属性、方法及下标的过程，所谓可空指的是调用的目标当前可能为空。如果可空的目标有值，那么就会调用成功，如果为空，这种调用会返回 nil。多个连续的调用可以被链接在一起形成一个调用链，任何一个为空，整个调用链就会失败。

可空链式调用(用?)与强制展开(用!) 的不同

```swift
class Person {
	var residence: Residence?
}

class Residence {
	var numberOfRooms = 1
}

let john = Person()

// 以下强制调用会出现运行时错误
let roomCount = john.residence!.numberOfRooms

// 可空链式调用可以避免出错，而是返回一个空值
if let roomCount = john.residence?.numberOfRooms {
	print("John's Residence has \(roomCount) rooms.")
} else {
	print("Unable to get the numebr of rooms")
}
```

+ 可以通过可空链式调用访问属性的可空值，并且判断访问是否成功
+ 可以通过可空链式调用来调用方法，并判断是否调用成功，即使这个方法没有返回值
+ 可以通过可空链式调用来访问下标：`john.residence?[0]`
+ 如果下标返回可空类型值，比如 Dictionary 中的 key 下标，那么同样可以是用可空链式调用
+ 其实就是在每个可空类型之后加个问号，可以有效解决值或者引用为空带来的问题

```swift
var testScores = ["Dave": [86, 82, 84], "Bev": [79, 94, 81]]

testScores["Dave"]?[0] = 91
testScores["Bev"]?[0]++
testScores["Wdx"]?[0] = 72 // failure
```

### 错误处理 Error Handling

错误遵从 `ErrorType` 协议类型，使用 `throw` 关键词来抛出错误，如

```swift
enum VendingMachineError: ErrorType {
	case InvalidSelection
	case InsufficientFunds(coinsNeeded: Int)
	case OutOfStock
}

// 抛出错误
throw VendingMachineError.InsufficientFunds(coinsNeeded: 5)
```

四种错误处理的方式

1. 把函数抛出的错误传递给调用此函数的代码
2. 用 `do-catch` 语句处理错误
3. 将错误作为可选类型
4. 断言错误根本不会发生

#### 用 throwing 传递错误

一个 throwing 函数从其内部抛出错误，并传递到该函数被调用时所在的区域中。注意，只有 throwing 函数可以传递错误。任何在某非 throwing 函数内部抛出的错误只能在此函数内部处理

```swift
func canThrowErrors() throws -> String
func cannotThrowErrors() -> String
```

下面是一个具体的例子

```swift
struct Item {
	var price: Int
	var count: Int
}

class VendingMachine {
	var inventory = [
		"Candy Bar": Item(price:12, count: 7),
		"Chips": Item(price:10, count:4),
		"Pretzels": Item(price:7, count: 11)
	]
	var coinsDeposited = 0
	
	func dispenseSnack(snack: String){
		print("Dispensing \(snack)")
	}
	
	func vend(itemNamed name: String) throws {
		guard var item = inventory[name] else {
			throw VendingMachineError.InvalidSelection
		}
		
		guard item.count > 0 else {
			throw VendingMachineError.OutOfStock
		}
		
		guard item.price <= coinsDeposited else {
			throw VendingMachineError.InsufficientFunds(coinsNeeded: item.price - coinsDeposited)
		}
		
		coisDeposited -= time.price
		item.count--
		inventory[name] = item
		dispenseSnack(name)
	}
}
```

也可以使用 `try?` 通过将其转换成一个可选值来处理错误。如果在评估 `try?` 表达式时一个错误被抛出，那么这个表达式的值就是 nil。例如下面代码中 x 和 y 有相同的值和特性

```swift
func someThrowingFunction() throws -> Int {
	// ...
}

let x = try? 
someThrowingFunction()

let y = Int? 
do {
	y = try someThrowingFunction()
} catch {
	y = nil
}
```

也可以在表达式前面写 `try!` 来使错误传递失效

```swift
let photo = try! loadImage("./Resources/JohnAppleseed.jpg")
```

#### 指定清理操作

可以使用 `defer` 语句在代码之前到要离开当前的代码段之前去执行一套语句，不管是以何种方式离开当前的代码段的。`defer` 关键字加上要被延时执行的语句。延时执行的语句不会包含任何会将控制权移交到外面的代码，操作是按照被指定的顺序的相反顺序执行，即第一条语句会在第二条语句执行之后执行。即使没有错误处理代码，也可以使用 `defer` 语句

```swift
func processFile(filename: String) throws {
	if exists(filename) {
		let file = open(filename)
		defer {
			close(file)
		}
		while let line = try file.readline() {
			// 处理文件
		}
		close(file)
	}
}
```

### 类型转换 Type Casting

使用 `is` 和 `as` 操作符实现。

+ 类型检查 `is`
+ 类型转换 `as`
+ 向下转型，从父类转换到子类 `as?` 或 `as!`

不确定类型也有两种别名，当然，只有在非用不可的时候才用这种不明确的类型，毕竟类型明确更清晰

+ `AnyObject` 可以代表任何 class 类型的实例
	+ 工作中使用 Cocoa APIs 一般会接收一个 [AnyObject] 类型的数组
+ `Any` 可以表示任何类型，包括方法类型
	+ 可以使用 `Any` 类型来混合不同的类型一起工作

### 嵌套类型 Nested Types

在外部对嵌套类型的引用，以被嵌套类型的名字为前缀，加上所要引用的属性名

```swift
let heartsSymbol = BlackjackCard.Suit.Hearts.rawValue
```

### 扩展 Extensions

向一个已有的类、结构体、枚举类型或者协议添加新功能，和 Objective-C 中的 categories 类型（但 Swift 的扩展没有名字）。注意，扩展可以添加新功能，但是不能重写已有的功能。使用关键字 `extension`

Swift 中的扩展可以：

+ 添加计算型属性和计算型静态属性
+ 定义实例方法和类型方法
+ 提供新的构造器
+ 定义下标
+ 定义和使用新的嵌套类型
+ 使一个已有类型符合某个协议

```swift
extension SomeType {
	// 在这里写添加的新功能
}

// 扩展类型以适配协议
extension SomeType: SomeProtocol, AnotherProtocol {
	// 协议实现
}
```

基本上所有的东西都可以利用扩展来添加到已有的类中

### 协议 Protocols

使用关键字 `protocol`，如果类在遵循协议的同时拥有父类，应该将父类名放在协议名之前，以逗号分隔

```swift
protocol SomeProtocol {
	// 协议内容
}
```

#### 对属性的规定

协议可以提供特定类型的实例属性或类属性(也就是确定是不是静态成员)，而不用指定是存储型属性还是计算型属性。当然还必须指明是只读的还是可读可写的

```swift
protocol SomeProtocol {
	var mustBeSettable: Int {get set}
	var doesNotNeedToBeSettable: Int {get}
	// 类属性
	static var someTypeProperty: Int {get set}
}
```

#### 对 Mutating 方法的规定

对普通方法的规定就是正常的方法定义以及是不是要 static。

有时需要在方法中改变它的实例，使用 mutating 关键字，表示可以在该方法中修改它所属的实例以及实例属性的值。

+ 用类实现协议中的 mutating 方法时，不用写 mutating 关键字
+ 用枚举实现协议中的 mutating 方法时，必须写 mutating 关键字

#### 对构造器的规定

不需要写花括号和构造器的实体

```swift
protocol SomeProtocol {
	init(someParameter: Int)
}
```

#### 委托(代理)模式

协议同样可以当作类型来使用，基于这种设计，可以有以下这种称为委托的设计模式。

它允许**类**或**结构体**将一些需要它们负责的功能**委托**给其他类型的实例。委托模式的实现很简单：定义协议来封装那些需要被委托的函数和方法。委托模式可以用来响应特定的动作或接收外部数据源提供的数据，而无须知道外部数据源的类型。

这个具体可以参考官方给出的代码，实际上是保持面向对象的一种快捷方式

#### 协议继承和扩展

协议的继承和扩展与类的继承与扩展基本一致，这里不赘述

#### 类专属协议

指的是结构体和枚举不能使用的协议，添加 `class` 关键字，而且必须第一个出现在协议的继承列表里

```swift
protocol SomeClassOnlyProtocol: class, SomeInheritedProtocol {
	// 协议定义
}
```

#### 协议合成

通过 `protocol<SomeProtocol, AnotherProtocol>` 的格式来进行合成，用逗号分隔。协议合成并不会生成一个新协议类型，而是将多个协议合成为一个临时的协议，超出范围后立即失效

+ `is`: 检查实例是否遵循了某个协议
+ `as?`: 返回一个可选值，当实例遵循某协议时，返回该协议类型，否则返回 nil
+ `as`: 向下强制转型，转型失败会引起运行时错误

### 泛型 Generics

比如说，交换两个值

```swift
func swapTwoValues<T>(inout a: T, inout _ b: T) {
	let t = a
	a = b
	b = t
}
```

使用泛型的类型有很多，比如说，栈

```swift
var stackOfString = Stack<String>()
stackOfString.push("uno")
stackOfString.push("docs")
```

当然，对于泛型，可以对类进行一定的约束，比如说 Dictionary 中的 key 就要求是 hashable 的

```swift
func someFunction<T: SomeClass, U: SomeProtocol>(SomeT: T, someU: U){
	// 函数主体
}
```

使用 where 语句来定义参数约束

```swift
func allItemsMatch<C1: Container, C2: Container where C1.ItemType == C2.ItemType, C1.ItemType: Equatable>(comeContainer: C1, anotherContainer: C2) -> Bool {
	// 函数主体
}
```

### 访问控制 Access Control

如果只是开发一个单目标的应用程序，完全可以不用申明代码的显式访问级别。

Swift 中的访问控制模型基于模块和源文件这两个概念。

模块指的是以独立单元构建和发布的 Framework 或 Application。在 Swift 中的一个模块可以使用 import 关键字引入另外一个模块。

有三种不同的访问级别

+ public: 没限制，一般设计大家用的 API 用这个
+ internal: 别人不能访问该模块中源文件里的实体，用作内部结构
+ private: 只能在当前文件中使用，隐藏实现细节

**使用原则：访问级别的统一性**：也就是说只能越来越松，而不能越来越紧

默认访问级别是 internal

```swift
public class SomePublicClass {}
internal class SomeInternalClass {}
private class SomePrivateClass {}
```

+ 类访问级别会影响到类成员的默认访问级别
	+ 一个 public 类的所有成员的访问级别默认为 internal 级别
+ 元组的访问级别与元组中访问级别最低的类型一致
+ 枚举中成员的访问级别继承自该枚举，不能自定义不同的访问级别
+ 子类的访问级别不得高于父类的访问级别
+ 泛型类型或泛型函数的访问级别取决于泛型类型、函数本身、泛型类型参数三者中的最低访问级别

### 高级运算符

Swift 中的算数运算符默认是不会溢出的，所有的溢出都会被捕获并报告为错误。另一套支持溢出的运算符以 `&` 开头，如：`&+, &-`

#### 位运算

支持 C 语言所有的位运算

+ 取反 `~`
+ 与 `&`
+ 或 `|`
+ 异或 `^`
+ 左移右移 `<<`, `>>`

#### 运算符重载

和 Cpp 类似，具体看代码，需要注意的是不能对默认的赋值运算符 `=` 进行重载

```swift
struct Vector2D {
	var x = 0.0, y = 0.0
}

// 中缀运算符
func + (left: Vector2D, right: Vector2D) -> Vector2D {
	return Vector2D(x: left.x + right.x, y: left.y + right.y)
}

// 前缀(prefix)/后缀(postfix)运算符，加不同关键字即可
prefix func - (vector: Vector2D) -> Vector2D{
	return Vector2D(x: -vector.x, y: -vector.y)
}

// 赋值运算符，需要加上 inout
func += (inout left: Vector2D, right: Vecter2D) {
	left = left + right
}

// 等价操作符
func == (left: Vector2D, right: Vector2D) -> Bool {
	return (left.x == right.x) && (left.y == right.y)
}
func != (left: Vector2D, right: Vector2D) -> Bool {
	return !(left == right)
}

// 自定义运算符
prefix func +++ (inout vector: Vector2D) -> Vector2D {
	vector += vector
	return vector
}
```

当然也可以自定义优先级和结合性

+ 结合性可取的值有 left, right, none
+ 结合性默认值是 none
+ 优先级如果没有指定，则默认为 100


