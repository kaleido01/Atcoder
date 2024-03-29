# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**19
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
n, K = mapInt()

points = []

for i in range(n):
  points.append(listInt())
  
ans = INF

for i in range(n):
  for j in range(i+1, n):
    for k in range(n):
      for l in range(k+1, n):
        sx,sy = points[i]
        tx,ty = points[j]
        ux,uy = points[k]
        vx,vy = points[l]
        if sx > tx:
          sx, tx = tx, sx
        if uy > vy:
          uy, vy = vy, uy
        
        sq = (tx-sx) * (vy-uy)
        if sq <= 0 : continue
        cnt = 0
        for p in range(n):
          mx, my = points[p]
          
          if sx <= mx <= tx and uy <= my <= vy:
            cnt +=1
        if cnt >= K:
          ans = min(ans, sq)
  
      
print(ans)