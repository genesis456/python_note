"""
空洞文件
"""

f = open('test','wb')

f.write(b'START')
f.seek(1024*1024*100,2)   #可以到终端查看文件大小
#空洞文件就是将要传入磁盘的文件大小先预订好

f.write(b'END')

f.close()