import turtle
import math

def polyline(t, n , leigth, angle):
    for i in range(n):
        t.fd(leigth)
        t.lt(angle)

def polygon(t, n , leigth):
    angle = 360 / n
    polyline(t, n, leigth, angle)

def arc(t, r, angle):
    arc_leigth = 2 * math.pi * r * angle / 360
    n = int(arc_leigth / 3) +1
    step_leigth = arc_leigth / n
    step_angle = float(angle) / n
    polyline(t, n, step_leigth, step_angle)

def circle(t, r):
    arc(t, r, 360)

def main():
    yuki = turtle.Turtle()
    radius = 100
    yuki.pu()
    yuki.fd(radius)
    yuki.lt(90)
    yuki.pd()
    circle(yuki, radius)

    turtle.mainloop()

main()
