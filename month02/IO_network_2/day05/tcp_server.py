"""
tcp_server.py  tcp套接字服务端功能流程
重点代码

注意 ： 功能性代码，注意流程和函数使用
"""

import socket


# 创建TCP套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8880))

# 设置监听
sockfd.listen(5)

# 阻塞等待客户端连接
while True:
    print("Waiting for connect...")
    #强制退出，避免报错，加一个捕获异常
    try:
        connfd,addr = sockfd.accept()
        print("Connect from",addr)  # 打印连接的客户端
    except KeyboardInterrupt:   #如果服务端强制退出报错（KeyboardInterrupt）处理
        print("Server exit")
        break
    except Exception as e:   #否则其他错误
        print(e)
        continue


    # 收发消息
    while True:
        data = connfd.recv(1024)
        # 连接的客户端退出，recv会立即返回空字符串
        if not data:
            break
        print(data.decode())
        n = connfd.send(b"Thanks")
        print("Send %d bytes"%n)
    connfd.close()    #若客户端退出，关闭连接套接字


# 关闭套接字
sockfd.close()











