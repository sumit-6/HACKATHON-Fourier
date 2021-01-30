from turtle import *
import numpy as np
import math
hideturtle()
def function_a(x):
    R=4/(math.pi)
    Q=4/(3*(math.pi))
    S=4/(5*(math.pi))
    T=4/(7*(math.pi))
    U=4/(9*math.pi)
    V=4/(11*math.pi)
    W=4/(13*math.pi)
    X=4/(15*math.pi)
    f=100*(R*math.cos(x)+Q*math.cos((R/Q)*x)+S*math.cos((R/S)*x)+T*math.cos((R/T)*x)+U*math.cos((R/U)*x)+V*math.cos((R/V)*x)+W*math.cos((R/W)*x)+X*math.cos((R/X)*x))
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
    f=100*(R*math.sin(x)+Q*math.sin((R/Q)*x)+S*math.sin((R/S)*x)+T*math.sin((R/T)*x)+U*math.sin((R/U)*x)+V*math.sin((R/V)*x)+W*math.sin((R/W)*x)+X*math.sin((R/X)*x))
    return f

def fun_a(x):
    f=function_a(x)
    return f
def fun_b(x):
    f=function_b(x)
    return f

screensize(2000,2000)

a=15
x=-15
dx=0.01
while x<=a:
    x+=dx
    hideturtle()
    pensize(1)
    screensize(2000,2000)
    color('green')
    def draw_1(matA):
            pu()
            speed(0)
            goto(fun_a(x),fun_b(x))
            pd()
            for point in matA:
                speed(0)
                goto(point[0],point[1])
    try:
        ayush=[[fun_a(x+dx),fun_b(x+dx)]]
        draw_1(ayush)
    except(ValueError,ZeroDivisionError,TypeError):
        continue
