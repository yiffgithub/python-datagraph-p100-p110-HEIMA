import  turtle,time

# membuat objek turtle
pen = turtle.Turtle()
pen.speed(0)
#
# for i in range(10000000):
#     pen.forward(300-i)
#     pen.left(91)
#
# pen.write('Hello, world!', font=('Arial', 24, 'normal'))
from my_package import my_tools
n=0
while True:

    times= my_tools.get_current_time()
    print(times)
    pen.write(times, font=('Arial', 24, 'normal'))
    time.sleep(1)
    n+=1
    pen.clear()
    if times[-2:]=='00':
            turtle.bye()

    elif n==5:
        #关闭页面
        turtle.bye()




input()