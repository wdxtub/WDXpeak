# iOS

## Cocoa Touch

### 事件处理

#### 事件分类

对于 iOS 设备用户来说，他们操作设备的方式主要有三种：触摸屏幕、晃动设备、通过遥控设施控制设备。对应的事件类型有以下三种：

1. 触屏事件（Touch Event）
2. 运动事件（Motion Event）
3. 远端控制事件（Remote-Control Event）

#### 响应者链

当发生事件响应时，必须知道由谁来响应事件。在 iOS 中，由响应者链来对事件进行响应。

所有事件响应的类都是 UIResponder 的子类，响应者链是一个由不同对象组成的层次结构，其中的每个对象将依次获得响应事件消息的机会。当发生事件时，事件首先被发送给第一响应者，第一响应者往往是事件发生的视图，也就是用户触摸屏幕的地方。事件将沿着响应者链一直向下传递，直到被接受并做出处理。一般来说，第一响应者是个视图对象或者其子类对象，当其被触摸后事件被交由它处理，如果它不处理，事件就会被传递给它的视图控制器对象 ViewController（如果存在），然后是它的父视图（superview）对象（如果存在），以此类推，直到顶层视图。接下来会沿着顶层视图（top view）到窗口（UIWindow 对象）再到程序（UIApplication 对象）。如果整个过程都没有响应这个事件，该事件就被丢弃。一般情况下，在响应者链中只要由对象处理事件，事件就停止传递。

一个典型的事件响应路线如下：

    First Responser --> The Window --> The Application --> App Delegate

#### 事件分发

第一响应者（First responder）指的是当前接受触摸的响应者对象（通常是一个 UIView 对象），即表示当前该对象正在与用户交互，它是响应者链的开端。响应者链和事件分发的使命都是找出第一响应者。

iOS 系统检测到手指触摸 (Touch) 操作时会将其打包成一个 UIEvent 对象，并放入当前活动 Application 的事件队列，单例的 UIApplication 会从事件队列中取出触摸事件并传递给单例的 UIWindow 来处理，UIWindow 对象首先会使用 hitTest:withEvent:方法寻找此次 Touch 操作初始点所在的视图(View)，即需要将触摸事件传递给其处理的视图，这个过程称之为 hit-test view。

hitTest:withEvent:方法的处理流程如下:

+ 首先调用当前视图的 pointInside:withEvent: 方法判断触摸点是否在当前视图内；
+ 若返回 NO, 则 hitTest:withEvent: 返回 nil，若返回 YES, 则向当前视图的所有子视图 (subviews) 发送 hitTest:withEvent: 消息，所有子视图的遍历顺序是从最顶层视图一直到到最底层视图，即从 subviews 数组的末尾向前遍历，直到有子视图返回非空对象或者全部子视图遍历完毕；
+ 若第一次有子视图返回非空对象，则 hitTest:withEvent: 方法返回此对象，处理结束；
+ 如所有子视图都返回空，则 hitTest:withEvent: 方法返回自身 (self)。

**说明**

1. 如果最终 hit-test 没有找到第一响应者，或者第一响应者没有处理该事件，则该事件会沿着响应者链向上回溯，如果 UIWindow 实例和 UIApplication 实例都不能处理该事件，则该事件会被丢弃；
2. hitTest:withEvent: 方法将会忽略隐藏 (hidden=YES) 的视图，禁止用户操作 (userInteractionEnabled=NO) 的视图，以及 alpha 级别小于 0.01(alpha<0.01)的视图。如果一个子视图的区域超过父视图的 bound 区域(父视图的 clipsToBounds 属性为 NO，这样超过父视图 bound 区域的子视图内容也会显示)，那么正常情况下对子视图在父视图之外区域的触摸操作不会被识别, 因为父视图的 pointInside:withEvent: 方法会返回 NO, 这样就不会继续向下遍历子视图了。当然，也可以重写 pointInside:withEvent: 方法来处理这种情况。
3. 我们可以重写 hitTest:withEvent: 来达到某些特定的目的，当然实际应用中很少用到这些。

