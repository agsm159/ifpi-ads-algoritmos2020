import turtle
import math

john = turtle.Turtle()
john.shape('turtle')

def polygon(t, n, leigth):
    angle = 360/n
    for i in range(n):
        t.fd(leigth)
        t.lt(angle)

    turtle.mainloop()

#Para montagem da circuferência.
def circle(t, r):
    circunferência = 2 * math.pi * r
    n = int(circuferência / 3) + 1
    leigth = circunferência / n
    polygon(t, n, length)

polygon(john, n = 50, leigth = 10)
