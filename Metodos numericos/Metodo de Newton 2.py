#               Metodo de Newton

# importa o modulo math
import math

#cria a funcao(x) = x**3 - 9x + 3

def funcao (xo):

   return (pow(xo,3)) - (9 * xo) + 3

#cria a derivada da funcao(x). 3x**2 - 9

def funcaoLinha(xo):

   return (3 * math.pow(xo,2)) - 9

#Leitura dos dados
#Le o valor inicial de x

xo = float(raw_input("Digite o valor de x0: "))

#Le precisao 1
precisao1 = float(raw_input("Precisao1: "))

#Le precisao 2

precisao2 = float(raw_input("Precisao2: "))

print '\n'


if (math.fabs(funcao(xo))) < precisao1:

   xBarra = xo

else:

   k = 1

   flag = True

   while flag:

      x1 = xo - (funcao(xo) / funcaoLinha(xo))

      print "Iteracao: %d" % (k)

      print "Valor de X: %f" % (x1)

      print "f(x): %f" % (funcao(x1))

      print '\n'

      if (math.fabs(funcao(x1))) < precisao1 or (math.fabs(x1 - xo)) < precisao2:

         xBarra = x1

         flag = False

      xo = x1

      k = k + 1


#Resultado final. Valor de xBarra

print 'Valor de xBarra: %f' % (xBarra)