"""
exit.py
"""

import os,sys

#父子进程退出不会影响对方继续运行

#1
# os.__exit(0)  #退出进程

#2
sys.exit("退出")  #退出进程，并打印字符串

#进程退出后续不再执行
print("exit test")