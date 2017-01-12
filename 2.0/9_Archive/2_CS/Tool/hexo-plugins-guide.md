# Hexo 插件指南

Hexo 作为我一直在用的静态博客生成引擎，整体质量非常过硬，虽然从 2.0 到 3.0 版本的更新造成了很多插件不兼容，但是随着版本的稳定，诸多靠谱的插件也都如雨后春笋层出不穷，这里介绍一些觉得比较好的插件。

## [hexo-admin](https://github.com/jaredly/hexo-admin)

这个就是给 hexo 做了一个网页版的编辑器，基本等于是弄得跟在线博客编辑器一样了，还是比较方便的，不过我还是习惯用本地编辑器。

## [hexo-render-marked](https://github.com/hexojs/hexo-renderer-marked)

hexo 的一大好处就是可以自定义 markdown 的渲染引擎，默认的对 gfm 的支持不是很好，所以我们换成这个。

安装很简单，执行下面即可

```
$ npm install hexo-renderer-marked --save
```

然后在站点的 `_config.yml` 文件中修改

```
marked:
  gfm: true
  pedantic: false
  sanitize: false
  tables: true
  breaks: true
  smartLists: true
  smartypants: true
```

具体的介绍就直接搬运了：

+ gfm - Enables GitHub flavored markdown
+ pedantic - Conform to obscure parts of markdown.pl as much as possible. Don't fix any of the original markdown bugs or poor behavior.
+ sanitize - Sanitize the output. Ignore any HTML that has been input.
+ tables - Enable GFM tables. This option requires the gfm option to be true.
+ breaks - Enable GFM line breaks. This option requires the gfm option to be true.
+ smartLists - Use smarter list behavior than the original markdown.
+ smartypants - Use "smart" typograhic punctuation for things like quotes and dashes.


## [hexo-generator-seo-friendly-sitemap](https://github.com/ludoviclefevre/hexo-generator-seo-friendly-sitemap)


给博客生成一个站点地图

安装 `$ npm install hexo-generator-seo-friendly-sitemap --save`

在 `_config.yml` 中添加

```
sitemap:
    path: sitemap.xml
```

## [hexo-generator-search](https://github.com/PaicHyperionDev/hexo-generator-search)

会生成一个 `search.xml` 文件方便添加搜索功能。

> Generate search data for Hexo 3.0. This plugin is used for generating a search.xml file, which contains all the neccessary data of your articles that you can use to write a local search engine for your blog.

安装 `$ npm install hexo-generator-search --save`

修改 `_config.yml`

```
search:
  path: search.xml
  field: post
```

不过这个功能需要自己配置另外的服务器，比如搭建在 SAE 之类的，所以暂时也先不折腾

## 总结

当然还有很多其他的插件，不过一般在配置博客的时候多多少少都会涉及，这里主要就提供一些不太常见的给大家。


