# 谷歌搜索技巧

<!-- MarkdownTOC -->

- 操作符
- 操作命令
    - 网站网页命令
- 图片搜索与影视搜索

<!-- /MarkdownTOC -->


## 操作符

`+` 强制搜索

由于Google会忽略和过滤一些常用词（称为stop words / common words），如and、how等。使用+可以让搜索引擎强制包括这些词。使用+还可以强制过滤关键词变体形式（不让搜索结果出现关键词的其它形式），如单复数、动词时态、ing形式等等。

`-`  逻辑非

用于过滤-号后面的关键词。如：MP3 -MP4，表示只搜索MP3而不要MP4的搜索结果。 -号后面没有空格。

`~` 同义词

关键词前加波浪线。如：~table 。

`*` 通配符

如：Google was founded in * 。

`**` 指数

作用同  ^ ，如：2**10 。

`" "` 引号

用引号精确搜索，有时可只用左侧引号。如："Google hacking" = "Google hacking 。

`|` 逻辑或

作用同 OR ，如：Google hacking | hacks 。

`..` 数字范围

用于限定数值范围，如：spring festival logo 2002..2009 。

`^` 指数

作用同  ** ，如：2^10 。

## 操作命令

`OR`  逻辑或

作用同 | ，如：Google hacking OR hacks 。

`define:`  关键词定义

查询关键词的网络释义。如： define:google 。

`ext:`  限定搜索指定文件类型

作用同 filetype:

`filetype:`  限定搜索指定文件类型
    作用同 ext: 如：filetype:pdf = ext:pdf 。目前文件类型支持如下格式：
    Adobe Acrobat PDF (.pdf)
    Adobe Postscript (.ps)
    Autodesk DWF (.dwf)
    Google地球 KML (.kml)
    Google地球 KMZ (.kmz)
    Lotus 1-2-3（wk1、wk2、wk3、wk4、wk5、wki、wks、wku）
    Lotus WordPro (.lwp)
    MacWrite (.mw)
    Microsoft Excel (.xls)
    Microsoft Powerpoint (.ppt)
    Microsoft Word (.doc)
    Microsoft Works（wks、wps、wdb）
    Microsoft Write (.wri)
    Rich Text Format富文本格式 (.rtf)
    Shockwave Flash (.swf)
    纯文本（ans、txt）

`intitle:`  限定搜索标题中含指定关键词的网页

如： intitle:google search guide 。限定多个关键词用 allintitle:

`inurl:`  限定搜索url中含指定关键词的网页

如： inurl:google search guide 。通过inurl:view.shtml 你可以找到在线的网络摄像头。 限定多个关键词用 allinurl:

`inanchor:`  限定搜索页面链接锚文本中含指定关键词的网页

如： inanchor:google search guide 。限定多个关键词用 allinanchor:

`intext:`  限定搜索正文文本（不含标题和链接）中含指定关键词的网页

如： intext:google vs mircosoft。

### 网站网页命令

`site:`  限定搜索某网站的网页

如： site:www.google.com 。

`link:`  搜索链向某网站/网址的网页

如： link:www.google.com 。

`related:`  搜索与某网页相似或相关的页面

如： related:www.google.com 。

`cache:`  搜索某网页在Google缓存（网页快照）中的旧版本

如： cache:www.google.com 。

`info:`  综合查询某网页的信息，即列出上述四个命令

如： info:www.google.com 。作用同 id:

## 图片搜索与影视搜索

filetype: 限定搜索指定文件类型的图片，支持如下格式：

+ filetype:jpg
+ filetype:gif
+ filetype:png
+ filetype:bmp

imagesize: 限定搜索指定尺寸的图片，如: imagesize:800x600

URL 参数：加在图片搜索网页的 URL 后面，可以实现更精细的搜索

+ &imgtype=news 资讯
+ &imgtype=face 脸部特写
+ &imgtype=clipart 剪贴画
+ &imgtype=lineart 素描
+ &imgtype=photo 照片
+ &imgc=gray 黑白图片
+ &imgc=mono 灰阶图片
+ &imgc=color 全彩图片
