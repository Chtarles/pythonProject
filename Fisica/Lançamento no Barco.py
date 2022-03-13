#from typing import Union, Any

from vpython import*

cena = canvas(width=500, height=500, center=vector(10, 10, 0), title='Lançando equipamento de ancoragem')

pxi = 0
pyi = 8.75
vi = 15
ang = 60
py = pyi

barco = sphere(pos=vector(38.5,0.5,0),radius=2, make_trail=True, trail_radius=0.1)
p1 = sphere(pos=vector(pxi, pyi, 0), radius=0.5, make_trail=True, trail_radius=0.1)
ex = arrow(canvas=cena, pos=vector(0, 0, 0), axis=vector(50, 0, 0), shaftwidth=0.2, color=color.red)
ey = arrow(canvas=cena, pos=vector(0, 0, 0), axis=vector(0, 20, 0), shaftwidth=0.2, color=color.blue)

gr = graph(width=400, height=400, title='Trajetória do objeto', foreground=color.black, background=color.black)
g1 = gcurve(graph=gr)

t = 0
dt = 0.01
tb = 1
dtb = 0.01
barco.vel = vector(4.5,0,0)


while t <= 5:
    if py >= 0:
        rate(100)
        vxi = vi * cos(radians(ang))
        vyi = vi * sin(radians(ang))

        px = pxi + vxi * t
        py = pyi + vyi * t - 0.5 * 9.8 * t ** 2

        #g1.plot(px, py, color=color.cyan)

        p1.pos = vector(px, py, 0)
        t = t + dt

        tb = tb + dtb
        barco.pos = barco.pos + (-barco.vel * dtb)


        # label(canvas = cena, pos = vec(10,-4,0), box = False, text='(t,px,py)=({:.1f},{:.1f},{:.1f})'.format(t,px,py))
    else:
        label(canvas=cena, pos=vec(10, -4, 0), box=False, text='(tempo decorrido:{:.1f}s,Posição de Colisão:{:.1f}m )'.format(t, px))
        label(canvas=cena, pos=vec(10, -10, 0), box=False, text='Objeto no Barco!')
        break