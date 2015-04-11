  

iOS实现图形编程可以使用三种API（UIKIT、CoreGraphics、OpenGL ES及GLKit）。  
  
这些api包含的绘制操作都在一个图形环境中进行绘制。一个图形环境包含绘制参数和所有的绘制需要的设备特定信息，包括屏幕图形环境、offscreen 位图环境和
PDF图形环境，用来在屏幕表面、一个位图或一个pdf文件中进行图形和图像绘制。在屏幕图形环境中进行的绘制限定于在一个UIView类或其子类的实例中绘制，并直
接在屏幕显示，在offscreen位图或PDF图形环境中进行的绘制不直接在屏幕上显示。  
  
**一、UIKIT API **  
  
UIKIT是一组Objective-C API，为线条图形、Quartz图像和颜色操作提供Objective-C
封装，并提供2D绘制、图像处理及用户接口级别的动画。  
  
UIKIT包括UIBezierPath（绘制线、角度、椭圆及其它图形）、UIImage（显示图像）、UIColor（颜色操作）、UIFont和UIScree
n（提供字体和屏幕信息）等类以及在位图图形环境、PDF图形环境上进行绘制和操作的功能等, 也提供对标准视图的支持，也提供对打印功能的支持。  
  
在UIKIT中UIView类本身在绘制时自动创建一个图形环境（对应Core
Graphics层的CGContext类型）作为当前的图形绘制环境。在绘制时可以调用UIGraphicsGetCurrentContext
函数获得当前的图形环境。  
  
**二、Core Graphics 与Quartz 2D API **  
  
CoreGraphics是一套C-based API， 支持向量图形，线、形状、图案、路径、剃度、位图图像和pdf 内容的绘制。  
  
Quartz2D 是Core Graphics中的2D绘制呈现引擎。Quartz是资源和设备无关的,提供路径绘制，anti-
aliased呈现，剃度填充图案，图像，透明绘制和透明层、遮蔽和阴影、颜色管理，坐标转换，字体、offscreen呈现、pdf文档创建、显示和分析等功能。  
  
Quartz2D能够与所有的图形和动画技术（如Core Animation, OpenGLES, 和 UIKit 等）一起使用。  
  
Quartz采用paint模式进行绘制。  
  
Quartz中使用的图形环境也由一个类CGContext表示。  
  
在Quartz 中可以把一个图形环境作为一个绘制目标。当使用Quartz 进行绘制时，所有设备特定的特性被包含在你使用的特定类型的图形环境中，因此通过给相同
的图像操作函数提供不同的图像环境你就能够画相同的图像到不同的设备上，因此做到了图像绘制的设备无关性。  
  
Quartz为应用提供如下几个图形环境：  
  
1）位图图形环境，用来创建一个位图。  
  
使用函数CGBitmapContextCreate来创建。  
  
2）PDF图形环境，用来创建一个pdf文件。  
  
Quartz2D API提供了两个函数来创建一个PDF图形环境：  
  
CGPDFContextCreateWithURL，带有一个作为pdf 输出的位置的Core Foundation URL来创建一个pdf 图形环境。  
  
CGPDFContextCreate,当想PDF 输出到一个data consumer时使用该函数。  
  
3） 窗口图形环境，用来在一个窗口上进行绘制。  
  
4） 层环境（CGLayer) ，是一个与另一个图形环境关联的offscreen绘制目标，使用层环境的目的是为了优化绘制层到创建它的图形环境的性能。层环境能
够比位图图形环境提供更好的offscreen绘制性能。  
  
Quartz提供的主要类包括：  
  
CGContext：表示一个图形环境；  
  
CGPath：使用向量图形来创建路径，并能够填充和stroke；  
  
CGImage：用来表示位图；  
  
CGLayer：用来表示一个能够用于重复绘制和offscreen绘制的绘制层；  
  
CGPattern：用来表示Pattern，用于重复绘制；  
  
CGShading和 CGGradient：用于绘制剃度；  
  
CGColor和 CGColorSpace:用来进行颜色和颜色空间管理；  
  
CGFont：用于绘制文本；  
  
CGPDFContentStream、CGPDFScanner、CGPDFPage、CGPDFObject,CGPDFStream,
CGPDFString等用来进行pdf文件的创建、解析和显示。  
  
**三、OpenGL ES和GLKit **  
  
