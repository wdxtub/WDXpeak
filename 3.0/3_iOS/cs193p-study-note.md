# Stanford - Developing iOS 8 Apps with Swift 2015 学习笔记

虽然有点旧，但是还是可以跟着规范的课程学一发

## 1 Logistics, iOS 8 Overview

### What's in iOS

+ Cocoa Touch
	+ Multi-Touch, Alerts, Core Motion, Web View, View Hierarchy, Map Kit, Localization, Image Picker, Controls, Camera
+ Media
	+ Core Audio, JPEG/PNG/TIFF, OpenAL, PDF, Audio Mixing, Quartz(2D), Audio Recording, Core Animation, Video Playback, OpenGL ES
+ Core Services
	+ Collections, Core Location, Address Book, Net Services, Networking, Threading, File Access, Preferences, SQLite, URL Utilities
+ Core OS
	+ OSX kernel, Power Management, Mach 3.0, Keychain Access, BSD, Certificates, Sockets, File System, Security, Bonjour

### Platform Components

+ Tools
	+ Xcode 6 (Latest is 7)
+ Language(s)
	+ Swift, Modern Language
	+ `let value = formatter.numberFromString(display.text!)?.doubleValue`
+ Frameworks
	+ Foundation, Core Data, UIKit, Core Motion, Map Kit
+ Design Strategy
	+ MVC


### Calculator Tutorial

+ Organization Identifier 是你的身份验证，需要保证独立性
+ 尽可能把控件放到蓝线上，也就意味着某种对齐
+ weak 关键字，与 reference counting 相关，具体后面会说
+ 对象都在 heap 中存在
+ 能用 let 尽量用 let，增加可读性
+ option(alt) 点击变量可以查看帮助
+ optional 类型，可能是当前类型的值，或者是 `nil`，例如 `String?`
	+ `nil` 就是 not set
+ 在 optional 类型后面加 `!` 可以取出对应的值，但如果原来值是 `nil`，就会崩溃
+ 所有的变量都必须被初始化


## 2 More Xcode and Swift, MVC

+ 为什么 `UILabel` 之类的 outlet 可以直接声明 `!` 而不需要像之前所说的那样所有变量都必须被初始化呢？因为作为控件变量称为 implicit unwrap，走 storyboard 另外的机制
+ 右键点击一个控件会显示当前和该控件绑定的事件，可以在这里操作进行绑定和解绑定
+ 新建数组 `var operandStack = Array<Double>()`，可以被 infer 的类型最好就不要明写出来
+ 变量的 set get 中有神奇变量 `newValue`
+ command + / 可以快速注释
+ 利用 Swift 本身的特性可以写出非常精简的代码
+ 之后是 MVC 的介绍

## 3 Applying MVC

+ 新建一个 class：File -> New -> File -> Swift File
+ 虽然没有要求类名和文件名一致，但是最好还是一样，这样比较符合惯例
+ 理论上来说不应该在一个 Model 类中 `import UIkit`
+ 可以用快捷语法来生成数组 `[TypeName]()`
+ 可以用快捷语法来生成字典 `[KeyType: ValueType]()`
+ `*`, `+`, `sqrt` 这些内置函数可以直接当参数传
+ 在字典里返回的是 optional 类型
+ 传参时除非传的是 class，不然都是传入一个复制的值
+ 传值的时候参数隐含是 `let` 的，即不可变
+ 函数可以直接返回一个 tuple
+ option(alt) 加点击文件可以把文件放到另一边
+ if let xxx = xxx {} 是通常的处理 optional 类型的方式
+ switch 如果列举了所有情况就不需要 `default: break`
+ `private enum Op: CustomStringConvertible` 由 `Printable` 更名而来

## 4 More Swift and Foundation Frameworks

不是所有的都记录，只挑了一些我觉得和之前学的语言差异比较大的，很多内容在我之前的学习笔记里都有覆盖

### Optional

An Optional is just an `enum`

```swift
enum Optional<T>{
	case None
	case Some(T)
}
```

```swift
let x: String? = nil
// is
let x = Optional<String>.None

let x: String? = "hello"
// is
let x = Optional<String>.Some("hello")

var y = x!
// is
switch x {
	case Some(let value): y = value
	case None: // raise an exception
}
```

