'''
import this
直接运行 输出python之美这首诗


import this
string = input('what is your name')
print(string)


# 学习turtle在屏幕上绘制图形
import turtle

# 设置画布大小 (1) turtle.screensize(canvwidth=None,canvheight=None,bg=None)
#turtle.screensize(800, 600, 'skyblue')
#(2) turtle.setup(width=0.5,height=0.75,startx=None,starty=None) 小数为占屏幕百分比 startx，starty为窗口左上角的顶点位置


#画笔的状态
turtle.pensize()#设置画笔的宽度
turtle.pencolor('brown')#没参数时返回当前画笔的颜色，有参数设置画笔颜色
turtle.speed(1)#设置画笔移动速度范围为[0,10]整数，数字越大越快

#绘图命令
turtle.forward(distance)#向当前画笔方向移动distance像素长
turtle.backward(distance)#后退相同像素长
turtle.right(degree)#顺时针移动degree度
turtle.left(degree)#逆时针移动degree度

'''

# import turtle as t
# import time
# 画出一个正方形
# turtle.pensize(4)
# turtle.pencolor('red')
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.mainloop()


# 绘制太阳花
# t.color('red', 'green')
# t.speed(10)
# t.begin_fill()  # 准备开始填充图形
# for i in range(50):
#     t.forward(200)
#     t.left(170)
# t.end_fill()
# time.sleep(1)


# 绘制蟒蛇
# import turtle


# def drawSnake(rad, angle, len, neckrad):
#     for _ in range(len):
#         turtle.circle(rad, angle)
#         turtle.circle(-rad, angle)
#     turtle.circle(rad, angle / 2)
#     turtle.forward(rad / 2)  # 直线前进
#     turtle.circle(neckrad, 180)
#     turtle.forward(rad / 4)


# if __name__ == "__main__":
#     turtle.setup(1500, 1400, 0, 0)
#     turtle.pensize(30)  # 画笔尺寸
#     turtle.pencolor("green")
#     turtle.seth(-40)    # 前进的方向
#     drawSnake(70, 80, 2, 15)


# 绘制小猪佩奇
import turtle as t
# 绘制小猪佩奇
# =======================================


t.pensize(4)
t.hideturtle()
t.colormode(255)
t.color((255, 155, 192), "pink")
t.setup(840, 500)
t.speed(10)

# 鼻子
t.pu()
t.goto(-100, 100)
t.pd()
t.seth(-30)
t.begin_fill()
a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.08
        t.lt(3)
        t.fd(a)
        t.end_fill()

t.pu()
t.seth(90)
t.fd(25)
t.seth(0)
t.fd(10)
t.pd()
t.pencolor(255, 155, 192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160, 82, 45)
t.end_fill()

t.pu()
t.seth(0)
t.fd(20)
t.pd()
t.pencolor(255, 155, 192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160, 82, 45)
t.end_fill()

# 头
t.color((255, 155, 192), "pink")
t.pu()
t.seth(90)
t.fd(41)
t.seth(0)
t.fd(0)
t.pd()
t.begin_fill()
t.seth(180)
t.circle(300, -30)
t.circle(100, -60)
t.circle(80, -100)
t.circle(150, -20)
t.circle(60, -95)
t.seth(161)
t.circle(-300, 15)
t.pu()
t.goto(-100, 100)
t.pd()
t.seth(-30)
a = 0.4
for i in range(60):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.08
        t.lt(3)
        t.fd(a)
        t.end_fill()

# 耳朵
t.color((255, 155, 192), "pink")
t.pu()
t.seth(90)
t.fd(-7)
t.seth(0)
t.fd(70)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50, 50)
t.circle(-10, 120)
t.circle(-50, 54)
t.end_fill()

t.pu()
t.seth(90)
t.fd(-12)
t.seth(0)
t.fd(30)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50, 50)
t.circle(-10, 120)
t.circle(-50, 56)
t.end_fill()

# 眼睛
t.color((255, 155, 192), "white")
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-95)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()

t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()

t.color((255, 155, 192), "white")
t.pu()
t.seth(90)
t.fd(-25)
t.seth(0)
t.fd(40)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()

t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()

# 腮
t.color((255, 155, 192))
t.pu()
t.seth(90)
t.fd(-95)
t.seth(0)
t.fd(65)
t.pd()
t.begin_fill()
t.circle(30)
t.end_fill()

# 嘴
t.color(239, 69, 19)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(-100)
t.pd()
t.seth(-80)
t.circle(30, 40)
t.circle(40, 80)

# 身体
t.color("red", (255, 99, 71))
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-78)
t.pd()
t.begin_fill()
t.seth(-130)
t.circle(100, 10)
t.circle(300, 30)
t.seth(0)
t.fd(230)
t.seth(90)
t.circle(300, 30)
t.circle(100, 3)
t.color((255, 155, 192), (255, 100, 100))
t.seth(-135)
t.circle(-80, 63)
t.circle(-150, 24)
t.end_fill()

# 手
t.color((255, 155, 192))
t.pu()
t.seth(90)
t.fd(-40)
t.seth(0)
t.fd(-27)
t.pd()
t.seth(-160)
t.circle(300, 15)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-10)
t.circle(-20, 90)