OpenGLES是一套多功能开放标准的用于嵌入系统的C-based的图形库，用于2D和3D数据的可视化。OpenGL被设计用来转换一组图形调用功能到底层图形
硬件（GPU），由GPU执行图形命令，用来实现复杂的图形操作和运算，从而能够高性能、高帧率利用GPU提供的2D和3D绘制能力。  
  
OpenGLES规范本身不定义绘制表面和绘制窗口，因此ios为了使用它必须提供和创建一个OpenGLES
的呈现环境，创建和配置存储绘制命令结果的framebuffer 及创建和配置一个或多个呈现目标。  
  
在 iOS中使用EAGL提供的EAGLContext类来实现和提供一个呈现环境，用来保持OpenGLES使用到的硬件状态。
EAGL是一个Objective-C API，提供使OpenGL ES与Core Animation和UIKIT集成的接口。  
  
在调用任何OpenGLES 功能之前必须首先初始化一个EAGLContext 对象。  
  
每一个iOS应用的每一个线程都有一个当前context，在调用OpenGLES函数时，使用或改变此context中的状态。  
  
EAGLContext的类方法setCurrentContext:用来设置当前线程的当前context。EAGLContext
的类方法currentContext
返回当前线程的当前context。在切换相同线程的两个上下文之前，必须调用glFlush函数来确保先前已提交的命令被提交到图形硬件中。  
  
可以采用不同的方式使用OpenGL ES以便呈现OpenGL ES内容到不同的目标：GLKit和CAEAGLLayer。  
  
为了创建全屏幕的视图或使OpenGL ES内容与UIKit视图集成，可以使用GLKit。在使用GLKit时，GLKit提供的类GLKView类本身实现呈现目
标及创建和维护一个framebuffer。  
  
为了使OpenGL ES内容作为一个Core Animation层的部分内容时，可以使用CAEAGLLayer
作为呈现目标，并需要另外创建framebuffer以及自己实现和控制整个绘制流程。  
  
GLKit是一组Objective-C 类，为使用OpenGL ES 提供一个面向对象接口，用来简化OpenGL
ES应用的开发。GLKit支持四个3D应用开发的关键领域：  
  
1） GLKView 和GLKViewController类提供一个标准的OpenGLES视图和相关联的呈现循环。GLKView可以作为OpenGLES内容
的呈现目标，GLKViewController提供内容呈现的控制和动画。视图管理和维护一个framebuffer，应用只需在framebuffer进行绘画即
可。  
  
2）GLKTextureLoader 为应用提供从iOS支持的各种图像格式的源自动加载纹理图像到OpenGLES
图像环境的方式，并能够进行适当的转换，并支持同步和异步加载方式。  
  
3）数学运算库，提供向量、矩阵、四元数的实现和矩阵堆栈操作等OpenGL ES 1.1功能。  
  
4）Effect效果类提供标准的公共着色效果的实现。能够配置效果和相关的顶点数据，然后创建和加载适当的着色器。GLKit
包括三个可配置着色效果类：GLKBaseEffect实现OpenGL ES 1.1规范中的关键的灯光和材料模式,
GLKSkyboxEffect提供一个skybox效果的实现, GLKReflectionMapEffect
在GLKBaseEffect基础上包括反射映射支持。  
  
使用GLKView和OpenGLES进行绘制过程：  
  
1）创建一个GLKView 对象  
  
GLKView对象可以编程或使用Interface Builder来创建和配置。  
  
在采用编程方式时，首先创建一个context然后调用initWithFrame:context:方法。  
  
使用Interface Builder方式时，在从storyboard加载一个GLKView后，创建一个context和设置它作为视图的context属性.  
  
在iOS中GLKit的使用需要创建OpenGLES 2.0以上的图形环境context。  
  
GLKit视图自动创建和配置它所有的OpenGLES
framebuffer对象和renderbuffers，可以通过修改视图的drawable属性来控制这些对象的属性。  
  
2）绘制OpenGL内容（发布绘制命令）  
  
使用GLKit视图绘制OpenGL内容需要三个子步骤：准备OpenGLES基础；发布绘制命令；呈现显示内容到Core Animation。 GLKit类本身
已经实现了第一个和第三个步骤，用户只需实现第二个步骤，在视图的方法drawRect或视图的代理对象的glkView:drawInRect:中调用适当的Ope
nGLES绘制命令进行内容绘制。  
  
GLKViewController类维护一个animation 呈现循环（包含两个方法update和display），用来实现连续的动画复杂的场景。  
  
animation呈现循环的交替速率由GLKViewController的属性framesPerSecond
指示，并使用preferredFramesPerSecond 属性来修改它。  
  
