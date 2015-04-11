帮助 : pandoc --help


pandoc --latex-engine=xelatex -V mainfont='STSong' --template=/Users/dawang/Desktop/ch-template.latex wakeup-travel.md -o tek.pdf

pandoc --latex-engine=xelatex -V mainfont='Lantinghei SC' --template=/Users/dawang/Desktop/ch-template.latex wakeup-travel.md -o tek.pdf

## 生成各种格式

### 生成 HTML

    pandoc in.md -0 out.html

附带上 css 样式（需要在同一个文件夹）

    pandoc in.md -c style.css out.html

但是每次都要把 css 拷贝过来，很麻烦，可以通过

    pandoc - -version 命令来查看当前默认的目录

我的目录是 /Users/dawang/.pandoc，只要把 style.css

放到这个目录下，那么在任意目录使用 pandoc 时，都可以自动读取到这个文件

### 生成独立 HTML

如果需要把 style.css 中的样式代码直接嵌入到 html 中，可以用下面这个命令

    pandoc -s - -self-contained -c style.css   in.md -o out.html

这个命令不但会把 css 文件嵌入到 html 中，也会把所有外部文件压缩进单个 html 文件中

### 转换成 Epub

    pandoc mybook.txt -o mybook.epub

### 转换成 doc

    pandoc -f markdown -t docx file.md -o file.docx

### 转换成 PPT

采用默认模板渲染一个独立的 DZSlides 幻灯片

    pandoc slides.md -o slides.html -t dzslides -s

首先要从 Github 上获取 github.com/hakimel/reveal.js，讲其放到幻灯片所在目录下即可
渲染幻灯片

    pandoc slides.md -o slides.html -t revealjs -s

还有多种主题

    pandoc slides.md -o slides.html -t revealjs -s -V theme=beige

+ beige：米色背景，深色文字
+ sky：天蓝色背景，白色细文字
+ night：黑色背景，白色粗文字
+ serif：浅色背景，灰色衬线文字
+ simple：白色背景，黑色文字
+ solarized：奶油色背景，深青色文字

### 生成 PDF

装了 MacTex 就行了，就是中文比较麻烦，需要用额外的模板


- [ ] a bigger project
    - [ ] test

