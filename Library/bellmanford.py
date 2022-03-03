

V, E, p = mapInt()    # Vは頂点数、Eは辺数
es = []    # 辺
for _ in range(E):
    # 頂点fromから頂点toへのコストcostの辺
    f, t, c = map(int,input().split())
    f -=1
    t -=1
    es.append([f, t, -c+p])

""" ベルマンフォード法。ある頂点から、各頂点への最小経路を解く"""
""" 計算量は全ての頂点をINFで初期化、全ての辺から伸びるコストを頂点分行うため O(VE)"""
""" 最大でもV回目までに更新は終わっているはず 1 - 2 - 3 のような経路を考えると1 - 2と 2 - 3の２回で済むはず"""
""" そのためV回目に更新がある場合は、負のサイクル、すなわちいくらでも経路を小さくできるため、その判定ができる。"""
def bellmanford(s):
    d = [INF] * V
    d[s] = 0
    negative = [False] * V
    for i in range(V):
        for j in range(E):
            e = es[j]
            if d[e[0]] == INF: continue
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                # n回目にも更新があるなら負の経路が存在する
                if i == V-1:
                    # 行き先が更新されたので、行き先が負のループの対象。
                    negative[e[1]] = True
                    d[e[1]] = -INF
    for i in range(V):
        for j in range(E):
            e = es[j]
            if d[e[0]] == INF: continue
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
            # 自身から行ける場所e[0] -> e[1] は全て負のループ
            if negative[e[0]]:
              negative[e[1]] = True
              d[e[1]] = -INF
    
    
    return d

d = bellmanford(0)    # 頂点0を始点とする

if d[V-1] == -INF:
    print(-1)
elif d[V-1] >=0:
    print(0)
else:
  print(-d[V-1])