### UIApplication

UIApplication 的核心作用是提供了 iOS 程序运行期间的控制和协作工作。

每一个程序在运行期必须有且仅有一个 UIApplication（或则其子类）的一个实例。在程序开始运行的时候，UIApplicationMain 函数是程序进入点，这个函数做了很多工作，其中一个重要的工作就是创建一个 UIApplication 的单例实例。在你的代码中你，你可以通过调用 [UIApplication sharedApplication] 来得到这个单例实例的指针。

UIApplication 的一个主要工作是处理用户事件，它会起一个队列，把所有用户事件都放入队列，逐个处理，在处理的时候，它会发送当前事件 到一个合适的处理事件的目标控件。此外，UIApplication 实例还维护一个在本应用中打开的 window 列表（UIWindow 实例），这样它就 可以接触应用中的任何一个 UIView 对象。UIApplication 实例会被赋予一个代理对象，以处理应用程序的生命周期事件（比如程序启动和关闭）、系统事件（比如来电、记事项警告）等等。

一个 UIApplication 可以有如下几种状态：

+ Not running（未运行）程序没启动
+ Inactive（未激活）程序在前台运行，不过没有接收到事件。在没有事件处理情况下程序通常停留在这个状态
+ Active（激活）程序在前台运行而且接收到了事件。这也是前台的一个正常的模式
+ Background（后台） 程序在后台而且能执行代码，大多数程序进入这个状态后会在在这个状态上停留一会。时间到之后会进入挂起状态 (Suspended)。有的程序经过特殊的请求后可以长期处于 Background 状态
+ Suspended（挂起）程序在后台不能执行代码。系统会自动把程序变成这个状态而且不会发出通知。当挂起时，程序还是停留在内存中的，当系统内存低时，系统就把挂起的程序清除掉，为前台程序提供更多的内存。

常见的代理方法有

1. (void)applicationWillResignActive:(UIApplication *)application
    + 说明：当应用程序将要入非活动状态执行，在此期间，应用程序不接收消息或事件，比如来电话了
2. (void)applicationDidBecomeActive:(UIApplication *)application
    + 说明：当应用程序入活动状态执行，这个刚好跟上面那个方法相反
3. (void)applicationDidEnterBackground:(UIApplication *)application
    + 说明：当程序被推送到后台的时候调用。所以要设置后台继续运行，则在这个函数里面设置即可
4. (void)applicationWillEnterForeground:(UIApplication *)application
    + 说明：当程序从后台将要重新回到前台时候调用，这个刚好跟上面的那个方法相反。
5. (void)applicationWillTerminate:(UIApplication *)application
    + 说明：当程序将要退出是被调用，通常是用来保存数据和一些退出前的清理工作。这个需要设置 UIApplicationExitsOnSuspend 的键值。
6. (void)applicationDidReceiveMemoryWarning:(UIApplication *)application
    + 说明：iPhone 设备只有有限的内存，如果为应用程序分配了太多内存操作系统会终止应用程序的运行，在终止前会执行这个方法，通常可以在这里进行内存清理工作防止程序被终止
7. (void)applicationSignificantTimeChange:(UIApplication*)application
    + 说明：当系统时间发生改变时执行
8. (void)applicationDidFinishLaunching:(UIApplication*)application
    + 说明：当程序载入后执行

### UIView

UIView 表示屏幕上的一块矩形区域，负责渲染区域的内容，并且响应该区域内发生的触摸事件。它在iOS App中占有绝对重要的地位，因为iOS中几乎所有可视化控件都是 UIView 的子类。

UIView 可以负责以下几种任务：

+ 绘制和动画
+ 布局和子视图管理
+ 事件处理

#### 视图绘制

