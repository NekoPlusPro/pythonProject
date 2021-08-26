# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

import turtle
for i in range(4):
    turtle.seth(90*i)
    turtle.circle(50,90)
    turtle.seth(90*i+180)
    turtle.circle(50,90)
turtle.hideturtle()
