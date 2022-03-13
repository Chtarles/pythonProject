''' Metodo de Newton para computar o zero de uma funcao
Entradas: f,df, eps, itmax, x0
saida: [raiz, iter, erraval]'''
from math import *

def newton(f,df,x0,eps,itmax):
    L = range(1,itmax+1)
    iteracao = 0
    a=x0
    for i in L:
        raiz=a
        if df(raiz) != 0: # se a derivada for zero sai
            raiz=raiz-f(raiz)/df(raiz)
            erro=raiz-a
            a=raiz
            iteracao=i
        else:
            iteracao = itmax+1
            break
        if abs(erro) <= eps:
            break
    if iteracao > itmax:
        iteracao = 0.25
    elif iteracao == itmax:
        iteracao = 0.75
    return [raiz, erro, iteracao]

# teste :
f= lambda x: x**2 -20
df= lambda x: 2*x

L=newton(f,df,1.5,0.0001,100)

print(L)