UIView 是按需绘制的，当整个视图或者视图的一部分由于布局变化，变成可见的，系统会要求视图进行绘制。对于那些需要使用 UIKit 或者 CoreGraphics 进行自定义绘制的视图，系统会调用drawRect:方法进行绘制。

当视图内容发生变化时，需要调用setNeedsDisplay或者setNeedsDisplayInRect:方法，告诉系统该重新绘制这个视图了。调用这个方法之后，系统会在下一个绘制周期更新这个视图的内容。由于系统要等到下一个绘制周期才真正进行绘制，可以一次性对多个视图调用setNeedsDisplay，它们会同时被更新。

#### 视图的几何属性

视图有 frame，center，bounds 等几个基本几何属性，其中:

+ frame 使用的最多，其坐标位置都是相对于父视图的，可以用于确定本视图在父视图中的位置和其自身的大小
+ center 的坐标位置也是相对于父视图的，通常用于移动，旋转等动画操作
+ bounds 是相对于自身的，通常情况下就是（0,0,width,height)， bounds 的含义可以认为是当前 view 被允许绘制的范围

#### 视图的 ContentMode

视图在初次绘制完成后，系统会对绘制结果进行快照，之后尽可能地使用快照，避免重新绘制。如果视图的几何属性发生改变，系统会根据视图的 contentMode 来决定如何改变显示效果。

默认的 contentMode 是 UIViewContentModeScaleToFill ，系统会拉伸当前的快照，使其符合新的 frame 尺寸。大部分 contentMode 都会对当前的快照进行拉伸或者移动等操作。如果需要重新绘制，可以把 contentMode 设置为 UIViewContentModeRedraw，强制视图在改变大小之类的操作时调用drawRect:重绘。

#### 动画

可以以动画的形式改变视图的下面这些属性，只需要告诉系统动画开始和结束时的数值，系统会自动处理中间的过渡过程。

+ frame
+ bounds
+ center
+ transform
+ alpha
+ backgroundColor
+ contentStretch

#### 布局和子视图管理

除了提供视图本身的内容之外，一个视图也可以表现得像一个容器。当一个视图包含其他视图时，两个视图之间就创建了一个父子关系。在这个关系中子视图被称为 subView ，父视图被称为 superView 。一个视图可以保护多个子视图，它们被存放在这个视图的 subviews 数组里。添加，删除，以及操作这些子视图的相对位置的函数如下：

+ addSubview:
+ insertSubview:...
+ bringSubviewToFront:
+ sendSubviewToBack:
+ exchangeSubviewAtIndex:withSubviewAtIndex:
+ removeFromSuperview（子视图调用）

**AutoResizing 和 Constraint**

当一个视图的大小改变时，它的子视图的位置和大小也需要相应地改变。UIView 支持自动布局，也可以手动对子视图进行布局。

当下列这些事件发生时，需要进行布局操作：

+ 视图的 bounds 大小改变
+ 用户界面旋转，通常会导致根视图控制器的大小改变
+ 视图的 layer 层的 Core Animation sublayers 发生改变
+ 程序调用视图的setNeedsLayout或layoutIfNeeded方法
+ 程序调用视图 layer 的setNeedsLayout方法
+ Autoresizing

视图的autoresizesSubviews属性决定了在视图大小发生变化时，如何自动调节子视图。

可以使用的掩码如下：

+ UIViewAutoresizingNone
+ UIViewAutoresizingFlexibleHeight
+ UIViewAutoresizingFlexibleWidth
+ UIViewAutoresizingFlexibleLeftMargin
+ UIViewAutoresizingFlexibleRightMargin
+ UIViewAutoresizingFlexibleBottomMargin
+ UIViewAutoresizingFlexibleTopMargin

可以通过位运算符将它们组合起来，例如UIViewAutoresizingFlexibleHeight|UIViewAutoresizingFlexibleWidth。

**Constraint**

Constraint 是另一种用于自动布局的方法。本质上，Constraint 就是对 UIView 之间两个属性的一个约束：

    attribute1 == multiplier × attribute2 + constant