### Other Classes

+ `NSObject`
	+ Base class for all objective-C classes. Some advanced features will require you to subclass from `NSObject`
+ `NSNumber`
	+ Generic number-holding class
+ `NSDate`
	+ Used to find out the date and time right now or to store past or future dates
+ `NSData`
	+ A "bag of bits"

### Data Structures

Three Types: Classes, Structures, Enumerations

+ Similarities
	+ Declasration syntax
	+ Properties and Functions
	+ Initializers
+ Differences
	+ Inheritance (class only)
	+ Introspection and casting (class only)
	+ Value type (struct, enum) vs. Reference type (class) 


### Value vs. Reference

+ Value (`struct` and `enum`)
	+ **Copied** when passed as an argument to a function
	+ **Copied** when assigned to a different variable
	+ **Immutable** if assigned to a variable with `let`
	+ Remember that function parameters are, by default, constants
	+ You can put the keyword `var` on an parameter, and it will be mutable, but it's still a copy
	+ You must note any `func` that can mutate a struct/enum with the keyword `mutating`
+ Reference (`class`)
	+ Stored in the heap and reference counted (automatically)
	+ Constant pointers to a class (`let`) still can mutate by calling methods and changing properites
	+ When passed as an argument, does not make a copy (just passing a pointer to same instance)
+ Choosing which to use?
	+ Usually you will choose `class` over `struct`. `struct` tends to be more for fundamental types. Use of `enum` is situational (any time you have a type of data with discret values)

### AnyObject

