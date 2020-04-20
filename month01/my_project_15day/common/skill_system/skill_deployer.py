def fun02():
    print("你是傻蛋")


# 2.	在skill_deployer.py中调用skill_manager.py。
#方法1：
import skill_system.skill_manager as ws
ws.re.get_return()
ws.re.run()
#方法2：
from skill_system.skill_manager import  *
re.get_return()
re.run()