其中方程两边不一定是等于关系，也可以是大于等于之类的关系。

Constraint 比 AutoResizing 更加灵活和强大，可以实现复杂的子视图布局。

#### 事件处理

UIView 是 UIResponder 的子类，可以响应触控事件。

通常可以使用addGestureRecognizer:添加手势识别器来响应触控事件，如果需要手动处理，则按需要重载 UIView 中的下面四个函数：

+ touchesBegan:withEvent:
+ touchesMoved:withEvent:
+ touchesEnded:withEvent:
+ touchesCancelled:withEvent:

### UIViewController

UIViewController（视图控制器），顾名思义，是 MVC 设计模式中的控制器部分。UIViewController 在 UIKit 中主要功能是用于控制画面的切换，其中的 view 属性（UIView 类型）管理整个画面的外观。

#### UIViewController 生命周期

假设现在有一个 AViewController(简称 Avc) 和 BViewController (简称 Bvc)，通过 navigationController 的 push 实现 Avc 到 Bvc 的跳转，下面是各个方法的执行执行顺序：

    1. A viewDidLoad
    2. A viewWillAppear
    3. A viewDidAppear
    4. B viewDidLoad
    5. A viewWillDisappear
    6. B viewWillAppear
    7. A viewDidDisappear
    8. B viewDidAppear

如果再从 Bvc 跳回 Avc，会产生下面的执行顺序：

    1. B viewWillDisappear
    2. A viewWillAppear
    3. B viewDidDisappear
    4. A viewDidAppear

可见 viewDidLoad 只会调用一次，再第二次跳回 Avc 的时候，AViewController 仍然存在于内存中，也就不需要 load 了。

### Core Animation