**四、其它图形编程相关API **  
  
1）Core Animation  
  
CoreAnimation是一套Objective-C
API，实现了一个高性能的复合引擎，并提供一个简单易用的编程接口，给用户UI添加平滑运动和动态反馈能力。  
  
CoreAnimation 是 UIKit实现动画和变换的基础，也负责视图的复合功能。使用Core
Animation可以实现定制动画和细粒度的动画控制，创建复杂的、支持动画和变换的layered 2D视图。  
  
CoreAnimation不属于绘制系统，但它是以硬件复合和操作显示内容的基础设施。这个基础设施的核心是layer对象，用来管理和操作显示内容。在ios
中每一个视图都对应Core Animation的一个层对象，与视图一样，层之间也组织为层关系树。一个层捕获视图内容为一个被图像硬件容易操作的位图。在多数应用
中层作为管理视图的方式使用，但也可以创建独立的层到一个层关系树中来显示视图不够支持的显示内容。  
  
OpenGLES的内容也可以与Core Animation内容进行集成。  
  
为了使用Core Animation实现动画，可以修改层的属性值来触发一个action对象的执行，不同的action对象实现不同的动画。  
  
CoreAnimation 提供了一下一组应用可以采用的类来提供对不同动画类型的支持：  
  
CAAnimation是一个抽象公共基类，CAAnimation采用CAMediaTiming
和CAAction协议为动画提供时间（如周期、速度、重复次数等）和action行为（启动、停止等）。  
  
CAPropertyAnimation是 CAAnimation的抽象子类，为动画提供一个由一个key路径规定的层属性的支持；  
  
CABasicAnimation是CAPropertyAnimation的具体子类，为一个层属性提供简单插入能力。  
  
CAKeyframeAnimation也是CAPropertyAnimation的具体子类，提供key帧动画支持。  
  
CATransition是CAAnimation的具体子类，提供影响整个层内容的事物效果。  
  
CAAnimationGroup也是CAAnimation的子类，允许动画对象组合到一起并同时运行。  
  
2）Image I/O  
  
ImageI/O
提供读写多数格式图像文件的数据的接口。主要包括图像源CGImageSourceRef和图像目标CGImageDestinationRef两个类。  
  
3）Sprite Kit  
  
SpriteKit建立于OpenGL ES之上，SpriteKit使用图形硬件来有效的呈现动画帧，因此可以高帧率地动画和呈现任意的2D纹理图像或游戏spri
te，呈现的内容包括sprites、文本、CGPath形状、视频等。  
  
在Sprite Kit中动画和呈现由一个SKView视图对象执行。游戏的内容组织为以SKScene对象表现的一个个场景。一个场景包含要呈现的sprites和
其它内容，一个场景也实现每个帧关联的逻辑和内容处理。  
  
在同一时刻，一个SKView视图只呈现一个场景，在场景呈现时，场景关联的动画和帧关联的逻辑被自动执行。在切换场景时使用SKTransition
类来执行两个场景间的动画。  
  
4）SceneKit  
  
SceneKit是一个使用3D图形技术实现的Objective-C 框架，包含一个高性能的呈现引擎和一个高级的描述性API。可以利用该框架创建简单的游戏和界
面丰富的用户UI，使用SceneKit仅需要使用描述性API描述你的场景的内容（如几何形状、材料、灯光和摄像等）和你想在那些内容上要执行的行动或动画即可。  
  
SceneKit的内容组织为由节点组成的树形结构，称为scene graph。一个场景包含一个根节点，定义场景的坐标空间，其它节点定义场景的可视内容。Sce
neKit在GPU上呈现每一帧之前在一个视图上显示场景、处理scene graph和执行动画处理。  
  
SceneKit包含的主要类：  
  
SCNView& SCNSceneRenderer：SCNView是显示或呈现SceneKit内容的视图。SCNSceneRenderer是一个协议，定义用
于视图的一些重要方法。  
  
SCNScene：
表现一个场景，是所有SceneKit内容的一个容器。场景可以从使用3D著作工具创建的一个文件中加载，也可以编程创建，场景需要在一个视图上显示。  
  
SCNNode：一个场景的基本构造块，表示scene graph树的一个节点。scene
graph树定义了场景上节点之间的逻辑结构，通过为一个节点附属geometries、lights、cameras来提供场景的可视内容。  
  
