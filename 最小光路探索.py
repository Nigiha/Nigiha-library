import numpy as np
import matplotlib as plt
plt.rcParams["backend"]="qtagg"

#屈折率を決める
def refractive_index(line, row):
    n1=1.0
    n2=1.2
    if row<=50:
        return n1
    elif row>50:
        return n2


#重き付き有向グラフ
line_total=100
row_total=100
inf=1000.0
edge=[(1,0), (3,1), (2,1), (3,2), (1,1), (2,3), (2,1), (1,3), (0,1)] #辺の方向
g=[[[inf]*len(edge) for _ in range(row_total)] for _ in range(line_total)] #空グラフ
for i in range(len(edge)): #グラフの値の挿入
    dx=edge[i][0]
    dy=edge[i][1]
    actual_distance=np.sqrt(dx**2+dy**2)
    for line in range(line_total-dy):
        for row in range(row_total-dx):
            g[line][row][i]=actual_distance*refractive_index(line, row)

#経路探索(ダイクストラ法)
