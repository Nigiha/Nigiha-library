import numpy as np
import heapq
import matplotlib as plt
plt.rcParams["backend"]="qtagg"

#屈折率
def refractive_index(line, row):
    n1=1.0
    n2=1.2
    if row<=5:
        return n1
    elif row>5:
        return n2
#頂点(line, row)の配列上での位置
def locate(line, row):
    return N_row*line+row

inf=1000.0

#重き付き有向グラフ
N_line=10
N_row=10
N_node=N_line*N_row
edge=[(1,0), (3,1), (2,1), (3,2), (1,1), (2,3), (2,1), (1,3), (0,1)] #辺の方向
gragh=[[inf]*N_node for _ in range(N_node)] #gragh[辺の始点][辺の終点],値は辺の光学的距離
for i in range(len(edge)): #グラフの値の挿入
    dx=edge[i][0]
    dy=edge[i][1]
    actual_distance=np.sqrt(dx**2+dy**2)
    for line in range(N_line-dy):
        for row in range(N_row-dx):
            gragh[locate(line, row)][locate(line+dy, row+dx)]=actual_distance*refractive_index(line, row) #辺の重みに光学的距離を用いる

#最短経路探索(ダイクストラ法)
def dijkstra(gragh, start, end):
    cost=[inf]*len(gragh) #各頂点までの(光学的)距離
    visit=[0]*len(gragh) #startからの最短経路未探索は0,探索済みは1
    cost[start]=0 #sart地点までの(光学的)距離0
    visit[start]=1 #start地点は探索済み
    heap=[]
    search_from=0
    while visit[end]==0:
        for i in range(len(gragh[search_from])):
            if gragh[search_from][i]!=inf:
                heapq.heappush(heap, (cost[i], i))
            cost[i]=min(cost[i], cost[search_from]+gragh[search_from][i])
        if heap==[]:
            break
        next=heapq.heappop(heap)
        search_from=next[1]
        visit[next[1]]=1


    print(cost[end])

dijkstra(gragh, 0, N_node-1)     