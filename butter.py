import numpy as np
import matplotlib.pyplot as plt
w=np.arange(0,10000)
dp=input("Enter the passband gain of the filter:")
ds=input("Enter the stopband gain of the filter:")
fp=input("Enter the passband cut-off frquency:")
fs=input("Enter the stopband cut-off frquency:")
#ws=2*np.pi*fs
#wp=2*np.pi*fp
a=(1/np.float(ds**2))-1
b=(1/np.float(dp**2))-1
N=np.ceil((np.log10(np.sqrt(a/np.float(b))))/np.float(np.log10(fs/fp)))
print "The order of the filter is:%d"%(N)
wc=(fs)/np.float(a**(1/(2*N)))
print "The cut-off frequency of the filter is:%f"%(wc)
v=np.abs(1/((1+(w/np.float(wc))**(2*N))**0.5))
plt.plot(w,v)
plt.show()