注：示例中部分代码的完整版可以在[这里](https://github.com/yixiangboy/IOSAnimationDemo)找到。

#### UIView Animation

**简单动画**

对于 UIView 上简单的动画，iOS 提供了很方便的函数：

    + animateWithDuration:animations:

第一个参数是动画的持续时间，第二个参数是一个 block，在 animations block 中对 UIView 的属性进行调整，设置 UIView 动画结束后最终的效果，iOS 就会自动补充中间帧，形成动画。

可以更改的属性有:

+ frame
+ bounds
+ center
+ transform
+ alpha
+ backgroundColor
+ contentStretch

这些属性大都是 View 的基本属性，下面是一个例子，这个例子中的动画会同时改变 View 的 frame，backgroundColor 和 alpha ：

```
[UIView animateWithDuration:2.0 animations:^{
    myView.frame = CGRectMake(50, 200, 200, 200);
    myView.backgroundColor = [UIColor blueColor];
    myView.alpha = 0.7;
}];
```

其中有一个比较特殊的 transform 属性，它的类型是 CGAffineTransform，即 2D 仿射变换，这是个数学中的概念，用一个三维矩阵来表述 2D 图形的矢量变换。用 transform 属性对 View 进行：

+ 旋转
+ 缩放
+ 其他自定义 2D 变换

iOS 提供了下面的函数可以创建简单的 2D 变换：

+ CGAffineTransformMakeScale
+ CGAffineTransformMakeRotation
+ CGAffineTransformMakeTranslation

例如下面的代码会将 View 缩小至原来的 1/4 大小：

[UIView animateWithDuration:2.0 animations:^{
    myView.transform = CGAffineTransformMakeScale(0.5, 0.5);
}];

**调节参数**

完整版的 animate 函数其实是这样的：

+ animateWithDuration:delay:options:animations:completion:
可以通过 delay 参数调节让动画延迟产生，同时还一个 options 选项可以调节动画进行的方式。可用的 options 可分为两类：

*控制过程*

例如 UIViewAnimationOptionRepeat 可以让动画反复进行， UIViewAnimationOptionAllowUserInteraction 可以让允许用户对动画进行过程中同 View 进行交互（默认是不允许的）

*控制速度*

动画的进行速度可以用速度曲线来表示（参考[这里](http://zhuanlan.zhihu.com/cheerfox/20031427#!)），提供的选项例如 UIViewAnimationOptionCurveEaseIn 是先慢后快，UIViewAnimationOptionCurveEaseOut 是先快后慢。

不同的选项直接可以通过“与”操作进行合并，同时使用，例如:

    UIViewAnimationOptionRepeat | UIViewAnimationOptionAllowUserInteraction

**关键帧动画**

上面介绍的动画中，我们只能控制开始和结束时的效果，然后由系统补全中间的过程，有些时候我们需要自己设定若干关键帧，实现更复杂的动画效果，这时候就需要关键帧动画的支持了。下面是一个示例：

```
[UIView animateKeyframesWithDuration:2.0 delay:0.0 options:UIViewKeyframeAnimationOptionRepeat | UIViewKeyframeAnimationOptionAutoreverse animations:^{
    [UIView addKeyframeWithRelativeStartTime:0.0 relativeDuration:0.5 animations:^{
        self.myView.frame = CGRectMake(10, 50, 100, 100);
    }];
    [UIView addKeyframeWithRelativeStartTime: 0.5 relativeDuration:0.3 animations:^{
        self.myView.frame = CGRectMake(20, 100, 100, 100);
    }];
    [UIView addKeyframeWithRelativeStartTime:0.8 relativeDuration:0.2 animations:^{
        self.myView.transform = CGAffineTransformMakeScale(0.5, 0.5);
    }];
} completion:nil];
```

这个例子添加了三个关键帧，在外面的 animateKeyframesWithDuration 中我们设置了持续时间为 2.0 秒，这是真实意义上的时间，里面的 startTime 和 relativeDuration 都是相对时间。以第一个为例，startTime 为 0.0，relativeTime 为 0.5，这个动画会直接开始，持续时间为 2.0 X 0.5 = 1.0 秒，下面第二个的开始时间是 0.5，正好承接上一个结束，第三个同理，这样三个动画就变成连续的动画了。

**View 的转换**

iOS 还提供了两个函数，用于进行两个 View 之间通过动画换场：

+ transitionWithView:duration:options:animations:completion:
+ transitionFromView:toView:duration:options:completion:
需要注意的是，换场动画会在这两个 View 共同的父 View 上进行，在写动画之前，先要设计好 View 的继承结构。

同样，View 之间的转换也有很多选项可选，例如 UIViewAnimationOptionTransitionFlipFromLeft 从左边翻转，UIViewAnimationOptionTransitionCrossDissolve 渐变等等。

#### CALayer Animation

UIView 的动画简单易用，但是能实现的效果相对有限，上面介绍的 UIView 的几种动画方式，实际上是对底层 CALayer 动画的一种封装。直接使用 CALayer 层的动画方法可以实现更多高级的动画效果。

注意：使用 CALayer 动画之前，首先需要引入 QuartzCore.framework。

**基本动画（CABasicAnimation）**

CABasicAnimation 用于创建一个 CALayer 上的基本动画效果，下面是一个例子：

```
CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"position.x"];
animation.toValue = @200;
animation.duration = 0.8;
animation.repeatCount = 5;
animation.beginTime = CACurrentMediaTime() + 0.5;
animation.fillMode = kCAFillModeRemoved;
[self.myView.layer addAnimation:animation forKey:nil];
```

**KeyPath**

这里我们使用了 animationWithKeyPath 这个方法来改变 layer 的属性，可以使用的属性有很多，具体可以参考这里和这里。其中很多属性在前面介绍的 UIView 动画部分我们也看到过，进一步验证了 UIView 的动画方法是对底层 CALayer 的一种封装。

需要注意的一点是，上面我们使用了 position 属性， layer 的这个 position 属性和 View 的 frame 以及 bounds 属性都不相同，而是和 Layer 的 anchorPoint 有关，可以由下面的公式计算得到：

```
position.x = frame.origin.x + 0.5 * bounds.size.width；
position.y = frame.origin.y + 0.5 * bounds.size.height；
```

关于 anchorPoint 和 position 属性的以及具体计算的原理可以参考[这篇文章](http://wonderffee.github.io/blog/2013/10/13/understand-anchorpoint-and-position/)。

*属性*

CABasicAnimation 的属性有下面几个：

+ beginTime
+ duration
+ fromValue
+ toValue
+ byValue
+ repeatCount
+ autoreverses
+ timingFunction

可以看到，其中 beginTime，duration，repeatCount 等属性和上面在 UIView 中使用到的 duration，UIViewAnimationOptionRepeat 等选项是相对应的，不过这里的选项能够提供更多的扩展性。

需要注意的是 fromValue，toValue，byValue 这几个选项，支持的设置模式有下面几种：

+ 设置 fromValue 和 toValue：从 fromValue 变化到 toValue
+ 设置 fromValue 和 byValue：从 fromValue 变化到 fromValue + byValue
+ 设置 byValue 和 toValue：从 toValue - byValue 变化到 toValue
+ 设置 fromValue： 从 fromValue 变化到属性当前值
+ 设置 toValue：从属性当前值变化到 toValue
+ 设置 byValue：从属性当前值变化到属性当前值 + toValue

看起来挺复杂，其实概括起来基本就是，如果某个值不设置，就是用这个属性当前的值。

另外，可以看到上面我们使用的:

    animation.toValue = @200;

而不是直接使用 200，因为 toValue 之类的属性为 id 类型，或者像这样使用 @ 符号，或者使用：

    animation.toValue = [NSNumber numberWithInt:200];

最后一个比较有意思的是 timingFunction 属性，使用这个属性可以自定义动画的运动曲线（节奏，pacing），系统提供了五种值可以选择：

+ kCAMediaTimingFunctionLinear 线性动画
+ kCAMediaTimingFunctionEaseIn 先快后慢
+ kCAMediaTimingFunctionEaseOut 先慢后快
+ kCAMediaTimingFunctionEaseInEaseOut 先慢后快再慢
+ kCAMediaTimingFunctionDefault 默认，也属于中间比较快

此外，我们还可以使用 [CAMediaTimingFunction functionWithControlPoints] 方法来自定义运动曲线，这个网站提供了一个将参数调节可视化的效果，关于动画时间系统的具体介绍可以参考这篇文章。

#### 关键帧动画（CAKeyframeAnimation）

同 UIView 中的类似，CALayer 层也提供了关键帧动画的支持，CAKeyFrameAnimation 和 CABasicAnimation 都继承自 CAPropertyAnimation，因此它有具有上面提到的那些属性，此外，CAKeyFrameAnimation 还有特有的几个属性。

**values 和 keyTimes**

使用 values 和 keyTimes 可以共同确定一个动画的若干关键帧，示例代码如下：

```
CAKeyframeAnimation *anima = [CAKeyframeAnimation animationWithKeyPath:@"transform.rotation"];//在这里@"transform.rotation"==@"transform.rotation.z"
NSValue *value1 = [NSNumber numberWithFloat:-M_PI/180*4];
NSValue *value2 = [NSNumber numberWithFloat:M_PI/180*4];
NSValue *value3 = [NSNumber numberWithFloat:-M_PI/180*4];
anima.values = @[value1,value2,value3];
// anima.keyTimes = @[@0.0, @0.5, @1.0];
anima.repeatCount = MAXFLOAT;

[_demoView.layer addAnimation:anima forKey:@"shakeAnimation"];
```

可以看到上面这个动画共有三个关键帧，如果没有指定 keyTimes 则各个关键帧会平分整个动画的时间(duration)。

**path**

使用 path 属性可以设置一个动画的运动路径，注意 path 只对 CALayer 的 anchorPoint 和position 属性起作用，另外如果你设置了 path ，那么 values 将被忽略。

```
CAKeyframeAnimation *anima = [CAKeyframeAnimation animationWithKeyPath:@"position"];
UIBezierPath *path = [UIBezierPath bezierPathWithOvalInRect:CGRectMake(SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-100, 200, 200)];
anima.path = path.CGPath;
anima.duration = 2.0f;
[_demoView.layer addAnimation:anima forKey:@"pathAnimation"];
```

#### 组动画（CAAnimationGroup)

组动画可以将一组动画组合在一起，所有动画对象可以同时运行，示例代码如下：

```
CAAnimationGroup *group = [[CAAnimationGroup alloc] init];
CABasicAnimation *animationOne = [CABasicAnimation animationWithKeyPath:@"transform.scale"];

animationOne.toValue = @2.0;
animationOne.duration = 1.0;

CABasicAnimation *animationTwo = [CABasicAnimation animationWithKeyPath:@"position.x"];
animationTwo.toValue = @400;
animationTwo.duration = 1.0;

[group setAnimations:@[animationOne, animationTwo]];
[self.myView.layer addAnimation:group forKey:nil];
```

需要注意的是，一个 group 组内的某个动画的持续时间（duration），如果超过了整个组的动画持续时间，那么多出的动画时间将不会被展示。例如一个 group 的持续时间是 5s，而组内一个动画持续时间为 10s ，那么这个 10s 的动画只会展示前 5s 。

#### 切换动画（CATransition）

CATransition 可以用于 View 或 ViewController 直接的换场动画：

```
self.myView.backgroundColor = [UIColor blueColor];
CATransition *trans = [CATransition animation];
trans.duration = 1.0;
trans.type = @"push";

[self.myView.layer addAnimation:trans forKey:nil];

// 这句放在下面也可以
// self.myView.backgroundColor = [UIColor blueColor];
```
为什么改变颜色放在前后都可以呢？具体的解释可以参考 SO 上的这个回答。简单来说就是动画和绘制之间并不冲突。

#### 更高级的动画效果

**CADisplayLink**

CADisplayLink 是一个计时器对象，可以周期性的调用某个 selecor 方法。相比 NSTimer ，它可以让我们以和屏幕刷新率同步的频率（每秒60次）来调用绘制函数，实现界面连续的不停重绘，从而实现动画效果。

示例代码（修改自[这里](http://www.cocoachina.com/ios/20150320/11382.html))：

```
#import "BlockView.h"

@implementation BlockView

- (void)startAnimationFrom:(CGFloat)from To:(CGFloat)to
{
    self.from = from;
    self.to = to;
    if (self.displayLink == nil) {
        self.displayLink = [CADisplayLink displayLinkWithTarget:self selector:@selector(tick:)];
        [self.displayLink addToRunLoop:[NSRunLoop currentRunLoop]
                               forMode:NSDefaultRunLoopMode];
    }
}

// 重复调用这个方法以重绘整个 View
- (void)tick:(CADisplayLink *)displayLink
{
    [self setNeedsDisplay];
}

- (void)endAnimation
{
    [self.displayLink invalidate];
    self.displayLink = nil;
}

- (void)drawRect:(CGRect)rect
{
    CALayer *layer = self.layer.presentationLayer;
    CGFloat progress = 1 - (layer.position.y - self.to) / (self.from - self.to);
    CGFloat height = CGRectGetHeight(rect);
    CGFloat deltaHeight = height / 2 * (0.5 - fabs(progress - 0.5));
    CGPoint topLeft = CGPointMake(0, deltaHeight);
    CGPoint topRight = CGPointMake(CGRectGetWidth(rect), deltaHeight);
    CGPoint bottomLeft = CGPointMake(0, height);
    CGPoint bottomRight = CGPointMake(CGRectGetWidth(rect), height);
    UIBezierPath* path = [UIBezierPath bezierPath];
    [[UIColor blueColor] setFill];
    [path moveToPoint:topLeft];
    [path addQuadCurveToPoint:topRight controlPoint:CGPointMake(CGRectGetMidX(rect), 0)];
    [path addLineToPoint:bottomRight];
    [path addQuadCurveToPoint:bottomLeft controlPoint:CGPointMake(CGRectGetMidX(rect), height - deltaHeight)];
    [path closePath];
    [path fill];
}

@end
```

**UIDynamicAnimator**

UIDynamicAnimator 是 iOS 7 引入的一个新类，可以创建出具有物理仿真效果的动画，具体提供了下面几种物理仿真行为：

+ UIGravityBehavior：重力行为
+ UICollisionBehavior：碰撞行为
+ UISnapBehavior：捕捉行为
+ UIPushBehavior：推动行为
+ UIAttachmentBehavior：附着行为
+ UIDynamicItemBehavior：动力元素行为

示例代码如下（来自[这里](http://www.teehanlax.com/blog/introduction-to-uikit-dynamics/))

```
self.animator = [[UIDynamicAnimator alloc] initWithReferenceView:self.view];

UIGravityBehavior* gravityBehavior = [[UIGravityBehavior alloc] initWithItems:@[self.myView]];
[self.animator addBehavior:gravityBehavior];

UICollisionBehavior* collisionBehavior = [[UICollisionBehavior alloc] initWithItems:@[self.myView]];
collisionBehavior.translatesReferenceBoundsIntoBoundary = YES;
[self.animator addBehavior:collisionBehavior];
```

可以发现这段代码和我们之前写的动画代码有很大不同，在这里 behavior 是用于控制 View 行为的，我们做的操作是把各种不同的 behavior 加到 animator 中。这段代码实现了 View 因为“重力”原因“掉到”地上，落地的同时还有一个碰撞效果。

**CAEmitterLayer**

CAEmitterLayer 是 Core Animation 提供的一个粒子发生器系统，可以用于创建各种粒子动画，例如烟雾，焰火等效果。

CAEmitterLayer 需要调节的参数很多，可以实现的效果也非常炫酷，具体可参考下面几个网址：

+ http://enharmonichq.com/tutorial-particle-systems-in-core-animation-with-caemitterlayer/#prettyPhoto/0/
+ https://www.invasivecode.com/weblog/caemitterlayer-and-the-ios-particle-system-lets/?doing_wp_cron=1438657800.4759559631347656250000

LTMorphingLabel 这个项目使用 CAEmitterLayer 实现了各种高端炫酷掉渣天的效果，大家想学习的话可以去看看它的代码。

## 面试问题

https://github.com/ChenYilong/iOSInterviewQuestions

http://draveness.me/guan-yu-xie-ios-wen-ti-de-jie-da/

https://github.com/lzyy/iOS-Developer-Interview-Questions

## 更多资料

更多学习资料：

+ https://github.com/100mango/zen
+ http://objccn.io/
+ http://nshipster.cn
+ https://github.com/oa414/objc-zen-book-cn
+ https://github.com/nixzhu/dev-blog
+ https://github.com/robovm/apple-ios-samples （苹果官方 Sample 代码集合）
+ https://github.com/leecade/ios-dev-flow （开发流程总结）
+ https://github.com/DaiYue/iOS-good-practices-in-Chinese （iOS 最佳实践）
+ https://github.com/tangqiaoboy/iOSBlogCN （iOS 开发博客列表）
+ https://github.com/Aufree/trip-to-iOS （iOS 学习资料整理）
+ http://www.hrchen.com/2013/05/performance-with-instruments/ (iOS 性能优化）
+ https://github.com/huang303513/iOS-Study-Demo

常用的库总结：

+ https://github.com/Tim9Liu9/TimLiu-iOS
+ https://github.com/vsouza/awesome-ios
+ https://github.com/cjwirth/awesome-ios-ui


