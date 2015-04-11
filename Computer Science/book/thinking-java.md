### 1. Java中的多态性理解（注意与C++区分）
 - **Java中除了static方法和final方法（private方法本质上属于final方法，因为不能被子类访问）之外，其它所有的方法都是动态绑定**，这意味着通常情况下，我们不必判定是否应该进行动态绑定—它会自动发生。
     - final方法会使编译器生成更有效的代码，这也是为什么说声明为final方法能在一定程度上提高性能（效果不明显）。
     - 如果某个方法是静态的，它的行为就不具有多态性：
    ```java
    class StaticSuper {
    	public static String staticGet() {
    		return "Base staticGet()";
    	}
    	
    	public String dynamicGet() {
    		return "Base dynamicGet()";
    	}
    }
    
    class StaticSub extends StaticSuper {
    	public static String staticGet() {
    		return "Derived staticGet()";
    	}
    	
    	public String dynamicGet() {
    		return "Derived dynamicGet()";
    	}
    }
    
    public class StaticPolymorphism {
    	
    	public static void main(String[] args) {
    		StaticSuper sup = new StaticSub();
    		System.out.println(sup.staticGet());
    		System.out.println(sup.dynamicGet());
    	}
    
    }
    ```
         输出：
>Base staticGet()
Derived dynamicGet()

 - **构造函数并不具有多态性，它们实际上是static方法，只不过该static声明是隐式的。**因此，构造函数不能够被override。

 - **在父类构造函数内部调用具有多态行为的函数将导致无法预测的结果**，因为此时子类对象还没初始化，此时调用子类方法不会得到我们想要的结果。
    ```java
    class Glyph {
    	void draw() {
    		System.out.println("Glyph.draw()");
    	}
    	Glyph() {
    		System.out.println("Glyph() before draw()");
    		draw();
    		System.out.println("Glyph() after draw()");
    	}
    }
    
    class RoundGlyph extends Glyph {
    	private int radius = 1;
    	
    	RoundGlyph(int r) {
    		radius = r;
    		System.out.println("RoundGlyph.RoundGlyph(). radius = " + radius);
    	}
    	
    	void draw() {
    		System.out.println("RoundGlyph.draw(). radius = " + radius);
    	}
    }
    
    public class PolyConstructors {
    
    	public static void main(String[] args) {
    		new RoundGlyph(5);
    
    	}
    
    }
    ```
输出：
>Glyph() before draw()
RoundGlyph.draw(). radius = 0
Glyph() after draw()
RoundGlyph.RoundGlyph(). radius = 5

 为什么会这样输出？这就要明确掌握**Java中构造函数的调用顺序**：
>（1）在其他任何事物发生之前，将分配给对象的存储空间初始化成二进制0；
（2）调用基类构造函数。从根开始递归下去，因为多态性此时调用子类覆盖后的draw()方法（要在调用RoundGlyph构造函数之前调用），由于步骤1的缘故，我们此时会发现radius的值为0；
（3）按声明顺序调用成员的初始化方法；
（4）最后调用子类的构造函数。

 - 只有非private方法才可以被覆盖，但是还需要密切注意覆盖private方法的现象，这时虽然编译器不会报错，但是也不会按照我们所期望的来执行，即覆盖private方法对子类来说是一个新的方法而非重载方法。因此，**在子类中，新方法名最好不要与基类的private方法采取同一名字（虽然没关系，但容易误解，以为能够覆盖基类的private方法）**。

 - Java类中属性域的访问操作都由编译器解析，因此不是多态的。**父类和子类的同名属性都会分配不同的存储空间**，如下：
    ```java
    // Direct field access is determined at compile time.
    class Super {
    	public int field = 0;
    	public int getField() {
    		return field;
    	}
    }
    
    class Sub extends Super {
    	public int field = 1;
    	public int getField() {
    		return field;
    	}
    	public int getSuperField() {
    		return super.field;
    	}
    }
    
    public class FieldAccess {
    
    	public static void main(String[] args) {
    		Super sup = new Sub();
    		System.out.println("sup.filed = " + sup.field + 
    				", sup.getField() = " + sup.getField());
    		Sub sub = new Sub();
    		System.out.println("sub.filed = " + sub.field + 
    				", sub.getField() = " + sub.getField() + 
    				", sub.getSuperField() = " + sub.getSuperField());
    	}
    
    }
    ```
     输出：