SCNGeometry、SCNLight、SCNCamera：分别是geometries、lights、cameras对应的类。SCNGeometry为场景
提供形状、文本或定制顶点数据，SCNLight为场景提供阴影效果，SCNCamera为场景提供可视点。  
  
SCNMaterial：为SCNGeometry对象定义表面外观属性，规定对象表面如何着色或纹理以及如何反应灯光。  
  
SceneKit内容的动画：  
  
SceneKit动画基于Core Animation 框架，可以隐式或显式创建。  
  
隐式创建是实际是通过动画节点的一些动画属性来实现：SceneKit自动在run
loop一次运行期间对一个场景包含节点属性的所有改变组合成一个原子操作，称为一个事务，由SCNTransaction
类表示；当设置SCNTransaction类的动画周期不为0时，所有对节点动画属性的改变自动执行动画。  
  
如下代码片段所示：

  

  1. `func fallAndFade(sender: a href=` `""` `AnyObject /a ) {`

  2. `` `SCNTransaction.setAnimationDuration(1.0)`

  3. `` `textNode.position = SCNVector3(x: 0.0, y: -10.0, z: 0.0)`

  4. `` `textNode.opacity = 0.0`

  5. `}`

  
显式创建动画时，可以选择CAAnimation一种类型的子类来创建特定类型的动画。使用key-
value为动画规定属性及设置动画参数，然后把创建的动画附属到场景的一个或多个元素。可以使用不同的Core
Animation动画类组合或序列化几个动画或创建动画在几个 keyframe值之间插入属性值。  
  
如下代码片段为显式创建动画的例子：

  

  1. `let animation = CABasicAnimation(keyPath: ` `"geometry.extrusionDepth"` `)`

  2. `` `animation.fromValue = 0.0`

  3. `` `animation.toValue = 100.0`

  4. `` `animation.duration = 1.0`

  5. `` `animation.autoreverses = ` `true`

  6. `` `animation.repeatCount = Float.infinity`

  7. `` `textNode.addAnimation(animation, forKey: “extrude")`

  
SceneKit也支持使用SCNSceneSource 类从一个场景文件中加载CAAnimation动画对象，然后附属它到SCNNode对象。  
  
5）Metal  
  
Metal框架是一个OpenGL ES类似的底层API，为GPU加速的先进的3D图形呈现或数据并行计算任务提供支持。Metal负责和3D绘图硬件交互，为图形
和计算命令的组织、处理、提交和相关资源和数据的管理提供一个细粒度的、底层的支持流式计算的现代API。Metal的目标是在执行GPU任务时尽量减少CPU的负载
，消除在GPU执行图形和数据并行计算操作时的性能瓶颈，能够有效的使用多线程并行创建和提交命令到GPU。  
  
Metal也提供了一个映射编程语言用来编写能够被Metal应用使用的图形映射或计算函数。Metal映射语言编写的代码能够在编译时与应用代码一起被编译，然后在
运行时被加载到GPU上执行；也支持运行时对Metal 映射语言代码进行编辑。  
  
在Metal架构中包括如下几个重要的类或协议：  
  
1、MTLDevice协议和对象  
  
一个MTLDevice代表一个执行命令的GPU设备，MTLDevice协议为其定义了相关接口，包括查询设备能力属性和创建其它设备特定的对象等接口，例如创建命
令队列、从内存中分配缓冲区以及创建纹理等。  
  
应用通过调用MTLCreateSystemDefaultDevice 函数来获取一个系统能够使用的MTLDevice对象。  
  
2、命令和命令编码器  
  
在Metal框架中，3D图形呈现命令、计算命令和blitting命令在提交到特定设备GPU上执行前必须进行相应的格式编码，以便能够被GPU识别和执行。  
  
Metal框架为每种命令提供了一种编码器协议：  
  
MTLRenderCommandEncoder协议：提供接口用来编码一个单次循环呈现期间要执行的3D图形呈现命令。MTLRenderCommandEncod
er 对象用来代表一次图形呈现流程的呈现状态和绘制命令。  
  
MTLComputeCommandEncoder协议：提供接口用来编码数据并行计算任务。  
  
MTLBlitCommandEncoder协议：提供接口用来编码在缓冲和纹理之间的简单拷贝操作。  
  
在同一时刻，仅能有一个命令编码器激活来添加命令到一个命令缓冲空间上，即每一个命令编码器必须在另一个使用相同命令缓冲空间的命令编码器创建前结束。  
  
