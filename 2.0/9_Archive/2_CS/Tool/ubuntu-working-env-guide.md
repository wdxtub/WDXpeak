# Ubuntu 工作环境打造指南

考虑到 mac 升级之后各种坑，latex 什么鬼都用不了，所以痛定思痛决定在 Ubuntu 上搞一个工作环境。基本就是云同步+markdown+pandoc+sublime 高亮编辑器。

环境 Ubuntu 14.04 64-bit

<!-- MarkdownTOC -->

- 中文输入法
- Dropbox
- Pandoc
- Latex 及中文支持
- 在当前目录下打开终端
- 安装 sublime 3
    - 插件精选
    - 常用技能
    - 常用快捷键
    - 配置更改

<!-- /MarkdownTOC -->


## 中文输入法

首先当然是要安装输入法，现在搜狗已经在 linux 上出了输入法，直接用即可。[安装指南](http://pinyin.sogou.com/linux/help.php)

下载 deb 包直接安装即可

安装完之后需要重启，在 language support 中把默认引擎改成 fcitx，然后选择搜狗拼音即可

## Dropbox

从[这里](https://www.dropbox.com/install?os=lnx)下载对应版本，然后登录设置正常使用即可

## Pandoc

从[这里](http://pandoc.org/installing.html) 下载 deb 包安装即可。

具体转换过程

    pandoc -s source.md -o target.pdf

注意目前纯英文才可以，图片需要是 PNG 格式

## Latex 及中文支持

各位阅读前，先说明以下总体上我们要做的几件事。

1. 安装TexLive。我们知道Latex只是一套排版的宏定义，为实现Latex，需要在各种操作系统上提供软件支持。TexLive就是实现此目的一个跨平台软件包。
2. Latex支持的字体非常多，自然包括中文。不过，为了更好地支持中日韩（因为这些是方块型的字符集，与字母类型的文字不同），需要安装CJK扩展包。
3. 为了使用额外的中文字体，需要配置Latex以便使用它们。
4. 使用测试文档，确认安装的字体不是已经生效了。


打开终端，安装以下TexLive和常用的一些Latex宏包（可以根据自己的需要增改）：

    sudo apt-get install texlive texlive-math-extra texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-pictures texlive-science latex-beamer texlive-base texlive-bibtex-extra texlive-xetex texlive-latex-extra

如果硬盘充裕的话，直接完整安装也可以：

    sudo apt-get install texlive-full latex-beamer

安装完后，就可以安装CJK的相关软件包了，如果只需要获得中文支持，那么执行：

    sudo apt-get install latex-cjk-chinese ttf-arphic-* hbf-*

否则，建议安装 latex-cjk-all 以获取完整支持。

    sudo apt-get install latex-cjk-all

Linux下的中文字体，对于Ubuntu来说有现成的。因此，只要第一步正常安装完毕，就可以用下面的测试文件进行测试。

```
\documentclass{article}
\usepackage{CJKutf8}
\begin{document}
\begin{CJK}{UTF8}{gkai}
这是一个楷体中文测试，处理简体字。
\end{CJK}
\begin{CJK}{UTF8}{gbsn}
这是一个宋体中文测试，处理简体字。
\end{CJK}
\begin{CJK}{UTF8}{bkai}
這是一個big5編碼的楷體中文測試，處理繁體文字。
\end{CJK}
\begin{CJK}{UTF8}{bsmi}
這是一個个big5編碼的明體中文測試，處理繁體文字。
\end{CJK}
\end{document}
```

将这部分代码粘贴到文本文件中，然后保存将其保存为test.tex。然后使用下面的命令生成PDF文档。

    pdflatex test.tex
    evince test.pdf

## 在当前目录下打开终端

直接安装一个软件包nautilus-open-terminal

终端输入：`sudo apt-get install nautilus-open-terminal`

重启系统！

## 安装 sublime 3

简单粗暴

    sudo add-apt-repository ppa:webupd8team/sublime-text-3
    sudo apt-get update
    sudo apt-get install sublime-text-installer

然后需要配置一下环境

先安装 package control，[教程](https://packagecontrol.io/installation)

### 插件精选

+ Theme: Gravity
+ Color Theme: Monokai Extended
+ MarkdownTOC
+ [SideBarEnhancements](https://github.com/titoBouzout/SideBarEnhancements): 侧边栏增强
+ [Alignment](https://github.com/wbond/sublime_alignment): 等号对齐
+ [AutoFileName](https://github.com/BoundInCode/AutoFileName): 文件路径自动提示

### 常用技能

1. 按住 `ctrl` 键，鼠标单击就是多重选择。
2. [键盘多重选择](http://baelabs.duapp.com/Sublime/multiple_selection_with_the_keyboard.html)
3. 根据选择文本自动添加 ', "",(),[] 匹配。
4. 搜索按钮的功能说明 ([冷风贡献](http://hi.baidu.com/chaoxinggsc/item/904a471aa937bc35f6625c42))

### 常用快捷键

1. Ctrl+L             选择整行（按住-继续选择下行）
2. Ctrl+Shift+K(shhift+del)     删除整行，  ctrl + KK 从光标处删之行尾，Ctrl+K Backspace 从光标处删除至行首
3. Ctrl+Shift+D       复制光标所在整行，插入在该行之前
4. Ctrl+D             选词 （按住-继续选择下个相同的字符串，再按，可跳到相应的方法定义处
5. Ctrl+Shift+M       选择括号内的内容（按住-继续选择父括号）
6. Ctrl+/             注释整行（如已选择内容，同“Ctrl+Shift+/”效果）
7. Ctrl + alt + /     取消注释
8. Ctrl+Shift+UP      与上行互换  ctrl + shift + up: 列模式编辑
9. Ctrl + R           跳转当前页的目标方法
10. Ctrl+K + U        大写
11. Ctrl+K + L        小写
12. 鼠标中间           列模式编辑
13. Ctrl+Shift+[]     代码折叠
14. ctrl+k ctrl+1:    折叠所有代码
15. Ctrl + K,B        打开侧边栏
16. ctrl + 回车：　　   光标后插入行，　Ctrl+Shift+Enter 光标前插入行
17. ctrl + m:         匹配括号
18. vim mode下        查找上一个下一个的快捷键是 是* #
19. ctrl +z, y:       撤销，恢复撤销
20. alt + .:          闭合当前标签
21. Ctrl+F2:          设置书签
22. F2:               下一个书签
23. Shift+F2:         上一个书签
24. ctrl + p:         即时的文件切换
25. ctrl + shift + a: 选择标签内的内容
26. ctrl + 单击：      多行随意位置添加光标
27. alt + F3( mac: ctrl + command + g): 选择页面中所有相同的词
28. ctrl + F3:        跳转到下一个选中的词
29. Ctrl+Shift+P Set Syntax:html : 设置文件类型
30. Shift + 右键:     连续多行光标选中 (by Gary Gauh)

### 配置更改

```
{
    "caret_style": "phase",
    "color_scheme": "Packages/Monokai Extended/Monokai Extended.tmTheme",
    "draw_white_space": "all",
    "ensure_newline_at_eof_on_save": true,
    "fade_fold_buttons": false,
    "file_exclude_patterns":
    [
        "*.Ulysses-Group.plist",
        "*.pyc",
        "*.pyo",
        "*.exe",
        "*.dll",
        "*.obj",
        "*.o",
        "*.a",
        "*.lib",
        "*.so",
        "*.dylib",
        "*.ncb",
        "*.sdf",
        "*.suo",
        "*.pdb",
        "*.idb",
        ".DS_Store",
        "*.class",
        "*.psd",
        "*.db",
        "*.sublime-workspace"
    ],
    "folder_exclude_patterns":
    [
        ".svn",
        ".git",
        ".hg",
        "CVS"
    ],
    "font_size": 19,
    "highlight_color_blue": true,
    "highlight_line": true,
    "highlight_modified_tabs": true,
    "ignored_packages":
    [
        "ActionScript",
        "AppleScript",
        "ASP",
        "Clojure",
        "D",
        "Erlang",
        "Go",
        "Graphviz",
        "Groovy",
        "OCaml",
        "OmniMarkupPreviewer",
        "Pascal",
        "R",
        "Rails",
        "Tag",
        "TCL",
        "Vintage"
    ],
    "rulers":
    [
        80,
        100
    ],
    "soda_folder_icons": true,
    "spell_check": false,
    "theme": "Gravity.sublime-theme",
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true,
    "word_wrap": true
}
```

最后是屌丝license, Build 3083

```
—– BEGIN LICENSE —–
Andrew Weber
Single User License
EA7E-855605
813A03DD 5E4AD9E6 6C0EEB94 BC99798F
942194A6 02396E98 E62C9979 4BB979FE
91424C9D A45400BF F6747D88 2FB88078
90F5CC94 1CDC92DC 8457107A F151657B
1D22E383 A997F016 42397640 33F41CFC
E1D0AE85 A0BBD039 0E9C8D55 E1B89D5D
5CDB7036 E56DE1C0 EFCC0840 650CD3A6
B98FC99C 8FAC73EE D2B95564 DF450523
—— END LICENSE ——
```
