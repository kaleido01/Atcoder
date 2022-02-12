# -*- coding: utf-8 -*-
from dis import dis
import sys

sys.setrecursionlimit(10**9)
INF=2 * 10**5
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



n, m = mapInt()

point = [1, n]

g = {}
d = {1: -INF, n: -INF}
d[1] = 0
used = {1: False, n: False}
used[1] = True
for i in range(m):
  a, b, c = mapInt()
  d[a] = -INF
  d[b] = -INF
  used[a] = False
  used[b] = False
  if a in g:
    g[a].append([c,b])
  else:
    g[a] = []
    g[a].append([c,b])
  if b in g:
    g[b].append([c,a])
  else:
    g[b] = []
    g[b].append([c,a])

  point.append(a)
  point.append(b)

point.sort()



# B = sorted(set(point))
# # B の各要素が何番目の要素なのかを辞書型で管理する
# D = { v: i for i, v in enumerate(B) }
# pressed = list(map(lambda v: D[v], point))

for i in range(len(point)-1):
  a = point[i]
  b = point[i+1]
  if a in g:
    g[a].append([b-a,b])
  else:
    g[a] = []
    g[a].append([b-a,b])
  if b in g:
    g[b].append([b-a,a])
  else:
    g[b] = []
    g[b].append([b-a,a])
  

def dijkstra(s):
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
            # print(e)
            if not used[e[1]]:
                heapq.heappush(que, [e[0] + d[v], e[1]])
    return d
  

dist = dijkstra(1)

print(dist[n])

  

