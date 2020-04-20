#tcp服务端流程
import socket

#创建tcp套接字　
#socket.AF_INET为ipv4，socket.SOCK_STREAM为流式套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定ip地址　　bind()里面的参数是本机地址，创建的端口号
sockfd.bind(("127.0.0.1",1540))  #127.0.0.1和 'localhost'都可以代表本机ＩＰ地址
#设置监听
sockfd.listen(5)

#阻塞等待处理连接　　提示等待连接
print("Waiting for connect..")
connfd,addr = sockfd.accept()    #连接成功的客户端端口号是系统自动分配的（因为客户端可以不绑定）
print("Conoect from",addr)  #打印连接的客户端地址

#收发消息
data = connfd.recv(1024)
print("收到：",data)
n = connfd.send(b"thanks")  #发送字节串
print("发送%d字节"%n)

#关闭套接字
connfd.close()
sockfd.close()


#可以在终端使用telnet命令创建模拟客户端：telnet＋目地ＩＰ地址（即绑定的）＋端口号
#多次运行可能会报错，只需换一个端口号（可能端口号被占用）