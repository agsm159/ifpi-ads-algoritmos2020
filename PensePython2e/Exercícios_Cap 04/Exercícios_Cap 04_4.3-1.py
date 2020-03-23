import turtle

bob = turtle.Turtle()
bob.shape('turtle')
bob.color('red')

def square(t):
    for i in range(4):
       t.fd(100)
       t.lt(90)

    turtle.mainloop()


square(bob)

