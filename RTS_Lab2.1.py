# Лабораторна робота №2.1
# Серебряков Роман, ІО-71
# Варіант №22
# Число гармонік в сигналі n = 10
# Гранична частота, w_max = 1200
# Кількість дискретних відліків, N = 64

# Додаткове завдання: реалізувати "табличний" метод

import random as r
import math
import matplotlib.pyplot as plt
import numpy as np
import datetime

n = 10
w_max = 1200
N = 64


def dft_matrix(N):
    i, j = np.meshgrid(np.arange(N), np.arange(N))
    return np.power(np.exp(- 2 * math.pi * 1J / N), i * j) / math.sqrt(N)


# Порівняння часу виконання звичайного методу та "табличного" для 4 <= N <= 640
def_times = []
table_times = []

for N_var in range(4, N*10+1, 16):
    default = datetime.datetime.now()
    w_real = [[math.cos(2 * math.pi * i * j / N_var) for j in range(N_var)] for i in range(N_var)]
    w_imag = [[math.sin(2 * math.pi * i * j / N_var) for j in range(N_var)] for i in range(N_var)]
    default = datetime.datetime.now() - default
    def_times.append(default.total_seconds() * (10 ** 6) + default.microseconds)

    table = datetime.datetime.now()
    dft_matrix(N_var)
    table = datetime.datetime.now() - table
    table_times.append(table.total_seconds() * (10 ** 6) + table.microseconds)

plt.plot([n for n in range(4, N*10+1, 16)], def_times)
plt.show()
plt.plot([n for n in range(4, N*10+1, 16)], table_times)
plt.show()
exit(0)


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
