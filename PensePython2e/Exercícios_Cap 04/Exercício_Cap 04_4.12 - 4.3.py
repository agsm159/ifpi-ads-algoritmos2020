import turtle
import math

def draw_pie(t, n, r):
    polypie(t, n, r)
    t.pu()
    t.fd(r * 2 + 10)
    t.pd()

def polypie(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        isoceles(t, r, angle / 2)
        t.lt(angle)

def isoceles(t, r, angle):
    x = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90 + angle)
    t.fd(2 * x)
    t.lt(90 + angle)
    t.fd(r)
    t.lt(180 - angle)

def main():
    luke = turtle.Turtle()

    luke.pu()
    luke.bk(110)
    luke.pd()

    size = 80
    draw_pie(luke, 5, size)
    draw_pie(luke, 6, size)
    draw_pie(luke, 7, size)

    luke.hideturtle()
    turtle.mainloop()

main()
