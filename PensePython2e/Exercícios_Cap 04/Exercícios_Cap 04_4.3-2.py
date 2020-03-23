import turtle

tom = turtle.Turtle()
tom.shape('turtle')

#Montagem de quadrados.
def square(t, leigth):
    for i in range(4):
        t.fd(leigth)
        t.lt(90)

    turtle.mainloop()

square(tom, 100)
