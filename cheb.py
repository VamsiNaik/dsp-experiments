import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
wp=0.35*np.pi
ws=0.7*np.pi
ds=0.1
dp=0.6
T=0.1
e=np.sqrt(((1.0/dp**2))-1.0))
def analog(wp,ws):
	Ap=((2/T)*np.tan(wp/2))
	As=((2/T)*np.tan(ws/2))
	return Ap,As
A=analog(wp,ws)
Ap=A[0]
print('op=',Ap)
As=A[1]
print('os=',As)
def order(ds,dp,As,Ap):
	x1=((1.0/(ds**2))-1.0)
	x2=((1.0/(ds**2))-1.0)
	x3=(x1/x2)
	y=(np.arccosh(x3)/np.arccosh(As/Ap))
	return y
N=order(ds,dp,As,Ap)
n2=np.ceil(N)
print "order=",n2
def tf(Ac,n2,T,e):
	k=(n2/2)
	j=cm.sqrt(-1)
	k1=1/n2
	yn1=((np.sqrt(1+(e**(-2))))+(e**(-1)))**(k1)
	yn2=((np.sqrt(1+(e**(-2))))+(e**(-1)))**(-k1)
	yn=0.5*(yn1-yn2)
	cs=(np.cos((((2*k)-1)*np.pi)/(2*n2)))**(2)
	ck=(yn**(2))+cs
	bk=(2*np.sin((((2*k)-1)*np.pi)/(2*n2)))*yn
	e1=(1/(np.sqrt(1+(e**(2)))))
	w=np.arange(0,np.pi,0.01)
	z=np.exp(j*w)
	s=(2/T)*((1-z**(-1))/(1+z**(-1)))
	y1=e1*(Ap**(2))*ck
	y2=((s**(2))+(bk*Ap*s)+(Ap**(2))*ck))
	y=y1/y2
	return y
hs=tf(Ac,n2,T,e)
w=np.arange(0,np.pi,0.01)
plt.xlabel('frequency')
plt.ylabel('magnitude|H(e**(jw)|')
plt.title('low pass filter')
plt.plot(w,np.abs(hs))
plt.show()

