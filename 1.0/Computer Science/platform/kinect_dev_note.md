# Kinect 应用开发实战

## Kinect的核心 NUI API

初始化及使用的方法

	步骤一：获得Kinect实例
	KinectSensor sensor = (from sensorToCheck inKinectSensor.KinectSensors where sensorToCheck.Status == KinectStatus.Connected select sensorToCheck).FirstOrDefault();
	
	以上为LINQ查询表达式，一般的语法
	foreach(KinectSensor kinect in KinectSensor.KinectSensors)
	{
		if (kinect.Status == KinectStatus.Connected)
		{
			kinectSensor = kinect;
			break;
		}
	}
	
	步骤二：调用KinectSensor.Start方法初始化并启动Kinect传感器
	
	步骤三：注册相关事件，如视频流或深度数据到来的事件、骨骼跟踪事件，并基于这些时间调用SDK提供的相关API进行处理
	
	KinectSensor.ColorFrameReady
	KinectSensor.DepthFrameReady
	KinectSensor.SkeletonFrameReady
	KinectSensor.AllFrameReady
	
	步骤四：调用KinectSensor.Stop方法关闭Kinect传感器
	
初始化选项，必须在初始化中设定，否则将无法使用
	
+ 色彩：来自传感器的彩色图像数据
+ 深度：来自传感器的深度图像数据
+ 深度和用户编号
+ 骨骼跟踪

## 数据流概述

可以设置两种不同质量水平及不同编码格式的彩色图像数据：

+ 图像质量高低将影响到Kinect传感器与计算机之间的传输速率
+ 应用程序可以设定彩色图像的编码格式，包括`RGB`、`YUV`两种

通常情况下，在传感器传输到计算机前，Bayer格式1280x1024的原始图像数据被压缩成RGB格式，传输速率可达到30帧每秒，但该算法有可能导致部分图像失真。如果要获取高质量未经压缩的数据，那么传送速率就不能超过15帧每秒。

#### Bayer数据

根据人眼对彩色响应带的宽度不大，着色面积却较大的特点，每个像素没有必要同时输出3种颜色。奇数扫描行输出RGRGRG...，偶数扫描行暑促GBGBGB...。实际处理时，每个像素RGB信号由像素本身输出的某一种颜色信号和相邻像素输出的其他颜色信号构成。这种采样方式在基本不降低图像质量的同时，可以将采样频率降低60%以上

Kinect提供两种彩色图像格式

1. RGB color 提供32bit, linear X8R8G8-formatted color位图
2. YUV color 提供16bit, linear UYVY-formatted color位图

#### 用户分割数据

在视野范围内，Kinect支持同时对两个用户进行识别和骨骼跟踪。骨骼跟踪的第一步是将用户从背景图像中分离出来。在Kinect SDK中，通过低3位字节的索引，应用程序可以将用户从整个深度数据中剥离出来，称为用户分割数据，它属于深度数据的一部分：

+ 深度图像的每个像素有2字节，共16位组成；
+ 每个像素的高13位代表从Kinect红外摄像头到最近物体对象的距离，以毫米为单位；
+ 低三位字节表示被跟踪的用户索引编号，这3位字节会被转换为整数值类型（0-7），并不作标志位

用户编号为0表示没有找到用户。Kinect SDK为用户索引定义了一些列常量，分别是：

+ DepthImageFrame.PlayerIndexBitmaskWidth（实际值为3）
+ DepthImageFrame.PlayerIndexBitmask（实际值为7，用于位运算）

#### 深度图像数据

深度数据流由深度图像帧组成。在某个深度图像帧中，每一个像素点包含了特定的距离信息——从Kinect红外摄像头的视角来看，该特定的(x,y)点坐标处离摄像头平面最近的物体到该平面的距离。可以通过`DepthImageStream.DepthRange`枚举类型了解当前摄像头的工作模式，在默认模式和近景模式下的有效可视范围是不同的，在`DepthImageStream`类的如下属性中定义：

+ TooFarDepth：获取深度值有效范围的最大值
+ TooNearDepth：获取深度值有效范围的最小值
+ UnknownDepth：位置深度距离的数值

使用`DepthImageStream.DepthImageFormat`来选择数据格式，有如下分辨率的深度数据流可以选择：

+ 分辨率640x480 DepthImageFormat.Resolution640x480Fps30
+ 分辨率320x240 DepthImageFormat.Resolution320x240Fps30
+ 分辨率80x60 DepthImageFormat.Resolution80x60Fps30

