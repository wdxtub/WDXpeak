# Seven Languages in Seven Weeks

Bruce A. Tate introduces us to seven different programming languages. It's meant to enlighten you
with introductions rather than make you an expert.

For each language, Tate will answer:

* What's the typing model?
* What's the programming model?
* How to interact with it?
* What are the decision constructs and core data structures?
* What core features make this language unique?

# Ruby

Ruby belongs in the family of scripting languages. It's an interpreted, dynamically/strong typed,
object-oriented language with some functional features. It's not hugely efficient in terms of
execution speed but makes programmers happier.

Go to [http://www.ruby-lang.org/en/downloads/] to download Ruby. Start a REPL by with the `irb`
command (stands for interactive ruby). Here's a quick sample:

    >> puts 'hello, world'
    hello, world
    >> nil
    >> language = 'my Ruby'
    >> 'my Ruby'
    >> puts "hello, #{language}"
    >> 'hello, my Ruby
    >> nil

Every line returns a value. Every method you define will always return a value. If nothing is
explicitly returned, the last expression will be implicitly returned.

Methods are defined like:

    def method_name(arg1, arg2)
      # method body
    end

The last line is an implicit return value. Arrays are initiated like:

    >> animals = ['ions', 'tigers', 'bears']
    >> animals[0]
    => "lions"

Hashes uses labels as keys and are used like:

    >> numbers = {1 => 'one', 2 => 'two', :array => [1,2,3]}
    >> numbers[1]
    => 1
    >> numbers[:array]
    => [1,2,3]

Ruby supports code blocks which are functions without names:

    >> 3.times { puts 'hello world' }
    >> 3.times do
    >>   puts 'hello world'
    >> end

Arguments are passed through vertical bars:

    >> animals.each { |a| puts a }

Everything is an object. The number `4` is an instance of `Fixnum`, which inherits from `Integer`
which inherits from `Numeric` which is an instance of `Class` which inherits from `Module` which
inherits from `Object`. Here's a class:

    class Person
      attr_accessor :first_name, :last_name

      def initialize(first, last)
        @first_name = first
        @last_name = last
      end

      def full_name
        @first_name + ' ' + @last_name
      end
    end

This implicitly inherits from `Object`. An explicit inherit looks like:

    class ClassName < SuperClassName

Ruby uses modules when inheritance doesn't make sense. Modules are collections of
functions/constants.

    module ToFile
      def filename
        "object_#{self.object_id}.txt"
      end

      def to_f
        File.open(filename, 'w') {|f| f.write(to_s)}
      end
    end

    class Person
      include ToFile
    end

    p1 = Person.new("John", "Doe")
    p1.filename # => 'object_123.txt'
    p1.to_f     # => saves to_s to file

Some strengths of Ruby:

* duck typing for polymorphic designs
* uniform/consistent object interfaces
* open classes and modules
* great for scripting and web development if scaling is reasonable

Some weaknesses:

* performance (many features hurt the performance)
* concurrency is tough with OOP
* type safety, tools are harder to build for such dynamic typing

Io ==

Prototype language like JavaScript where every object is a clone of another. Core strengths are
embeddable onto small VMs, concurrency, customizable syntax, and simplicity of syntax.

The interpreter is here: <http://iolanguage.com>

    Io> "Hi ho, Io" print

No syntatic sugar, you're sending a message to the String object. Create new objects by cloning
existing ones. We're creating a Vehicle object (not a class) and assigning a value to the
`description` slot:

    Io> Vehicle := Object clone
    Io> Vehicle description := "Something to take you places"
    Io> Vehicle description
    ==> Something to take you places

    Io> Vehicle slotNames
    ==> list("type", "description")

    Io> Vehicle type
    ==> Vehicle

Slots are automatically created if they don't already exist for `:=`. You can also use the `=`
syntax, which will throw an exception if the slot doesn't exist.

There are no classes, interfaces, or modules. There are only objects. Io uses convention - if your
variable is lowercase than it's an instance. If it starts with an uppercase - then it's more of a
blueprint:

    Io> ferrari := Vehicle clone
    Io> ferrari slotNames
    ==> list()
    Io> ferrari type
    ==> Car

If a slot name doesn't exist, Io will pass it up the cloned chain. Instead of superclass, Io calls
it an object's prototype.

Methods are created like:

    Io> method("So, you've come for an argument." println)
    Io> Vehicle drive := method("Vroom" println)
    Io> ferrari drive
    Vroom
    ==> Vroom
    Io> ferrari getSlot("drive")
    ==> method("Vroom" println)

The `proto` slot is useful for debugging. There's also a master namespace called `Lobby`.

Some useful objects:

* use the `list` method to create lists which have the slots: `size`, `append`, `average`, `sum`,
  `at`, `pop`, `prepend`, and `isEmpty`.
* use `Map clone` to create hashes which have the slots: `atPut`, `at`, `asObject`, `asList`,
  `keys`, and `size`.
* booleans are represented by `true` and `false` (`and` and `or` for operations)
* to create a singleton just overwrite the `clone` slot to return itself

Loops can be done like:

    loop("getting dizzy..." println)
    ^C
    while(i <= 11, i println; i = i + 1);
    for(i, 1, 11, i println);
    for(i, 1, 11, 2, i println); # optional increment

Io has operators, to see it use `OperatorTable` in the REPL. This is another object. You can add
operators too:

    OperatorTable addOperator("xor", 11)
    true xor := method(bool, if(bool, false, true))
    false xor := method(bool, if(bool, true, false))

Everything in Io are messages and Io provides reflection. A message is made up of the `sender`,
`target`, and `arguments`. `call` gives you access to this meta information.

Io is especially suited for DSLs since you can redefine any operators or symbols. For example, a
"map" DSL of names to numbers:

    OperatorTable addAssignOperator(":", "atPutNumber")
    curlyBrackets := method(
      r := Map clone
      call message arguments foreach(arg,
        r doMessage(arg))
      r
    )
    Map atPutNumber := method(
      self atPut(
        call evalArgAt(0) asMutable removePrefix("\"") removeSuffix("\""),
        call evalArgAt(1))
    )

Io also serves the concurrency niche. Prefixing a method with `@@` will initiate it in its own
thread (asynchronous methods).

# Prolog

> You'll get astounding answers only if you know how to ask the questions.
> Think Rain Man.

Whereas Ruby and Io are imperative languages, Prolog is a declarative one. Imperative languages are
recipes where you throw together ingredients and describe a step-by-step process. Declarative
languages lets you throw facts and references, the language will figure things out on its own.

The building blocks of Prolog:

* **Facts** are assertions about the world
* **Rules** are inferences about facts
* **Query** is a question about the world

Facts/rules go into a **knowledge base** efficient for queries. If a word begins with a lowercase,
it's an **atom** (like a Ruby symbol). A **variable** starts with an uppercase or underscore. Let's
start with this knowledge base. The first three lines are facts, the last statement is a rule.

    likes(wallace, cheese).
    likes(grommit, cheese).
    likes(wendolene, sheep).

    friend(X, Y) :- \+(X = Y), likes(X, Z), likes(Y, Z).

Put this into a `friends.pl` file. Load it uses `gprolog` and enter `['friends']`. Now ask questions
in the REPL `likes(wallace, sheep).` or `likes(grommit, cheese).`. Things get more interesting with:

    | ?- friend(wallace, wallace).
    | ?- friend(grommit, wallace).

In our rule earlier, `\+` is a logical negation so we make sure `X != Y`. Another example the author
lists out facts about food types and their flavors:

    food_type(..name.., ..category..).
    flavor(..flavor.., ..category..).
    food_flavor(X, Y) :- food_type(X, Z), flavor(Y, Z).

Now you can ask questions like:

    food_type(What, meat).
    What = spam ? ;
    What = sauage ? ;
    no

The `What` keyword meant we asked Prolog to find some food that were meat. It can infer which are
sweet also:

    flavor(sweet, What).

Prolog's equivalent of variable assignment is called **unification** which makes two structures
identical.

    cat(lion).
    cat(tiger).

    dorothy(X, Y, Z) :- X = lion, Y = tiger, Z = bear.
    twin_cats(X, Y) :- cat(X), cat(Y).

`=` means unify to make both sides the same. It's similar to `==` also.

    | ?- dorothy(lion, tiger, bear).
    yes
    | ?- dorothy(One, Two, Three).
    One = lion
    Three = bear
    Two = tiger
    yes

Lists have variable lengths and tuples have fixed lengths. A list is specified like `[1, 2, 3]` and
a tuple like `(1, 2, 3)`. You can construct lists in several ways:

    (A, B, C) = (1, 2, 3).
    [1, 2, 3] = [X, Y, Z].
    [a, b, c] = [Head|Tail]

The last binds `Head` to `a` and `Tail` to `[b,c]`. The special identifier `_` is a wildcard that
will bind with anything.

# Scala

Scala is a hybrid of OOP and functional paradigms. It's built on top of JVM. Tate points out mutable
state from OOP is a huge problem for concurrency. Scala doesn't eliminate mutable state completely,
but gives you the option to.

Everything is an object:

    scala> println("Hello, surreal world")
    scala> 1 + 1
    scala> (1).+(1)
    scala> "abc" + 4
    scala> 4 * "abc"
    ... error ...

It uses type inference most of the time but is actually strongly typed at compile time.

Values are assigned like `val a = 1`. Variables are assigned like `var b = 2`. Values are immutable
whereas variables are mutable.

`Nil` is Scala's null and is just an empty list. Nils and numbers are not booleans so the compiler
will complain if you use them for if statements.

Functions are defined like:

    def functionname {
      /* function body */
    }

Scala supports ranges and tuples. `val range = 0 until 10` is a range. You can also do `(0 to 10) by
5`. Tuples use parentheses `("Elvis", "Presley")`. Classes look like:

    class Person(firstName: String, lastName: String)
    class Compass {
      val directions = List("north", "east", "south", "west")
      def direction() = directions(bearing)
      def inform(turnDirection: String) {
        print("Turning " + turnDirection + ". Now bearing " + direction)
      }
    }
    class Employee(override val first: String,
                            val last: String,
                            val number: Int) extends Person(first, last) {
      /* ... */
    }

You can see the flexibility in the syntax above. Many portions are optional.

    val myCompass = new Compass
    myCompass.inform("right")
    myCompass.direction

Constructors are implemented with the special method `this` and you can have multiple constructors
with varying arguments like Java.

Singletons are created using the `object` keyword:

    object TrueRing {
      def rule = println("To rule them all")
    }
    TrueRing.rule

Scala has **traits** which are similar to Ruby's modules:

    trait Nice {
      def greet() = println("Howdily doodily.")
    }
    class Character(override val name:String) extends Person(name) with Nice
    val flanders = new Character("Ned")
    flanders.greet

Scala can infer the return type but you can also specify it:

    def double(x:Int):Int = x * 2

Lists are created like `List(1, 2, 3)`. If you mix data types Scala will use the lowest common
denominator **Any**. Use `()` instead of `[]` to access items in the list. You can also create a
`Set` which has no order. Maps are created like:

    Map(0 -> "zero", 1 -> "one", 2 -> "two")
    val map = new HashMap[Int, String]
    map += 4 -> "four"
    map += 8 -> "eight"
    map(4)

Lists implement the `foreach` method which takes a code block as its argument:

    list.foreach(hobbit => println(hobbit))

Scala implements pattern matching which conditionally executes code based on pieces of data. The
simplest form is match/case like switch/case:

    chore match {
      case "clean dishes" => "scrub, dry"
      case "cook dinner" => "chop, sizzle"
      case _ => "whine, complain"
    }

    n match {
      case 0 => 1
      case x if x > 0 => factorial(n - 1) * n /* notice the guard */
    }

Scala uses actors and message passing for concurrency. Actors have pools of threads/queues. You send
a message to an actor to place an object on its queue.

    import scala.actors._
    import scala.actors.Actor._

    case object Poke
    case object Feed

    class Kid() extends Actor {
      def act() {
        loop {
          react {
            case Poke => {
              println("Ow, quit it...")
            }
            case Feed => {
              println("Gurgle, burp...")
            }
          }
        }
      }
    }

    val bart = new Kid().start
    val lisa = new Kid().start
    bart ! Poke
    lisa ! Poke
    bart ! Feed
    lisa ! Feed

Wrapping up, Scala supports OOP/functional paradigms and employs static/strong typing. Its core
strengths are concurrency, strong libraries from Java, DSLs, and bridges.

# Erlang

> Few languages have the mystique of Erlang, the concurrency language that
> makes hard things easy and easy things hard.

Erlang's virtual machine is called **BEAM** which is efficient but lacks simple syntax. Erlang
stands for Ericsson Language but also shares its name with Agner Karup Erlang, a mathematician
behind telephone network analysis.

Erlang was built for concurrency and is very stable. There are no threads, instead it uses
lightweight processes. The implementation is different than Scala, but it still uses the actor
model.

It's entirely functional. Get started with the REPL via `erl`:

    1> % This is a comment
    1> 2 + 2.
    2> 2 + 2.0.  % 4.0, there's some coercion
    3> "string".
    4> [1, 2, 3]. % lists are heterogeneous
    5> [72, 97, 32, 72, 97, 32, 72, 97].  % "Ha Ha Ha"
    6> {one, two, three}  % tuples are fixed-length lists

**Atoms** start with lowercase. Variables start with an uppercase:

    Var = 1.

Variables are also immutable, you can't reassign `Var`.

Erlang's pattern matching is similar to Prolog's:

    1> [Head | Tail] = [1, 2, 3].
    2> Head.
    1
    3> Tail.
    [2, 3]

You can even do this at the bit level using `<<` and `>>`:

    <<A:3, B:3, C:5, D:5>> = All.

Erlang is dynamically typed. Let's make some functions in the file `basic.erl`:

    -module(basic).
    -export([mirror/1]).  % export function mirror, /1 means 1 parameter

    mirror(Anything) -> Anything.

Now run the REPL, to execute your module:

    c(basic).
    basic:mirror(smiling_mug).

Pattern matching works on function arguments also:

    number(one)   -> 1;
    number(two)   -> 2;
    number(three) -> 3.

This will work with atoms one, two, and three. It will error on four.

    fact(0) -> 1;
    fact(N) -> N * fact(N - 1).

    fib(0) -> 1;
    fib(1) -> 1;
    fib(N) -> fib(N - 1) + fib(N - 2);

Here's some control structures for handling branches:

    Animal = "dog".
    case Animal of
      "dog" -> underdog;
      "cat" => thundercat;
      _ -> something_else
    end.

    if
      ProgramsTerminated > 0 ->
        success;
      ProgramsTerminated < 0 ->
        error;
      true -> confused
    end.

There's anonymous functions:

    Negate = fun(I) -> -I end.

Concurrency works with these primitives:

* `!` for sending a message
* `spawn` to spawn processes
* `receive` to receive messages

    -module(translate).
    -export([loop/0]).

    loop() ->
      receive
        "casa" ->
          io:format("house~n"),
          loop();
        "blanca" ->
          io:format("white~n"),
          loop();
        _ ->
          io:format("I Don't understand.~n"),
          loop();
      end.

Let's spawn them:

    1> c(translate).
    2> Pid = spawn(fun translate:loop/0).  % fun for function

Erlang has built in support for spawning remote functions also. In this case, we get a process ID
back which you can view on your OS.

    3> Pid ! "casa".
    "house"
    "casa"
    4> Pid ! "blanca".
    "white"
    "blanca"
    5> Pid ! "loco".
    "I don't understand."
    "loco"

For remote services, you'd spawn and send with:

    spawn(Node, function)
    node@server ! message

Erlang has support for linking processes. This increases reliability. When one process dies, it will
send an exit signal to its linked twin.

    -module(coroner).
    -export([loop/0]).

    loop() ->
      process_flag(trap_exit, true),
      receive
        {monitor, Process} ->
          link(Process),
          io:format("Monitoring process.~n"),
          loop();
        {'EXIT', From, Reason} ->
          io:format("The shooter ~p died with reason ~p.", [From, Reason]),
          io:format("start another one.~n),
          loop()
      end.

Erlang's strengths are its concurrency and fault tolerance. It has a lightweight share-nothing
model. OTP has many libraries for building enterprise systems.

# Clojure

Clojure is a Lisp dialect on the JVM. Lisp is a language of lists and uses its own data structures
to express code (called "data as code"). This is ideal for metaprogramming.

The primary dialects of Lisp are Common Lisp and Scheme. Scheme/Clojure belong to the family of
lisp-1 where functions/variables occupy the same namespace. Common Lisp comes from lisp-2, where
functions/variables reside different namespaces.

Tate uses the `leiningen` tool to manage Clojure/Java configurations.

    $ lein new seven-languages
    $ cd seven-languages
    $ lein repl
    user=> (println "Give me some Clojure!")
    Give me some Clojure!
    nil
    user=> (* 10 10)
    100
    user => (= 1 1.0)
    true
    user => (< 1 2)
    true
    user => (class true)
    java.lang.Boolean
    user => (if (> 1 2)
      (println "True it is.")
      (println "It is false."))
    It is false.
    nil

`0` and `''` are true but `nil` is false.

Some common containers are lists, vectors, sets, and maps. In Clojure, lists are used for code while
vectors are used for data:

    (list 1 2 3)
    '(1 2 3)

    [:hutt :wookie :ewok]
    ([:hutt :wookie :ewok] 2)  ; :ewok

    #{:x-wing :y-wing :tie-fighter} ; sets

    {:chewie :wookie :lea :human} ; maps
    (def mentors {:darth-vader "obi wan", :luke "yoda"})
    (mentors :luke) ; "yoda"

Functions are defined using `defn`:

    (defn optional-doc-string [params] body)
    (defn force-it [] (str "Use the force," "Luke."))

Variable assignment is called **binding** and works via the `def` keyword.

    (def line [[0 0] [10 20]])

Functions are just data and can be passed around as arguments.

    user=> (def people ["Lea", "Han Solo"])
    user=> (count "Lea")
    3
    user=> (map count people)
    (3 8)

Some other useful functions which take functions as arguments:

* `apply` applies a function to argument list
* `filter` filters a list for a condition

Here's an example of recursion to evaluate the size of a vector:

    (defn size [v]
      (if (empty? v)
           0
           (inc (size (rest v)))))

This will grow the stack until all memory is exhausted. Tail recursion optimization gets around this
but must be explicit in Clojure by using `loop` or `recur`.

    (loop [x x-initial-value, y y-initial-value] (do-something-with x y))

Most languages execute parameters first and then puts it on the call stack. Macros get around this
problem. Tate implements `unless` so `(unless test body)` translates to `(if (not test) body)`.

Clojure executes in two stages: macro expansion then running. Some macros you've already used are
`;` and `'`.

    (defmacro unless [test body]
      (list 'if (list 'not test) body))

The substitutions occur without executing them.

Clojure uses STM (software transactional memory) to deal with concurrency. This uses multiple
versions of data to maintain consistency and integrity. Changing state must be done within scope of
a transaction.

    user=> (def movie (ref "Star Wars"))
    user=> movie
    #<Ref@...: "Star Wars">
    user=> (deref movie)
    "Star Wars"
    user=> @movie
    "Star Wars"
    user=> (alter movie str ": The Empire Strikes Back")
    IllegalStateException: No transaction running
    user=> (dosync (alter movie str": The Empire Strikes Back"))
    "Star Wars: The Empire Strikes Back"

Use `ref-set` instead of `alter` to change the initial value. Use atoms for thread safety of a
single reference.

Clojure's core strengths are that it is a Lisp, it's on the JVM, and it has a good concurrency
approach.

# Haskell

Haskell is a pure functional language with powerful features. The most popular compiler is probably
GHC or Glasgow Haskell Compiler. Use the REPL with `ghci`.

    > 4
    > 4 * 5 + 1
    > "hello"
    > "hello" ++ "world"
    > ['a', 'b']
    > (4 + 5) == 9
    > (5 + 5) /= 10

Haskell has significant whitespace.

    > if (5 == 5) then "true" else "false"

It's strongly typed, so only boolean expressions are allowed for if tests. Binding works with the
`let` keyword. This binds variables and functions.

    > let x = 10
    > let double x = x * 2
    > double 2
    4

Put this into `double.hs`:

    module Main where
        
        double x = x + x

Now load it with `ghci` via `:load double.hs`. Haskell does a good job of inferring types, but you
can do it explicitly:

    double :: Integer -> Integer
    double x = x + x

Use `:t` to query about types as in `:t double`. As with other languages, you can use pattern
matching to implement factorials:

    factorial :: Integer -> Integer
    factorial 0 = 1
    factorial x = x * factorial (x - 1)

Guards use `|`:

    factorial x
      | x > 1 = x * factorial (x - 1)
      | otherwise = 1

Let's play with lists:

    let (h:t) = [1, 2, 3, 4]
    > h
    1
    > t
    [2, 3, 4]

Some pattern matching functions for lists:

    module Main where
      size [] = 0
      size (h:t) = 1 + size t

      prod [] = 1
      prod (h:t) = h * prod t

The `:` operator is used heavily for list construction/deconstruction:

    > 1:[2, 3]
    [1,2,3]

Lists are homogeneous. Haskell supports ranges `[1..4]`. It also supports list comprehension:

    > [x * 2 | x <- [1, 2, 3], x /= 4]
    [2, 4, 6]

Anonymous functions have the form `(\param1 .. paramn -> function_body).`

    > (\x -> x ++ " captain.") "Logical ,"
    "Logical, captain."
    > map (\x -> x * x) [1, 2, 3]
    [1, 4, 9]

Haskell uses lazy evaluation.

Its strongest feature is the type system. It's static but uses inference so the programmer doesn't
have to work hard. Define your own type with `data`:

    data Boolean = True | False
    data Suit = Spades | Hearts
    data Rank = Ten | Jack | Queen | King | Ace

Haskell will have a tough time showing these values, use `deriving (Show)` to remedy it:

    data Suit = Spades | Hearts deriving (Show)
    type Card = (Rank, Suit)

**Monads** lets use compose functions with specific properties. It lets you deal with the no state
aspect of pure functional languages by simulating state.

Monads are made up of a type constructor, return function, and bind function.

    module Main where
      data Position t = Position t deriving (Show)

      stagger (Position d) = Poosition (d + 2)
      crawl (Position d) = Position (d + 1)

      rtn x = x
      x >>== f = f x

Now a pirate hunting for treasure looks like this:

    treasureMap pos = pos >>==
                      stagger >>==
                      stagger >>==
                      crawl >>==
                      rtn