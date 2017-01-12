Flask之Hello world 详解
========================
以下讲解假设你对python有基本了解,熟悉wsgi,以及了解某种python web framework.  

    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return "HELLO WROLD"
    
    if __name__ == '__main__':
        app.run(debug=True)

1. Flask的实例app就是我们的WSGI application.
2. 创建Flask实例需要指定一个参数,这个参数一般是application的模块名字或者是包名.Flask根据这个参数定位templates,static files等.
3. route装饰器告诉Flask什么样的请求路径对应这个函数

####Routing
route()装饰器支持变量规则,用`<variable_name>`表示.还可以制订一个转换器.例如:  

    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return 'User %s' % username
    
    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return 'Post %d' % post_id

    @app.route('/user/<path:location>')
    def show_path(location):
        return location

有三种转换器:  

    int	    accepts integers
    float	like int but for floating point values
    path	like the default but also accepts slashes

####HTTP METHOD

    from flask import request

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == "POST":
            return 'post'
        else:
            return 'get'
    
####Static Files
在package或则module同目录下创建static目录  

    url_for('static', filename='style.css')
####rendering templates
    默认Flask配置JinJia2作为模板引擎,因为他们是一家的.Flask会在templates目录下查找模板文件,如果application是一个module,那么这个templates目录与application同级目录.如果他是一个package:  

* case 1: a module:

    /application.py
    /templates
       /hello.html
* case 2: a application
    
    /application
        /__init__.py
        /templates
            /hello.html

渲染模板使用render_template()  
    
    from flask import render_template
    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html',name=name)
JinJia2 模板的语法和Mako以及django的语法都差不多,可以稍作了解  

    <!doctype html>
    <title>Hello from Flask</title>
    {% if name %}
      <h1>Hello {{ name }}!</h1>
    {% else %}
      <h1>Hello World!</h1>
    {% endif %}

####Context locals
先跳过   
