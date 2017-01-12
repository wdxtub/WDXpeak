# Swift Programming Language

Swift is the new programming language used for iOS and OS X applications. This guide is by Apple.

## The Basics

Declare constants/variables with `let`/`var`:

    let maxLogin = 10
    var loginAttempts = 0
    var x = 0.0, y = 0.0, z = 0.0

Type annotations can be made with a colon, below reads "welcome message of type string" - although
Swift can usually infer the type from constant/variable initialization.

    var welcomeMessage: String
    welcomeMessage = "Hello!"
    println(welcomeMessage)

Comments are specified with `//` or `/* ... */`, nested multiline comments are enabled:

    /* starting comment
    /* nested */
    ending comment*/

Semicolons are optional, most example code is written without it. You can use it to combine multiple
statements into one line though:

    let message = "Hello!"; println(message)

Integers are whole numbers, can be signed/unsigned in 8,16,32,64 bit forms. Example types are
`UInt8` or `Int32`. Bounds are specified like `UInt8.min` or `Int32.max`. `Int` defaults to current
32 or 64 bit platform. You'll usually want `Int` or `UInt`.

Floats are numbers with fractional components and can be stored with: `Double` for 64-bit floating
point number or `Float` for 32-bit.

Numeric literals can be inferred with prefixes: no prefix is decimal, `0b` for binary, `0o` for
octal, `0x` for hex. Suffixes can be `e` or `p` meaning `*10^n` or `*2^n`. So `1.25e2` means `1.25 *
10^2` and `15p2` means `15 * 2^2`.

Define type aliases with `typealias` keyword:

    typealias AudioSample = UInt16
    var maxAmp = AudioSample.min

Bool types represent boolean values: `true` and `false`. They're useful with `if` statements:

    if turnipsAreDelicious {
        // ...
    }

Tuples are multiple values grouped together:

    let http404Error = (404, 'Not Found')
    let (statusCode, _) = http404Error // underscore can be used to ignore decomposition
    println("The status code is \(statusCode)")
    println("The status code is \(http404Error.0)")

Tuples accept naming too:

    let http200Status = (statusCode: 200, description: "OK")
    println("The status code is \(http200Status.statusCode)")

Optionals can be used when value may not be present and is specified with a suffix `?` like `Int?`.
They can be used in `if` statements like booleans. Use the suffix `!` to force unwrap the optional's
underlying value. A common pattern is optional binding:

    if let actualNum = possibleNum.toInt() {
        // ... use actualNum ..
    }

`nil` is the empty value for Swift and can be assigned to optional constants/variables. It's also
the default when initializing optional constants/variables.

Implicitly unwrapped optionals are declared using `!` suffix. They're used like optionals but
already have a value.

Assertions are made with `assert()`.

## Basic Operators

Swift's basic operators are similar to C's, except modulus is allowed on floating point numbers and
Swift includes range operators (`..` and `...`).

There are 3x categories: unary/prefix/postfix, binary/infix, and ternary.

* `=` for assignment
* `+`, `-`, `*`, `/` for arithmetic
* `%` for remainder
* `++`, `--` for increment/decrement
* `-` for unary negate
* `+` for unary plus, doesn't do anything but can be useful for code annotation
* `=+` or any other arithmetic operators for compound assignments
* `==`, `!=`, `>`, `>=`, `<`, `<=` for comparisons
* `===`, `!===` for comparing identities (same instance)
* `a ? b : c` for ternary conditional
* `a...b` for closed range (includes a and b, eg `for i in 1...5`)
* `a..<b` for half-closed ranged (includes a but not b, eg `for i in 1..<5`)
* `!`, `&&`, `||` for logical NOT, AND, OR

## Strings and Characters

String literals are placed in double quotes, `"Some string literal value"`. Use a backslash to
escape characters. Use `\()` for string interpolation.

Strings are value types and are passed as values to methods. Strings/characters can be concatenated
with `+`. Specify a character like so:

    let character1: Character = "!"

Useful methods and properties:

* `countElements(str)` - returns length
* `str.isEmpty`
* `str.hasPrefix(str2)`
* `str.hasSuffix(str2)`
* `str.uppercaseString`
* `str.lowercaseString`
* `str.utf8` - collection of UInt8 character representations
* `str.utf16` - collection of UInt16 character representations
* `str.unicodeScalars` - collection of UnicodeScalar

