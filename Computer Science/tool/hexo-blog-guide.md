# hexo+github+多说 搭建博客指南

<!-- MarkdownTOC -->

- 安装
    - 可能出现的问题
- 快速指南
- 部署
- 技巧
- 主题
- 多说
- 高阶

<!-- /MarkdownTOC -->


这三个东西具体是啥，就不说了，hexo快速简单，经过权衡我最终选择使用了这个。

## 安装

    $npm install hexo -g

没出啥问题之后，就是安装好了，然后初始化博客

    $hexo init wdxblog
    $cd wdxblog
    $npm install
    $hexo server

此时文件目录为

+ blog
    + `_config_yml` // 注配置文件
    + db.json // 数据
    + debug.log // 调试日志
    + `node_mudules` // nodejs 相关依赖
    + package.json // 配置依赖
    + scaffolds // 脚手架 - 也就是一个工具模板
    + source // 存放blog正文的地方
    + themes // 存放皮肤的地方

访问 http://localhost:4000 可以看到

### 可能出现的问题

如果你的电脑没有翻墙 可能会打不开页面。因为页面中默认使用了ajax.google.com 下的js包。因此我们要把包删掉

解决办法：

进入你刚新建好的 blog根目录 ，进入 `themes/landscape/layout/_partial`

找到 after-footer.ejs 把

    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"> </script>

替换成

    <script src="http://cdn.bootcss.com/jquery/2.1.1/jquery.min.js" > </script>

找到 header.ejs 注释掉或者删掉 下面这句css引用

    <link href="//fonts.googleapis.com/css?family=Source+Code+Pro" rel="stylesheet" type="text/css">

重新 hexo server 之后。访问 http://localhost:4000 就会看到blog主页了。

## 快速指南

写新文章 `$ hexo new <title>`

运行服务器 `$ hexo server`

生成静态页面 `$ hexo generate`

部署到远程站 `$ hexo deploy`

hexo new page "pageName" #新建页面

hexo generate #生成静态页面至public目录


## 部署

新建一个 repo `wdxtub.github.io`

然后每次 `hexo g` 之后把 public 文件夹下的东西复制过去，用客户端 update 即可

## 技巧

+ CNAME 等需要上传的内容，可以放到 source 文件夹下

## 主题

git clone https://github.com/yuche/hexo-theme-kael.git themes/kael

https://github.com/yuche/hexo-theme-kael

## 多说

多说的 ID 是在后台管理中去得的。

你在「工具」>>「获取代码」>> var duoshuoQuery = {short_name:"yuche"};
shortname 部分就是你的 ID 了

## 高阶

+ .deploy：执行hexo deploy命令部署到GitHub上的内容目录
+ public：执行hexo generate命令，输出的静态网页内容目录
+ scaffolds：layout模板文件目录，其中的md文件可以添加编辑
+ scripts：扩展脚本目录，这里可以自定义一些javascript脚本
+ source：文章源码目录，该目录下的markdown和html文件均会被hexo处理。该页面对应repo的根目录，404文件、favicon.ico文件，CNAME文件等都应该放这里，该目录下可新建页面目录。
    + _drafts：草稿文章
    + _posts：发布文章
+ themes：主题文件目录
+ _config.yml：全局配置文件，大多数的设置都在这里
+ package.json：应用程序数据，指明hexo的版本等信息，类似于一般软件中的关于按钮

