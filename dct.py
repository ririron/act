import numpy as np
import matplotlib.pyplot as plt
import time

def dct ( x, N):
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        re = 0
        im = 0
        for n in range(N-1):
            re += x[n] * np.cos(-2*np.pi*k*n/N)
            im += x[n] * np.sin(-2*np.pi*k*n/N)
        X[k] = complex(re, im)
    return X



N = 2048
print 'N = %d' % N
t = np.arange(0, N)
C = np.sin(2*np.pi*t/N)
t1 = time.time()
C = dct(C, N)
t2 = time.time()
C = np.abs(C)**2
plt.plot(t, C, marker = 'o')
plt.show()
print '(1)time: %f' %(t2 - t1)

C2 = np.sin(2*np.pi*t/N)+np.sin(2*np.pi*t/N * 10)
t1 = time.time()
C2 = dct(C2, N)
t2 = time.time()
C2 = np.abs(C2)**2
plt.plot(t, C2, marker = 'o')
plt.show()
print '(2)time: %f' %(t2 - t1)

C3 = np.sin(2*np.pi*t/N)+np.sin(2*np.pi*t/N * 10) +np.sin(2*np.pi*t/N * 20)/5
t1 = time.time()
C3 = dct(C3, N)
t2 = time.time()
C3 = np.abs(C3)**2
plt.plot(t, C3, marker = 'o')
plt.show()
print '(3)time: %f' %(t2 - t1)
