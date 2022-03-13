from vpython import *

cena = canvas(title='Lançamento Oblíquo', width=800, height=400,
              center=vector(10, 5, 5), autoscale=False)

ex = arrow(canvas=cena, pos=vector(0, 0, 0), axis=vector(30, 0, 0), shaftwidth=0.1)
ey = arrow(canvas=cena, pos=vector(0, 0, 0), axis=vector(0, 10, 0), shaftwidth=0.1)
# ez = arrow(canvas = cena, pos=vector(0,0,0), axis=vector(0,0,20), shaftwidth=0.1)

ball = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.yellow, make_trail=True, trail_radius=0.1)
pointer = arrow(canvas=cena, pos=vector(0, 0, 0), axis=vector(0, 0, 0), shaftwidth=0.1, color=color.blue)

pox = arrow(canvas=cena, pos=vector(0, 0, 0), axis=vector(0, 0, 0), shaftwidth=0.1, color=color.red)
poy = arrow(canvas=cena, pos=vector(0, 0, 0), axis=vector(0, 0, 0), shaftwidth=0.1, color=color.red)

t = 0
dt = 0.001
vi = 20
xi = 0
yi = 0
ang = radians(30)

while t <= 20:
    rate(300)

    if (ball.pos.y >= 0):

        ball.pos.x = xi + vi * cos(ang) * t
        ball.pos.y = yi + vi * sin(ang) * t - 4.9 * t ** 2

        pointer.pos.x = ball.pos.x
        pointer.pos.y = ball.pos.y

        pox.pos.x = ball.pos.x
        pox.pos.y = ball.pos.y

        poy.pos.x = ball.pos.x
        poy.pos.y = ball.pos.y

        vx = vi * cos(ang)
        vy = vi * sin(ang) - 9.8 * t

        pox.axis.x = vx
        poy.axis.y = vy

        pointer.axis.x = vx
        pointer.axis.y = vy

        t += dt

    else:
        label(pos=vec(0, -5, 0), text='Atingiu o solo!', box=False)
        label(pos=vec(0, -6, 0), text='R = {:.1f}'.format(ball.pos.x), box=False)
        label(pos=vec(0, -7, 0), text='t = {:.2f}'.format(t), box=False)