Metal为了支持多个不同任务的并行执行，提供了一个MTLParallelRenderCommandEncoder协议来支持多个MTLBlitCommand
Encoder在不同线程同时运行提交不同的命令缓冲到同一个命令缓冲空间。每一个线程有一个它自己的命令缓冲对象，在同一时刻，该缓冲对象只能被该线程的一个命令编
码器存取。  
  
MTLParallelRenderCommandEncoder对象允许一次呈现循环的命令编码分解到多个命令编码器进行编码，使用多线程进行并行处理来提高处理效
率。  
  
一个命令编码器对象调用endEncoding方法来结束。  
  
命令编码器对象的创建：  
  
命令编码器对象由MTLCommandBuffer对象负责创建。MTLCommandBuffer协议定义了如下方法用来创建相应类型的命令编码器对象：  
  
renderCommandEncoderWithDescriptor:为执行图形呈现任务创建一个MTLRenderCommandEncoder 对象。方法的
参数MTLRenderPassDescriptor表现一个编码呈现命令的目标（是一个附属点的集合，最多可以包括四个颜色点数据附属点、一个深度点数据附属点、一
个图案点数据附属点），在MTLRenderPassDescriptor对象的附属点属性中指定要呈现的图形目标。  
  
computeCommandEncoder方法为数据并行计算任务创建一个MTLComputeCommandEncoder 对象。  
  
blitCommandEncoder方法为内存Blit操作和纹理填充操及mipmaps的产生等操作创建一个MTLBlitCommandEncoder 对象。  
  
parallelRenderCommandEncoderWithDescriptor:方法创建一个MTLParallelRenderCommandEncod
er对象。呈现目标由 参数MTLRenderPassDescriptor规定。  
  
3、命令缓冲MTLCommandBuffer对象及协议  
  
在经过命令编码器编码后的命令被命令编码器添加到一个称为命令缓冲的MTLCommandBuffer对象上，然后该CommandBuffer对象被提交到GPU来
执行其中包含的命令。  
  
MTLCommandBuffer协议为CommandBuffer对象定义接口以及提供命令编码器的创建、提交CommandBuffer到一个命令队列以及检查状
态等操作方法。  
  
一个CommandBuffer对象包含打算在特定设备（GPU）上执行的被编码的命令。一旦所有的编码完成，CommandBuffer本身必须提交到一个命令队列
，并标记命令缓冲为准备好状态，以便能够被GPU 执行。  
  
在标准标准应用中，通常一个呈现帧的呈现命令使用一个线程被编码进一个命令缓冲中。  
  
MTLCommandBuffer对象的创建和相应方法：  
  
一个MTLCommandBuffer对象由MTLCommandQueue的commandBuffer方法或commandBufferWithUnretain
edReferences方法创建。  
  
一个MTLCommandBuffer对象仅能提交到创建它的MTLCommandQueue 对象中。  
  
一个MTLCommandBuffer对象还实现协议定义的如下方法：  
  
enqueue方法用来在命令队列中为该命令缓冲保留一个位置。  
  
commit方法使MTLCommandBuffer对象被提交执行。  
  
addScheduledHandler:方法用来为一个命令缓冲对象登记一个在该命令缓冲被调度时被调用的代码执行块。可以为一个命令缓冲对象登记多个调度执行块。  
  
waitUntilScheduled方法等待命令缓冲被调度及在为该命令缓冲登记的所有调度执行块已经执行完。  
  
addCompletedHandler:方法为一个命令缓冲对象登记一个在设备已经执行完该命令缓冲后被调用的代码执行块。也可以为一个命令缓冲对象登记多个完成执
行代码块。  
  
waitUntilCompleted方法等待命令缓冲中命令被设备执行完和为该命令缓冲登记的所有完成执行块都执行结束。  
  
presentDrawable:方法用来在命令缓冲对象被调度时呈现一个可显示资源（CAMetalDrawable 对象）的内容。  
  
4、MTLCommandQueue协议和命令队列对象  
  
MTLCommandQueue协议为包含命令缓冲的一个队列。命令队列用来组织其中包含的命令缓冲对象的执行次序和控制命令队列中的命令缓冲对象包含的命令什么时候
被执行。  
  
MTLCommandQueue协议为命令队列定义了接口，主要的接口包括命令缓冲对象的创建。  
  
MTLCommandQueue对象的创建：  
  
使用MTLDevice对象的newCommandQueue方法或newCommandQueueWithMaxCommandBufferCount:方法来创建
一个命令队列对象。  
  
下图为以上这些对象之间的关系图：

