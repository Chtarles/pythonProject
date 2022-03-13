### Importanto as Bibliotecas
from vpython import * #Importar a biblioteca visual para o Python.
import numpy as np    #Importar a biblioteca utilizada para cálculos.
### Carácterísticas da Cena
cena = canvas(
                title='Colisões', # Criar o palco onde ocorrerá o movimento
                width=800, height=400,                   # Tamanho da imagem
                userzoom = False,                        # O usuário não pode aproximar ou afastar a câmera
                userspin = True,                         # O usuário pode girar a câmera.
                      up = vec(0,1,0),                   # Determina a posição UP.
                ambient  = color.gray(.3),               # Cor da iluminação dos objetos
                  center = vector(0,0,0),                # Posição central do código
              background = vec(.6,.9,.6)                 # Cor do background
         )
# Características do Plano.

inclinacao = np.divide(45*np.pi,180)                         # Ângulo em radianos.
axisp = vec(np.cos(inclinacao),np.sin(inclinacao),0)         # Vetor onde ocorre o movimento

suporte=box(
             pos=carro2.pos-vec(0,2,0),    # Posição relativao ao eixo principal
          length = 10, height=.1, width=1,      # Tamanho do suporte
           color = color.white,                # cor do objeto
          atrito = .006
           )

suporte.rotate(
               origin = vec(0,0,0),
                angle = inclinacao,           # Informação de rotação do objeto
                 axis = vec(0,0,1),           # Eixo de Rotação
              )

sup=box(
         pos = vec(np.cos(inclinacao)*suporte.length/2,np.sin(inclinacao)*suporte.length/2,0),     # Posição do apoio
      length = .3, height=.45, width=1,                                                            # Suporte da mesa
       color = color.white,                                                                        # cor do objeto
        )

sup.rotate(
             angle = inclinacao,           # Informação de rotação do objeto
          #  origin = vec(0,0,0),
              axis = vec(0,0,1)             # Eixo de Rotação
            )

Carro1 = box(                                 # Cria o objeto carro, correspondente a massa
     length = 1.5,height=.4, width=.5,       # Tamanho da massa
                pos = vec(1,0,0),            # Posição inicial do centro do objeto
                vel = vec(0,0,0),            # Velocidade inicial do objeto
              massa = 7,                     # Massa do objeto
              color = color.cyan             # Cor do Objeto
           )

carro1.rotate(
              angle = inclinacao,             # Informação par a rotação  do objeto
               axis = vec(0,0,1)              # Eixo em que o objeto gira
             )

carro2 = box(                                 # Cria o objeto carro, correspondente a massa
     length = 1.5,height=.4, width=.5,       # Tamanho da massa
                pos = vec(-1,0,0),            # Posição inicial do centro do objeto
                vel = vec(0,0,0),            # Velocidade inicial do objeto
              massa = 7,                     # Massa do objeto
              color = color.cyan             # Cor do Objeto
           )

carro2.rotate(
              angle = inclinacao,             # Informação par a rotação  do objeto
               axis = vec(0,0,1)              # Eixo em que o objeto gira
             )



mola = True
if mola is True:
    mola=helix(
          length0 = suporte.length/2,                        # Tamanho original da mola e tamanho
           length = suporte.length,                        # Tamanho da mola comprimida/exticada
              pos = vec(np.cos(inclinacao)*suporte.length/2,np.sin(inclinacao)*suporte.length/2,0),
             radius = 0.1,                    # Raio da mola
             k = 8,                          # Constante de Hook da mola
             thickness = 0.08,                # espessura
             coils = 12,                      # Número de voltas
             color = color.red                # Cor do objeto
           )

mola.rotate(
              angle =np.pi+inclinacao,          # Informação par a rotação  do objeto
              axis= vec(0,0,1)                  # Eixo em que o objeto gira
             )
