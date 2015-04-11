![](http://p1.zhimg.com/81/85/8185d60cc48385e3ab76f4d7951af72d.jpg)

##

![](http://p2.zhimg.com/41/ac/41ac1b02b_is.jpg) 村之姑， 我读书少，你们可别骗我

事实上在早年 OpenGL 即使在游戏领域也是对 DirectX 压倒性的优势。John Carmack 曾嘲讽 DirectX 是“horribly
broken” 的 API。

直到 DirectX6 时代 OpenGL 都被认为是比 DirectX 更加优秀的 API，即使那个时候 DirectX 已经有《CS》《极品飞车
5》等大作的支持，却依然不受当时 FPS 游戏霸主 id Software 的待见。作为那个时代的显卡杀手，《Quake III》都仅仅只支持
OpenGL。

DirectX7 发布之后 DirectX 和 OpenGL 开始逐渐平起平坐。直到 2000 年 DirectX8 的发布才使 DirectX
在游戏领域完全确立了自己的优势 —— 支持革命性的 programmable GPU rendering pipeline 来代替原有的 fixed
function pipeline，引入了 Vertex Shader 和 Pixel Shader。而 OpenGL 的核心正式支持
programmable rendering pipeline 已经是四年之后 OpenGL 2.0 发布的时候了。想想这中间会有多少游戏公司 /
游戏引擎公司会倒向 DirectX 吧。

说到 OpenGL 衰落的原因，不得不提到 OpenGL 开发的机制。OpenGL 早期一直是由 ARB (

OpenGL Architecture Review Board，成员包括 Nvidia, ATI, Intel, Apple, IBM, SGI
等等）成员共同维护。每个成员可以为了支持自己硬件新的 feature 来开发 OpenGL enxtension, 所有成员一致通过的 extension
才能加入到下个版本 OpenGL 核心中。这就造成了不同成员为了各自利益互相斗争，拖慢了开发进度。微软曾经也是 ARB
的成员之一，后来因为受不了这种机制退出专心搞自己的 DirectX 去了。

如果一个 API 越流行，那么去学习这个 API 的人就会越多，游戏公司会越容易招到掌握这个 API 的图形程序员，也就会更多的基于这个 API
开发游戏。用这个 API 的游戏越来越多，就会更多的得到

硬件厂商的支持，为面向这个 API 的驱动做更多的优化，然后这个 API 就会更加流行。如此进入一个良性循环，这就造成了 DirectX
现在称霸游戏领域，OpenGL 几乎绝迹的局面。

在 06 年从 ARB 交由 Khronos Group 掌管之后, OpenGL 最近几年也迎头赶上，从性能，易用性来说其实和 DirectX
已经相差不大。但是在相比 DirectX 没有突出优点的情况下（除了跨平台），已经习惯使用 DirectX 的游戏厂商也不可能重新投出 OpenGL
的怀抱。

最后一点，OpenGL 只是一个单纯的图形库，而 DirectX 是包含图形(Direct3D), 声音(DirectSound),
输入(DirectInput), 网络(DirectPlay)的一整套游戏开发解决方案。对开发者来说使用 DirectX 显然要方便的多。

下面是我之前一个同事看完我的回答的评论，也贴上来吧。

“还有很重要的一点, GL 从不淘汰任何老的 API. DX10 相对于 DX9,是个全新的 API,革命性的更新,彻底推倒重来. 但 GL
为了向后兼容,保留了很多对硬件和驱动都不友好的 API.除了跨平台和早期对精度的要求比 DX 高,其他简直是一无是处”

[查看知乎讨论](http://www.zhihu.com/question/23241456)

