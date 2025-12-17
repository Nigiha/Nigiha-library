import numpy as np

#---区分求積A---
def simA(f:list, a:float, b:float, N:int) ->float:
    dx=(b-a)/N
    S=0.0
    for i in range(1, N+1):
        S+=f[i]*dx
    return S

#---区分求積B---
def simB(f:list, a:float, b:float, N:int) ->float:
    dx=(b-a)/N
    S=0.0
    for i in range(N):
        S+=f[i]*dx
    return S

#---台形法---
def trape(f:list, a:float, b:float, N:int) ->float:
    dx=(b-a)/N
    S=dx/2*(f[0]+f[N])
    for i in range(1, N):
        S+=f[i]*dx
    return S

#---シンプソン法---
def simpson(f:list, a:float, b:float, N:int) ->float:
    dx=(b-a)/N
    S=dx/3*(f[0]+f[N])
    Nh=N//2
    for i in range(1, Nh+1):
        S+=4*f[2*i-1]/3*dx
    for i in range(1, Nh):
        S+=2*f[2*i]/3*dx
    return S

#---被積分関数---
def func(a:float, b:float, N:int) ->np.ndarray:
    dx=(b-a)/N
    f=[]##
    for i in range(N+1):
        x=a+i*dx##
        f.append(4/(1+x**2))##f[i]=pow(x, -2)
    return f

#---メイン---
def main():
    b=1.0 #積分範囲
    a=0.0 #積分範囲
    for i in range(1, 7):
        N=pow(10, i) #分割数
        f=func(a, b, N)
        SA=simA(f, a, b, N)
        SB=simB(f, a, b, N)
        S_trape=trape(f, a, b, N)
        S_simp=simpson(f, a, b, N)
        print("N={:6.0e}, SA={:14.7e}, SB={:14.7e}, S_trape={:14.7e}, S_simp={:14.7e}".format(N, SA, SB, S_trape, S_simp))

main()