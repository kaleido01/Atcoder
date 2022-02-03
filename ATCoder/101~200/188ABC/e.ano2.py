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
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from collections import deque
import heapq

n,m = mapInt()

a = listInt()

ans = -1 * INF
done =[ False for i in range(n)]
nodes = [[] for i in range(n)]
for i in range(m):
  x, y = mapInt()
  x -=1
  y -=1
  nodes[x].append(y)
  
minA = []
for i in range(n):
  minA.append((a[i],i))

minA.sort()

q = deque()

for i in range(n):
  v , pos = minA[i]
  if done[pos]:
    continue
  q.append(minA[i])
  
  while(q):
    cost,pos = q.popleft()
    # print(pos)
      
    for node in nodes[pos]:
      if done[node]:
        continue
      done[node] = True
      w = a[node]
      # print(w)
      ans = max(ans, w - cost)
      q.append((cost, node))
    

print(ans)