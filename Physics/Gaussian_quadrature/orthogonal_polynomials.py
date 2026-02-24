import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy.optimize import root_scalar
from scipy import integrate
import pandas as pd
import os



n_max=10 #n_max次の多項式まで考える
round_order=15



#-----3項間漸化式によって直交多項式を代数的に導出-----
x_sym=sym.symbols("x")
def Legendre(i, P):
    if i==0:
        return 1
    elif i==1:
        return x_sym
    else:
        return (2*i-1)/i*x_sym*P[i-1]-(i-1)/i*P[i-2]

def Chebyshev(i, T):
    if i==0:
        return 1
    elif i==1:
        return x_sym
    else:
        return 2*x_sym*T[i-1]-T[i-2]
    
def Laguerre(i, L):
    if i==0:
        return 1
    elif i==1:
        return 1-x_sym
    else:
        return (-(1/i)*x_sym+(2*i-1)/i)*L[i-1]-((i-1)/i)*L[i-2]
    
def Hermite(i, H):
    if i==0:
        return 1
    elif i==1:
        return 2*x_sym
    else:
        return 2*x_sym*H[i-1]-2*(i-1)*H[i-2]


P=[0]*(n_max+1)
T=[0]*(n_max+1)
L=[0]*(n_max+1)
H=[0]*(n_max+1)

p=[0]*(n_max+1)
t=[0]*(n_max+1)
l=[0]*(n_max+1)
h=[0]*(n_max+1)

for i in range(n_max+1):
    P[i]=Legendre(i, P)
    p[i]=sym.lambdify(x_sym, P[i], 'numpy')
    T[i]=Chebyshev(i, T)
    t[i]=sym.lambdify(x_sym, T[i], 'numpy')
    L[i]=Laguerre(i, L)
    l[i]=sym.lambdify(x_sym, L[i], 'numpy')
    H[i]=Hermite(i, H)
    h[i]=sym.lambdify(x_sym, H[i], 'numpy')



#-----グラフの描画-----
plt.subplot(2, 2, 1)
plt.title("Legendre")
plt.xlabel("x")
plt.ylabel("P_n(x)")
plt.xlim(-1.0, 1.0)
plt.ylim(-1.05, 1.05)
x=np.linspace(-1.0, 1.0, 1000)
for i in range(1, n_max+1):
    plt.plot(x, p[i](x), label="n="+str(i))
plt.grid()
plt.legend()

plt.subplot(2, 2, 2)
plt.title("Chebyshev")
plt.xlabel("x")
plt.ylabel("T_n(x)")
plt.xlim(-1.0, 1.0)
plt.ylim(-1.05, 1.05)
x=np.linspace(-1.0, 1.0, 1000)
for i in range(1, n_max+1):
    plt.plot(x, t[i](x), label="n="+str(i))
plt.grid()
plt.legend()

plt.subplot(2, 2, 3)
plt.title("Laguerre")
plt.xlabel("x")
plt.ylabel("L_n(x)")
plt.xlim(-2.0, 10.0)
plt.ylim(-10.0, 10.0)
x=np.linspace(-2.0, 10.0, 1000)
for i in range(1, n_max+1):
    plt.plot(x, l[i](x), label="n="+str(i))
plt.grid()
plt.legend()

plt.subplot(2, 2, 4)
plt.title("Hermite")
plt.xlabel("x")
plt.ylabel("H_n(x)")
plt.xlim(-2.0, 2.0)
plt.ylim(-25, 25)
x=np.linspace(-2.0, 2.0, 1000)
for i in range(1, n_max+1):
    plt.plot(x, h[i](x), label="n="+str(i))
plt.grid()
plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "orthogonal_polynomials.png"))
# plt.show()



#-----直行多項式の零点を計算-----
p_root=[[]for _ in range(n_max+1)]
t_root=[[]for _ in range(n_max+1)]
l_root=[[]for _ in range(n_max+1)]
h_root=[[]for _ in range(n_max+1)]

x_max=100.0
for i in range(n_max+1):
    x=-x_max
    step=0.1
    while x<x_max:
        if p[i](x)*p[i](x+step)<0:
            p_root[i].append([round(root_scalar(p[i], bracket=(x, x+step)).root, round_order)])
        if t[i](x)*t[i](x+step)<0:
            t_root[i].append([round(root_scalar(t[i], bracket=(x, x+step)).root, round_order)])
        if l[i](x)*l[i](x+step)<0:
            l_root[i].append([round(root_scalar(l[i], bracket=(x, x+step)).root, round_order)])
        if h[i](x)*h[i](x+step)<0:
            h_root[i].append([round(root_scalar(h[i], bracket=(x, x+step)).root, round_order)])
        x+=step



#-----重みの計算-----
def l_i(x, i, n, root):
    val=1
    for j in range(n):
        if i!=j:
            val*=(x-root[n][j][0])/(root[n][i][0]-root[n][j][0])
    return val

def w(x, p):
    if p==P:
        return 1
    elif p==T:
        return 1/np.sqrt(1-x**2)
    elif p==L:
        return np.exp(-x)
    else:
        return np.exp(-x**2)
    
for n in range(n_max+1):
    for i in range(n):
        p_func=lambda x: w(x, P)*l_i(x, i, n, p_root)
        p_integrated=integrate.quad(p_func, -1.0, 1.0)
        p_root[n][i].append(round(p_integrated[0], round_order))

        t_func=lambda x: w(x, T)*l_i(x, i, n, t_root)
        t_integrated=integrate.quad(t_func, -1.0, 1.0)
        t_root[n][i].append(round(t_integrated[0], round_order))

        l_func=lambda x: w(x, L)*l_i(x, i, n, l_root)
        l_integrated=integrate.quad(l_func, 0.0, np.inf)
        l_root[n][i].append(round(l_integrated[0], round_order))

        h_func=lambda x: w(x, H)*l_i(x, i, n, h_root)
        h_integrated=integrate.quad(h_func, -np.inf, np.inf)
        h_root[n][i].append(round(h_integrated[0], round_order))
        


#-----出力データをcsv化-----
data=[]
for n in range(1, n_max+1):
    for i in range(len(p_root[n])):
        data.append(["P_n(x)", n, i, p_root[n][i][0], p_root[n][i][1]])
    for i in range(len(t_root[n])):
        data.append(["T_n(x)", n, i, t_root[n][i][0], t_root[n][i][1]])
    for i in range(len(l_root[n])):
        data.append(["L_n(x)", n, i, l_root[n][i][0], l_root[n][i][1]])
    for i in range(len(h_root[n])):
        data.append(["H_n(x)", n, i, h_root[n][i][0], h_root[n][i][1]])
df=pd.DataFrame(data, columns=["p_n(x)", "n", "i", "x_i", "w_i"])
df["p_n(x)"]=pd.Categorical(df["p_n(x)"], categories=["P_n(x)", "T_n(x)", "L_n(x)", "H_n(x)"], ordered=True)
df=df.sort_values(by=["p_n(x)", "n", "i"])
df.set_index(["p_n(x)",  "n", "i"], inplace=True)
df.to_csv(os.path.join(os.path.dirname(__file__), "orthogonal_polynomials.csv"))