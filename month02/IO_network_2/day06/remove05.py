"""
前情回顾

1. 网络
   OSI七层模型
   三次握手四次挥手
   tcp udp传输协议的差异

   （这是什么 具体解释 延伸扩展 你怎么用）

2. 套接字 ：  流式，数据报

3. tcp服务端

   socket->bind->listen->accept->recv/send->close

   tcp客户端

   socket->connect->send/recv->close()

4. 缓冲区
5. 粘包 ： 人为添加边界，发送延迟


练习1： 使用udp完成，从客户端输入单词，得到单词解释
客户端可以循环输入单词


练习2： 使用udp，从客户端录入学生信息，在服务端将学生信息写入文件
要求每个学生信息占一行
ID  NAME  AGE  SCORE

"""