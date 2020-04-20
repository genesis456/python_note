import pygame

#熟悉矩形窗口函数
hero_rect = pygame.Rect(100,500,120,125)
print("英雄的原点%d %d"%(hero_rect.x,hero_rect.y))
print("英雄的尺寸 %d %d"%(hero_rect.width,hero_rect.height))
print("%d %d"%hero_rect.size)  # 120 125


# #创建游戏窗口
# pygame.init() #初始化方法
# #创建游戏的窗口  （希望和背景图窗口一样大480*700）
# screen = pygame.display.set_mode((480,700))  #宽和高是一个元组
# #set_mode()创建的默认窗口和屏幕一样大
#
#
# #显示英雄的飞机
# hero = pygame.image.load(".")
# while True:   #设置一个无限循环窗口，启动时不会立即退出
#     pass
# pygame.quit()