t.pu()
t.seth(90)
t.fd(30)
t.seth(0)
t.fd(237)
t.pd()
t.seth(-20)
t.circle(-300, 15)
t.pu()
t.seth(90)
t.fd(20)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-170)
t.circle(20, 90)

# 脚
t.pensize(10)
t.color((240, 128, 128))
t.pu()
t.seth(90)
t.fd(-75)
t.seth(0)
t.fd(-180)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)

t.pensize(10)
t.color((240, 128, 128))
t.pu()
t.seth(90)
t.fd(40)
t.seth(0)
t.fd(90)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)

# 尾巴
t.pensize(4)
t.color((255, 155, 192))
t.pu()
t.seth(90)
t.fd(70)
t.seth(0)
t.fd(95)
t.pd()
t.seth(0)
t.circle(70, 20)
t.circle(10, 330)
t.circle(70, 30)
t.done()

# from turtle import*


# def nose(x, y):  # 鼻子

#     penup()  # 提起笔

#     goto(x, y)  # 定位

#     pendown()  # 落笔，开始画

#     setheading(-30)  # 将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）

#     begin_fill()  # 准备开始填充图形

#     a = 0.4

#     for i in range(120):

#         if 0 <= i < 30 or 60 <= i < 90:

#             a = a + 0.08

#             left(3)  # 向左转3度

#             forward(a)  # 向前走a的步长

#         else:

#             a = a - 0.08

#             left(3)

#             forward(a)

#     end_fill()  # 填充完成

#     penup()

#     setheading(90)

#     forward(25)

#     setheading(0)

#     forward(10)

#     pendown()

#     pencolor(255, 155, 192)  # 画笔颜色

#     setheading(10)

#     begin_fill()

#     circle(5)

#     color(160, 82, 45)  # 返回或设置pencolor和fillcolor

#     end_fill()

#     penup()

#     setheading(0)

#     forward(20)

#     pendown()

#     pencolor(255, 155, 192)

#     setheading(10)

#     begin_fill()

#     circle(5)

#     color(160, 82, 45)

#     end_fill()


# def head(x, y):  # 头

#     color((255, 155, 192), "pink")

#     penup()

#     goto(x, y)

#     setheading(0)

#     pendown()

#     begin_fill()

#     setheading(180)

#     circle(300, -30)

#     circle(100, -60)

#     circle(80, -100)

#     circle(150, -20)

#     circle(60, -95)

#     setheading(161)

#     circle(-300, 15)

#     penup()

#     goto(-100, 100)

#     pendown()

#     setheading(-30)

#     a = 0.4

#     for i in range(60):

#         if 0 <= i < 30 or 60 <= i < 90:

#             a = a + 0.08

#             lt(3)  # 向左转3度

#             fd(a)  # 向前走a的步长

#         else:

#             a = a - 0.08

#             lt(3)

#             fd(a)

#     end_fill()


# def ears(x, y):  # 耳朵

#     color((255, 155, 192), "pink")

#     penup()

#     goto(x, y)

#     pendown()

#     begin_fill()

#     setheading(100)

#     circle(-50, 50)

#     circle(-10, 120)

#     circle(-50, 54)

#     end_fill()

#     penup()

#     setheading(90)

#     forward(-12)

#     setheading(0)

#     forward(30)

#     pendown()

#     begin_fill()

#     setheading(100)

#     circle(-50, 50)

#     circle(-10, 120)

#     circle(-50, 56)

#     end_fill()


# def eyes(x, y):  # 眼睛

#     color((255, 155, 192), "white")

#     penup()

#     setheading(90)

#     forward(-20)

#     setheading(0)

#     forward(-95)

#     pendown()

#     begin_fill()

#     circle(15)

#     end_fill()

#     color("black")

#     penup()

#     setheading(90)

#     forward(12)

#     setheading(0)

#     forward(-3)

#     pendown()

#     begin_fill()

#     circle(3)

#     end_fill()

#     color((255, 155, 192), "white")

#     penup()

#     seth(90)

#     forward(-25)

#     seth(0)

#     forward(40)

#     pendown()

#     begin_fill()

#     circle(15)

#     end_fill()

#     color("black")

#     penup()

#     setheading(90)

#     forward(12)

#     setheading(0)

#     forward(-3)

#     pendown()

#     begin_fill()

#     circle(3)

#     end_fill()


# def cheek(x, y):  # 腮

#     color((255, 155, 192))

#     penup()

#     goto(x, y)

#     pendown()

#     setheading(0)

#     begin_fill()

#     circle(30)

#     end_fill()


# def mouth(x, y):  # 嘴

#     color(239, 69, 19)

#     penup()

#     goto(x, y)

#     pendown()

#     setheading(-80)

#     circle(30, 40)

#     circle(40, 80)


# def setting():  # 参数设置

#     pensize(4)

#     hideturtle()  # 使乌龟无形（隐藏）

#     colormode(255)  # 将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内

#     color((255, 155, 192), "pink")

#     setup(840, 500)

#     speed(10)


# def main():

#     setting()  # 画布、画笔设置

#     nose(-100, 100)  # 鼻子

#     head(-69, 167)  # 头

#     ears(0, 160)  # 耳朵

#     eyes(0, 140)  # 眼睛

#     cheek(80, 10)  # 腮

#     mouth(-20, 30)  # 嘴

#     done()


# if __name__ == '__main__':

#     main()
