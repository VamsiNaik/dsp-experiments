import numpy as np
import matplotlib.pyplot as plt
x=input("Enter first signal : ")
n=len(x)
h=x[::-1]
print "the timereversal of x[n] is:"
print h
y=np.zeros(2*n-1)
for i in range(n):
	for j in range(n):
		y[i+j]=y[i+j]+x[i]*h[j]
print "The autocorrelation is given by:"
print y
for i in range(n-1):
	x.append(0)
t=np.linspace(0,2*n-2,2*n-1)
plt.subplot(211)
plt.stem(t,x)
plt.subplot(212)
plt.stem(t-n+1,y)
plt.show()