深度图像中的每个像素为16位，定义一个short数据来存储深度图像，代码如下：

	short[] depthPixelData = new short[depthFrame.PixelDataLength];
	depthFrame.CopyPixelDataTo(depthPixelData);
	
	Int32 pixelIndex = (Int32)(p.X + ((Int32)p.Y * depthFrame.Width));

对于深度图像中的某个点p(X, Y)，`depthFrame.Width`为深度图像宽度。通过位运算来计算某个像素所表达的目标物体与Kinect的距离：

	Int32 depth = depthPixelData[pixelIndex] >> DepthImageFrame.PlayerIndexBitmaskWidth;
	
### 如何获取数据流

有两种模式获取数据流：轮询模型和事件模型。应用程序可以同时灵活选择采用何种数据获取模式，比如使用事件方式获取`ColorImageStream`产生的数据，同时采用轮询模式从`SkeletonStream`流获取数据。但不能对同一数据流同时使用这两种模式。

事件模型对编程而言更为优雅，轮询模式获取数据实现起来要更为复杂。但在某些场景下，例如XNA开发环境，只能采用轮询模型。

#### 轮询模式(Polling Model)

最简单的读取帧数据的方法。首先开启图像数据流，然后请求帧数据并设置等待时间为T，单位为毫秒；如果帧数据尚未就绪，则系统将等待T时间后返回。如果帧数据成功返回，则应用程序课请求下一帧数据，并在同一线程执行其他操作。各种图像帧的请求方法如下：

+ 彩色图像帧：ColorImageStream.OpenNextFrame(T)
+ 深度图像帧：DepthImageStream.OpenNextFrame(T)
+ 骨骼数据帧：SkeletonStream.OpenNextFrame(T)

#### 事件模型(Event Model)

应用程序注册数据流的`FrameReady`事件，每当时间触发时，会调用事件的属性`FrameReadyEventArgs`来获取数据帧。例如，在使用深度数据流时，方法调用`DepthImageFrameReadyEventArgs`对象的`OpenDepthImageFrame`方法，获取`DepthImageFrame`对象。程序应该检测获取的`DepthImageFrame`对象是否为空，因为有可能在某些情况下，虽然事件触发了，但是没有产生数据帧。除此之外，事件模型不需要其他的检查和异常处理。

	获取彩色图像帧数据流
	void sensor_ColorFrameReady(object sender, ColorImageFrameReadyEventArgs e)
	{
		ColorImageFrame colorFrame = e.OpenColorImageFrame();
	}
	
	获取深度图像帧数据流
	void sensor_DepthFrameReady(object sender, DepthImageFrameReadyEventArgs e)
	{
		DepthImageFrame depthFrame = e.OpenDepthImageFrame();
	}
	
	获取骨骼数据帧数据流
	void sensor_SkeletonFrameReady(object sender, SkeletonFrameReadyEventArgs e)
	{
		SkeletonFrameskeletonFrame = e.OpenSkeletonFrame();
	}
	
	三种数据帧同步获取
	void sensor_AllFramesReady(object sender, AllFramesReadyEventArgs e)
	{
		ColorImageFrame colorFrame = e.OpenColorImageFrame();
		DepthImageFrame depthFrame = e.OpenDepthImageFrame();
		SkeletonFrameskeletonFrame = e.OpenSkeletonFrame();
	}


#### 骨骼跟踪

全身有20个骨骼支点，具体可以参考网络图片和示例。头部、手部都只有一个点，意味着通过骨骼追踪，无法区分手指，也无法分辨出人脸的朝向。

启用主动跟踪时，可以通过调用相关API获得完整的下一组骨骼数据。如果是被动跟踪，可以提供额外4个用户有限的位置信息（该用户的中心位置）。默认情况下，最先被捕捉的两个用户将被启用主动跟踪。


## NUI坐标转换

Kinect SDK NUI API中包含彩色图像二维坐标、深度图像空间坐标、骨骼跟踪空间坐标。对于Kinect视野范围中的一个点，在这三个坐标系的坐标和度量并不一致，通过NUI坐标转换，将人体深度图像空间坐标映射为骨骼空间坐标。

Kinect SDK提供了相关的API做相关转换，并且定义了`ColorImagePoint`、`SkeletonPoint`、`DepthImagePoint`三种点类型。在核心类`KinectSensor`中提供了相关转换方法，主要有

+ MapDepthToColorImagePoint
+ MapDepthToSkeletonPoint
+ MapSkeletonPointToColor
+ MapSkeletonPointToDepth

