import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["backend"]="qtagg"

fac=2*5.224*10**3/6.582**2
a=5.224*8.288**2*10**(-1)

x_max=0.5
dx=0.001
x=np.arange(-x_max, x_max, dx)
N=len(x)

def g(E, x, psi, dpsi):
    return -fac*(E-Pot(x))*psi
def Pot(x):
    return a*x**2+x**4

def RungeKutta(E): #4次ルンゲクッタ
    psi=np.zeros(N)
    dpsi=np.zeros(N)
    psi[0]=0.0
    dpsi[0]=0.01
    node=0
    for i in range(N-1):
        k1=dpsi[i]
        l1=g(E, x[i], psi[i], dpsi[i])
        k2=dpsi[i]+dx/2*l1
        l2=g(E, x[i]+dx/2, psi[i]+dx/2*k1, dpsi[i]+dx/2*l1)
        k3=dpsi[i]+dx/2*l2
        l3=g(E, x[i]+dx/2, psi[i]+dx/2*k2, dpsi[i]+dx/2*l2)
        k4=dpsi[i]+dx*l3
        l4=g(E, x[i]+dx, psi[i]+dx*k3, dpsi[i]+dx*l3)
        psi[i+1]=psi[i]+dx*(k1+2*k2+2*k3+k4)/6.0
        dpsi[i+1]=dpsi[i]+dx*(l1+2*l2+2*l3+l4)/6.0
        if psi[i+1]*psi[i]<0:
            node+=1
    return psi, node

def binary_search(Emin, Emax, node): #零点が(node)個になるような最大のEを求める二分探索
    for i in range(30):
        Etry=(Emin+Emax)/2
        psi, node0=RungeKutta(Etry)
        if node0>node:
            Emax=Etry
        else:
            Emin=Etry
    return Etry, psi

def plot(E, psi):
    fig=plt.figure()
    ax=fig.add_subplot(1, 1, 1)
    for i in range(len(E)):
        ax.plot(x, psi[i]+E[i], label="E_"+str(i)+"={:.3f}".format(E[i]))
    ax.plot(x, Pot(x), "-", c="black", label="Potential")
    ax.legend()
    plt.show()

def main():
    E=[]
    psi=[]
    for node in range(4):
        e,p=binary_search(0.0, 10.0, node)
        E.append(e)
        psi.append(p)
    plot(E, psi)

main()