# Método da Dicotomia

from math import e
import numpy as np

# INGRESO
fx = lambda x: e**-x*(x-1/2)
#fx = lambda x: x ** 3 - x ** 2 - 1
a = 0
b = 2
tolera = 0.0001

# PROCEDIMENTO
tabela = []
intervalo = b - a

fa = fx(a)
fb = fx(b)
i = 1
while (intervalo > tolera):
    c = (a + b) / 2
    fc = fx(c)
    tabela.append([i, a, c, b, fa, fc, fb, intervalo])
    i = i + 1

    teste = np.sign(fa) * np.sign(fc)
    if (teste < 0):
        b = c
        fb = fc
    else:
        a = c
        fa = fc
    intervalo = b - a
c = (a + b) / 2
fc = fx(c)
tabela.append([i, a, c, b, fa, fc, fb, intervalo])
tabela = np.array(tabela)

raiz = c

# OUTPUT
np.set_printoptions(precision=4)
print('[ i, a, c, b, f(a), f(c), f(b), intervalo]')
# print(tabela)

# TABELA
n = len(tabela)
for i in range(0, n, 1):
    linha = tabela[i]
    formato = '{:.0f}' + ' ' + (len(linha) - 1) * '{:.3f} '
    linha = formato.format(*linha)
    print(linha)

print('raiz: ', raiz)
