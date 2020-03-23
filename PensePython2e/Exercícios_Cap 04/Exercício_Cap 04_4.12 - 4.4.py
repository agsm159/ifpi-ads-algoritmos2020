import turtle
import math


def circle(t, r):
    arc(t, r, 360)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()

def fdlt(t, n, angle=90):
    fd(t, n)
    lt(t, angle)

def fdbk(t, n):
    fd(t, n)
    bk(t, n)

def skip(t, n):
    pu(t)
    fd(t, n)
    pd(t)

def stump(t, n, angle=90):
    lt(t)
    fd(t, n)
    rt(t, angle)

def hollow(t, n):
    lt(t)
    skip(t, n)
    rt(t)

def post(t, n):
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, altura):
    hollow(t, n * altura)
    fdbk(t, n)
    hollow(t, -n * altura)

def hangman(t, n, altura):
    stump(t, n * altura)
    fdbk(t, n)
    lt(t)
    bk(t, n * altura)
    rt(t)

def diagonal(t, a, b):
    angle = math.atan2(b, a) * 180 / math.pi
    dist = math.sqrt(a ** 2 + b ** 2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, altura):
    diagonal(t, -n / 2, altura * n)
    diagonal(t, n / 2, altura * n)


def bump(t, n, altura):
    stump(t, n * altura)
    arc(t, n / 2.0, 180)
    lt(t)
    fdlt(t, n * altura + n)


def draw_a(t, n):
    diagonal(t, n / 2, 2 * n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n / 2, 2 * n)

def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n / 2)

def draw_c(t, n):
    hangman(t, n, 2)
    fd(t, n)

def draw_d(t, n):
    bump(t, 2 * n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    fd(t, n)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    fd(t, n / 2)
    beam(t, n / 2, 2)
    fd(t, n / 2)
    post(t, n)

def draw_h(t, n):
    post(t, 2 * n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2 * n)

def draw_i(t, n):
    beam(t, n, 2)
    fd(t, n / 2)
    post(t, 2 * n)
    fd(t, n / 2)

def draw_j(t, n):
    beam(t, n, 2)
    arc(t, n / 2, 90)
    fd(t, 3 * n / 2)
    skip(t, -2 * n)
    rt(t)
    skip(t, n / 2)

def draw_k(t, n):
    post(t, 2 * n)
    stump(t, n, 180)
    vshape(t, 2 * n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2 * n)
    fd(t, n)

def draw_n(t, n):
    post(t, 2 * n)
    skip(t, n)
    diagonal(t, -n, 2 * n)
    post(t, 2 * n)

def draw_m(t, n):
    post(t, 2 * n)
    draw_v(t, n)
    post(t, 2 * n)

def draw_o(t, n):
    skip(t, n)
    circle(t, n)
    skip(t, n)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n / 2)

def draw_q(t, n):
    draw_o(t, n)
    diagonal(t, -n / 2, n)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n / 2, n)

def draw_s(t, n):
    fd(t, n / 2)
    arc(t, n / 2, 180)
    arc(t, n / 2, -180)
    fdlt(t, n / 2, -90)
    skip(t, 2 * n)
    lt(t)

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n / 2)
    post(t, 2 * n)
    skip(t, n / 2)

def draw_u(t, n):
    post(t, 2 * n)
    fd(t, n)
    post(t, 2 * n)

def draw_v(t, n):
    skip(t, n / 2)
    hangman(t, n, 2)
    skip(t, n / 2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2 * n)
    skip(t, n)
    diagonal(t, -n, 2 * n)

def draw_v(t, n):
    skip(t, n / 2)
    diagonal(t, -n / 2, 2 * n)
    diagonal(t, n / 2, 2 * n)
    skip(t, n / 2)

def draw_y(t, n):
    skip(t, n / 2)
    stump(t, n)
    hangman(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n / 2)

def draw_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2 * n)
    fd(t, n)

def draw_(t, n):
    skip(t, n)

def main():
    size = 20
    mi = turtle.Turtle()

    for f in [draw_h, draw_e, draw_l, draw_l, draw_o]:
        f(mi, size)
        skip(mi, size)

    mi.hideturtle()
    turtle.mainloop()

main()
