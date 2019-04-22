
import numpy as np
from matplotlib import pyplot as plt
#from scipy import signal as sgl
import cmath as cm
w=np.linspace(-np.pi,np.pi,10000)
x=[1,2,3,4]
l=len(x)
n=0
j=cm.sqrt(-1)
X_w=0
for n in range(l):
    X_w+=(x[n]*np.exp(-j*w*n))
plt.plot(w,X_w)
plt.show()
X_mgtd=np.abs(X_w)
X_phase=np.angle(X_w)
plt.plot(w,X_mgtd)
plt.show()
plt.plot(w,X_phase)
plt.show()
