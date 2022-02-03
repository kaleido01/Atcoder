# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
init1 = lambda n: [-1 for _ in range(n)]
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# h, w = mapInt()
n, m = mapInt()
height = listInt()

g= [ [] for i in range(n)]

for i in range(m):
  x , y = mapInt()
  x -=1
  y -=1
  if height[x] <= height[y]:
    x, y = y, x
  
  diff = height[x] - height[y]
  
  g[x].append([0,y])
  g[y].append([diff,x])
  
  
  
  
def dijkstra(s):
    # 始点から各頂点への最短距離
    d = [INF] * n
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
  
  
  
dist = dijkstra(0)
# print(dist)
ans = 0
for i in range(n):
  ans = max(ans, -1 * (dist[i] - height[0] + height[i]))

print(ans)
# q = deque()

# q.append(0)


# while q:
#   pos = q.popleft()
  
#   nodes = g[pos]
  
#   for node in nodes:
#     if done[node]: continue
#     done[node] = True
#     if ans[node] == -INF:
#       v = height[pos] - height[node] 
#       if v > 0:
#         ans[node] = v + ans[pos]
#         q.append(node)

#       else:
#         ans[node] = 2 * v + ans[pos]
#     else:
#       v = height[pos] - height[node]
#       if ans[pos] + v > ans[node]:
#         ans[node] = ans[pos] + v
#         q.append(node)

    
            

# print(ans)
# print(max(ans))