>sup.filed = 0, sup.getField() = 1
sub.filed = 1, sub.getField() = 1, sub.getSuperField() = 0

     Sub子类实际上**包含了两个称为field的域**，然而在引用Sub中的field时所产生的默认域并非Super版本的field域，因此为了得到Super.field，必须**显式地指明**super.field。

### 2. is-a关系和is-like-a关系
- is-a关系属于纯继承，即只有在基类中已经建立的方法才可以在子类中被覆盖，如下图所示：
![is-a.png](http://upload-images.jianshu.io/upload_images/46178-5fbaec520e33a8d3.png)
基类和子类有着完全相同的接口，**这样向上转型时永远不需要知道正在处理的对象的确切类型，这通过多态来实现。**

- is-like-a关系：子类扩展了基类接口。它有着相同的基本接口，**但是他还具有由额外方法实现的其他特性。**
![has-a.png](http://upload-images.jianshu.io/upload_images/46178-335a5bca78e970b4.png)
缺点就是子类中接口的扩展部分不能被基类访问，因此**一旦向上转型，就不能调用那些新方法。**

### 3. 运行时类型信息（RTTI + 反射）
 - 概念
RTTI：运行时类型信息使得你可以在程序运行时发现和使用类型信息。
 - 使用方式
Java是如何让我们在运行时识别对象和类的信息的，主要有两种方式（还有辅助的第三种方式，见下描述）：
     - 一种是“传统的”RTTI，它假定我们在编译时已经知道了所有的类型，比如`Shape s = (Shape)s1；`
     - 另一种是**“反射”机制**，它运行我们在运行时发现和使用类的信息，即使用`Class.forName()`。
     - 其实还有第三种形式，就是关键字`instanceof`，它返回一个bool值，它保持了类型的概念，它指的是**“你是这个类吗？或者你是这个类的派生类吗？”**。而如果用==或equals比较实际的Class对象，就没有考虑继承—它或者是这个确切的类型，或者不是。

 - 工作原理
要理解RTTI在Java中的工作原理，**首先必须知道类型信息在运行时是如何表示的**，这项工作是由称为`Class对象`的特殊对象完成的，它包含了与类有关的信息。Java送Class对象来执行其RTTI，**使用类加载器的子系统实现**。

 无论何时，只要你想在运行时使用类型信息，就**必须首先获得对恰当的Class对象的引用**，获取方式有三种：
 （1）如果你没有持有该类型的对象，则`Class.forName()`就是实现此功能的便捷途，因为它不需要对象信息；
 （2）如果你已经拥有了一个感兴趣的类型的对象，那就可以通过调用`getClass()`方法来获取Class引用了，它将返回表示该对象的实际类型的Class引用。Class包含很有有用的方法，比如：
    ```java
    package rtti;
    interface HasBatteries{}
    interface WaterProof{}
    interface Shoots{}
    
    class Toy {
    	Toy() {}
    	Toy(int i) {}
    }
    
    class FancyToy extends Toy
    implements HasBatteries, WaterProof, Shoots {
    	FancyToy() {
    		super(1);
    	}
    }
    
    public class RTTITest {
    	
    	static void printInfo(Class cc) {
    		System.out.println("Class name: " + cc.getName() + 
    				", is interface? [" + cc.isInterface() + "]");
    		System.out.println("Simple name: " + cc.getSimpleName());
    		System.out.println("Canonical name: " + cc.getCanonicalName());
    	}
    	
    	public static void main(String[] args) {
    		Class c = null;
    		try {
    			c = Class.forName("rtti.FancyToy"); // 必须是全限定名（包名+类名）
    		} catch(ClassNotFoundException e) {
    			System.out.println("Can't find FancyToy");
    			System.exit(1);
    		}
    		printInfo(c);
    		
    		for(Class face : c.getInterfaces()) {
    			printInfo(face);
    		}
    		
    		Class up = c.getSuperclass();
    		Object obj = null;
    		try {
    			// Requires default constructor.
    			obj = up.newInstance();
    		} catch (InstantiationException e) {
    			System.out.println("Can't Instantiate");
    			System.exit(1);
    		} catch (IllegalAccessException e) {
    			System.out.println("Can't access");
    			System.exit(1);
    		}
    		printInfo(obj.getClass());
    	}
    
    }
    ```
输出：
>Class name: rtti.FancyToy, is interface? [false]
Simple name: FancyToy
Canonical name: rtti.FancyToy
Class name: rtti.HasBatteries, is interface? [true]
Simple name: HasBatteries
Canonical name: rtti.HasBatteries
Class name: rtti.WaterProof, is interface? [true]
Simple name: WaterProof
Canonical name: rtti.WaterProof
Class name: rtti.Shoots, is interface? [true]
Simple name: Shoots
Canonical name: rtti.Shoots
Class name: rtti.Toy, is interface? [false]
Simple name: Toy
Canonical name: rtti.Toy

 （3）Java还提供了另一种方法来生成对Class对象的引用，即使用**类字面常量**。比如上面的就像这样：`FancyToy.class;`来引用。
这样做不仅更简单，而且更安全，因为它**在编译时就会受到检查（因此不需要置于try语句块中）**，并且它根除了对forName方法的引用，所以也更高效。类字面常量不仅可以应用于普通的类，也可以应用于接口、数组以及基本数据类型。
 ---
 **注意**：当使用“.class”来创建对Class对象的引用时，**不会自动地初始化该Class对象，初始化被延迟到了对静态方法（构造器隐式的是静态的）或者非final静态域（注意final静态域不会触发初始化操作）进行首次引用时才执行：**。而使用Class.forName时会自动的初始化。

 为了使用类而做的准备工作实际包含三个步骤：
- 加载：由类加载器执行。查找字节码，并从这些字节码中创建一个Class对象
- 链接：验证类中的字节码，为静态域分配存储空间，并且如果必需的话，将解析这个类创建的对其他类的所有引用。
- 初始化：如果该类具有超类，则对其初始化，执行静态初始化器和静态初始化块。

 这一点非常重要，下面通过一个实例来说明这两者的区别：
```java
package rtti;
import java.util.Random;
class Initable {
    	static final int staticFinal = 47;
    	static final int staticFinal2 = ClassInitialization.rand.nextInt(1000);
	
    	static {
    		System.out.println("Initializing Initable");
    	}
}
class Initable2 {
    	static int staticNonFinal = 147;
    	
    	static {
    		System.out.println("Initializing Initable2");
    	}
}
class Initable3 {
    	static int staticNonFinal = 74;
    	
    	static {
    		System.out.println("Initializing Initable3");
    	}
}
public class ClassInitialization {

    	public static Random rand = new Random(47);
    	
    	public static void main(String[] args) {
    		// Does not trigger initialization
    		Class initable = Initable.class;
    		System.out.println("After creating Initable ref");
    		// Does not trigger initialization
    		System.out.println(Initable.staticFinal);
    		// Does trigger initialization(rand() is static method)
    		System.out.println(Initable.staticFinal2);
    		
    		// Does trigger initialization(not final)
    		System.out.println(Initable2.staticNonFinal);
    		
    		try {
    			Class initable3 = Class.forName("rtti.Initable3");
    		} catch (ClassNotFoundException e) {
    			System.out.println("Can't find Initable3");
    			System.exit(1);
    		}
    		System.out.println("After creating Initable3 ref");
    		System.out.println(Initable3.staticNonFinal);
    	}
}
 ```
 输出：
>After creating Initable ref
47
Initializing Initable
258
Initializing Initable2
147
Initializing Initable3
After creating Initable3 ref
74
 ---

 - RTTI的限制？如何突破？ — 反射机制
如果不知道某个对象的确切类型，RTTI可以告诉你，但是有一个**限制：这个类型在编译时必须已知，这样才能使用RTTI识别它，也就是在编译时，编译器必须知道所有要通过RTTI来处理的类。**

   可以突破这个限制吗？是的，突破它的就是**反射机制**。
  `Class`类与`java.lang.reflect`类库一起对反射的概念进行了支持，该类库包含了`Field`、`Method`以及`Constructor`类（每个类都实现了`Member`接口）。这些类型的对象是由JVM在运行时创建的，用以表示未知类里对应的成员。这样你就可以使用`Constructor`创建新的对象，用`get()/set()`方法读取和修改与`Field`对象关联的字段，用`invoke()`方法调用与`Method`对象关联的方法。另外，还可以调用`getFields()、getMethods()和getConstructors()`等很便利的方法，以返回表示字段、方法以及构造器的对象的数组。这样，**匿名对象的类信息就能在运行时被完全确定下来，而在编译时不需要知道任何事情。**
 
  ---
 ####反射与RTTI的区别
 当通过反射与一个未知类型的对象打交道时，JVM只是简单地检查这个对象，看它属于哪个特定的类（就像RTTI那样），在用它做其他事情之前必须先加载那个类的`Class`对象，因此，那个类的`.class`文件对于JVM来说必须是可获取的：要么在本地机器上，要么可以通过网络取得。所以**RTTI与反射之间真正的区别只在于：对RTTI来说，编译器在编译时打开和检查.class文件（也就是可以用普通方法调用对象的所有方法）；而对于反射机制来说，.class文件在编译时是不可获取的，所以是在运行时打开和检查.class文件。**

 下面的例子是用反射机制打印出一个类的所有方法（包括在基类中定义的方法）：

    ```java
    package typeinfo;
    
    import java.lang.reflect.Constructor;
    import java.lang.reflect.Method;
    import java.util.regex.Pattern;
    
    // Using reflection to show all the methods of a class.
    // even if the methods are defined in the base class.
    public class ShowMethods {
    	private static String usage = 
    		"usage: \n" + 
    	    "ShowMethods qualified.class.name\n" +
    	    "To show all methods in class or: \n" +
    	    "ShowMethods qualified.class.name word\n" +
    	    "To search for methods involving 'word'";
    	
    	private static Pattern p = Pattern.compile("\\w+\\.");
    
    	public static void main(String[] args) {
    		if(args.length < 1) {
    			System.out.println(usage);
    			System.exit(0);
    		}
    		int lines = 0;
    		try {
    			Class<?> c = Class.forName(args[0]);
    			Method[] methods = c.getMethods();
    			Constructor[] ctors = c.getConstructors();
    			if(args.length == 1) {
    				for(Method method : methods) {
    					System.out.println(p.matcher(method.toString()).replaceAll(""));
    				}
    				for(Constructor ctor : ctors) {
    					System.out.println(p.matcher(ctor.toString()).replaceAll(""));
    				}
    				lines = methods.length + ctors.length;
    			} else {
    				for(Method method : methods) {
    					if(method.toString().indexOf(args[1]) != -1) {
    						System.out.println(p.matcher(method.toString()).replaceAll(""));
    						lines++;
    					}
    				}
    				for(Constructor ctor : ctors) {
    					if(ctor.toString().indexOf(args[1]) != -1) {
    						System.out.println(p.matcher(ctor.toString()).replaceAll(""));
    						lines++;
    					}
    				}
    			}
    		} catch (ClassNotFoundException e) {
    			System.out.println("No such Class: " + e);
    		}
    
    	}
    }
    ```

 输出：
>public static void main(String[])
public final native void wait(long) throws InterruptedException
public final void wait() throws InterruptedException
public final void wait(long,int) throws InterruptedException
public boolean equals(Object)
public String toString()
public native int hashCode()
public final native Class getClass()
public final native void notify()
public final native void notifyAll()
public ShowMethods()

### 4. 代理模式与Java中的动态代理
- 代理模式
在任何时刻，只要你想要将额外的操作从“实际”对象中分离到不同的地方，特别是当你希望能够很容易地做出修改，从没有使用额外操作转为使用这些操作，或者反过来时，代理就显得很有用（设计模式的关键是封装修改）。例如，如果你希望跟踪对某个类中方法的调用，或者希望度量这些调用的开销，那么你应该怎样做呢？这些代码**肯定是你不希望将其合并到应用中的代码，因此代理使得你可以很容易地添加或移除它们。**
    ```java
    interface Interface {
    	void doSomething();
    	void somethingElse(String arg);
    }
    
    class RealObject implements Interface {
    
    	@Override
    	public void doSomething() {
    		System.out.println("doSomething.");
    	}
    
    	@Override
    	public void somethingElse(String arg) {
    		System.out.println("somethingElse " + arg);
    	}
    }
    
    class SimpleProxy implements Interface {
    	
    	private Interface proxy;
    	
    	public SimpleProxy(Interface proxy) {
    		this.proxy = proxy;
    	}
    
    	@Override
    	public void doSomething() {
    		System.out.println("SimpleProxy doSomething.");
    		proxy.doSomething();
    	}
    
    	@Override
    	public void somethingElse(String arg) {
    		System.out.println("SimpleProxy somethingElse " + arg);
    		proxy.somethingElse(arg);
    	}
    }
    
    public class SimpleProxyDemo {
    	
    	public static void consumer(Interface iface) {
    		iface.doSomething();
    		iface.somethingElse("bonobo");
    	}
    
    	public static void main(String[] args) {
    		consumer(new RealObject());
    		consumer(new SimpleProxy(new RealObject()));
    	}
    
    }
    ```
输出：
> doSomething.
somethingElse bonobo
SimpleProxy doSomething.
doSomething.
SimpleProxy somethingElse bonobo
somethingElse bonobo

- 动态代理
Java的动态代理比代理的思想更向前迈进了一步，因为它可以**动态地创建代理并动态地处理对所代理方法的调用。**
    ```java
    import java.lang.reflect.InvocationHandler;
    import java.lang.reflect.Method;
    import java.lang.reflect.Proxy;
    
    class DynamicProxyHandler implements InvocationHandler {
    	
    	private Object proxy;
    	
    	public DynamicProxyHandler(Object proxy) {
    		this.proxy = proxy;
    	}
    	
    	@Override
    	public Object invoke(Object proxy, Method method, Object[] args)
    			throws Throwable {
    		System.out.println("*** proxy: " + proxy.getClass() +
    				". method: " + method + ". args: " + args);
    		if(args != null) {
    			for(Object arg : args)
    				System.out.println(" " + arg);
    		}
    		return method.invoke(this.proxy, args);
    	}
    }
    
    public class SimpleDynamicProxy {
    	
    	public static void consumer(Interface iface) {
    		iface.doSomething();
    		iface.somethingElse("bonobo");
    	}
    
    	public static void main(String[] args) {
    		RealObject real = new RealObject();
    		consumer(real);
    		// insert a proxy and call again:
    		Interface proxy = (Interface)Proxy.newProxyInstance(
    				Interface.class.getClassLoader(), 
    				new Class[]{ Interface.class },
    				new DynamicProxyHandler(real));
    		
    		consumer(proxy);
    	}
    
    }
    ```
输出：
> doSomething.
somethingElse bonobo
\*\*\* proxy: class typeinfo.\$Proxy0. method: public abstract void typeinfo.Interface.doSomething(). args: null
doSomething.
\*\*\* proxy: class typeinfo.\$Proxy0. method: public abstract void typeinfo.Interface.somethingElse(java.lang.String). args: [Ljava.lang.Object;@6a8814e9
 bonobo
somethingElse bonobo

### 5. 即时编译器技术 — JIT
Java虚拟机中有许多附加技术用以提升速度，尤其是与加载器操作相关的，被称为“即时”（Just-In-Time，JIT）编译器的技术。**这种技术可以把程序全部或部分翻译成本地机器码（这本来是JVM的工作），程序运行速度因此得以提升。**当需要装载某个类时，编译器会先找到其.class文件，然后将该类的字节码装入内存。此时，有两种方案可供选择：
（1）一种就是让即时编译器编译所有代码。但这种做法有两个缺陷：这种加载动作散落在整个程序生命周期内，累加起来要花更多时间；并且会增加可执行代码的长度（字节码要比即时编译器展开后的本地机器码小很多），这将导致页面调度，从而降低程序速度。
（2）另一种做法称为惰性评估（lazy evaluation），意思是即时编译器只在必要的时候才编译代码，这样，从不会被执行的代码也许就压根不会被JIT所编译。**新版JDK中的Java HotSpot技术就采用了类似方法**，代码每次被执行的时候都会做一些优化，所以执行的次数越多，它的速度就越快。

### 6. 访问控制权限
- Java访问权限修饰词：**public、protected、包访问权限（默认访问权限，有时也称friendly）和private。**
- 包访问权限：当前包中的所有其他类对那个成员具有访问权限，但对于这个包之外的所有类，这个成员却是private。
- protected：继承访问权限。有时基类的创建者会希望有某个特定成员，把对它的访问权限赋予派生类而不是所有类。这就需要protected来完成这一工作。protected也提供包访问权限，也就是说，相同包内的其他类都可以访问protected元素。protected指明**“就类用户而言，这是private的，但对于任何继承于此类的导出类或其他任何位于同一个包内的类来说，它却是可以访问的”**。比如：
基类：
    ```java
    package access.cookie;
    public class Cookie {
        public Cookie() {
            System.out.println("Cookie Constructor");
        }
     
        void bite() {  // 包访问权限，其它包即使是子类也不能访问它
            System.out.println("bite");
        }
    }
    ```
子类：
    ```java
    package access.dessert;
    import access.cookie.Cookie;

    public class ChocolateChip extends Cookie {

    	public ChocolateChip() {
    		System.out.println("ChocolateChip constructor");
    	}
    	
    	public void chomp() {
    		bite();  // error, the method bite() from the type Cookie is not visible
    	}
    }
    ```
可以发现子类并不能访问基类的包访问权限方法。此时可以将Cookie中的bite指定为public，但**这样做所有的人就都有了访问权限，为了只允许子类访问，可以将bite指定为protected即可。**

### 7. 组合和继承之间的选择
- 组合和继承**都允许在新的类中放置子对象**，组合是显式的这样做，而继承则是隐式的做。
- **组合技术通常用于想在新类中使用现有类的功能而非它的接口这种情形**。即在新类中嵌入某个对象，让其实现所需要的功能，但新类的用户看到的只是为新类所定义的接口，而非所嵌入对象的接口。为取得此效果，需要在新类中嵌入一个现有类的private对象。但**有时，允许类的用户直接访问新类中的组合成分是极具意义的，即将成员对象声明为public**。如果成员对象自身都隐藏了具体实现，那么这种做法是安全的。当用户能够了解到你正在组装一组部件时，会使得端口更加易于理解。比如Car对象可由public的Engine对象、Wheel对象、Window对象和Door对象组合。但务必要记得这仅仅是一个特例，**一般情况下应该使域成为private**。
- 在继承的时候，使用某个现有类，并开发一个它的特殊版本。通常，**这意味着你在使用一个通用类，并为了某种特殊需要而将其特殊化。**稍微思考一下就会发现，用一个“交通工具”对象来构成一部“车子”是毫无意义的，因为“车子”并不包含“交通工具”，它仅是一种交通工具（is-a关系）。
- **“is-a”（是一个）的关系是用继承来表达的，而“has-a”（有一个）的关系则是用组合来表达的**。
- 到底是该用组合还是继承，一个最清晰的判断方法就是问一问自己是否需要从新类向基类进行向上转型，需要的话就用继承，不需要的话就用组合方式。

### 8. final关键字
- 对final关键字的误解
当final修饰的是基本数据类型时，它指的是数值恒定不变（就是编译期常量，如果是static final修饰，则强调只有一份），而对对象引用而不是基本类型运用final时，其含义会有一点令人迷惑，因为用于对象引用时，final使引用恒定不变，一旦引用被初始化指向一个对象，就无法再把它指向另一个对象。然而，**对象其自身却是可以被修改的**，Java并未提供使任何对象恒定不变的途径（但可以自己编写类以取得使对象恒定不变的效果），这一限制同样适用数组，它也是对象。
- **使用final方法真的可以提高程序效率吗？**
将一个方法设成final后，编译器就可以把对那个方法的所有调用都置入“嵌入”调用里。只要编译器发现一个final方法调用，就会（根据它自己的判断）忽略为执行方法调用机制而采取的常规代码插入方法（将自变量压入堆栈；跳至方法代码并执行它；跳回来；清除堆栈自变量；最后对返回值进行处理）。相反，**它会用方法主体内实际代码的一个副本来替换方法调用**。这样做可避免方法调用时的系统开销。当然，若方法体积太大，那么程序也会变得雍肿，可能受到到不到嵌入代码所带来的任何性能提升。因为任何提升都被花在方法内部的时间抵消了。

 在最近的Java版本中，虚拟机（特别是hotspot技术）能自动侦测这些情况，并颇为“明智”地决定是否嵌入一个final 方法。然而，最好还是不要完全相信编译器能正确地作出所有判断。通常，**只有在方法的代码量非常少，或者想明确禁止方法被覆盖的时候，才应考虑将一个方法设为final。**

 类内所有private 方法都自动成为final。由于我们不能访问一个private 方法，所以它绝对不会被其他方法覆盖（若强行这样做，编译器会给出错误提示）。可为一个private方法添加final指示符，但却不能为那个方法提供任何额外的含义。

### 9. 策略设计模式与适配器模式的区别
- 策略设计模式
创建一个能够根据所传递的参数对象的不同而具有不同行为的方法，被称为策略设计模式，这类方法包含所要执行的算法中固定不变的部分，而“策略”包含变化的部分。策略就是传递进去的参数对象，它包含要执行的代码。
- 适配器模式
在你无法修改你想要使用的类时，可以使用适配器模式，适配器中的代码将接受你所拥有的接口，并产生你所需要的接口。

### 10. 内部类
- 内部类与组合是完全不同的概念，这一点很重要。
- 为什么需要内部类？ — **主要是解决了多继承的问题，继承具体或抽象类**
    - 一般来说，内部类继承自某个类或实现某个接口，内部类的代码操作创建它的外围类的对象。所以可以认为**内部类提供了某种进入其外围类的窗口。**
    - 内部类最吸引人的原因是：每个内部类都能独立地继承自一个（接口的）实现，所以无论外围类是否已经继承了某个（接口的）实现，对于内部类都没有影响。
    - 如果没有内部类提供的、可以继承多个具体的或抽象的类的能力，一些设计与编程问题就很难解决。从这个角度看，内部类使得多重继承的解决方案变得完整。接口解决了部分问题，而内部类有效的实现了“多重继承”。也就是说，**内部类允许继承多个非接口类型。**

     考虑这样一种情形：如果必须在一个类中以某种方式实现两个接口。由于接口的灵活性，你有两种选择：使用单一类或者使用内部类。但如果拥有的是抽象的类或具体的类，而不是接口，那就只能使用内部类才能实现多重继承。

 使用内部类，还可以获得其他一些特性：
    - 内部类可以有多个实例，每个实例都有自己的状态信息，并且与其外围类对象的信息相互独立。
    - 在单个外围类中，可以让多个内部类以不同的方式实现同一个接口或继承同一个类。
    - 创建内部类对象的时刻并不依赖于外围类对象的创建。
    - 内部类并没有令人迷惑的is-a关系，它就是一个独立的实体。

### 11. String类型 — 不可变
- **用于String的“+”与“+=”是Java中仅有的两个重载过的操作符，而Java并不允许程序员重载任何操作符。**
- 考虑到效率因素，编译器会对String的多次+操作进行优化，优化使用`StringBuilder`操作（`javap -c class字节码文件名 命令`查看具体优化过程）。这让你觉得可以随意使用String对象，反正编译器会为你自动地优化性能。但编译器能优化到什么程度还不好说，不一定能优化到使用StringBuilder代替String相同的效果。比如：
    ```java
    public class WitherStringBuilder {
    	public String implicit(String[] fields) {
    		String result = "";
    		for(int i = 0; i < fields.length; i++)
    			result += fields[i];
    		return result;
    	}
    	
    	public String explicit(String[] fields) {
    		StringBuilder result = new StringBuilder();
    		for(int i = 0; i < fields.length; i++)
    			result.append(fields[i]);
    		return result.toString();
    	}
    }
    ```
运行`javap -c WitherStringBuilder`，可以看到两个方法对应的字节码。
**implicit方法：**
> public java.lang.String implicit(java.lang.String[]);
   Code:
      0: ldc #16 // String
      2: astore_2
      3: iconst_0
      4: istore_3
      **5: goto 32
      8: new #18 // class java/lang/StringBuilder**
     11: dup
     12: aload_2
     13: invokestatic #20 // Method java/lang/String.valueOf:(
Ljava/lang/Object;)Ljava/lang/String;
     16: invokespecial #26 // Method java/lang/StringBuilder."<
init>":(Ljava/lang/String;)V
     19: aload_1
     20: iload_3
     21: aaload
     22: invokevirtual #29 // Method java/lang/StringBuilder.ap
pend:(Ljava/lang/String;)Ljava/lang/StringBuilder;
     25: invokevirtual #33 // Method java/lang/StringBuilder.to
String:()Ljava/lang/String;
     28: astore_2
     29: iinc 3, 1
     32: iload_3
     33: aload_1
     34: arraylength
     35: if_icmplt 8
     38: aload_2
     39: areturn
 public java.lang.String implicit(java.lang.String[]);
   Code:
      0: ldc #16 // String
      2: astore_2
      3: iconst_0
      4: istore_3
      5: goto 32
      8: new #18 // class java/lang/StringBuilder
     11: dup
     12: aload_2
     13: invokestatic #20 // Method java/lang/String.valueOf:(
Ljava/lang/Object;)Ljava/lang/String;
     16: invokespecial #26 // Method java/lang/StringBuilder."<
init>":(Ljava/lang/String;)V
     19: aload_1
     20: iload_3
     21: aaload
     22: invokevirtual #29 // Method java/lang/StringBuilder.ap
pend:(Ljava/lang/String;)Ljava/lang/StringBuilder;
     25: invokevirtual #33 // Method java/lang/StringBuilder.to
String:()Ljava/lang/String;
     28: astore_2
     29: iinc 3, 1
     32: iload_3
     33: aload_1
     34: arraylength
     35: if_icmplt 8
     38: aload_2
     39: areturn

 可以发现，StringBuilder是在循环之内构造的，这意味着每经过循环一次，就会创建一个新的StringBuilder对象。

 **explicit方法：**
  >public java.lang.String explicit(java.lang.String[]);
    Code:
       0: **new #18 // class java/lang/StringBuilder**
       3: dup
       4: invokespecial #45 // Method java/lang/StringBuilder."<
init>":()V
       7: astore_2
       8: iconst_0
       9: istore_3
      **10: goto 24**
      13: aload_2
      14: aload_1
      15: iload_3
      16: aaload
      17: invokevirtual #29 // Method java/lang/StringBuilder.ap
pend:(Ljava/lang/String;)Ljava/lang/StringBuilder;
      20: pop
      21: iinc 3, 1
      24: iload_3
      25: aload_1
      26: arraylength
      27: if_icmplt 13
      30: aload_2
      31: invokevirtual #33 // Method java/lang/StringBuilder.to
String:()Ljava/lang/String;
      34: areturn
}

 可以看到，不仅循环部分的代码更简短、更简单，而且它只生成了一个StringBuilder对象。显式的创建StringBuilder还允许你预先为其指定大小。**如果你已经知道最终的字符串大概有多长，那预先指定StringBuilder的大小可以避免多次重新分配缓冲。**
 
  --- 
 ####总结
 因此，当你为一个类重写toString()方法时，如果字符串操作比较简单，那就可以信赖编译器，它会为你合理地构造最终的字符串结果。但是，如果你要在toString()方法中使用循环，那么最好自己创建一个StringBuilder对象，用它来构造最终的结果。
 
 ---

