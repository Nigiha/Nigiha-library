#最短経路探索(ダイクストラ法)
def dijkstra(gragh, start, end): #graghの頂点startからendまでの最短経路をもとめるダイクストラ法
    import heapq
    inf=float("INF")
#-----step1-----
    cost=[inf]*len(gragh) #各頂点までの最小光路長
    visit=[0]*len(gragh) #startからの最短経路未探索は0,探索済みは1
    path_data=[-1]*len(gragh)#経路復元用(termまでの最適経路のtermの1つ前の頂点を記録)
    cost[start]=0 #sart地点までの(光学的)距離0
    heap=[(0, start)] #起点選択用優先度つきキュー
    search=start #起点

    while visit[end]==0: #endに達するまで繰り返し
#-----step2-----
        for i in range(len(gragh[search])): #頂点iからのびるすべての辺について
            term=gragh[search][i][0] #辺の終点
            dist=gragh[search][i][1] #辺のコスト
            if cost[term]>cost[search]+dist: #古いコスト>新しいコストなら
                cost[term]=cost[search]+dist #コストを更新
                path_data[term]=search #経路を記録(termまでの最適経路のtermの1つ前の頂点を記録)
                heapq.heappush(heap, (cost[term], term)) #次の起点の候補に追加
        visit[search]=1 #searchは探索済み
#-----step3-----
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