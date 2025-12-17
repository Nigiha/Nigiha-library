import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0, 50, 0.001)
def f(y, dydx, x):
    return -np.sin(y) #微分方程式

x=np.arange(0, 50, 0.001)
def g(y, dydx, x):
    return -y

def RK4_secondoder(f, x):
    dx=x[1]-x[0]
    N=len(x)
    dydx=np.zeros(N)
    y=np.zeros(N)
    dydx[0]=1.0 #初期条件
    y[0]=0.0
    for i in range(N-1):
        k1=dydx[i]
        l1=f(y[i], dydx[i], x[i])
        k2=dydx[i]+dx/2*l1
        l2=f(y[i]+dx/2*k1, dydx[i]+dx/2*l1, x[i]+dx/2)
        k3=dydx[i]+dx/2*l2
        l3=f(y[i]+dx/2*k2, dydx[i]+dx/2*l2, x[i]*dx/2)
        k4=dydx[i]+dx*l3
        l4=f(y[i]+dx*l3, dydx[i]+dx*l3, x[i]+dx)
        y[i+1]=y[i]+dx*(k1+2*k2+2*k3+k4)/6.0
        dydx[i+1]=dydx[i]+dx*(l1+2*l2+2*l3+l4)/6.0
    return y, dydx

plt.figure()
plt.title("pendulum solution (l/g=1)")
plt.plot(x, RK4_secondoder(f, x)[0], color="red", label="actual_solution")
plt.plot(x, RK4_secondoder(g, x)[0], color="blue", label="approximate_solution")
plt.legend()
plt.show()
