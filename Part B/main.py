import time
import ctypes
from numpy.ctypeslib import ndpointer
import numpy as np
import matplotlib.pyplot as plt

Cpp = ctypes.CDLL('./Source.so')
dft = Cpp.dft
dft.restype = None
dft.argtypes = [ndpointer(ctypes.c_double), ctypes.c_int]

fft = Cpp.fft

fft.restype = None
fft.argtypes = dft.argtypes

test_sample = []

N = []
Ts = []
dft_time = []
fft_time = []

for i in range(4, 14):
    N.append(2**(i))  # [4,5,6,7,8,9,10,11,12,13]
    Ts.append(1/2**(i))
    dft_time.append(0)
    fft_time.append(0)

for i in range(10):
    t = np.arange(0, 1+Ts[i], Ts[i])
    x = 1*np.cos(2*np.pi*3*t)
    y = -1*np.sin(2*np.pi*3*t)

    input = np.column_stack((x, y))
    dftoutput = input
    fftoutput = input

    startdft = time.time()*1000  # 1.5
    dft(dftoutput, N[i])
    enddft = time.time()*1000  # 1.6

    dft_time[i] = enddft - startdft

    startfft = time.time()*1000
    fft(fftoutput, N[i])
    endfft = time.time()*1000
    fft_time[i] = endfft - startfft

print(dft_time)
print(fft_time)

n = len(fftoutput)
sum = 0
for i in range(n):
    diff = fftoutput[i] - dftoutput[i]
    square_diff = diff**2
    sum += square_diff

MSE = sum/n
print(MSE)

plt.plot(N, dft_time, label='DFT')
plt.plot(N, fft_time, label='FFT')
plt.legend()
plt.xlabel('Number Of Samples')
plt.ylabel('Time')
plt.show()

plt.plot(fftoutput, dftoutput)
plt.xlabel('FFT')
plt.ylabel('DFT')
plt.show()
