#行列式の計算を、LU分解を用いた方法として実装
#永年方程式を二分法を用いて解く


import numpy as np


#-----LU分解-----
def LUD(matrix): #分解したい行列を引数、分解したL,Uを返す関数
    n=len(matrix) #n×n行列
    L=np.zeros((n, n)) #分解した下三角行列用
    U=np.eye(n) #分解した上三角行列用

    A=matrix
    for i in range(n):
        #l00=a00
        l00=A[0][0]

        #l1=a1
        l1=np.zeros((n-i-1, 1))
        for j in range(n-i-1):
            l1[j]=A[j+1][0]

        #u1^T=α1^T/l00
        u1=np.zeros((1,n-i-1))
        for j in range(n-i-1):
            u1[0][j]=A[0][j+1]/l00

        #A1=l1@u1^T+L1@U1　 → 　AをA1-l1@u1^Tに置き換え
        A1=np.zeros((n-i-1, n-i-1)) #A1はAの一番目の行と列を取り除いたもの
        l1u1=l1@u1
        for j in range(n-i-1):
            for k in range(n-i-1):
                A1[j][k]=A[j+1][k+1]-l1u1[j][k]
        A=A1


        #l1をLのi列目に代入
        L[i][i]=l00
        for j in range(len(l1)):
            L[j+i+1][i]=l1[j][0]
        #u1をUのi行目に代入 
        for j in range(len(l1)):
            U[i][j+i+1]=u1[0][j]

    return L, U

#-----行列式計算-----
def det(matrix):
    L, U=LUD(matrix)
    total_det=1.0
    for i in range(len(matrix)):
        total_det*=L[i][i]
    return total_det

#-----   -----
a=0 #coulomb積分
b=1 #共鳴積分

def ethylene(e):
    return [
        [a-e, b],
        [b, a-e]
    ]

def butadiene(e):
    return [
        [a-e, b,   0,   0],
        [b,   a-e, b,   0],
        [0,   b,   a-e, b],
        [0,   0,   b,   a-e]
    ]

def toluene(e):
    return [
        [a-e, 0, 0, 0, b, 0, 0],
        [0, a-e, 0, 0, 1, 1, 0],
        [0, 0, a-e, 0, 0, b, b],
        [0, 0, 0, a-e, b, 0, b],
        [b, b, 0, b, a-e, 0, 0],
        [0, b, b, 0, 0, a-e, 0],
        [0, 0, b, b, 0, 0, a-e]
    ]


#-----二分法-----
region=[-10.0, 10.0]
step=0.1
eps=1e-4

def judge(a:float, b:float):
    return det(toluene(a))*det(toluene(b))

def bisection(a, b):
    n=0
    dx=b-a
    while dx > eps:
        x=(b+a)/2
        if judge(x, a)<0:
            b=x
        else:
            a=x
        dx=abs(b-a)
        # print("Search from {:4.2f}to{:4.2f}. F(x)={:>10.3e}".format(x, dx, f1(x)))
        n+=1
    else:
        print('e={:10.6f}'.format(x))

def main():
    x0=region[0]
    while x0 <= region[1]-step:
        if judge(x0, x0+step) < 0:
            # print("Rough Search from {:4.2f} to {:4.2f}".format(x0, x0+step))
            bisection(x0, x0+step)
        x0+=step

main()