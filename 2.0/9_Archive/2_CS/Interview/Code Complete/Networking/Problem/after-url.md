# After URL

出处

What happens after you typed a URL in your browser and pressed return key?

## Solution

如果要连到远程服务器，首先需要知道服务器的IP地址和端口。其次需要发送接入请求到服务器，服务器返回响应数据。因此，如何寻址和如何建立链接是本题的关键。本题属于知识性问题，没有太多的解题技巧，直接给出解答如下

1. 进行寻址：如果在浏览器缓存中存有URL的对应IP，则直接查询其IP；否则，访问DNS(Domain Name System)进行寻址(Domain Name Resolution)。
2. DNS或者URL cache返回网页服务器的IP地址。
3. 浏览器与网页服务器通过三次握手建立TCP连接。由于是网页浏览服务，故浏览器连接到服务器的80端口。
4. 浏览器与服务器建立HTTP会话(session)，接收来自服务器的HTTP数据。
5. 浏览器解析HTTP数据，在本地窗口内渲染并显示网页。
6. 当浏览器页面被关闭时，终止HTTP会话并关闭链接。


