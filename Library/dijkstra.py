import heapq

n = 4
g = [[[1, 1], [4, 2]], [[1, 0], [2, 2], [5, 3]], [[4, 0], [2, 1], [1, 3]], [[1, 2], [5, 1]]] # 隣接リスト


"""ダイクストラ"""
"""優先度付きキューを使用して求めるため、配列の第一引数がコスト、第二引数が次の頂点の番号になる。"""


def dijkstra(s):
    # 始点から各頂点への最短距離
    d = [float('inf')] * n
    d[s] = 0
    # 各頂点が訪問済みかどうか
    used = [False] * n
    used[s] = True
    # 仮の距離を記録するヒープ
    que = []
    for e in g[s]:
        heapq.heappush(que, e)
    while que:
        cost, v = heapq.heappop(que)
        if used[v]:
            continue
        d[v] = cost
        used[v] = True
        for e in g[v]:
            if not used[e[1]]:
                heapq.heappush(que, [e[0] + d[v], e[1]])
    return d
  
  
print(dijkstra(0))