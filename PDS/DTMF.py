import matplotlib.pyplot as plt
import numpy as np
import pyaudio

duracao = 1.5  # em segundos
f1 = 852
f2 = 1477  # 9
volume = 0.5  # intervalo [0.0, 1.0]

Fs = 44100  # frequencia de amostragem - DEVE SER INTEIRO
Ts = 1.0 / Fs  # intervalo de amostragem

t = np.arange(start=0, stop=duracao, step=Ts)  # vetor do tempo

round(f1)
round(f2)


y1 = np.sin(2 * np.pi * f1 * t)
y2 = np.sin(2 * np.pi * f2 * t)

y = y1 + y2

samples = y.astype(np.float32)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=Fs, output=True)
stream.write(volume * samples)
stream.stop_stream()
stream.close()
p.terminate()

# Som

n = len(y)  # tamanho do signal
k = np.arange(n)
T = n / Fs
frq = k / T  # dois lados do range de frequencia
frq = frq[np.arange(int(n / 2))]  # um lado do range de frequencia

Y = np.fft.fft(y) / n  # computando a Transformada de fourier e normalizando

Y = Y[range(int(n / 2))]

for c in range(4):
    for r in range(3):
        y = np.ndarray(f1[c], f2[r])

tons = np.zeros([len(y)])

for i in range(len(y)):
    tons[i, :] = (y1[i][0])

    tons[i, :] += (y2[i][1])

    tons[i, :] /= 2.1

# Teclado

D = 0  # tecla 1

D = 1  # tecla 2

D = 2  # tecla 3

D = 3  # tecla 4

D = 4  # tecla 5

D = 5  # tecla 6

D = 6  # tecla 7

D = 7  # tecla 8

D = 8  # tecla 9

D = 9  # tecla *

D = 10  # tecla 0

D = 11  # tecla #

tom = tons[D, :]

# plotando
fig, ax = plt.subplots(2, 1)

ax[0].plot(t[:1000], y[:1000])
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('y')

ax[1].plot(frq[:2500], abs(Y[:2500]), 'r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')

# SOM DTMF
plt.title('Tecla %d' % (D + 1))

plt.show()
