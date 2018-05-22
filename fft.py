import numpy as np
import matplotlib.pyplot as plt
import time

N=2048
print 'N = %d' % N
t = np.arange(0, N)
C = np.sin(2*np.pi*t/N)
t1 = time.time()
F = np.fft.fft(C)
t2 = time.time()
F=np.abs(F)**2
plt.plot(t,F)
plt.show()
print '(1)time: %f' %(t2 - t1)

t = np.arange(0, N)
C2 = np.sin(2*np.pi*t/N * 10)
t1 = time.time()
F2 = np.fft.fft(C2)
t2 = time.time()
F2 = np.abs(F2)**2
plt.plot(t,F2)
plt.show()
print '(2)time: %f' %(t2 - t1)

t = np.arange(0, N)
C3 = np.sin(2*np.pi*t/N)+np.sin(2*np.pi*t/N * 10)
t1 = time.time()
F3 = np.fft.fft(C3)
t2 = time.time()
F3=np.abs(F3)**2
plt.plot(t,F3)
plt.show()
print '(3)time: %f' %(t2 - t1)
