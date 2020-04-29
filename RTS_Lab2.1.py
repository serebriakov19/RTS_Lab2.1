# Лабораторна робота №2.1
# Серебряков Роман, ІО-71
# Варіант №22
# Число гармонік в сигналі n = 10
# Гранична частота, w_max = 1200
# Кількість дискретних відліків, N = 64

import random as r
import math
import matplotlib.pyplot as plt

n = 10
w_max = 1200
N = 64
w_real = [[math.cos(2 * math.pi * i * j / N) for j in range(N)] for i in range(N)]
w_imag = [[math.sin(2 * math.pi * i * j / N) for j in range(N)] for i in range(N)]


x = [0] * N

for i in range(n):
    A = r.randrange(2)
    W = r.randrange(w_max)
    f = r.randrange(1000000)
    for t in range(N):
        x[t] += A * math.sin(W * t + f)


def disc_fourier_transf(x: list):
    result = [[sum(w_real[p][k] * x[k] for k in range(N)), sum(w_imag[p][k] * x[k] for k in range(N))] for p in range(N)]
    return result


dft = disc_fourier_transf(x)
x_list = []
dft_list = []

for i in range(len(x)):
    x_list.append(x[i])
    a = math.sqrt(dft[i][0] ** 2 + dft[i][1] ** 2)
    dft_list.append(a)

plt.plot([i for i in range(len(x_list))], x_list)
plt.show()

plt.plot([i for i in range(len(dft_list))], dft_list)
plt.show()
