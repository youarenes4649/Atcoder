import heapq
INF = 10**10
N, K = map(int,input().split())
adj = [[] for i in range(N)]
ans = []

def dijkstra(s, g):
    dists  = [INF for i in range(N)]
    dists[s] = 0
    pq = [(0, s)] # 優先度付きキューのオブジェクトそのものはただのリスト
    while(pq):
        
        d, node = heapq.heappop(pq)
        if (d > dists[node]): # 探索の対象にする必要があるか確認
            continue
        for next, cost in adj[node]:
            if d + cost < dists[next]: # 更新すべきか確認
                dists[next] = d + cost
                heapq.heappush(pq, (dists[next],next))
    if dists[g] == INF:
        return -1
    else:
        return dists[g]
