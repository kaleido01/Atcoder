# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input())for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from itertools import combinations, permutations, combinations_with_replacement
from collections import deque
import heapq
n, m, Q, K = mapInt()
k = listInt()

g= [ [] for i in range(n)]
for i in range(m):
  a, b = mapInt()
  a -=1
  b -=1
  g[a].append(b)
  g[b].append(a)
  
query = []
for i in range(Q):
  a, b = mapInt()
  a-=1
  b-=1
  query.append((a,b))
  
# def dijkstra(s):
#     # 始点から各頂点への最短距離
#     d = [float('inf')] * n
#     d[s] = 0
#     # 各頂点が訪問済みかどうか
#     used = [False] * n
#     used[s] = True
#     # 仮の距離を記録するヒープ
#     que = []
#     for e in g[s]:
#         heapq.heappush(que, e)
#     while que:
#         cost, v = heapq.heappop(que)
#         if used[v]:
#             continue
#         d[v] = cost
#         used[v] = True
#         for e in g[v]:
#             if not used[e[1]]:
#                 heapq.heappush(que, [e[0] + d[v], e[1]])
#     return d
  
dis = []

q = deque()
for i in range(K):
  # dis.append(dijkstra(k[i]-1))
  q.append(k[i]-1)
  dist = [ -1 for _ in range(n)]
  dist[k[i]-1] = 0
  while(q):
    pos = q.popleft()
    nodes = g[pos]
    for node in nodes:
      # print(node, dist)
      if dist[node] != -1: continue
      dist[node] = dist[pos] +1
      q.append(node)
  dis.append(dist)

for i in range(Q):
  a, b = query[i]
  
  ans = INF
  for j in range(K):
    ans = min(ans, dis[j][a] + dis[j][b])
  print(ans)
  
