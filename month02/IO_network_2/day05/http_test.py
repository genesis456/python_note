"""
http请求过程演示
"""

from  socket import *

# tcp套接字 （http-->tcp）
s = socket()
s.bind(('0.0.0.0',8005))
s.listen(3)

# 获取请求
c,addr = s.accept()
print("Connect from",addr)

data = c.recv(4096)  #接收http请求
print(data)

# 模拟返回响应报文
# 格式：
    #响应行：反馈基本响应情况
    #响应头：对响应内容进行描述
    #空行
    #响应体：响应的主体内容信息
response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>Hello World</h1>
"""

c.send(response.encode())


c.close()
s.close()

#在浏览器查ip地址和端口号0.0.0.0：8005