## Collection Types

Swift provides two: arrays and dictionaries.

Arrays are specified like: `Array<SomeType>` or `[SomeType]`:

    var shoppingList: [String] = ["Eggs", "Milk"]
    var shoppingList = ["Eggs", "Milk"] // type inferred

Useful methods, properties, etc:

* `arr.count`
* `arr.isEmpty`
* `arr.append(obj)`
* `arr.insert(obj, atIndex: index)`
* `arr.removeAtIndex(index)`
* `arr.removeLast()`
* `arr += obj`
* `arr += [obj1, obj2, obj3, ...]`
* `arr + arr2` concats arrays
* `arr[index]`
* `arr[index] = obj`
* `arr[index1...index2] = [obj1, obj2, obj3, ...]`
* `for obj in arr { }`
* `for (index, obj) in enumerate(arr) { }`
* `var arr = [SomeType]()` declare/initializes empty array
* `var threeDoubles = [Double](count: 3, repeatedValue: 0.0)` initializes repeated array

Dictionaries are specified like: `Dictionary<KeyType, ValueType>` or `[KeyType: ValueType]`:

    var airports: [String: String] = ["TYO": "Tokyo", "DUB": "Dublin"]

Useful methods, properties, etc:

* `d.count`
* `d[key]` can be nil, so returns optional type
* `d[key] = value`
* `d[key] = nil` removes entry
* `d.updateValue(val, forKey: key)` expression returns old value
* `for (key, val) in d { }`
* `d.keys` please note it's unordered
* `d.values` please note it's unordered
* `var d = [Int: String]()` declare/initializes empty dictionary
* `d = [:]` resets to empty dictionary if type can be inferred

A KeyType must be hashable (conforms to `Hashable` protocol) to be used as a key. All of Swift's
basic types are hashable.

## Control Flow

There's the standard `for-condition-increment` loop found in C. There's also the new `for-in` loop
for iterating over collections:

    for index in 1...5 {
        // index only exists within this scope, use `_` in place of index to ignore
    }
    for val in anArray { ... }
    for (key, val) in aDictionary { ... }

Swift also implements the `while` and `do while` loops found in C.

`if`, `else if`, and `else` are also all implemented.

`switch` is implemented but differs a bit. Swift uses type checking to make sure the statement is
exhaustive or contains a `default`. There is no implicit fall through. Multiple matches are
separated with a comma. You can also use range or tuple matching. With tuple matching, use an
underscore to denote any possible value.

Value binding can be used in switches:

    switch point {
    case (let x, 0):
        ...
    case (0, let y):
        ...
    case let (x, y) where x == -y: // where can be used for additional conditionals
        ...
    case let (x, y):
    }

Swift has 4x control transfer statements:

* `continue`
* `break`
* `fallthrough` used in switch case statements to fall through to next case
* `return`

Switch and loop statements can be labeled to work with the control transfer statements:

    label labelName : while condition {
        // ...
        switch value {
        case valueOne:
            break labelName
        // ...
        }
    }

## Functions

Function declarations look like:

    func sayHello(firstName: String, lastName) -> String {
        return "Hello, " + firstName + " " + lastName + "!"
    }

Specify a tuple as the return value to return multiple values. Swift can infer the tuple keys:

    func abc() -> (a: Int, b: Int, c: Int) {
        // ...
        return (1, 2, 3)
    }

External parameter names can be used (eg named parameters):

    func someFunction(externalParameterName localParameterName: Int) { }
    someFunction(externalParameterName: 0)

