from vpython import*

cena = canvas(title='Oscilador de Duas Molas', width=800, height=600, center=vector(5, 0, 0), background=color.black)

t = 0
dt = 0.01
A = 6
w1 = 1
o = radians(0)
w2 = 2

epx = A * cos(w1 * t + o)
epy = A * sin(w2 * t + o)

esfera = sphere(canvas=cena, pos=vector(epx, 10 + epy, 0), radius=1, color=color.yellow, make_trail=True, trail_radius=0.1)

molaparede = helix(canvas=cena, pos=vector(10, 10, 0), axis=vector(0, 0, 0), coils=5)
placaparede = box(canvas=cena, pos=vector(10, 10, 0), size=vector(0.5, 5, 5), color=color.green)

molapiso = helix(canvas=cena, pos=vector(0, 0, 0), axis=vector(0, 0, 0), coils=5)
placapiso = box(canvas=cena, pos=vector(0, 0, 0), size=vector(5, 0.5, 5), color=color.cyan)

while True:
    rate(200)
    epx = A * cos(w1 * t + o)
    epy = A * sin(w2 * t + o)
    esfera.pos.x = epx
    esfera.pos.y = 10 + epy

    molaparede.axis.x = -10 + epx
    molaparede.axis.y = epy

    molapiso.axis.x = epx
    molapiso.axis.y = 10 + epy
    t = t + dt