![](_resources/iOS图形编程总结image0.jpg)

  

如图中所示：必须为一个呈现命令编码器设置呈现相关的状态、设置和创建相关的呈现用到的缓冲区、纹理等Metal资源对象。  
  
为呈现命令编码器指定的状态包括一个呈现管道流水线状态（Render Pipeline State）,一个深度和图案状态（Depth Stencil
State）,一个采样状态（Sampler State）。  
  
一个Blit命令编码器与一个缓冲区和一个纹理关联，用来在两者之间进行Blit操作。  
  
命令编码器指定图形或计算功能时可以分配三种类型的MTLResource Metal资源对象使用：  
  
MTLBuffer表现一个能够包含任意类型数据的无格式内存。MTLBuffer通常用于多边形顶点vertex、着色器shader及计算状态数据。  
  
MTLTexture表现一个有着特定纹理类型和点格式的具有相应格式的图像数据。纹理对象可以作为多边形顶点vertex、片段fragment或计算功能的一个源
，也可以在呈现描述符中作为图形呈现的输出目标。  
  
MTLSamplerState对象当一个图形或计算功能在一个MTLTexture上执行纹理采样操作时使用，用来定义地址、过滤和其它属性。  
  
图形呈现编码器MTLRenderCommandEncoder 可以使用setVertex*及setFragment*
方法组作为其参数来为相应的映射函数分配一个或多个资源。  
  
5、CAMetalLayer 对象和CAMetalDrawable 协议  
  
CoreAnimation定义了一个CAMetalLayer类和一个CAMetalDrawable 协议用来提供一个Metal内容呈现的层后备视图。CAMe
talLayer对象包含有关要呈现内容的位置、尺寸、可视属性（背景颜色、边界和阴影）及Metal呈现内容使用到的资源等。CAMetalDrawable
协议是MTLDrawable 的扩展，指定了可显示资源对象要符合的MTLTexture协议，使可显示资源对象可用作呈现命令的目标。  
  
为了实现Metal内容在一个CAMetalLayer对象的呈现，应为每次呈现流程创建一个CAMetalDrawable对象，从中得到它包含的MTLTextu
re 对象，然后在呈现流水线描述MTLRenderPipelineDescriptor 的颜色附属点属性中使用，指定其为图形呈现命令的目标。  
  
一个CAMetalLayer对象调用CAMetalLayer 对象的nextDrawable 方法来创建。  
  
在创建一个可显示资源作为图形命令的目标后，就可以调用如下步骤完成图形的绘制。  
  
1） 首先创建一个MTLCommandQueue 对象，然后使用它创建一个MTLCommandBuffer对象；  
  
2） 创建一个MTLRenderPassDescriptor对象，为其规定用作图形缓冲中的编码呈现命令目标的附属点集合；然后使用这个MTLRenderPas
sDescriptor 对象创建一个MTLRenderCommandEncoder对象；  
  
3） 创建相应的Metal资源对象，来存储绘制用到资源数据，如顶点坐标和顶点颜色数据；并调用MTLRenderCommandEncoder的setVerte
x*:offset:atIndex: 和setFragment*:offset:atIndex:方法来为呈现编码器指定用到的资源；  
  
4） 创建一个MTLRenderPipelineDescriptor 对象并为其指定vertexFunction和fragmentFunction
属性，这些属性使用Metal映射语言代码中读取的相应映射函数MTLFunction对象来设置。  
  
5) 使用MTLDevice的newRenderPipelineStateWithDescriptor:error:方法或类似方法并根据MTLRenderP
ipelineDescriptor创建一个MTLRenderPipelineState对象；然后调用MTLRenderCommandEncoder
的setRenderPipelineState:方法来为呈现编码器对象MTLRenderCommandEncoder设置管道流水线；  
  
6）调用MTLRenderCommandEncoder 的drawPrimitives:vertexStart:vertexCount:方法来执行图形的呈现
，然后调用MTLRenderCommandEncoder的endEncoding
方法来结束本次呈现流程的编码，最后调用MTLCommandBuffer的commit方法来在GPU上执行整个绘制命令。  

  

喜欢我们的内容，可以点击右上角**「分享到朋友圈」**，或**「查看官方账号」**并关注我们。  

阅读原文

阅读

__ 举报

[阅读原文](http://mp.weixin.qq.com/s?__biz=MjM5OTM0MzIwMQ==&mid=201674464&idx=1&sn
=ac151ad07370fc89c35b68ffaef8cdda&scene=0#rd)

