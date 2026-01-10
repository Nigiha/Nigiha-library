import numpy as np
#LU分解 U(上三角行列の対角成分を1にする)
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

#----------
matrix=[
    [8, 16, 24, 32],
    [2, 7, 12, 17],
    [6, 17, 32, 59],
    [7, 22, 46, 105],
]

L, U=LUD(matrix)
print(matrix, "\n=\n", L, "\n×\n", U)
