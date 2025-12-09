import numpy as np
import heapq
import matplotlib.pyplot as plt
plt.rcParams["backend"]="qtagg"

#屈折率
def refractive_index(line, row):
    n=[1.8, 1.6, 1.4, 1.2, 1.0]
    boundary=[0, 60, 120, 180, 240] #0は入れる,1000は入れない
    for i in range(len(boundary)-1):
        if boundary[i]<=line<boundary[i+1]:
            return n[i], boundary
    return n[-1], boundary
    

#頂点(line, row)の配列上での位置
def locate(line, row):
    return N_row*line+row

inf=float("INF")

#重き付き有向グラフ
N_line=301
N_row=301
N_node=N_line*N_row
list_edge = [
    (1,0), (0,1),
    (1,1),
    (2,1), (1,2),
    (3,1), (1,3),
    (3,2), (2,3),
    (4,1), (1,4),
    (4,3), (3,4),
    (5,1), (1,5),
    (5,2), (2,5),
    (5,3), (3,5),
    (5,4), (4,5)
] #辺の方向
gragh=[[] for _ in range(N_node)] #隣接グラフ[辺の始点(N_node)][(辺の終点,光学的距離),...]
for node in range(N_node): #すべての頂点について
    line=node//N_row
    row=node%N_row
    for edge in list_edge: #list_edgeにある辺を追加
        dx=edge[0]
        dy=edge[1]
        terminal=locate(line+dy, row+dx)
        if line+dy<N_line and row+dx<N_row: #(N_line)×(N_row)を超えない範囲で
            actual_distance=np.sqrt(dx**2+dy**2)
            refractive=refractive_index(line, row)
            optical_distance=actual_distance*refractive[0] #光路長=距離×屈折率
            gragh[node].append([terminal, optical_distance])

#最短経路探索(ダイクストラ法)
def dijkstra(gragh, start, end): #graghの頂点startからendまでの最短経路をもとめるダイクストラ法
    cost=[inf]*len(gragh) #各頂点までの最小光路長
    visit=[0]*len(gragh) #startからの最短経路未探索は0,探索済みは1
    path_data=[-1]*len(gragh)#経路復元用(termまでの最適経路のtermの1つ前の頂点を記録)
    cost[start]=0 #sart地点までの(光学的)距離0
    heap=[(0, start)] #起点選択用優先度つきキュー
    search=start #起点
    while visit[end]==0: #endに達するまで繰り返し
        for i in range(len(gragh[search])): #頂点iからのびるすべての辺について
            term=gragh[search][i][0] #辺の終点
            dist=gragh[search][i][1] #辺のコスト
            if cost[term]>cost[search]+dist: #古いコスト>新しいコストなら
                cost[term]=cost[search]+dist #コストを更新
                path_data[term]=search #経路を記録(termまでの最適経路のtermの1つ前の頂点を記録)
                heapq.heappush(heap, (cost[term], term)) #次の起点の候補に追加
        visit[search]=1 #searchは探索済み

        if heap==[]: #次の候補が空ならブレーク
            break
        while heap: 
            a=heapq.heappop(heap) #heapからコスト最小のものを取り出す
            if visit[a[1]]==1: #選んだものの頂点が探索済みならcontinue(選びなおす)
                continue
            else: #探索済みならこれを次の起点にする
                search=a[1]
                break

    print(cost[end])
    return path_data

#経路復元
def path_restore(path): #経路を終点から復元
    path_x=[]
    path_y=[]
    i=N_node-1
    while i>=0:
        x=i%N_row
        y=i//N_row
        path_x.append(x)
        path_y.append(y)
        i=path[i]
    return(path_x, path_y)

#図をプロット
def plot(x, y, boundary):
    plt.figure()
    plt.gca().invert_yaxis()
    for i in range(1, len(boundary)):
        plt.axhline(y=boundary[i]+0.5, color="red", linestyle="--")
    plt.plot(x, y, marker=".", markersize=2, label="Light Path")
    plt.title("Fermat's Principle")
    plt.legend()
    plt.grid()
    plt.show()

path=dijkstra(gragh, 0, N_node-1)
x, y=path_restore(path)
plot(x, y, boundary=refractive_index(0,0)[1])