- `System.out.printf()`和`System.out.format()`方法模仿自C的`printf`，可以格式化字符串，两者是完全等价的。

 Java中，所有新的格式化功能都由`java.util.Formatter`类处理。
`String.format()`方法参考了C中的`sprintf()`方法，以生成格式化的String对象，是一个static方法，它接受与`Formatter.format()`方法一样的参数，但返回一个String对象。当你只需使用`format()`方法一次的时候，该方法很方便。
    ```java
    import java.util.Arrays;
    import java.util.Formatter;
    
    public class SimpleFormat {
    
    	public static void main(String[] args) {
    		int x = 5;
    		double y = 5.324667;
    		System.out.printf("Row 1: [%d %f]\n", x, y);
    		System.out.format("Row 1: [%d %f]\n", x, y);
    		
    		Formatter f = new Formatter(System.out);
    		f.format("Row 1: [%d %f]\n", x, y);
    		
    		String str = String.format("Row 1: [%d %f]\n", x, y);
    		System.out.println(str);
    		
    		Integer[][] a = {
    			{1, 2, 3}, {4, 5, 6},
    			{7, 8, 3}, {9, 10, 6}
    		};
    		System.out.println(Arrays.deepToString(a));
    	}
    }
    ```

### 12. 序列化控制
- 当我们对序列化进行控制时，可能某个特定子对象不想让Java序列化机制自动保存与恢复。如果子对象表示的是我们不希望将其序列化的敏感信息（如密码），通常会面临这种情况。即使对象中的这些信息是private属性，一经序列化处理，人们就可以通过读取文件或者拦截网络传输的方式来访问到它。有两种办法可以防止对象的敏感部分被序列化：
    - 实现`Externalizable`代替实现`Serializable`接口来对序列化过程进行控制，`Externalizable`继承了`Serializable`接口，同时增添了两个方法：`writeExternal()`和`readExternal()`。

     **两者在反序列化时的区别**：
     - 对Serializable对象反序列化时，**由于Serializable对象完全以它存储的二进制位为基础来构造，因此并不会调用任何构造函数，**因此Serializable类无需默认构造函数，但是当Serializable类的父类没有实现Serializable接口时，反序列化过程会调用父类的默认构造函数，因此该父类必需有默认构造函数，否则会抛异常。
     - 对Externalizable对象反序列化时，**会先调用类的不带参数的构造方法**，这是有别于默认反序列方式的。如果把类的不带参数的构造方法删除，或者把该构造方法的访问权限设置为private、默认或protected级别，会抛出`java.io.InvalidException: no valid constructor`异常，因此**Externalizable对象必须有默认构造函数，而且必需是public的。**
 - `Externalizable`的替代方法：如果不是特别坚持实现Externalizable接口，那么还有另一种方法。我们可以实现`Serializable`接口，并添加`writeObject()`和`readObject()`的方法。一旦对象被序列化或者重新装配，就会分别调用那两个方法。也就是说，**只要提供了这两个方法，就会优先使用它们，而不考虑默认的序列化机制。**

     这些方法必须含有下列准确的签名：
    ```java
    private void writeObject(ObjectOutputStream stream) 
            throws IOException;
    private void readObject(ObjectInputStream stream)
            throws IOException, ClassNotFoundException
    ```
 - 可以用`transient`关键字逐个字段地关闭序列化，它的意思是“**不用麻烦你保存或恢复数据—我自己会处理的**”。由于Externalizable对象在默认情况下不保存它们的任何字段，所以**transient关键字只能和Serializable对象一起使用。**