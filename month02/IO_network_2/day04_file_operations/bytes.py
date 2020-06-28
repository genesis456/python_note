s = "hello" #  字符串，只有Ａscii字符才能加b转换

print(s)

s = b"hello"  #  字节串
print(s)

"""
所有的字符串都能转换为字节串
但是并不是所有的字节串都能转换为字符串
"""

s = "你好".encode()   #  将字符串－－－＞字节串
print(s)

#  字节串  ---> 字符串
print(s.decode())