一般应用场景，包括从骨骼关节点坐标，包括从骨骼关节点坐标映射到彩色图像或深度图像坐标中，或者从深度图像的某点映射到彩色图像或骨骼空间坐标。在深度图像帧的`DepthImageFrame`类也有3个坐标映射方法：

+ MapFromSkeletonPoint 将骨骼关节点坐标映射为深度图像点坐标
+ MapToColorImagePoint 将深度图像中的某点坐标映射为同步对应的彩色图像帧的点坐标
+ MapToSkeletonPoint 将深度图像中的某点坐标映射为同步对应的骨骼数据帧的点坐标

Kinect SDK的核心类kinectSensor有4个方法完成深度图像坐标系、骨骼跟踪坐标系和彩色图像坐标系之间的转换：

+ MapDepthToSkeletonPoint: 深度图像坐标系->骨骼跟踪坐标系
+ MapSkeletonPointToDepth: 骨骼跟踪坐标系->深度图像坐标系
+ MapDepthToColorImagePoint: 深度图像坐标系->彩色图像坐标系
+ MapSkeletonPointToColor: 骨骼跟踪坐标系->彩色图像坐标系

每个骨骼帧包括一个平面向量和一个计算平面方程的系数。骨骼跟踪系统会更新每个帧的“用户背景”和“用户分割数据”。通常来说，地面可能并不总是可用的。在这种情况下，以SDK预测的“地面截面”作为一个零向量。“地面截面”可以在`SkeletonFrame.FloorClipPlane`属性中获得。


## Kinect用户交互设计的若干思考

Xbox360的Kinect Hub有了一种简单且易理解的控制方式——`悬停选择`和`翻页控制`。

#### 关节点重叠的处理方法

考虑到玩家的不同站姿会带来多个关节点接近或重叠的情况，这样Kinect就很难检测到玩家的动作。Kinect游戏《十项全能》中的射箭运动给出了经典的解决方案：利用游戏画面引导玩家做出最佳角度的姿势。

#### Kinect体感操作局限性及解决方案

Kinect体感操作局限性 | 解决方案
-- | --
视野范围有限，超出后无法全身骨骼追踪 | 系统予以提示，要求用户回到可视范围中
无法判断人体的正面或反面 | 用多个Kinect组合使用，深度图像合成3D图像
骨骼关节节点重叠时动作识别困难，或容易产生噪声数据 | 重新设计体感动作；通过相邻点进行推测
现有Kinect分辨率过低，如手指识别精度不够 | 新一代Kinect硬件水平的提高
空气中操作，没有触感 | 界面配合音乐及动画反馈
无法即时执行“确定”、“取消”等动作 | 通过“悬停控制”实现确定；通过特定姿势实现取消
目标操作精度不够 | 合理布局界面，采用Metro风格
动作幅度大，容易疲劳 | 合理定义手势。非游戏类的手势操作，要求幅度和运动范围尽可能小。注重“体感操作”的人体工程学
用户无意识的动作会干扰动作识别 | 重新定义手势，避免与人类自然手势冲突

### Kinect体感操作交互设计的七条军规

#### 军规一：控制手势集符合人类自然手势

最简单常用的手势包括：用挥手来获得控制焦点；悬停控制来执行“确定”；双手手掌“靠近、伸展”来代表“放大、缩小”等。

控制手势集的每个动作/姿势都要保证“正交”，可以通过动作/姿势的进一步组合来扩展命令。此外，动作识别要对用户自然的走动及日常肢体语言保持“迟钝”，对于捕捉到的用户无意动作，应做适当的过滤处理，避免“非预期”的手势识别。

#### 军规二：让用户的肢体移动幅度尽可能小

短距离滑动，Maya-Like Menu

#### 军规三：操作界面的对象采用Metro风格

光滑、快、现代。各个控制模块保持合理的间距，并可以采用“磁石效应”按钮，这样可以极大方便用户操作。

#### 军规四：“确认操作”保持简单、一致

Kinect体感应用程序可以采用悬停选择(Hover Button)、滑动解锁(Slide Swipping)和手掌前推(Push Button)来进行确认操作，建议在应用程序中选择其中之一，并在所有交互界面中保持一致。

#### 军规五：手势操作尽可能在同一个平面内

不在同一平面的手势操作会带来更多的实现复杂度，识别率也会因此降低。聋哑人手语识别的一大难点也在于此。

#### 军规六：从三维的视角去看交互设计

有些时候在X-Y平面不好判断的动作，在Y-Z平面情况就不一样了。

#### 军规七：配有简单明了的手势说明

这个不用多说了，要教会用户如何使用。