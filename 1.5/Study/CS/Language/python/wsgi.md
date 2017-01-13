深入理解WSGI
===================
WSGI是什么?是一种规范,用来规范Python web应用与服务器之间通信的标准.好比你和老外说话也需要建立一种事先制定的语言来沟通一样.如果今天你碰一德国人,然后你就去学德语,如果碰到日本人,然后去学日语,这样累死了,干脆定一种标准,大家都说英语好了.全世界通用.同样的道理,在python语言中,web框架多如牛毛,这么多框架如果大家都不遵守规则,然后写服务器也没啥规范,这个世界就乱套了.因此python2.5就提出了WSGI, [PEP3333](http://www.python.org/dev/peps/pep-3333/).

####python web 框架有哪些?

1. Django
2. Pyramid
3. Tornado
4. Flask
5. web.py
.....
####python wsgi server有那些?

1. CherryPy WSGI Server  

    cherrypy除了作为web server外,其实他还是一个web framework ,其宣称是"A high-speed, production ready, thread-pooled,generic HTTP server". 
2. Gunicorn  

    gunicorn就是一个纯粹的web server.他使用的pre-fork模型,使用一个central master 进程,用来管理多个worker processes.,这些worker processes 直接处理请求.  

3. Tornado  
    
    Tornado同时是web应用开发框架和网络库,用来处理异步操作.同时有自己的WSGI server.

4. Twisted Web

    Twisted Web 来自于 Twisted 网络库

5. uWSGI

    uWSGI是一个很全面的项目,目标是提供全栈式服务,uWSGI server 就是其中的一个组建.

6. mod_wsgi
    
    mod_wsgi是一个WSGI兼容的模块,能够在Apache HTTP Server 上运行 WSGI应用.

####wsgi对web框架/应用的规范是怎样的?
WSGI应用接口由一个callable对象实现,这个callable对象可以是function,method,class,或者是显现的__call__的实例方法.这个callable只要满足以下两个条件:  
* 必须接收两个位置参数
    * 字典对象
    * 一个回调函数,用于发送HTTP 状态码/消息和HTTP头给server.
* 必须返回响应体给 server,返回对象作为字符串包装在迭代器里面.

####application/framework
application的骨架代码:   

    #这个就是我们的application 对象, 名字随便取,但是如果你用mod_wsgi的话,就必须叫"application"
    def application(#接收两个参数
            #字典对象,包含类似CGI的环境参数,从客户端接收过来的请求有server填充
            environ,
            #start_response是一个回调函数,由server提供.用来发送HTTP status和header给server
            start_response):
    
        #响应体
        response_body = "The request method was %s" % environ['REQUEST_METHOD']
        #状态码
        status = "200 OK"
        
        #响应头
        response_headers = [('Content-Type':'text/plain'),
                            ('Content-Length':str(len(response_body)))]
        #发送给server
        start_response(status, response_headers)
    
        #把响应体返回给server
        #注意:尽管response_body是一个iterable,但是要包装成list,否则server会单个字节的发送给client.
        return [response_body]

####web server size
python标准库中提供了wsgiref模块提供了一个参考实现.
    
    from wsgiref import make_server
    
    httpd = make_server(
        'localhost',
        8000,
        application
        )
    httpd.handle_request()
    
####middleware 
middleware要尽可能透明  
