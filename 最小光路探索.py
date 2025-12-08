import numpy as np
import matplotlib as plt
plt.rcParams["backend"]="qtagg"

#屈折率
def refractive_index(line, row):
    n1=1.0
    n2=1.2
    if row<=50:
        return n1
    elif row>50:
        return n2
#頂点(line, row)の配列上での位置
def locate(line, row):
    return N_row*line+row

#重き付き有向グラフ
N_line=4
N_row=4
N_node=N_line*N_row
inf=1000.0
edge=[(1,0), (3,1), (2,1), (3,2), (1,1), (2,3), (2,1), (1,3), (0,1)] #辺の方向
gragh=[[inf]*N_node for _ in range(N_node)] #gragh[辺の始点][辺の終点]
for i in range(len(edge)): #グラフの値の挿入
    dx=edge[i][0]
    dy=edge[i][1]
    actual_distance=np.sqrt(dx**2+dy**2)
    for line in range(N_line-dy):
        for row in range(N_row-dx):
            gragh[locate(line, row)][locate(line+dy, row+dx)]=actual_distance*refractive_index(line, row)

#経路探索(ダイクストラ法)