If the external/local names are the same, use `#`:

    func someFunction(#parameterName: Int) { }
    someFunction(parameterName: 0)

Default values use `=`:

    func someFunction(parameterName: Int = 0) { }
    someFunction()

Variadic parameters can be specified with `...`:

    func someFunction(numbers: Double...) -> Double {
      // numbers is a [Double] array
    }

Parameters are constants by default, use `var` to make them variables. Note that it's still not
passed by reference. To do that, use `inout` and `&`:

    func someFunction(var string: String) { }
    func someFunction(inout a: Int) { }
    someFunction(&a)

The function type is specified by its parameter types and return type:

    func addTwoInts(a: Int, b: Int) -> Int { } // (Int, Int) -> Int
    var mathFunction: (Int, Int) -> Int = addTwoInts
    assert(5 == mathFunction(2, 3))
    func printMathResult(mathFunction: (Int, Int) -> Int, a: Int, b: Int) {
        println("Result: \(mathFunction(a, b))")
    }
    printMathResult(addTwoInts, a, b)
    func returnsMathFunc() -> (Int, Int) -> Int {
      return addTwoInts
    }

Functions can be nested. Scoping follows the same rules as local variables.

## Closures

Closure syntax looks like:

    { (parameters) -> returnType in
        statements
    }

Example sorting of an array looks like:

    reversed = sorted(names, { (s1: String, s2: String) -> Bool in return s1 > s2 })

Actually, the Swift compiler can infer the type:

    reversed = sorted(names, { s1, s2 in return s1 > s2 })

Single expressions can even omit the return, it will be implicit:

    reversed = sorted(names, { s1, s2 in s1 > s2 })

Swift provides shorthand argument names for positions:

    reverse = sorted(names, { $0 > $1 })

Of course the shortest way would be to use String's `>` operator:

    reverse = sorted(names, >)

Swift allows for trailing closures, if the closure is the last argument for the function:

    someFunction() {
        // closure defined here
    }
    reverse = sorted(names) { $0 > $1 }

Closures are reference types in Swift.

## Enumerations

Here's an example:

    enum CompassPoint {
        case North
        case South
        case East
        case West
    }
    // or
    enum CompassPoint {
        case North, South, East, West
    }
    var direction = CompassPoint.West
    var direction : CompassPoint
    direction = .West // type inference

North, South, East, West are member values or members of the CompassPoint enumeration.

Here's an example switch statement, note that it must be exhaustive:

    switch direction {
        case .North:
            // ...
        case .South:
            // ...
        case .East:
            // ...
        case .West:
            // ...
    }

Enums can have associated values:

    enum Barcode {
        case UPCA(Int, Int, Int, Int)
        case QRCode(String)
    }
    var barcode = Barcode.UPCA(8, 85909, 51226, 3)
    switch barcode {
        case let .UPCA(numberSystem, manufacturer, product, check):
            // ...
        case let .QRCode(productCode):
            // ...
    }

Enums can also have raw values, note that Int will do auto-increment like in C:

    enum ASCIIControlCharacter: Character {
        case Tab = "\t"
        case LineFeed = "\n"
    }
    enum Planet: Int {
        case Mercury = 1, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
    }

Use `toRaw()` and `fromRaw()` to transform values.

## Classes and Structures

Classes and structures are very similar: they both have properties, methods, initializers, or
protocol conformation. Classes have additional capabilities: inheritance, type casting,
deinitializers, and reference counting.

    class SomeClass {
        var someProperty = 0
    }
    struct SomeStructure {
        var someProperty = false
        var someName: String?
    }
    let someClass = SomeClass()
    let someStructure = SomeStructure(someName: "John Doe")
    println("some property: \(someClass.someProperty)")

All structures and enumerations are value types. Value types are copied in memory when passed to
methods or re-assigned. Classes are reference types. Swift's String, Array, and Dictionary are all
implemented as structures.

## Properties

There are instance properties and type properties (aka instance/class properties). If an instance
was assigned with `let`, those properties cannot be altered.

Swift supports lazy stored properties marked with `@lazy`, which isn't calculated until after
initialization:

    @lazy var importer = DataImporter()
    // dataImporter.importer isn't initialized until it's first used

There are also computed properties, which don't store a value but have defined getters/setters:

    struct Rect {
        var center: Point {
        get {
            return Point(x: centerX, y: centerY)
        }
        set(newCenter) { /* if no parameter is declared, `newValue` will be used */
          centerX = newCenter.x
          centerY = newCenter.y
        }
        }
    }

If you only define a getter, there's a shorthand:

    var center: Point {
        return Point(x: centerX, y: centerY)
    }

`willSet` and `didSet` are observers called just before/after the value is set:

    var totalSteps = 0 {
    willSet(newTotalSteps) { }
    didSet { }
    }

Computed/observed property capabilities can also be done with global/local variables.

Type properties are prefixed with the keyword `static`:

    class SomeClass {
      static var someTypeProperty = "test"
    }
    SomeClass.someTypeProperty // "test"

## Methods

Instance and class methods both exist for classes, structures, and enumerations:

    class Counter {
        var count = 0
        func increment() {
            count++
        }
        func reset() {
            count = 0
        }
    }

Apple recommends suffixing method names with parameters by a preposition like `with`, `for`, or
`by`. The default behavior of methods are that the first parameter is given a local name but
remaining parameters are given a local/global parameter name:

    class Counter {
        func incrementBy(amount: Int, numberOfTimes: Int) {
            count += amount * numberOfTimes
        }
    }
    counter.incrementBy(5, numberOfTimes: 3)

Access the current instance with `self`.

By default, structures and enumerations are value types so properties cannot be modified. A method
must be prefixed with `mutating` if it does modify any stored properties. In a mutating method, even
`self` can be re-assigned.

Type methods are prefixed with `class` for classes and `static` for structures:

    class SomeClass {
        class func someTypeMethod() {
            // ...
        }
    }

## Subscripts

Subscripts are called with `[]` and can take any number of parameters. The syntax to declare one is:

    subscript(index: Int) -> Int {
        get { }
        set { } // uses `newValue`
    }

## Inheritance

Subclasses are specified with `:` such as `class Bicycle: Vehicle {}`. Within methods, use `super`
to access the superclass's self.

When overriding an instance method, class method, instance property, or subscript use the prefix
`override`. You'd override a property to add your own custom getters/setters or observers.

To prevent overrides, use the `@final` prefix keyword.

## Initialization

Initializers are defined with the `init` keyword and work just like method definitions:

    init(aProperty: Int) { // Swift automatically creates a global parameter name for every param
        someProperty = aProperty
    }

Although if external parameter names are explicitly defined, they must be used when initializing. If
they're implicitly defined, they're optional to use.

During `init`, event constant property values defined with `let` can be assigned to.

Structures get a default initializer with all of its properties as parameters, called a memberwise
initializer.

You can define multiple initializers using different parameters. An initializer can also delegate to
other initializers to keep things DRY. A designated initializer is one that fully initializes a
class, usually there's one per class. Convenience initializers are secondary and eventually call the
designated initializer. Designated initializers may call a superclass initializer. Convenience
initializers are prefixed with `convenience`.

## Deinitialization

A deinitializer is called immediately after a class instance is deallocated:

    deinit {
        // ...
    }

They're called automatically and you're not allowed to directly call it yourself.

## Automatic Referencing Counting

Swift uses ARC for memory management. All references are strong by default, so you'll need to
explicitly mark weak references to prevent retain cycles. A weak reference is prefixed with `weak`:

    class Person {
        var apartment: Apartment?
    }
    class Apartment {
        weak var tenant: Person?
    }

Once both person and apartment strong references are set to nil, both instances will be garbage
collected.

There's also unowned references which are assumed to always hold a value. In the above example, an
apartment may or may not have a tenant so it was appropriate to use `weak`. In the below example, a
credit card must always be associated with a customer, so we'll use `unowned`:

    class Customer {
        var card: CreditCard?
    }
    class CreditCard {
        unowned let customer: Customer
    }

Once customer strong references are set to nil, both instances will be garbage collected.

A strong reference cycle can also occur if a closure is assigned to an instance property and the
closure captures `self`. Closures are reference types. Swift solves this with closure capture lists.

Place a capture list before a closure's parameter list:

    @lazy var someClosure: (Int, String) -> String = {
        [unowned self] (index: Int, string: String) -> String in
        // ...
    }

If the parameter list and return type are inferred or there's no parameter list:

    @lazy var someClosure: () -> String = {
        [unowned self] in
        // ...
    }

## Optional Chaining

Optional chaining uses `?` between an optional value and its property/method instead of `!` forced
unwrap. The difference is that optional chaining fails gracefully whereas the forced unwrap triggers
a runtime error.

    class Person {
        var residence: Residence?
    }
    class Residence {
        var numberOfRooms = 1
    }
    let john = Person()
    let roomCount = john.residence!.numberOfRooms // runtime error
    let roomCount = john.residence?.numberOfRooms // nil as inferred Int?

This works for methods and subscripts also. It can be chained:

    john.residence?.address?.street

## Type Casting

Type casting is done with `is` and `as` operators. It can be done to make sure types conform to
certain protocols or inherit from certain parent classes. In these examples, Movie and Song inherit
from MediaItem.

    var mediaItem: MediaItem
    // ...
    if mediaItem is Movie {
        // ...
    } else if mediaItem is Song {
        // ...
    }

You can downcast types using `as` or `as?`. The question mark form returns an optional value and
should be used when you're not sure if type conversion will succeed. `as` will trigger a runtime
error if there's a type mismatch.

    if let movie = item as? Movie {
        // ...
    } else if let song = item as? Song {
        // ...
    }

Swift provides `Any` and `AnyObject` to refer to any instance of any type at all except functions
and an instance of any class type (eg use `Any` for integers or enums too). Working with Cocoa APIs
will usually use Any/AnyObject since collections in Objective-C don't require a type.

## Nested Types

Swift lets you nest types. This is common for enumerations, utility classes, etc...

    struct BlackJackCard {
        enum Suit: Character {
            case Spades = "S", Hearts = "H", Diamonds = "D", Clubs = "C"
        }
    }
    let heartsSymbol = BlackJackCard.Suit.Hearts.toRaw()

## Extensions

Extensions adds behavior to existing classes like categories in Objective-C.

    extension SomeType: SomeProtocol, AnotherProtocol { // protocols are optional
        // ... add properties, initializers, methods, subscripts, nested types, etc...
    }

## Protocols

Protocols are like interfaces in Java. A class is said to adopt or conform to a protocol.

    protocol SomeProtocol {
        // ... definitions go here ...
    }

Protocols only have definitions, no implementations. On the structure/class side:

    structure SomeStructure: SomeProtocol, SomeProtocol2 {
        // ...
    }

Protocols can require any number of properties/methods. Getters/setters can also be specified as
required:

    protocol SomeProtocol {
      var someProperty: String
      var mustBeSettable: Int { get set }
      var mustBeGettable: Int { get }
      func random() -> Int
    }

Defined protocols becomes a type that you can use anywhere else a type is expected:

    func someFunc(someObj: SomeProtocol) -> SomeProtocol { }
    var someObj : SomeProtocol?

Extensions work well with protocols to extend existing types to conform to a specific protocol.

You can also define optional requirements (oxymoron?) prefixed with `@optional`. These can be called
using optional chaining such as `someOptionalMethod?(someArgument)`. This can only be used if the
entire protocol is marked with `@objc`.

## Generics

Generics lets you parameterize types to make your code more flexible.

    func swap(inout a: Int, inout b: Int) {
        let temporaryA = a
        a = b
        b = temporaryA
    }

The function above can be made more flexible with generics:

    func swap<T>(inout a: T, inout b: Int) {
        let temporaryA : T = a // note that type placeholder T can be inferred
        a = b
        b = temporaryA
    }

You can constrain type placeholders like `<T: SomeClass>`. Generics can also be used with class
definitions.

    class SomeClass<T: SomeType, U: SomeProtocol> {
        var item: T?
        var item2: U?
    }
    let someObj = SomeClass<MyClass, MyProtocol>()

Protocols let you define a generic type alias that's not specified until the protocol is adopted:

    protocol Container {
        typealias ItemType // makes sure append and subscript use same type
        mutating func append(item: ItemType)
        var count: Int { get }
        subscript(i: Int) -> ItemType { get }
    }

`where` can also be used for more constraints:

    func someFunc<T1: SomeType, T2: SomeType2 where T1.ItemType == C2.ItemType>(t1: T1, t2: T2)

## Advanced Operators

Some other operators:

* `~`, `&`, `|`, `^` bitwise NOT AND OR XOR
* `<<`, `>>` bitwise shift left/right
* `&+`, `&-`, `&*`, `&/`, `&%` opt in to overflow operations (default is error)

Swift supports operator overloading using `@infix`, `@prefix`, and `@postfix` - useful for
overloading the equivalence operator:

    @infix func + (left: SomeType, right: SomeType) -> SomeType {}

You can even overload compound assignment operators (but not assignment itself!):

    @assignment func += (inout left: SomeType, right: SomeType) {}

Declare your own operators with `operator` keyword:

    operator prefix +++ {}
    @prefix @assignment func +++ (inout obj: SomeType) -> SomeType {}

Declared operators can also have a declared precedence or associativity:

    operator infix +- { associativity left precedence 140 } // precedence defaults to 100