+ Special "Type" (actually it's a Protocol)
	+ Used primarily for compatibility with exsiting Objective-C-based APIs
+ Where will you see it?
	+ As properties (eigher singularly or as an array of them), e.g. ...
	+ `var destinationViewController: AnyObject`
	+ `var toolbarItems: [AnyObject]`
+ How do we use `AnyObject`
	+ We don't usually use it directly
	+ Instead, we convert it to another, known type 
+ How do we convert it?
	+ We need to create a new vairable which is of a known object type
+ Casting AnyObject
	+ We "force" an `AnyObject` to be something else by "casting" it using the `as` keyword 

### 总结

语言的细节还有很多，需要在实践中不断熟悉，这里不需要过度在意细节，动手最重要

## 5 Objective C Compatibility, Property List, Views

+ 主要介绍了 Swift 与 Objc 的桥接，这里官方的指南都有介绍，具体不赘述
+ Property List is really just the definition of a term
	+ pass around data "blindly"
	+ "generic data structure", be passed to API
	+ example: `NSUserDefaults`, small database
	+ 持久化的方式
+ Views
	+ `UIView` subclass
	+ Defines a coordinate space, for drawing, and for handling touch events
	+ Hierarchical (only one superview, but many/zero subviews)
	+ The hierarchy is most often constructed in Xcode graphically
		+ But it can be done in code as well
	+ Where does the view hierarchy start?
		+ THe top of the (usable) view hierarchy is the Controller's `var view: UIView`
		+ This view is the one whose bounds will change on rotation
		+ This view is likely the ones you will programmatically add `subview` to
		+ All of your MVC's View's `UIView` will have this view as an ancestro
		+ It's wutomatically hooked up for you when you create an MVC in Xcode
	+ 在代码中初始化 `UIView` 需要实现两个必要 `init` 函数，因为有两种方式可以创建
	+ 或者也可以用 `awakeFromNib` 针对 storyboard
+ View Coordinate System
	+ Origin is upper left
	+ Units are points, not pixels
		+ Pixels are the minimum-sized unit of drawing your device is capable of
		+ Points are the units in the coordinate system
		+ Most of the time there are 2 pixels per point, but it could be only 1 or something else
		+ How many pixels per point are there? `UIView`'s `var contentScaleFactor: CGFloat`
	+ The boundaries of where drawing happends
		+ `var bounds: CGRect` // a view's internal drawing space's origin and size
		+ This is the rectangle containing the drawing space **in its own coordinate system**
		+ It is up to your views' implementation to interpret what `bounds.origin` means (often nothing)   
	+ Where is the `UIView`? 注意都是在 superview 里的，不是自己的
		+ `var center: CGPoint` // the center of a `UIView` **in its superview's coordinate system**
		+ `var frame: CGRect` // the rect containing a `UIView` **in its superview's coordinate system**
+ bounds vs frame
	+ Use `frame` and/or `center` to **position** a `UIView`
	+ `frame.size` 不总是等于 `bounds.size` -> 因为旋转的时候 frame 要大得多！
+ Creating Views
	+ Most often your views are created via your storyboard
	+ To draw, just create a `UIView` subclass and override `drawRect`
	+ NEVER call drawRect!! EVER! Or else!
+ 绘制的方法也有很多，主要是 Bezier 已经一些 UIKit 的设定
+ `UIColor`: RGB, HSB or even a pattern (using UIImage)
	+ have alpha (transparency) 0(fully transparent) 1.0(fully opaque)
	+ 如果需要透明需要把 `UIView` 的 `var opaque = false`
+ Drawing Text
	+ Usually we use a `UILabel` to put text on screen
	+ To draw in `drawRect`, use `NSAtrributedString`
	+ Mutability is done with `NSMutableAttributedString`
	+ `NSattributedString` is not a String, nor an NSString
+ Fonts
	+ The absolutely best way to get a font in code
		+ `class func preferredFontForTextStyle(UIFontTextStyle) -> UIFont
		+ `UIFontTextStyle.Headline`
		+ `UIFontTextStyle.Body`
		+ `UIFontTextStyle.Footnote`
	+ There are also "system fonts"
		+ Don't use for user's **content**. Use preferred fonts for that 
+ 在 storyboard 中按着 `ctrl + shift` 再点击控件会出现一个界面让你选择你想要选择的控件，很有用
+ 如果需要在更新某个值的时候同时更新绘制，利用 `didSet` 方式声明变量
+ 如果需要一个 view 在旋转之后更新，在其 attribute inspector 中把 Mode 改为 Redraw

## 6 Protocols and Delegation, Gestures

+ 在一个 UIView 的代码前加上 `@IBDesignable` 可以直接在 storyboard 中绘制图案
+ 在一个 UIView 中的变量前加上 `@IBInspectable` 就可以直接在 storyboard 中更改
+ Extension 只能添加，不能修改原来的方法或者属性
	+ 是一个很容易滥用的机制！注意场景
+ Protocol - A way to express an API minimally
	+ is a TYPE just like any other type, except 
		+ It has no storage or implementation associated with it
		+ 没有对应的实现，只是一个羊头，没有狗肉
+ Delegation
	+ A very important use of `protocols`
	+ How it plays out
		+ Create a delegation `protocol` (defines what the View wants the Controller to take care of)
		+ Create `delegate` property in the View whose type is that delegation `protocol`
		+ Use the `delegate` property in the View to get/do things it can't own or control
		+ Controller declares that it implements the `protocol`
		+ Controller sets `self` as the delegate of the View by setting the property in #2 above
		+ Implement the `protocol` in the Controller
	+ Now the View is hooked up to the Controlle
	+ weak 用来避免循环引用
	+ `let smiliness = dataSource?.smilinessForFaceView(self) ?? -0.0`
		+ `??` 符号表示，如果左边的表达式是 nil，那么用右边的值
	+ comman + shift + o 可以快速检索并打开文件
+ Gestures
	+ we can get notified of the raw touch events
	+ Gestrues are recognized by instances of `UIGestureRecognizer`
	+ Two sides to using a gesture recognizer
		1. Adding a gesture recognizer to a `UIView`
		2. Providing a method to "handle" that gesture
	+ Usually the first is done by a Controller
	+ The second is provided either by the `UIView` or a controller
+ UISplitViewController (Two MVCs side by side)
	+ 左边 Master，右边 Detail

## 7 Multiple MVCs

+ UINaviationController
	+ Pushes and pops MVCs off of a stack
	+ 只有顶上的 title bar 是 `UINavigationController` 绘制的
	+ `rootViewController` 用来切换显示不同的 MVC
+ You can get the sub-MVCs via the `viewControllers` property
	+ `var viewControllers: [UIViewController] { get set }
+ Every `UIViewController` knows the Split View, Tab Bar or Navigation Controller it is currently in 
+ Wirting up MVCs
	+ ctrl + drag in storyboard
	+ 当然也可以在代码中实现，不过这个课程里只用 storyboard，我个人也觉得交给 storyboard 就好
	+ Editor -> Embed in -> Navigation Controller
+ Segue
	+ Four Basic Segues
	+ Show Segue, Show Detail Segue, Modal Segue(better not), Popover Segue
	+ always create a new instance of an MVC，不会用已有的
	+ 要保证 identifier 和代码里用的一致
	+ More important use of the identifier: **preparing** for a segue
+ Preparing for a Segue
	+ It is crucial to understand that this preparation is happening BEFORE outlets get set!
	+ It is a very common bug to prepare an MVC thinking its outlets are set
+ Preventing Segues
	+ You can prevent a segue from happening too
	+ `shouldPerformSegueWithIdentifier` 返回 false 即可
+ Label 的 Autoshrink 属性可以避免出现文字过长
+ Popovers
	+ Popovers pop an entire MVC over the rest of the screen
	+ is not a `UIViewController`
	+ Things to note when **preparing** for a popover segue
	+ `popOverPresentationController` 针对 iphone 和 ipad 有不同的表现形式，但是也是可以自由定制的，有对应的方法
+ override 基类的 property 的 didSet 方法不会覆盖原来的，而是在原来的基础上添加

## 8 View Controller Lifecycle, Autolayout

+ After instantiation and outlet-setting, `viewDidLoad` is called
	+ This is an exceptionally good place to put a lot of setup code
	+ It's better than an `init` because your outlets are all set up by the thime this is called
	+ update your UI from your model
	+ but **geometry** of your view (`bounds`) is not set yet!
+ Just before your `view` appears on screen, you get notified
	+ `func viewWillAppear(animated: Bool)`
	+ don't pu something in this method that really wants to be in `viewDidLoad`
	+ Do something here if things your display is changing while your MVC is off-screen
	+ Your view's geometry is set here, but there are other plaes to react to geometry
+ You get notified when you will disappear off screen too
	+ This is where you put "remember what's going on" and cleanup code
+ Geometry changed?
	+ Most of the time this will be automatically handled with Autolayout
	+ But you can get involved in geometry changes directly with
		+ `func viewWillLayoutSubviews()`
		+ Autolayout happens between these two method
		+ `func viewDidLayoutSubviews()` 
+ Autorotation
	+ You can control which orientations your app supports in the Settings of your project
	+ Almost always, your UI just responds naturally to rotation with autolayout
+ In low-memory situations, `didReceiveMemoryWarning` get called
+ `awakeFromNib`
	+ This method is sent to all objects that come out of a storyboard (including your Controller)
	+ Happens before outlets are set!
	+ **Put code somewhere else** if at all possible
+ Size Classes
	+ Compact, Regular, Any
	+ 可以在 storyboard 中进行不同组合的配置，下面也会有说明
	+ 可以在 Inspector 里设置不同控件和 constrain 的范围（最下面的部分）

## 9 ScrollView and Multithreading

+ 先设置 scrollView 的 contentSize，然后就可以正常添加不同的 frame
+ 注意不同坐标系的转换
+ UIScrollView
	+ add your "too big" `UIView` in code using `addSubview`
	+ Now don't forget to set the `contentSize`
+ Scolling programmatically
	+ `func scrollRectToVisible(CGRect, animated: Bool)`
+ Zooming (affine transform)，可以设置最大最小的放大
	+ Will not work without **delegate** method to specify view to zoom
	+ 也可以编程 zoom  
+ Closure
	+ capture variables in the surrounding context
	+ can lead to very elegant code
	+ 使用时需要小心，因为可能会出现循环引用 `[unowned self] in ...`
+ Queues
	+ Multithreading is mostly about "queues" in iOS.
	+ Functions (usually closures) are lined up in a queue.
	+ Then thos functions are pulled off the queue and executed on an associated thread
+ Main Queue
	+ All UI activity MUST occur on this queue and this queue only.
	+ non-UI activity that is at all time consuming must NOT occur on that queue.
	+ We want our UI to be responsive!
	+ Functions are pulled off and worked on in the main queue only when it is "quiet"
	+ `dispatch)async(queue)` 执行完成后再 dispatch main queue 以更新 UI
+ Other Queue 不同的优先级
	+ QOS_CLASS_USER_INTERACTIVE // quick and high priority
	+ QOS_CLASS_USER_INITIATED // high priority, might take time
	+ QOS_CLASS_UTILITY // long running
	+ QOS_CLASS_BACKGROUND // user not concerned with this 
+ 还可以执行一些延迟排队的任务

## 10 Table View

+ UITextField
	+ Like UILabel, but editable
	+ Keyboard appear when `UITextField` becomes "first responder"
	+ `becomeFirstResponder` and `resignFirstResponder`
	+ Delegate can get involved with Return key, etc
+ UITableView
	+ displayer data in a table
	+ one-dimensional table
	+ subclass of `UIScrollView`
	+ Displaying multi-dimensional tables
		+ uaually done via a UINavigationController with multiple MVC's where View is `UITableView`
	+ Group style and plain style
	+ Table Header, Table Footer, Section, Section header
	+ Subtitle, Basic, Right Detail, Left Detail
+ UITableViewCell 用来自定义
+ 两个重要部分 delegate 和 dataSource，如果需要动态的列表
+ `dequeueReusableCellWithIndentifier` 来重用 cell  
+ `UITableViewDataSource`
	+ Number of sections is 1 by default
	+ No default for `numberOfRowsInSection`
	+ do not implement these `dataSource` method for a static table
+ Loading your table view with data
	1. set the table view's `dataSource` to your Controller (automatic with `UITableViewController`)
	2. implement `numberOfSectionsInTableView` and `numberOfRowsInSection`
	3. implement `cellForRowAtIndexPath` to return loaded-up `UITableViewCells`
+ UITableView Target/Action
	+ `UITableViewDelegate` method sent when row is selected
	+ `func reloadData()`
+ 这一部分很重要，要重点掌握

## 11 Unwind Segues, Alerts, Timers, View Animation

+ Unwind Segue
	+ The only segue that does NOT create a new MVC
	+ Jumping up the stack of cards in a navigation controller
	+ Dismissing a Modally segued-to MVC while reporting information back to the presenter
	+ ctrl+drag to the exit icon
+ Alerts and Action Sheets
	+ pop up and ask the user something mechanism
+ Alerts
	+ Pop up in the middle of the screen
	+ Usually ask questions with only two(or one) answers
	+ Can be disruptive to your user-iterface, so use carefully
	+ Often used for "asynchronous" problems
	+ Can have a text field to get a quikc answer
+ Action Sheets
	+ Usually slide in from the bottom of the screen on iPhone, and in a popover on iPad
	+ Can be displayed from bar button item or from any rectangular area in a view
	+ Generally asks questions that have more than two answers
+ Timer `NSTimer`
	+ Setting up a timer to call a method periodically
	+ more for larger-grained activities 
	+ It might help system performance to set a tolerance for "late firing"
	+ the firing time is relative to the start of the timer
+ Kinds of Animation
	+ Animating `UIView` properties
	+ Animation of View Controller transition
	+ Core Animation 
+ UIView Animation
	+ Change to certain `UIView` properties can be animated over time
		+ frame, transform(translation, rotation and scale), alpha(opacity)
	+ Done with `UIView` class method(s) using closure
	+ `animateWithDuration`
	+ `UIViewAnimationOptions`: BeginFromCurrentState, AllowUserInteraction, LayoutSubview, Repeat, Autoreverse, OverrideInheritedDuration, OverrideInheritedCurve, AllowAnimatedContent, CurveEaseInEaseOut, CurveEaseIn, CurveLinear
	+ Sometimes you want to make an entire view modification at once
	+ Use closures again with this `UIView` class method

## 12 Dynamic Animation

+ Set up physics relating animatable objects and let them run until they resulve to stasis
+ Steps
	+ Create a `UIDynamicAnimator`
	+ Add `UIDynamicBehaviro`s to it (gravity, collisions, etc)
	+ Add `UIDynamicItem`s (usualy `UIView`s) to the `UIDynamicBehavior`s
+ UIGravityBehavior
	+ angle, magnitude
+ Stasis
	+ `UIDynamicAnimator`'s delegate tells you when animation pauses
	+ `dynamicAnimatorDidPause(UIDynamicAnimator)`

## 13 Application Lifecycle and Core Motion

+ Notification
	+ For Model (or global) to Controller communication
	+ `NSnotificationCenter`，类似一个观察者模式，注册并获取变动时的通知
+ Application Lifecycle
	+ Not running, Inactive, Active, Background, Suspended
	+ `application(UIApplication, didFinishLauchingWithOptions: [NSObject: AnyObject])`
	+ 用来知道自己的 app 是在什么情况下被打开的（不只是用户点击这一种）
+ UIApplication
	+ Shared instance
		+ manages all global behavior
		+ never need to subclass it
		+ It delegates everything you need to be involved in to its `UIApplicationDelegate` 
+ Info.plist
	+ Many of your application's settings are in Info.plist
+ Capabilities
	+ Some features require enabling (iCloud, Game Center, etc)
	+ Switch on in Capabilities tab (Inside your Project Settings)
+ Airdrop 需要先注册，参考 Trak 的 info.plist
+ Core Motion
	+ API to access motion sensing hardware on your device
	+ Primary inputs: Accelerometer, Gyro, Magnetometer
	+ Class used to get this input is `CMMotionManager`
	+ Usage
		+ Check to see what hardware is available
		+ Start the sampling going and poll the motion manager for the latest sample it have
		+ ...or...
		+ check to see what hardware is available
		+ Set the rate at which you want data to be reported from the hardware
		+ Register a closure (and a queue to run it on) to call each time a sample is taken
	+ Checking availability of hardware sensor
		+ `var {accelerometer, gyro, magnetometer, deviceMotion}Available: Bool`
	+ Starting the hardware sensors collecting data
		+ you only need to do this if you are going to poll for data
		+ `func start{Accelerometer, Gyro, Magnetometer, DeviceMotion}Updates()`
	+ Is the hardware currently collection data?
		+ `var {accelerometer,gyro,magnetometer,deviceMotion}Active: Bool`
	+ Stop the hardware collecting data
		+ `func stop{Accelerometer,Gyro,Magnetometer,DeviceMotion}Updates()`
+ CMDeviceMotion
	+ 各种传感器的组合 

## 14 Core Location and MapKit

+ Core Location
	+ Framework for managing location and heading
		+ No user-interface
	+ Basic object is `CLLocation`
		+ Properties: `coordinate`, `altitude`, `horizontal/verticallAccuracy`, `timestamp`, `speed`, `course`
+ The more accuracy you request, the more battery will be used
+ `CLLocationManager`
	+ Check if the hardware you are on/user supports the kind of location updating you want
	+ Create a `CLLocationManager` instance and set the `delegate` to receive updates
	+ Configure the manager according to what kind of location updating you want
	+ Start the manager monitoring for location changes
+ Kinds of location monitoring
	+ Accuracy-based continual updates
	+ Updates only when "significant" changes in location occur
	+ Region-based updates
	+ Heading monitoring 
+ Asking `CLLocationManager` what your hardware can do
	+ `class func authorizationStatus() -> CLAuthorizationStatus` // Authorized, Denied or Restricted
	+ `class func locationServicesEnabled() -> Bool` // user enabled (or not) locations for your app
+ You must add an Info.plist entry 
	+ `NSLocationWhenInUseUsageDescription`
	+ `NSLocationAlwaysUsageDescription`
+ Error reporting to the `delegate`
	+ `func locationManager(CLLocationManager, didFailWithError: NSError)`
	+ Not always a fatal thing, so pay attention to this `delegate` method
+ 也可以进行后台更新
+ Map Kit
	+ UI, can have annotations on it
	+ Each annotation is a `coordinate`, a `title` and a `subtitle`
	+ Annotation can have a `callout`. It appears when the annotation view is clicked
	+ `import MapKit`
	+ 地图部分也是玩法很多的，需要仔细研究研究 
+ MKLocalSearch
	+ Can search by natural language strings asynchronously
+ MKDirections, MKRoute, MKPolyline
+ Overlays, MKOverlayView
+ callout 只能代码配合 storyboard 实现，因为 storyboard 压根不会显示这个 callout

## 15 Modal Segues

+ Modal View Controller
	+ A way of segueing that takes over the screen (should be used with care)
	+ Example (Contacts application)
	+ No back button (only Cancel)
+ Hearing back from a Modally segue-to View Controller
	+ To communicate results, generally you would Unwind (though delegation possible too)
	+ `func dismissViewControllerAnimated(Bool, completion: () -> Void)`
	+ Remember that unwind automatically dismisses
+ How is the modal view controller animated
	+ `var modalTransitionStyle: UIModalTransitionStyle`
	+ `.CoverVertical`, `.FlipHorizontal`, `.CrossDissolve`, `.PartialCurl`

## 16 Camera, Persistence and Embed Segues

+ UIImagePickerController
	+ Modal view to get media from camera or photo library
	+ Usage
		1. Create it & set its delegate
		2. Configure it (source, kind of media, user edibility)
		3. Present it
		4. Respond to delegate method when user is done/cancels picking the media
	+ Sources: `.PhotoLibrary`, `.Camera`, `.SavedPhotosAlbum`
	+ `kUTTypeImage`, `kUTTypeMovie` from `import MobileCoreServices`
+ 相机这部分等移植图像处理库的时候再细细研究
+ Persistence
	+ Archiving, SQLite, File System, Core Data
+ Archiving
	+ A mechanism for making ANY object graph persistent
	+ Requires all object in the graph to implement `USCoding` protocol
+ SQLite
	+ SQL in a single file
	+ Fast, low memory, reliable
	+ Open SOurce, comes bundled in iOS
	+ Not good for everything
	+ Not a server-based technology
	+ In used by Core Data
+ File System
	+ Acess files in the Unix filesystem
		1. Get the root of a path into an NSURL
		2. Append path componnets to the URL
		3. Write to/read from the files
		4. Manage the filesystem with `NSFileManager` 
	+ You can only write inside your application's sandbox
		+ Security, Privacy, Cleanup
+ Core Data
	+ Object-oriented database
	+ Very, very powerful framework in iOS
	+ How does it work?
		+ Create a visual mapping (using Xcode tool) between database and objects
		+ Create and query for objects using object-oriented API
		+ Access the "columns in the database table" using `@NSManaged var`s on those objects
+ Embed Segues
	+ Putting a VC's self.view in another VC's view hierarchy
	+ This can be a very powerful encapsulation technique 
	+ Drag out a `Container View from the object palette into the scene you want to embed it in
	+ Automatically sets up an "Embed Segue" from container VC to the contained VC
	+ The embedded VC's outlets are not set at the time `prepareForSegue(sender:)` is called

## 17 Internationalization and Settings

+ Two steps to making international versions of your application
	+ Internationalization (i18n)
	+ Localization (l10n)
+ Internationalization
	+ This is a process of making string externally editable (from storyboard or code)
	+ It also involves using certain "formatting" classes for things like dates, number, etc
+ Localization
	+ A process of translating those externalized strings for a given language
+ Storyboards are localized by changing the strings inside only
	+ And we rely on Autolayout to make it all look nice
+ First step: Registering Localizable Languages
	+ Go to the Project pane in Xcode then Info tab to add Localizations
	+ 注意是 project 不是 target 
+ Formatters
	+ locale, region of the world
	+ It is separate from language
	+ In different regions some things might display differently: numbers, dates, currency, etc
	+ 有各种 Formatter，可以仔细看看
	+ Date 是一个比较难处理的，需要注意
+ UIImage
	+ There are a number of ways to approach this.
	+ The image files themselves (if not in Images.xcassets) can be made localizable (File Inspector)
	+ Or you can keep them in Images.scassets and use NSLocalizedString for the image name
+ Editor -> Export For Localization
	+ `.xliff` cantain all of your resources
+ 可以创建不同的 scheme 来以不同的语言来运行 app
+ Settings
	+ A little bit of UI for your application
	+ 在类似 Info.plist 里进行创建 -> Settings Bundle
	+ 创建时会有一个例子，是很好的参考学习方式
	+ 每个 item 有 identifier


