import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
wc=np.pi/4
n0=np.arange(-100,100,1)
h0=0.25*np.sinc(0.25*n0)
n=np.arange(-17,17,1)
h=0.25*np.sinc(0.25*n)
m=31
k=np.arange(0,m)
w=0.5-0.46*np.cos(2*np.pi*k/(m-1))
hw=[]
for i in range(m):
	p=h[i]*w[i]
	hw=np.append(hw,p)

def dtft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=10000
	n=len(x)
	p=np.linspace(-np.pi,np.pi,N)
	for i in range(0,N):
		w=p[i]
		sum=0
		for k in range(0,n):
			sum=sum+(x[k]*np.exp(-j*w*k))
		y.append(abs(sum))
	return y
N=10000
n1=np.linspace(-np.pi,np.pi,N)
t=dtft(hw)
t1=20*np.log(t)
plt.subplot(5,1,1)
plt.xlabel('----->M')
plt.ylabel('------>|x[k]|')
plt.title('sinc function')
plt.stem(h)
plt.subplot(5,1,2)
plt.xlabel('----->M')
plt.ylabel('------>|x[k]|')
plt.title('window')
plt.stem(k,w)
plt.subplot(5,1,3)
plt.xlabel('----->M')
plt.ylabel('------>|x[k]|')
plt.title('sinc x window function')
plt.stem(k,hw)
plt.subplot(5,1,4)
plt.xlabel('digital freq')
plt.ylabel('------>|x[k]|')
plt.title('Digital LPF')
plt.plot(n1,t)
plt.subplot(5,1,5)
plt.xlabel('digital freq')
plt.ylabel('------>|x[k]| in db')
plt.title('Digital LPF')
plt.plot(n1,t1)
plt.show()

