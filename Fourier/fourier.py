from turtle import *
import numpy as np
import math
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

def function_a(x):
    R=4/(math.pi)
    Q=4/(3*(math.pi))
    S=4/(5*(math.pi))
    T=4/(7*(math.pi))
    U=4/(9*math.pi)
    V=4/(11*math.pi)
    W=4/(13*math.pi)
    X=4/(15*math.pi)
    f=R*math.cos(x)+Q*math.cos((R/Q)*x)+S*math.cos((R/S)*x)+T*math.cos((R/T)*x)+U*math.cos((R/U)*x)+V*math.cos((R/V)*x)+W*math.cos((R/W)*x)+X*math.cos((R/X)*x)
    return f
def function_b(x):
    R=4/(math.pi)
    Q=4/(3*(math.pi))
    S=4/(5*(math.pi))
    T=4/(7*(math.pi))
    U=4/(9*math.pi)
    V=4/(11*math.pi)
    W=4/(13*math.pi)
    X=4/(15*math.pi)
    f=R*math.sin(x)+Q*math.sin((R/Q)*x)+S*math.sin((R/S)*x)+T*math.sin((R/T)*x)+U*math.sin((R/U)*x)+V*math.sin((R/V)*x)+W*math.sin((R/W)*x)+X*math.sin((R/X)*x)
    return f

def fun_a(x):
    f=function_a(x)
    return f
def fun_b(x):
    f=function_b(x)
    return f

a=15
x=-15
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
            goto(x,fun_a(x))
            pd()
            for point in matA:
                speed(10)
                goto(point[0],point[1])
    try:
        ayush=[[x+dx,fun_a(x+dx)]]
        draw_1(ayush)
    except(ValueError,ZeroDivisionError,TypeError):
        continue


a=15
x=-15
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
            goto(x,fun_b(x))
            pd()
            for point in matA:
                speed(10)
                goto(point[0],point[1])
    try:
        ayush=[[x+dx,fun_b(x+dx)]]
        draw_1(ayush)
    except(ValueError,ZeroDivisionError,TypeError):
        continue
