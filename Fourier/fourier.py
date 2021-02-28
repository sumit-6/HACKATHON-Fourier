from turtle import *
import numpy as np
import math
decision = int(input("Enter '0' if you want to plot cosine series or '1' if you want to plot sine series of rectangular wave: "))
N = int(input("Enter number of terms of the fourier series you want to plot: "))
a = int(input("Enter the value of 'a' in order to plot the series from x = '-a' to x = 'a' : "))
hideturtle()
def bluelines():
    screensize(2000,2000)
    hideturtle()
    speed(0)
    color('pink')
    for i in range(31):
        pu()
        goto(-15+i,-15)
        pd()
        goto(-15+i,15)
        pu()
    for j in range(31):
        pu()
        goto(-15,-15+j)
        pd()
        goto(15,-15+j)
        pu()
def setup():
    screensize()
    p=1
    hideturtle()
    speed(0)
    setworldcoordinates(-7,-7,7,7)
    setpos(0,0)
    clear()
    bluelines()
    setpos(0,0)
    setheading(0)
    pd()
    color('black')
    for i in range(15):
        setpos(0,0)
        fd(p)
        write(p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(-p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(-p)
        lt(90)
        p=p+1
setup()

def function_x(x,n):
    R = 4/(math.pi*((2*0)+1))
    Q = 4/(math.pi*((2*0)+1))
    sum = R*(math.cos((R/Q)*x))
    for i in range(1,n,1):
        Q = 4/(math.pi*((2*i)+1))
        sum = sum + Q*(math.cos((R/Q)*x))
    return sum

def function_y(x,n):
    R = 4/(math.pi*((2*0)+1))
    Q = 4/(math.pi*((2*0)+1))
    sum = R*(math.sin((R/Q)*x))
    for i in range(1,n,1):
        Q = 4/(math.pi*((2*i)+1))
        sum = sum + Q*(math.sin((R/Q)*x))
    return sum


if (decision == 0):
    x=-a
    dx=0.05
    while x<=a:
        x+=dx
        hideturtle()
        pensize(3)
        screensize(2000,2000)
        color('orange')
        def draw_1(matA):
                pu()
                speed(0)
                goto(x,function_x(x,N))
                pd()
                for point in matA:
                    speed(0)
                    goto(point[0],point[1])
        try:
            ayush=[[x+dx,function_x(x+dx,N)]]
            draw_1(ayush)
        except(ValueError,ZeroDivisionError,TypeError):
            continue

elif (decision == 1):
    x=-a
    dx=0.02
    while x<=a:
        x+=dx
        hideturtle()
        pensize(3)
        screensize(2000,2000)
        color('red')
        def draw_1(matA):
                pu()
                speed(0)
                goto(x,function_y(x,N))
                pd()
                for point in matA:
                    speed(0)
                    goto(point[0],point[1])
        try:
            ayush=[[x+dx,function_y(x+dx,N)]]
            draw_1(ayush)
        except(ValueError,ZeroDivisionError,TypeError):
            continue
else:
    print("You have entered wrong input!!!")

