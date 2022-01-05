# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
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

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

h, w = mapInt()

rs, cs = mapInt()
rt, ct = mapInt()

rs, cs = rs-1, cs-1
rt, ct = rt-1, ct-1

grid = inithw(h)
que = deque()
countTurn = inithwv(h, w, INF)

for i in range(4):
  ny, nx = rs + d4[i][0], cs + d4[i][1]
  if not (0 <= ny < h and 0 <= nx < w):
    continue
  if grid[ny][nx] == "#":
    continue
  countTurn[ny][nx] = 0
  que.append([ny, nx, i, 0])
# print(grid)
def bfs():
  while (len(que) > 0):
    
    cy, cx, cd, count = que.popleft()
    
    for i in range(len(d4)):
      ny, nx = cy + d4[i][0], cx + d4[i][1]
      nd = i
      nc = count + (cd != nd)
      # print(ny, nx)
      if not (0 <= ny < h and 0 <= nx < w) or nc > countTurn[ny][nx]:
        continue
      
      if grid[ny][nx] == "#":
        continue
      if ny == rt and nx == ct:
        countTurn[ny][nx] = min(nc, countTurn[ny][nx])
        continue
      
      countTurn[ny][nx] = min(nc, countTurn[ny][nx])
      if nd == cd:
        que.appendleft([ny, nx, nd, nc])
      else:
        que.append([ny, nx, nd, nc])
        
    
bfs()
# print(countTurn)
print(countTurn[rt][ct])
# print(1+ True)