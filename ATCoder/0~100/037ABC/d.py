# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
init1 = lambda n: [-1 for _ in range(n)]
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

h, w = mapInt()
g = inithw(h)

ans =[ [-1 for i in range(w)]for i in range(h)]
done =[ [False for i in range(w)]for i in range(h)]

# pq = []
# for i in range(h):
#   for j in range(w):
#     heapq.heappush(pq, (g[i][j], i, j))


q = deque()
# while(pq):
#   x ,i, j = heapq.heappop(pq)
#   if done[i][j]: continue
#   done[i][j] = True
#   q.append((i, j))
#   while(q):
#     cy, cx = q.popleft()
#     for dy, dx in d4:
#       ny = cy + dy
#       nx = cx + dx
      
#       if not (0 <= ny < h and 0 <=nx < w): continue
#       if g[cy][cx] <= g[ny][nx]: continue
      
#       ans[ny][nx] += ans[cy][cx]
#       ans[ny][nx] %= MOD
#       if done[i][j]: continue
#       done[i][j] = True
#       q.append((ny, nx))
  

def memo(pos):
  cy, cx = pos
  if ans[cy][cx] != -1:
    return ans[cy][cx]
  nothing = True
  for dy, dx in d4:
    ny = cy + dy
    nx = cx + dx
    if not (0 <= ny < h and 0 <=nx < w): continue
    if g[cy][cx] >= g[ny][nx]: continue
    nothing = False
    v = memo((ny, nx))
    # print(v)
    if ans[cy][cx] == -1:
      ans[cy][cx] = 1+ v
    else:
      ans[cy][cx] += v
      
    ans[cy][cx] %= MOD
    if done[i][j]: continue
    done[i][j] = True
    # q.append((ny, nx))
  if nothing:
    ans[cy][cx] = 1
  return ans[cy][cx]

# while pq:
#   _ ,i, j = heapq.heappop(pq)
#   memo((i,j))
  
for i in range(h):
  for j in range(w):
    memo((i, j))

x = 0

for i in range(h):
  for j in range(w):
    x += ans[i][j]
    x %= MOD
# print(ans)
print(x)
    