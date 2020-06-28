"""
编写一个接口函数，从终端输入端口名称获取端口运行状态中的地址值

思路分析：

1、根据输入的端口名称找到对应的段落

2、在该段落中匹配address

"""


import re


def get_address():
    f = open('exc.txt')
    while True:
        # 获取一段内容
        data = ''   #每次break跳出，data都会重新定义为空
        for line in f:
            if line == '\n':
                break
            data += line

        # data为空说明到了文档结尾
        if not data:
            break

        obj = re.match(port, data)  #用输入的端口号匹配是哪一段
        #如果obj不是none  data就是目标段落
        if obj:
            # print("yes")  #判断是否存在该端口
            pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'   #正则表达式

            obj = re.search(pattern,data)
            if not obj:   #如果没有address,就找Internet address 或Unknow
                pattern = r"([0-9]{1,3}\.){3}[0-9]{1,3}/\d+|Unknow"
                obj = re.search(pattern, data)
                return obj.group()

            return obj.group()

    return"某有该端口"


if __name__ == '__main__':
    port = input("端口：")
    st = get_address()
    print(st)
