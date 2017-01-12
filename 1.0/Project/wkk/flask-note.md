# Flask Study Note

## 基本介绍

+ 保持核心简单且易扩展
+ 简单的任务应该保持简单，它们的实现不应是大量代码的堆叠
+ web 开发是危险的，注意数据安全
+ 依赖两个外部库
    * Werkzeug 一个WSGI(在 web 应用和多种服务器之间开发和部署的标准 Python 接口)
    * Jinja2 渲染模板

## 安装

+ 使用 `virutalenv` 可以有效保证环境的互不影响
+ `sudo pip install virualenv`
+ 利用 `activate-wkk.sh` 激活环境
+ `pip install Flask`

## 快速入门

参考代码 `hello.py`

+ 激活env `. ./activate-wkk.sh`
+ 运行 `python hello.py`
+ 用 route() 装饰器来告诉 Flask 什么 url 触发我们的函数
+ 如果要同网络的可以访问 `app.run(host='0.0.0.0`)

用上面方法每次修改代码都需要手动重启开发服务器，在调试模式下 Flask 可以自动重新载入

方法一：

    app.debug = True
    app.run()

方法二：

    app.run(debug = True)

`route()` 装饰器把一个函数绑定到对应的 URL 上，如果想要添加变量部分，需要标记为 `<variable_name>` 或者可以用 `<converter:variable_name>` 来制定一个转换器：

    @app.route('/user/<username>')
    def show_user_profile(username):
        return 'User %s' % username

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        return 'Post %d' % post_id

现有的转换器

+ 默认为 string
+ int 接受整数
+ float 接受整数或浮点数
+ path 接受斜线

** 构建 URL `url_for()` **

** HTTP 方法 ** 

可以提供 methods 参数来控制 POST/GET

    @app.route('/login', methods=['GET','POST'])
    def login():
        if request.method == 'POST':
            do_the_login()
        else:
            show_the_login_form()

** 静态文件 **

在包中建立一个 static 文件夹即可，使用 `/static` 来访问

    url_for('static', filename='style.css')

** 模板渲染 **

尽量不要在 Python 里生成 HTML，繁琐且容易出错。Flask 使用 Jinja2 模板引擎来完成这一切。可以使用 `render_template()` 方法来渲染模板。

Flask 会在 templates 文件夹里寻找模板。

    from flask import render_template

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name = None):
        return render_template('hello.html', name=name)

这里 hello.html 是模板

    <!doctype html>
    <title>Hello from Flask</title>
    {% if name %}
        <h1>Hello {{ name }} !</h1>
    {% else %}
        <h1>Hello World!</h1>
    {% endif %}

使用继承，模板会非常有用

## 模板

Jinja2 默认配置

+ 所有扩展名为 .html .htm .xml .xhtml 的模板会开启自动转义
+ 模板可以利用 {% autoescape %} 标签选择自动转义的开关
+ 全局变量
    * config
    * request
    * session
    * g
    * url_for()
    * get_flashed_messages()
+ 标准过滤器
    * tojson()

注册过滤器

    @app.template_filter('reverse')
    def reverse_filter(s):
        return s[::-1]
    或
    def reverse_filter(s):
        return s[::-1]
    app.jinja_env.filters['reverse'] = reverse_filter
    这样使用
    {% for x in mylist | reverse %}
    {% endfor %} 

## 测试 Flask 应用

Python 自带有 unittest 包
