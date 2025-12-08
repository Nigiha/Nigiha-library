import numpy as np
import heapq
import matplotlib as plt
plt.rcParams["backend"]="qtagg"

#屈折率
def refractive_index(line, row):
    n1=1.0
    n2=3.0
    if row<=50:
        return n1
    elif row>50:
        return n2
#頂点(line, row)の配列上での位置
def locate(line, row):
    return N_row*line+row

inf=float("INF")

#重き付き有向グラフ
N_line=101
N_row=101
N_node=N_line*N_row
list_edge=[(1,0), (3,1), (2,1), (3,2), (1,1), (2,3), (2,1), (1,3), (0,1)] #辺の方向
gragh=[[] for _ in range(N_node)] #gragh[辺の始点(N_node)][(辺の終点,光学的距離),...]
for node in range(N_node):
    line=node//N_row
    row=node%N_row
    for edge in list_edge:
        dx=edge[0]
        dy=edge[1]
        terminal=locate(line+dy, row+dx)
        if terminal<N_node:
            actual_distance=np.sqrt(dx**2+dy**2)
            optical_distance=actual_distance*refractive_index(line, row)
            gragh[node].append([terminal, optical_distance])

#最短経路探索(ダイクストラ法)
def dijkstra(gragh, start, end):
    cost=[inf]*len(gragh) #各頂点までの(光学的)距離
    visit=[0]*len(gragh) #startからの最短経路未探索は0,探索済みは1
    cost[start]=0 #sart地点までの(光学的)距離0
    heap=[]
    search=0
    while visit[end]==0:
        for i in range(len(gragh[search])):
            idx=gragh[search][i][0]
            idx2=gragh[search][i][1]
            if cost[idx]>cost[search]+idx2:
                heapq.heappush(heap, (cost[idx], idx))
                cost[idx]=cost[search]+idx2
        visit[search]=1
        if heap==[]:
            break
        a=heapq.heappop(heap)
        search=a[1]

    print(cost[end])

dijkstra(gragh, 0, N_node-1)     