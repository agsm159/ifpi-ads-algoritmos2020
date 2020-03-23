import turtle

kakaroto = turtle.Turtle()
kakaroto.shape('turtle')

#Código para fazer poligonos.
def polygon(t, n, leigth):
    angle = 360/n
    for i in range(n):
        t.fd(leigth)
        t.lt(angle)

    turtle.mainloop()

polygon(kakaroto, n = 3, leigth = 50)
