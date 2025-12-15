import numpy as np

#1変数1階微分
def RK4_firstorder(f, x):
    dx=x[1]-x[0]
    N=len(x)
    y=np.zeros(N)
    y[0]=0.0 #初期条件
    for i in range(N):
        k1=f(y[i], x[i])
        k2=f(y[i]+k1*(dx/2), x[i]+dx/2)
        k3=f(y[i]+k2*(dx/2), x[i]+dx/2)
        k4=f(y[i]+k2*dx, x[i]+dx)
        y[i+1]=y[i]+(dx/6)*(k1+2*k2*2*k3+k4)
    return y

#1変数2階微分
def RK4_secondoder(f, x):
    dx=x[1]-x[0]
    N=len(x)
    dydx=np.zeros(N)
    y=np.zeros(N)
    dydx[0]=0.1 #初期条件
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

