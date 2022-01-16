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
intInput = lambda: int(input())
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

n, m = mapInt()
dic = {}
grid = [ [] for i in range(n)]
# その頂点に向かっている辺の数（入力辺の数)
in_edge = [0] * n

for i in range(m):
  a, b = mapInt()
  a -= 1
  b -= 1
  if (a, b) in dic:
    continue
  dic[(a, b)] = True
  grid[a].append(b)
  in_edge[b] += 1
  
minHeap = []
for i in range(n):
  if in_edge[i] == 0:
    heapq.heappush(minHeap, i)

#startから追っていく
ans = []
while(minHeap):
  x = heapq.heappop(minHeap)
  ans.append(x+1)
  for node in grid[x]:
    in_edge[node] -= 1
    if in_edge[node] == 0:
      heapq.heappush(minHeap, node)


# サイクルがある場合、入力辺の数が０になる前に、whileを抜けるため答えが頂点分存在しない。
if len(ans) != n:
  print(-1)
  sys.exit()
print(*ans)