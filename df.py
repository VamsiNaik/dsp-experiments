mport numpy as np
from matplotlib import pyplot as plt
import cmath as cm
x=[1,1,1,1]
N=input("Enter the number of DFT points: ")
h=cm.sqrt(-1)
k=np.arange(0,N)
n1=np.arange(0,N)

if len(x)<N:
    q =N-len(x)
    x=np.append(x,np.zeros(q))
    
Xk=[]
for i in k:
    sum=0;
    for j in n1:
        sum+=x[j]*np.exp((-h*2*np.pi*i*j)/(N))
    Xk=np.append(Xk,sum)
print Xk
print len(Xk)

