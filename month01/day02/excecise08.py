"""
已知：加速度，初速度，时间
　　计算：距离
　　加速度　＝　(距离 - 初速度　×　时间) * 2 / 时间平方
     距离 = 加速度 * 时间平方 / 2 + 初速度　×　时间

  日期：６／０７／２０１９
"""


speed = float(input("请输入加速度："))
velocity = float(input("请输入初速度："))
time = float(input("请输入时间："))
distance = speed * time**2 / 2 + velocity * time

print("距离是：",distance)
